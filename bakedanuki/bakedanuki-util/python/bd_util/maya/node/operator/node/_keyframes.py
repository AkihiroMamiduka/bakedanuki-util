"""Node-level animation operations shared by every NodeOperator."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from maya import cmds
from maya.api import OpenMaya as om

from ...modifier import ModifierManager
from ..attr import _keyframe_bake, _keyframe_snapshot, _keyframe_target
from .dg._anim_layer import (
    leaf_plugs,
    live_node,
    locked_plug,
    node_object,
    supported_plug,
)

if TYPE_CHECKING:
    from ..._versioned_accessors import (  # pyright: ignore[reportMissingModuleSource]
        AnimLayerNode,
    )


def _literal_attribute(value: object) -> str:
    if (
        not isinstance(value, str)
        or not value
        or any(character in value for character in "*?\x00")
    ):
        raise ValueError("Expected a nonempty, literal attribute name.")
    return value


def _node_name(node: om.MObject) -> str:
    return (
        om.MFnDagNode(node).fullPathName()
        if node.hasFn(om.MFn.kDagNode)
        else live_node(node).name()
    )


def _explicit_plug(node: om.MObject, attribute: str) -> om.MPlug:
    selection = om.MSelectionList()
    try:
        selection.add(f"{_node_name(node)}.{attribute}")
        plug = selection.getPlug(0)
    except RuntimeError as exc:
        raise ValueError(
            f"Animation attribute does not exist: {attribute!r}."
        ) from exc
    current = plug
    while current.isChild or current.isElement:
        if current.isElement:
            if (
                current.logicalIndex()
                not in current.array().getExistingArrayAttributeIndices()
            ):
                raise ValueError(
                    f"Animation array element does not exist: {attribute!r}."
                )
            current = current.array()
        else:
            current = current.parent()
    return plug


def _supported(plug: om.MPlug) -> bool:
    if not supported_plug(plug):
        return False
    try:
        _keyframe_snapshot.curve_type_for_plug(plug)
    except RuntimeError:
        return False
    return True


class NodeKeyframeManager:
    """Collect scalar channels on one node and queue node-level edits."""

    __slots__ = (
        "_node",
        "_node_handle",
        "_modifier_manager",
        "_layer",
        "_layer_handle",
    )

    def __init__(
        self,
        node: om.MObject,
        modifier_manager: ModifierManager,
        layer: om.MObject | None = None,
    ) -> None:
        self._node = node
        self._node_handle = om.MObjectHandle(node)
        self._modifier_manager = modifier_manager
        self._layer = layer
        self._layer_handle = None if layer is None else om.MObjectHandle(layer)

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    def anim_layer(self, name: str | AnimLayerNode) -> NodeKeyframeManager:
        """Return an entry point for one explicit animation layer."""
        layer = node_object(name)
        if not layer.hasFn(om.MFn.kAnimLayer):
            raise TypeError("Expected an animation layer.")
        return NodeKeyframeManager(
            self._node, self._modifier_manager, layer=layer
        )

    def bake(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        include_static: bool = True,
        sample_by: float = 1.0,
    ) -> None:
        """Sample selected node channels and replace their raw inputs with keys.

        Attribute collection and sampling occur on the first DG execution.
        Automatic collection uses keyable scalar leaves, optionally including
        channel-box leaves. Explicit compound and existing array attributes are
        expanded to scalar leaves and may be nonkeyable.
        """
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(_literal_attribute(value) for value in attributes)
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        if type(include_static) is not bool:
            raise TypeError("include_static must be a bool.")
        frames, rate = _keyframe_bake.capture_grid(
            start_frame, end_frame, sample_by
        )
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> (
            tuple[tuple[_keyframe_target.Target, om.MPlug], ...]
        ):
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The node is not available in the scene.")
            node = node_handle.object()
            fn = live_node(node)
            _keyframe_target.check_editable_node(fn)
            layer = None
            layer_name: str | None = None
            root_name: str | None = None
            if layer_handle is not None:
                if not layer_handle.isAlive() or not layer_handle.isValid():
                    raise RuntimeError(
                        "The animation layer is not available in the scene."
                    )
                layer = layer_handle.object()
                layer_fn = live_node(layer)
                if not layer.hasFn(om.MFn.kAnimLayer):
                    raise TypeError("Expected an animation layer.")
                _keyframe_target.check_editable_node(layer_fn)
                layer_name = layer_fn.name()
                if layer_fn.findPlug("lock", False).asBool():
                    raise RuntimeError(
                        f"Cannot edit locked animation layer {layer_name}."
                    )
                queried_root = cmds.animLayer(query=True, root=True)
                root_name = (
                    queried_root if isinstance(queried_root, str) else None
                )

            candidates = (
                [_explicit_plug(node, attribute) for attribute in attrs]
                if attrs is not None
                else [
                    fn.findPlug(fn.attribute(index), False)
                    for index in range(fn.attributeCount())
                    if om.MFnAttribute(fn.attribute(index)).parent.isNull()
                ]
            )
            found: dict[str, tuple[_keyframe_target.Target, om.MPlug]] = {}
            for candidate in candidates:
                for plug in leaf_plugs(candidate):
                    automatic = attrs is None
                    if automatic and not (
                        plug.isKeyable
                        or include_channel_box
                        and plug.isChannelBox
                    ):
                        continue
                    path = _keyframe_target.plug_path(plug)
                    if not _supported(plug):
                        if not automatic:
                            raise TypeError(
                                f"Unsupported bake attribute: {path}."
                            )
                        continue
                    if locked_plug(plug):
                        if not automatic:
                            raise RuntimeError(
                                f"Cannot bake locked plug {path}."
                            )
                        continue
                    if (
                        layer_name is not None
                        and layer_name != root_name
                        and not _keyframe_target.layer_member(layer_name, plug)
                    ):
                        if not automatic:
                            raise RuntimeError(
                                f"{path} is not a member of animation layer "
                                f"{layer_name}."
                            )
                        continue
                    target: _keyframe_target.Target = (
                        plug
                        if layer is None
                        else _keyframe_target.LayerTarget(plug, layer)
                    )
                    found[path] = (target, plug)
            if not found:
                raise ValueError(
                    "No supported animation attributes were selected."
                )
            return tuple(found.values())

        _keyframe_bake.queue_bakes(
            self._modifier_manager,
            resolve_targets,
            frames,
            rate,
            include_static=include_static,
            empty_error=(
                "No animated attributes were selected. "
                "Use include_static=True to bake static values."
            ),
        )


__all__ = ("NodeKeyframeManager",)
