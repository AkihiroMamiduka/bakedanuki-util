"""AnimationClipの検査と、ModifierManagerによる一括復元。"""

from __future__ import annotations

import math
from collections.abc import Callable, Iterable
from dataclasses import replace
from typing import cast

from maya import cmds
from maya.api import OpenMaya as om

from .animation_clip import (
    AnimationClip,
    AnimationLayerData,
    LayerSettingData,
    RestoreMode,
    literal_name,
    finite_number,
)
from ._animation_clip_capture import (
    capture_settings,
    layer_tree,
    plug_for,
    sample,
)
from ._animation_clip_time import transformed_for_restore
from .modifier import ModifierManager
from .nodes import Nodes
from .operator.attr import _keyframe_target, _keyframe_snapshot
from .operator.attr.keyframe import KeyframeManager
from .operator.attr.keyframe_data import AnimCurveData
from .operator.node._core import NodeOperator
from .operator.node.dg._anim_layer import (
    AnimLayerOperations,
    node_object,
    live_node,
    locked_plug,
    PlugIdentity,
)


def mapped_name(name: str, namespace: str | None) -> str:
    if namespace is None:
        return name
    prefix = namespace + ":" if namespace else ""
    return "|".join(
        prefix + part.rsplit(":", 1)[-1] if part else ""
        for part in name.split("|")
    )


def absolute(name: str) -> str:
    return name if name.startswith(("|", ":")) else ":" + name


def command(manager: ModifierManager, callback: Callable[[], object]) -> None:
    def prepare(modifier: om.MDGModifier) -> None:
        modifier.pythonCommandToExecute(callback)

    manager.queue_dg_modifier(prepare)


def _ui_frame(frame: float, rate: float) -> float:
    return om.MTime(frame * rate, om.MTime.kSeconds).asUnits(om.MTime.uiUnit())


def _converted(data: AnimCurveData) -> AnimCurveData:
    rate = om.MTime(1, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)
    return replace(
        data,
        seconds_per_frame=rate,
        keys=tuple(
            replace(key, frame=_ui_frame(key.frame, data.seconds_per_frame))
            for key in data.keys
        ),
    )


def _restore_curve(
    manager: ModifierManager,
    keyframe: KeyframeManager,
    data: AnimCurveData,
    mode: RestoreMode,
    start: float,
    end: float,
) -> None:
    if mode == "replace_all":
        keyframe.set_curve_data(data)
    else:
        if mode == "replace_range":
            keyframe.delete_keys(start, end)
        if keyframe.get_curve_data() is None:
            # New curves should retain the saved weighting and infinity.
            keyframe.set_curve_data(data)
        else:
            keyframe.set_key_data(
                data.keys, seconds_per_frame=data.seconds_per_frame
            )


def _same_setting(actual: LayerSettingData, saved: LayerSettingData) -> bool:
    if actual.curve is None or saved.curve is None:
        return actual.curve is saved.curve and actual.value == saved.value
    expected = _converted(saved.curve)
    if replace(actual.curve, keys=()) != replace(expected, keys=()) or len(
        actual.curve.keys
    ) != len(expected.keys):
        return False
    for index, (a, b) in enumerate(zip(actual.curve.keys, expected.keys)):
        if (
            replace(
                a,
                frame=b.frame,
                value=b.value,
                in_tangent_xy=b.in_tangent_xy,
                out_tangent_xy=b.out_tangent_xy,
            )
            != b
        ):
            return False
        if any(
            not math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12)
            for x, y in zip(
                (a.frame, a.value),
                (b.frame, b.value),
            )
        ):
            return False
        for actual_xy, saved_xy, tangent, outside in (
            (a.in_tangent_xy, b.in_tangent_xy, b.in_tangent_type, index == 0),
            (
                a.out_tangent_xy,
                b.out_tangent_xy,
                b.out_tangent_type,
                index == len(expected.keys) - 1,
            ),
        ):
            # Maya derives these legacy tangents from type and key spacing.
            # Editing their angle or weight changes their type to fixed.
            if tangent in ("fast", "slow"):
                continue
            if not expected.weighted or outside:
                # Endpoint length affects neither interpolation nor infinity.
                # Maya can renormalize it when restoring automatic tangents.
                actual_length = math.hypot(*actual_xy) or 1.0
                saved_length = math.hypot(*saved_xy) or 1.0
                actual_xy = (
                    actual_xy[0] / actual_length,
                    actual_xy[1] / actual_length,
                )
                saved_xy = (
                    saved_xy[0] / saved_length,
                    saved_xy[1] / saved_length,
                )
            if any(
                # Maya rounds weighted tangent lengths when restoring them.
                not math.isclose(
                    x,
                    y,
                    rel_tol=1e-7 if expected.weighted else 1e-12,
                    abs_tol=1e-12,
                )
                for x, y in zip(actual_xy, saved_xy)
            ):
                return False
    return True


