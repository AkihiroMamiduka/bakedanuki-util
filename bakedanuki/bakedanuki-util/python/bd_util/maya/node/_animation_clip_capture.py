"""AnimationClipの対象収集と読み取り。sceneを編集しない。"""

from __future__ import annotations

import math
from collections.abc import Iterable
from typing import cast

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from .animation_clip import (
    AnimationClip,
    AnimationLayerData,
    ChannelAnimationData,
    NodeAnimationData,
    LayerSettingData,
    LAYER_SETTINGS,
    LayerMode,
    literal_name,
    finite_number,
)
from .operator.attr import (
    _keyframe_snapshot,
    _keyframe_tangent,
    _keyframe_target,
)
from .operator.attr._keyframe_discovery import curve_objects, has_animation
from .operator.attr.define.std.at.scalar._base import sample_reader
from .operator.attr.keyframe import KeyframeManager
from .operator.attr.keyframe_data import AnimCurveData, KeyData
from .operator.node._core import NodeOperator
from .operator.node.dg._anim_layer import (
    node_object,
    live_node,
    leaf_plugs,
    supported_plug,
)


def node_name(node: om.MObject) -> str:
    return (
        om.MFnDagNode(node).fullPathName()
        if node.hasFn(om.MFn.kDagNode)
        else live_node(node).name()
    )


def plug_for(node: om.MObject, attribute: str) -> om.MPlug:
    selection = om.MSelectionList()
    selection.add(f"{node_name(node)}.{literal_name(attribute)}")
    plug = selection.getPlug(0)
    # Explicit nonexistent multi indices must not be materialized by capture.
    current = plug
    while current.isChild or current.isElement:
        if current.isElement:
            if (
                current.logicalIndex()
                not in current.array().getExistingArrayAttributeIndices()
            ):
                raise ValueError(f"Missing array element: {plug.name()}.")
            current = current.array()
        else:
            current = current.parent()
    return plug


def supported(plug: om.MPlug) -> bool:
    return supported_plug(
        plug
    ) and oma.MFnAnimCurve().timedAnimCurveTypeForPlug(plug) in (
        oma.MFnAnimCurve.kAnimCurveTA,
        oma.MFnAnimCurve.kAnimCurveTL,
        oma.MFnAnimCurve.kAnimCurveTU,
    )


def discrete(plug: om.MPlug) -> bool:
    return _keyframe_tangent.is_discrete(plug)


def sample(
    plug: om.MPlug, frames: Iterable[float]
) -> list[tuple[float, float]]:
    # Reuse the scalar sampler's units and upstream dirty propagation.
    from .operator.attr.define.std.at.scalar._base import sample_plug_values

    return sample_plug_values(plug, frames=frames)


def frame_grid(start: float, end: float, step: float) -> tuple[float, ...]:
    span = (end - start) / step
    if not math.isfinite(span) or span > 10_000_000:
        raise ValueError("The clip sample grid exceeds 10,000,001 points.")
    count = math.floor(span)
    result = [start + i * step for i in range(count + 1)]
    if result[-1] < end:
        result.append(end)
    else:
        result[-1] = end
    return tuple(result)


def sampled_curve(
    plug: om.MPlug, samples: Iterable[tuple[float, float]], rate: float
) -> AnimCurveData:
    tangent = "step" if discrete(plug) else "linear"
    return AnimCurveData(
        curve_type=_keyframe_snapshot.curve_type_for_plug(plug),
        seconds_per_frame=rate,
        weighted=False,
        pre_infinity="constant",
        post_infinity="constant",
        keys=tuple(
            KeyData(
                frame=t,
                value=v,
                in_tangent_type="linear",
                out_tangent_type=tangent,
                in_tangent_xy=(1.0, 0.0),
                out_tangent_xy=(1.0, 0.0),
                tangents_locked=False,
                weights_locked=False,
                breakdown=False,
            )
            for t, v in samples
        ),
    )


def layer_tree() -> tuple[str | None, list[tuple[str, str | None]]]:
    root = cast(str | None, cmds.animLayer(query=True, root=True))
    result: list[tuple[str, str | None]] = []

    def visit(parent: str) -> None:
        for child in cast(
            list[str], cmds.animLayer(parent, query=True, children=True) or []
        ):
            result.append((child, None if parent == root else parent))
            visit(child)

    if root:
        visit(root)
    return root, result


def layer_input(plug: om.MPlug, layer: str | None) -> om.MPlug:
    if layer is not None:
        value = cmds.animLayer(
            layer, query=True, layeredPlug=_keyframe_target.plug_path(plug)
        )
        if not isinstance(value, str) or not value:
            raise RuntimeError(f"Missing layer input: {layer}, {plug.name()}.")
        selection = om.MSelectionList()
        selection.add(value)
        return selection.getPlug(0)
    current = plug
    seen: set[str] = set()
    while current.name() not in seen:
        seen.add(current.name())
        source = current.sourceWithConversion()
        if source.isNull:
            return current
        fn = om.MFnDependencyNode(source.node())
        attribute = om.MFnAttribute(source.attribute()).name
        if not fn.typeName.startswith("animBlendNode") or attribute not in (
            "output",
            "outputX",
            "outputY",
            "outputZ",
        ):
            break
        current = fn.findPlug(
            "inputA" + attribute.removeprefix("output"), False
        )
    return current


def capture_settings(
    name: str, start: float | None, end: float | None
) -> tuple[LayerSettingData, ...]:
    node = node_object(name)
    result: list[LayerSettingData] = []
    for attr in LAYER_SETTINGS:
        plug = live_node(node).findPlug(attr, False)
        curve = KeyframeManager(plug).get_curve_data(start, end)
        if curve is None and plug.isDestination:
            raise RuntimeError(
                f"Cannot preserve driven layer setting {name}.{attr}."
            )
        result.append(LayerSettingData(attr, float(plug.asDouble()), curve))
    return tuple(result)


def channel_layers(
    plug: om.MPlug,
    root: str | None,
    tree: list[tuple[str, str | None]],
    selected: set[str | None],
) -> list[str | None]:
    return ([None] if root in selected else []) + [
        name
        for name, _ in tree
        if name in selected and _keyframe_target.layer_member(name, plug)
    ]


def preserved_animation(
    plug: om.MPlug,
    root: str | None,
    tree: list[tuple[str, str | None]],
    selected: set[str | None],
    settings_cache: dict[str, bool],
) -> bool:
    parents = dict(tree)
    for layer in channel_layers(plug, root, tree, selected):
        raw = layer_input(plug, layer)
        if has_animation(raw):
            return True
        if (
            raw.isChild
            and live_node(raw.node()).typeName
            == "animBlendNodeAdditiveRotation"
            and any(
                has_animation(sibling) for sibling in leaf_plugs(raw.parent())
            )
        ):
            return True
        if layer is None:
            if raw.name() == plug.name():
                continue
            layer = root
        while layer is not None:
            if layer not in settings_cache:
                fn = live_node(node_object(layer))
                settings_cache[layer] = any(
                    has_animation(fn.findPlug(attr, False))
                    for attr in LAYER_SETTINGS
                )
            if settings_cache[layer]:
                return True
            layer = None if layer == root else parents[layer] or root
    return False