def _apply_settings(
    manager: ModifierManager,
    layer: om.MObject,
    data: AnimationLayerData,
    *,
    locked_only: bool,
) -> None:
    for setting in data.settings:
        if (setting.name == "lock") != locked_only:
            continue
        plug = live_node(layer).findPlug(setting.name, False)
        keyframe = KeyframeManager(plug, modifier_manager=manager)
        if setting.curve is not None:
            keyframe.set_curve_data(setting.curve)
        else:
            curve = keyframe.get_curve_data()
            if curve is not None:
                keyframe.delete_anim_curve()
            elif plug.isDestination:
                raise RuntimeError(
                    f"Cannot replace a driven layer setting: {plug.name()}."
                )

            def set_value(
                modifier: om.MDGModifier,
                plug: om.MPlug = plug,
                value: float = setting.value,
            ) -> None:
                _keyframe_target.check_editable_node(live_node(plug.node()))
                if locked_plug(plug):
                    raise RuntimeError(
                        f"Cannot edit locked setting: {plug.name()}."
                    )
                modifier.newPlugValueDouble(plug, value)

            manager.queue_dg_modifier(set_value)


def restore(
    clip: AnimationClip,
    modifier_manager: ModifierManager,
    *,
    targets: Iterable[NodeOperator | om.MObject | str] | None,
    namespace: str | None,
    mode: RestoreMode,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    time_scale: float | None,
    duration_frames: float | None,
    restore_layer_settings: bool,
    tolerance: float,
) -> None:
    if not isinstance(cast(object, modifier_manager), ModifierManager):
        raise TypeError("modifier_manager must be a ModifierManager.")
    if mode not in ("merge", "replace_all", "replace_range"):
        raise ValueError("mode must be merge, replace_all or replace_range.")
    if type(restore_layer_settings) is not bool:
        raise TypeError("restore_layer_settings must be a bool.")
    tolerance = finite_number(tolerance, "tolerance")
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative.")
    if namespace is not None:
        if targets is not None:
            raise ValueError(
                "targets and namespace cannot be specified together."
            )
        if not isinstance(cast(object, namespace), str) or any(
            c in namespace for c in "|.*?[]"
        ):
            raise ValueError("namespace must be a literal namespace.")
        namespace = namespace.strip(":")
    if isinstance(targets, (str, NodeOperator, om.MObject)):
        raise TypeError("targets must be an iterable of nodes.")
    data = transformed_for_restore(
        AnimationClip.from_dict(clip.to_dict()),
        offset_frames=offset_frames,
        to_start_frame=to_start_frame,
        to_end_frame=to_end_frame,
        time_scale=time_scale,
        duration_frames=duration_frames,
    )
    destination: tuple[str | om.MObject, ...]
    if targets is None:
        destination = tuple(
            absolute(mapped_name(node.name, namespace)) for node in data.nodes
        )
    else:
        destination = tuple(
            (
                literal_name(value)
                if isinstance(value, str)
                else node_object(value)
            )
            for value in targets
        )
    if len(destination) != len(data.nodes):
        raise ValueError(
            "targets must have the same length as the saved node list."
        )
    # Existing destinations retain identity across renames; unresolved names can
    # refer to nodes created by earlier steps in this same manager.
    captured = tuple(
        (
            node_object(value)
            if not isinstance(value, str) or cmds.objExists(value)
            else value
        )
        for value in destination
    )
    handles = tuple(
        None if isinstance(value, str) else om.MObjectHandle(value)
        for value in captured
    )

    def plan(manager: ModifierManager) -> None:
        resolved: list[om.MObject] = []
        for value, handle in zip(captured, handles):
            if handle is not None and (
                not handle.isValid() or not handle.isAlive()
            ):
                raise RuntimeError(
                    "A clip destination was deleted before execution."
                )
            node = node_object(value)
            _keyframe_target.check_editable_node(live_node(node))
            if any(node == previous for previous in resolved):
                raise ValueError(
                    "Multiple source nodes cannot map to one destination."
                )
            resolved.append(node)
        start = _ui_frame(data.start_frame, data.seconds_per_frame)
        end = _ui_frame(data.end_frame, data.seconds_per_frame)
        setting_bounds = (start, end) if data.clipped else (None, None)
        bindings: list[tuple[PlugIdentity, str | None, AnimCurveData]] = []
        for node, saved in zip(resolved, data.nodes):
            for channel in saved.channels:
                plug = plug_for(node, channel.attribute)
                if locked_plug(plug):
                    raise RuntimeError(
                        f"Cannot restore locked plug: {plug.name()}."
                    )
                if (
                    _keyframe_snapshot.curve_type_for_plug(plug)
                    != channel.curve.curve_type
                ):
                    raise ValueError(
                        f"Clip channel type mismatch: {plug.name()}."
                    )
                bindings.append(
                    (PlugIdentity.capture(plug), channel.layer, channel.curve)
                )
        layer_nodes: dict[str, om.MObject] = {}
        changed_layers: set[str] = set()
        root, tree = layer_tree()
        root_data = AnimationLayerData(
            "BaseAnimation", None, data.root_settings
        )
        root_changed = bool(data.root_settings) and root is None
        if root is not None and data.root_settings:
            root_node = node_object(root)
            _keyframe_target.check_editable_node(live_node(root_node))
            if live_node(root_node).findPlug("lock", False).asBool():
                raise RuntimeError(
                    "Cannot restore a locked root animation layer."
                )
            same_root = all(
                _same_setting(a, b)
                for a, b in zip(
                    capture_settings(root, *setting_bounds), data.root_settings
                )
            )
            if not same_root and not restore_layer_settings:
                raise ValueError(
                    "Root animation layer settings differ; use restore_layer_settings=True."
                )
            root_changed = not same_root or restore_layer_settings
        parent_map = dict(tree)
        names = {
            layer.name: mapped_name(layer.name, namespace)
            for layer in data.layers
        }
        if len(set(names.values())) != len(names):
            raise ValueError(
                "Layer namespace replacement produced duplicate names."
            )
        existing: set[str] = set()
        for layer in data.layers:
            name = names[layer.name]
            if not cmds.objExists(absolute(name)):
                continue
            node = node_object(absolute(name))
            if not node.hasFn(om.MFn.kAnimLayer) or name == root:
                raise ValueError(
                    f"Expected a non-root animation layer: {name}."
                )
            _keyframe_target.check_editable_node(live_node(node))
            if live_node(node).findPlug("lock", False).asBool():
                raise RuntimeError(f"Cannot restore locked layer: {name}.")
            existing.add(layer.name)
            layer_nodes[layer.name] = node
            expected_parent = (
                None if layer.parent is None else names[layer.parent]
            )
            current = capture_settings(name, *setting_bounds)
            same = parent_map[name] == expected_parent and all(
                _same_setting(a, b) for a, b in zip(current, layer.settings)
            )
            if not same and not restore_layer_settings:
                raise ValueError(
                    f"Animation layer settings differ: {name}. Use restore_layer_settings=True to replace them."
                )
            if not same or restore_layer_settings:
                changed_layers.add(layer.name)
        for parent in {layer.parent for layer in data.layers}:
            expected = [
                names[layer.name]
                for layer in data.layers
                if layer.parent == parent and layer.name in existing
            ]
            actual = [name for name, _ in tree if name in expected]
            if actual != expected and not restore_layer_settings:
                raise ValueError(
                    "Animation layer order differs; use restore_layer_settings=True."
                )
        nodes = Nodes(modifier_manager=manager)
        if data.root_settings and root is None and not data.layers:

            def create_root(modifier: om.MDGModifier) -> None:
                obj = modifier.createNode("animLayer")
                modifier.renameNode(obj, "BaseAnimation")
                modifier.newPlugValueBool(
                    om.MFnDependencyNode(obj).findPlug("override", False), True
                )

            manager.queue_dg_modifier(create_root)
        for layer in data.layers:
            if layer.name not in existing:
                override = bool(
                    next(
                        item.value
                        for item in layer.settings
                        if item.name == "override"
                    )
                )
                created = nodes.create.animLayer(
                    name=absolute(names[layer.name]), override=override
                )
                layer_nodes[layer.name] = created.m_obj
                changed_layers.add(layer.name)

        # Defer the remaining plan until all layer objects have entered the DG.
        def populate(work: ModifierManager) -> None:
            if root_changed:
                current_root = cast(str, cmds.animLayer(query=True, root=True))
                _apply_settings(
                    work,
                    node_object(current_root),
                    root_data,
                    locked_only=False,
                )
            for layer in data.layers:
                node = layer_nodes[layer.name]
                if live_node(node).name() != names[layer.name]:
                    raise RuntimeError(
                        "Maya could not create the exact saved layer name."
                    )
                if layer.name in changed_layers:

                    def reparent(
                        layer: AnimationLayerData = layer,
                        node: om.MObject = node,
                    ) -> object:
                        parent = (
                            live_node(layer_nodes[layer.parent]).name()
                            if layer.parent is not None
                            else cast(
                                str, cmds.animLayer(query=True, root=True)
                            )
                        )
                        return cmds.animLayer(
                            live_node(node).name(), edit=True, parent=parent
                        )

                    command(work, reparent)
                    _apply_settings(work, node, layer, locked_only=False)
                member_plugs = [
                    binding.resolve()
                    for binding, selected, _ in bindings
                    if selected == layer.name
                ]
                if member_plugs:
                    cast(
                        AnimLayerOperations,
                        Nodes(modifier_manager=work).existing(node),
                    ).add_plugs(member_plugs)

            def order(modifier: om.MDGModifier) -> None:
                for parent in {layer.parent for layer in data.layers}:
                    siblings = [
                        layer.name
                        for layer in data.layers
                        if layer.parent == parent
                    ]
                    for left, right in reversed(
                        list(zip(siblings, siblings[1:]))
                    ):

                        def move(
                            left: str = left,
                            right: str = right,
                            parent: str | None = parent,
                        ) -> object:
                            parent_name = (
                                live_node(layer_nodes[parent]).name()
                                if parent is not None
                                else cast(
                                    str, cmds.animLayer(query=True, root=True)
                                )
                            )
                            current = cast(
                                list[str],
                                cmds.animLayer(
                                    parent_name, query=True, children=True
                                )
                                or [],
                            )
                            left_name, right_name = (
                                live_node(layer_nodes[left]).name(),
                                live_node(layer_nodes[right]).name(),
                            )
                            if current.index(left_name) > current.index(
                                right_name
                            ):
                                return cmds.animLayer(
                                    left_name,
                                    edit=True,
                                    moveLayerBefore=right_name,
                                )
                            return None

                        modifier.pythonCommandToExecute(move)

            work.queue_dg_modifier(order)

            def channels(edits: ModifierManager) -> None:
                checks: list[
                    tuple[PlugIdentity, tuple[tuple[float, float], ...]]
                ] = []
                for binding, layer, curve_data in bindings:
                    plug = binding.resolve()
                    keyframe = KeyframeManager(plug, modifier_manager=edits)
                    if layer is not None:
                        keyframe = keyframe.anim_layer(
                            live_node(layer_nodes[layer]).name()
                        )
                    target = (
                        plug
                        if layer is None
                        else _keyframe_target.LayerTarget(
                            plug, layer_nodes[layer]
                        )
                    )
                    _keyframe_target.resolve_curve(target, write=True)
                    if data.layer_mode == "preserve":
                        _restore_curve(
                            edits, keyframe, curve_data, mode, start, end
                        )
                    else:
                        if mode == "replace_all":
                            keyframe.set_curve_data(
                                replace(curve_data, keys=())
                            )
                        elif mode == "replace_range":
                            keyframe.delete_keys(start, end)
                        pairs = tuple(
                            (
                                _ui_frame(
                                    key.frame, curve_data.seconds_per_frame
                                ),
                                key.value,
                            )
                            for key in curve_data.keys
                        )
                        out_type = (
                            "step"
                            if curve_data.keys
                            and curve_data.keys[0].out_tangent_type == "step"
                            else "linear"
                        )
                        keyframe.set_keys(
                            pairs,
                            in_tangent_type="linear",
                            out_tangent_type=out_type,
                        )
                        checks.append((binding, pairs))

                def verify(modifier: om.MDGModifier) -> None:
                    for binding, pairs in checks:
                        plug = binding.resolve()
                        actual = sample(plug, (frame for frame, _ in pairs))
                        for (frame, expected), (_, value) in zip(
                            pairs, actual
                        ):
                            slack = max(tolerance, 32 * math.ulp(expected))
                            if (
                                not math.isfinite(value)
                                or abs(value - expected) > slack
                            ):
                                raise RuntimeError(
                                    f"Cannot resolve clip value at {plug.name()}, frame {frame}: expected {expected}, got {value}."
                                )

                edits.queue_dg_modifier(verify)

            work.queue_dg_batch(channels)

            def locks(edits: ModifierManager) -> None:
                for layer in data.layers:
                    if layer.name in changed_layers:
                        _apply_settings(
                            edits,
                            layer_nodes[layer.name],
                            layer,
                            locked_only=True,
                        )
                if root_changed:
                    current_root = cast(
                        str, cmds.animLayer(query=True, root=True)
                    )
                    _apply_settings(
                        edits,
                        node_object(current_root),
                        root_data,
                        locked_only=True,
                    )

            work.queue_dg_batch(locks)

        manager.queue_dg_batch(populate)

    modifier_manager.queue_dg_batch(plan)