def capture(
    nodes: Iterable[NodeOperator | om.MObject | str],
    *,
    attributes: Iterable[str] | None,
    include_channel_box: bool,
    include_static: bool,
    start_frame: float | None,
    end_frame: float | None,
    layer_mode: LayerMode,
    layers: Iterable[str] | None,
    sample_by: float,
) -> AnimationClip:
    if isinstance(nodes, (str, NodeOperator, om.MObject)):
        raise TypeError("nodes must be an iterable of nodes.")
    if type(include_channel_box) is not bool:
        raise TypeError("include_channel_box must be a bool.")
    if type(include_static) is not bool:
        raise TypeError("include_static must be a bool.")
    if layer_mode not in ("flatten", "preserve"):
        raise ValueError("layer_mode must be flatten or preserve.")
    if layers is not None and layer_mode != "preserve":
        raise ValueError(
            "layers is available only with layer_mode='preserve'."
        )
    if isinstance(attributes, str) or isinstance(layers, str):
        raise TypeError("attributes and layers must be iterables of names.")
    attrs = (
        None
        if attributes is None
        else tuple(literal_name(item) for item in attributes)
    )
    step = finite_number(sample_by, "sample_by")
    if step <= 0:
        raise ValueError("sample_by must be positive.")
    start = (
        None
        if start_frame is None
        else finite_number(start_frame, "start_frame")
    )
    end = None if end_frame is None else finite_number(end_frame, "end_frame")
    if start is not None and end is not None and start > end:
        raise ValueError("start_frame must not exceed end_frame.")
    collected: list[tuple[om.MObject, tuple[om.MPlug, ...]]] = []
    handles: set[om.MObjectHandle] = set()
    for value in nodes:
        node = node_object(value)
        fn = live_node(node)
        handle = om.MObjectHandle(node)
        if handle in handles:
            raise ValueError("Duplicate source node.")
        handles.add(handle)
        candidates = (
            [plug_for(node, attr) for attr in attrs]
            if attrs is not None
            else [
                fn.findPlug(fn.attribute(i), False)
                for i in range(fn.attributeCount())
                if om.MFnAttribute(fn.attribute(i)).parent.isNull()
            ]
        )
        found: dict[str, om.MPlug] = {}
        for candidate in candidates:
            for plug in leaf_plugs(candidate):
                if attrs is None and not (
                    plug.isKeyable or include_channel_box and plug.isChannelBox
                ):
                    continue
                if not supported(plug):
                    if attrs is not None:
                        raise TypeError(
                            f"Unsupported clip attribute: {plug.name()}."
                        )
                    continue
                found[_keyframe_target.plug_path(plug)] = plug
        collected.append((node, tuple(found.values())))
    if not collected or not any(plugs for _, plugs in collected):
        raise ValueError("No supported animation attributes were selected.")
    root, tree = layer_tree()
    selected: set[str | None] = (
        {literal_name(layer) for layer in layers}
        if layers is not None
        else {
            name
            for name, _ in tree
            if any(
                _keyframe_target.layer_member(name, plug)
                for _, plugs in collected
                for plug in plugs
            )
        }
    )
    if layers is None:
        selected.add(root)
    if not selected.issubset({root, *(name for name, _ in tree)}):
        raise ValueError("Unknown animation layer in layers.")
    if not include_static:
        settings_cache: dict[str, bool] = {}
        collected = [
            (
                node,
                tuple(
                    plug
                    for plug in plugs
                    if (
                        has_animation(plug)
                        if layer_mode == "flatten"
                        else preserved_animation(
                            plug, root, tree, selected, settings_cache
                        )
                    )
                ),
            )
            for node, plugs in collected
        ]
        if not any(plugs for _, plugs in collected):
            raise ValueError(
                "No animated attributes were selected. "
                "Use include_static=True to capture static values."
            )
        if layers is None:
            selected = {
                root,
                *(
                    name
                    for name, _ in tree
                    if any(
                        _keyframe_target.layer_member(name, plug)
                        for _, plugs in collected
                        for plug in plugs
                    )
                ),
            }
    parents = dict(tree)
    required = {name for name in selected if name is not None and name != root}
    for name in tuple(required):
        parent = parents[name]
        while parent is not None:
            required.add(parent)
            parent = parents[parent]
    saved_tree = [(name, parent) for name, parent in tree if name in required]
    frames: list[float] = []
    if start is None or end is None:
        seen_curves: set[om.MObjectHandle] = set()
        range_curves: list[om.MObject] = []
        for _, plugs in collected:
            for plug in plugs:
                if layer_mode == "flatten":
                    range_curves.extend(
                        curve_objects(plug, traverse_inputs=True)
                    )
                else:
                    for layer in channel_layers(plug, root, tree, selected):
                        target = (
                            plug
                            if layer is None
                            else _keyframe_target.LayerTarget(plug, layer)
                        )
                        curve = _keyframe_target.resolve_curve(target)
                        if curve is not None:
                            range_curves.append(curve.object())
        if layer_mode == "preserve":
            for name in ([root] if root else []) + [
                name for name, _ in saved_tree
            ]:
                fn = live_node(node_object(name))
                for attr in LAYER_SETTINGS:
                    range_curves.extend(
                        curve_objects(
                            fn.findPlug(attr, False), traverse_inputs=True
                        )
                    )
        for obj in range_curves:
            handle = om.MObjectHandle(obj)
            if handle in seen_curves:
                continue
            seen_curves.add(handle)
            curve = oma.MFnAnimCurve(obj)
            if curve.isTimeInput and curve.numKeys:
                frames.extend(
                    curve.input(i).asUnits(om.MTime.uiUnit())
                    for i in (0, curve.numKeys - 1)
                )
        if not frames:
            raise ValueError(
                "Explicit start_frame and end_frame are required when no time-key range is available."
            )
    range_start = min(frames) if start is None else start
    range_end = max(frames) if end is None else end
    if range_start > range_end:
        raise ValueError("The resolved clip range is reversed.")
    rate = om.MTime(1, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)
    clipped = start is not None or end is not None
    bounds = (range_start, range_end) if clipped else (None, None)
    grid = (
        frame_grid(range_start, range_end, step)
        if layer_mode == "flatten"
        else ()
    )
    records: list[NodeAnimationData] = []
    for node, plugs in collected:
        channels: list[ChannelAnimationData] = []
        for plug in plugs:
            attribute = _keyframe_target.plug_path(plug).split(".", 1)[1]
            if layer_mode == "flatten":
                channels.append(
                    ChannelAnimationData(
                        attribute,
                        None,
                        sampled_curve(plug, sample(plug, grid), rate),
                    )
                )
                continue
            for layer in channel_layers(plug, root, tree, selected):
                manager = KeyframeManager(plug)
                if layer is not None:
                    manager = manager.anim_layer(layer)
                data = manager.get_curve_data(*bounds)
                if data is None or not data.keys:
                    raw = layer_input(plug, layer)
                    if raw.isDestination and data is None:
                        raise RuntimeError(
                            f"Cannot preserve a driven input without a time curve: {raw.name()}."
                        )
                    value = sample_reader(raw, om.MTime.uiUnit())()
                    data = sampled_curve(
                        plug,
                        (
                            [(range_start, value)]
                            if range_start == range_end
                            else [(range_start, value), (range_end, value)]
                        ),
                        rate,
                    )
                channels.append(ChannelAnimationData(attribute, layer, data))
        records.append(NodeAnimationData(node_name(node), tuple(channels)))
    layer_records = (
        tuple(
            AnimationLayerData(name, parent, capture_settings(name, *bounds))
            for name, parent in saved_tree
        )
        if layer_mode == "preserve"
        else ()
    )
    if not any(record.channels for record in records):
        raise ValueError(
            "No channels belong to the selected animation layers."
        )
    return AnimationClip(
        nodes=tuple(records),
        layers=layer_records,
        root_settings=(
            capture_settings(root, *bounds)
            if layer_mode == "preserve" and root
            else ()
        ),
        layer_mode=layer_mode,
        clipped=clipped,
        start_frame=range_start,
        end_frame=range_end,
        seconds_per_frame=rate,
        sample_by=step,
    )
