"""Node-level animation operations shared by every NodeOperator."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from maya import cmds
from maya.api import OpenMaya as om

from ...modifier import ModifierManager
from ..attr import (
    _keyframe_bake,
    _keyframe_delete,
    _keyframe_euler,
    _keyframe_reduce,
    _keyframe_snapshot,
    _keyframe_tangent,
    _keyframe_target,
)
from ..attr._keyframe_tangent import TangentTypeValue
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
    from ._core import NodeOperator


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


def _optional_explicit_plug(
    node: om.MObject, attribute: str
) -> om.MPlug | None:
    try:
        return _explicit_plug(node, attribute)
    except ValueError:
        return None


def _supported(plug: om.MPlug) -> bool:
    if not supported_plug(plug):
        return False
    try:
        _keyframe_snapshot.curve_type_for_plug(plug)
    except RuntimeError:
        return False
    return True


def _resolve_layer(
    layer_handle: om.MObjectHandle | None,
) -> tuple[om.MObject | None, str | None, str | None]:
    if layer_handle is None:
        return None, None, None
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
        raise RuntimeError(f"Cannot edit locked animation layer {layer_name}.")
    queried_root = cmds.animLayer(query=True, root=True)
    root_name = queried_root if isinstance(queried_root, str) else None
    return layer, layer_name, root_name


def _collect_targets(
    node: om.MObject,
    attributes: tuple[str, ...] | None,
    include_channel_box: bool,
    layer: om.MObject | None,
    layer_name: str | None,
    root_name: str | None,
    *,
    allow_missing: bool,
) -> tuple[tuple[tuple[_keyframe_target.Target, om.MPlug], ...], set[str]]:
    fn = live_node(node)
    candidates: list[om.MPlug]
    if attributes is None:
        candidates = [
            fn.findPlug(fn.attribute(index), False)
            for index in range(fn.attributeCount())
            if om.MFnAttribute(fn.attribute(index)).parent.isNull()
        ]
        matched: set[str] = set()
    else:
        candidates = []
        matched = set()
        for attribute in attributes:
            candidate = (
                _optional_explicit_plug(node, attribute)
                if allow_missing
                else _explicit_plug(node, attribute)
            )
            if candidate is None:
                continue
            candidates.append(candidate)
            matched.add(attribute)

    found: dict[str, tuple[_keyframe_target.Target, om.MPlug]] = {}
    checked_node = False
    for candidate in candidates:
        for plug in leaf_plugs(candidate):
            automatic = attributes is None
            if automatic and not (
                plug.isKeyable or include_channel_box and plug.isChannelBox
            ):
                continue
            path = _keyframe_target.plug_path(plug)
            if not _supported(plug):
                if not automatic:
                    raise TypeError(
                        f"Unsupported animation attribute: {path}."
                    )
                continue
            if locked_plug(plug):
                if not automatic:
                    raise RuntimeError(f"Cannot edit locked plug {path}.")
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
            if not checked_node:
                _keyframe_target.check_editable_node(fn)
                checked_node = True
            target: _keyframe_target.Target = (
                plug
                if layer is None
                else _keyframe_target.LayerTarget(plug, layer)
            )
            found[path] = (target, plug)
    return tuple(found.values()), matched


def _existing_curve_targets(
    targets: tuple[tuple[_keyframe_target.Target, om.MPlug], ...],
    *,
    automatic: bool,
) -> tuple[tuple[_keyframe_target.Target, om.MPlug], ...]:
    found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
    for target, plug in targets:
        try:
            curve = _keyframe_target.resolve_curve(target)
        except RuntimeError:
            if automatic:
                continue
            raise
        if curve is None:
            continue
        _keyframe_target.resolve_curve(target, write=True)
        found.append((target, plug))
    return tuple(found)


def _rotation_target(
    node: om.MObject,
    layer: om.MObject | None,
) -> _keyframe_euler.RotationTarget:
    if not node.hasFn(om.MFn.kTransform):
        raise TypeError("Euler filter requires a transform or joint node.")
    fn = live_node(node)
    plugs = tuple(
        fn.findPlug(attribute, False)
        for attribute in ("rotateX", "rotateY", "rotateZ")
    )
    targets = tuple(
        plug if layer is None else _keyframe_target.LayerTarget(plug, layer)
        for plug in plugs
    )
    if len(targets) != 3:
        raise RuntimeError(
            "Euler filter could not resolve three rotation plugs."
        )
    return _keyframe_euler.RotationTarget(
        _node_name(node),
        fn.findPlug("rotateOrder", False),
        (targets[0], targets[1], targets[2]),
    )


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
        tangent_type: TangentTypeValue = "auto",
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
        discrete_tangent_type: TangentTypeValue = None,
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
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type, in_tangent_type, out_tangent_type
        )
        discrete_type = (
            _keyframe_tangent.to_tangent_type(discrete_tangent_type)
            if discrete_tangent_type is not None
            else None
        )
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> (
            tuple[tuple[_keyframe_target.Target, om.MPlug], ...]
        ):
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The node is not available in the scene.")
            node = node_handle.object()
            _keyframe_target.check_editable_node(live_node(node))
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found, _ = _collect_targets(
                node,
                attrs,
                include_channel_box,
                layer,
                layer_name,
                root_name,
                allow_missing=False,
            )
            if not found:
                raise ValueError(
                    "No supported animation attributes were selected."
                )
            return found

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
            in_type=in_type,
            out_type=out_type,
            discrete_type=discrete_type,
        )

    def set_tangents(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        tangent_type: TangentTypeValue = None,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
        discrete_tangent_type: TangentTypeValue = None,
    ) -> None:
        """Set tangent types on existing keys in selected node channels."""
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(_literal_attribute(value) for value in attributes)
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type, in_tangent_type, out_tangent_type
        )
        discrete_type = (
            _keyframe_tangent.to_tangent_type(discrete_tangent_type)
            if discrete_tangent_type is not None
            else None
        )
        if in_type is None and out_type is None and discrete_type is None:
            return
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> (
            tuple[tuple[_keyframe_target.Target, om.MPlug], ...]
        ):
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The node is not available in the scene.")
            node = node_handle.object()
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found, _ = _collect_targets(
                node,
                attrs,
                include_channel_box,
                layer,
                layer_name,
                root_name,
                allow_missing=False,
            )
            return _existing_curve_targets(found, automatic=attrs is None)

        _keyframe_tangent.queue_batch(
            self._modifier_manager,
            resolve_targets,
            start,
            end,
            in_type,
            out_type,
            discrete_type,
        )

    def set_weighted(
        self,
        weighted: bool,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
    ) -> None:
        """Set weighted tangents on existing curves in selected channels."""
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(_literal_attribute(value) for value in attributes)
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The node is not available in the scene.")
            node = node_handle.object()
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found, _ = _collect_targets(
                node,
                attrs,
                include_channel_box,
                layer,
                layer_name,
                root_name,
                allow_missing=False,
            )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    found, automatic=attrs is None
                )
            )

        _keyframe_snapshot.queue_weighted_batch(
            self._modifier_manager,
            resolve_targets,
            weighted,
        )

    def set_tangent_locks(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        tangents_locked: bool | None = None,
        weights_locked: bool | None = None,
    ) -> None:
        """Set tangent and weight locks on existing keys in node channels."""
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(_literal_attribute(value) for value in attributes)
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        tangent_lock, weight_lock = _keyframe_tangent.capture_locks(
            tangents_locked, weights_locked
        )
        if tangent_lock is None and weight_lock is None:
            return
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The node is not available in the scene.")
            node = node_handle.object()
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found, _ = _collect_targets(
                node,
                attrs,
                include_channel_box,
                layer,
                layer_name,
                root_name,
                allow_missing=False,
            )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    found, automatic=attrs is None
                )
            )

        _keyframe_tangent.queue_locks(
            self._modifier_manager,
            resolve_targets,
            start,
            end,
            tangent_lock,
            weight_lock,
        )

    def delete_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
    ) -> None:
        """Delete existing keys across node curves as one atomic edit."""
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(_literal_attribute(value) for value in attributes)
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The key deletion node is not available.")
            node = node_handle.object()
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found, _ = _collect_targets(
                node,
                attrs,
                include_channel_box,
                layer,
                layer_name,
                root_name,
                allow_missing=False,
            )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    found, automatic=attrs is None
                )
            )

        _keyframe_delete.queue_delete_batch(
            self._modifier_manager,
            resolve_targets,
            start_frame,
            end_frame,
        )

    def reduce_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        tolerance: float,
        preserve_breakdowns: bool = True,
    ) -> None:
        """Reduce keys across existing node curves as one atomic edit."""
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(_literal_attribute(value) for value in attributes)
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The key reduction node is not available.")
            node = node_handle.object()
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found, _ = _collect_targets(
                node,
                attrs,
                include_channel_box,
                layer,
                layer_name,
                root_name,
                allow_missing=False,
            )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    found, automatic=attrs is None
                )
            )

        _keyframe_reduce.queue_reduce_batch(
            self._modifier_manager,
            resolve_targets,
            start_frame,
            end_frame,
            tolerance,
            preserve_breakdowns,
        )

    def euler_filter(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
    ) -> None:
        """Filter synchronized rotateX/Y/Z keys to nearby Euler solutions."""
        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        node_handle = self._node_handle
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_euler.RotationTarget, ...]:
            if not node_handle.isAlive() or not node_handle.isValid():
                raise RuntimeError("The Euler filter node is not available.")
            layer, _, _ = _resolve_layer(layer_handle)
            return (_rotation_target(node_handle.object(), layer),)

        _keyframe_euler.queue_filter(
            self._modifier_manager,
            resolve_targets,
            start,
            end,
        )


class NodesKeyframeManager:
    """Collect channels across nodes and queue one atomic bake."""

    __slots__ = ("_modifier_manager", "_layer", "_layer_handle")

    def __init__(
        self,
        modifier_manager: ModifierManager,
        layer: om.MObject | None = None,
    ) -> None:
        self._modifier_manager = modifier_manager
        self._layer = layer
        self._layer_handle = None if layer is None else om.MObjectHandle(layer)

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    def anim_layer(self, name: str | AnimLayerNode) -> NodesKeyframeManager:
        """Return a multi-node entry point for one animation layer."""
        layer = node_object(name)
        if not layer.hasFn(om.MFn.kAnimLayer):
            raise TypeError("Expected an animation layer.")
        return NodesKeyframeManager(self._modifier_manager, layer=layer)

    def bake(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        include_static: bool = True,
        sample_by: float = 1.0,
        tangent_type: TangentTypeValue = "auto",
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
        discrete_tangent_type: TangentTypeValue = None,
    ) -> None:
        """Bake selected channels on multiple nodes as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate bake node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(
                dict.fromkeys(
                    _literal_attribute(value) for value in attributes
                )
            )
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        if type(include_static) is not bool:
            raise TypeError("include_static must be a bool.")
        frames, rate = _keyframe_bake.capture_grid(
            start_frame, end_frame, sample_by
        )
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type, in_tangent_type, out_tangent_type
        )
        discrete_type = (
            _keyframe_tangent.to_tangent_type(discrete_tangent_type)
            if discrete_tangent_type is not None
            else None
        )
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> (
            tuple[tuple[_keyframe_target.Target, om.MPlug], ...]
        ):
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
            matched: set[str] = set()
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "A bake node is not available in the scene."
                    )
                targets, names = _collect_targets(
                    handle.object(),
                    attrs,
                    include_channel_box,
                    layer,
                    layer_name,
                    root_name,
                    allow_missing=True,
                )
                found.extend(targets)
                matched.update(names)
            if attrs is not None:
                missing = tuple(
                    attribute
                    for attribute in attrs
                    if attribute not in matched
                )
                if missing:
                    joined = ", ".join(repr(value) for value in missing)
                    raise ValueError(
                        "Animation attributes do not exist on any selected "
                        f"node: {joined}."
                    )
            if not found:
                raise ValueError(
                    "No supported animation attributes were selected."
                )
            return tuple(found)

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
            in_type=in_type,
            out_type=out_type,
            discrete_type=discrete_type,
        )

    def set_tangents(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        tangent_type: TangentTypeValue = None,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
        discrete_tangent_type: TangentTypeValue = None,
    ) -> None:
        """Set tangent types across nodes as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate tangent node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(
                dict.fromkeys(
                    _literal_attribute(value) for value in attributes
                )
            )
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type, in_tangent_type, out_tangent_type
        )
        discrete_type = (
            _keyframe_tangent.to_tangent_type(discrete_tangent_type)
            if discrete_tangent_type is not None
            else None
        )
        if in_type is None and out_type is None and discrete_type is None:
            return
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> (
            tuple[tuple[_keyframe_target.Target, om.MPlug], ...]
        ):
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
            matched: set[str] = set()
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "A tangent node is not available in the scene."
                    )
                targets, names = _collect_targets(
                    handle.object(),
                    attrs,
                    include_channel_box,
                    layer,
                    layer_name,
                    root_name,
                    allow_missing=True,
                )
                found.extend(targets)
                matched.update(names)
            if attrs is not None:
                missing = tuple(
                    attribute
                    for attribute in attrs
                    if attribute not in matched
                )
                if missing:
                    joined = ", ".join(repr(value) for value in missing)
                    raise ValueError(
                        "Animation attributes do not exist on any selected "
                        f"node: {joined}."
                    )
            return _existing_curve_targets(
                tuple(found), automatic=attrs is None
            )

        _keyframe_tangent.queue_batch(
            self._modifier_manager,
            resolve_targets,
            start,
            end,
            in_type,
            out_type,
            discrete_type,
        )

    def set_weighted(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        weighted: bool,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
    ) -> None:
        """Set weighted tangents across existing curves as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate weighted node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(
                dict.fromkeys(
                    _literal_attribute(value) for value in attributes
                )
            )
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
            matched: set[str] = set()
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "A weighted node is not available in the scene."
                    )
                targets, names = _collect_targets(
                    handle.object(),
                    attrs,
                    include_channel_box,
                    layer,
                    layer_name,
                    root_name,
                    allow_missing=True,
                )
                found.extend(targets)
                matched.update(names)
            if attrs is not None:
                missing = tuple(
                    attribute
                    for attribute in attrs
                    if attribute not in matched
                )
                if missing:
                    joined = ", ".join(repr(value) for value in missing)
                    raise ValueError(
                        "Animation attributes do not exist on any selected "
                        f"node: {joined}."
                    )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    tuple(found), automatic=attrs is None
                )
            )

        _keyframe_snapshot.queue_weighted_batch(
            self._modifier_manager,
            resolve_targets,
            weighted,
        )

    def set_tangent_locks(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        tangents_locked: bool | None = None,
        weights_locked: bool | None = None,
    ) -> None:
        """Set tangent and weight locks across nodes as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate tangent lock node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(
                dict.fromkeys(
                    _literal_attribute(value) for value in attributes
                )
            )
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        tangent_lock, weight_lock = _keyframe_tangent.capture_locks(
            tangents_locked, weights_locked
        )
        if tangent_lock is None and weight_lock is None:
            return
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
            matched: set[str] = set()
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "A tangent lock node is not available in the scene."
                    )
                targets, names = _collect_targets(
                    handle.object(),
                    attrs,
                    include_channel_box,
                    layer,
                    layer_name,
                    root_name,
                    allow_missing=True,
                )
                found.extend(targets)
                matched.update(names)
            if attrs is not None:
                missing = tuple(
                    attribute
                    for attribute in attrs
                    if attribute not in matched
                )
                if missing:
                    joined = ", ".join(repr(value) for value in missing)
                    raise ValueError(
                        "Animation attributes do not exist on any selected "
                        f"node: {joined}."
                    )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    tuple(found), automatic=attrs is None
                )
            )

        _keyframe_tangent.queue_locks(
            self._modifier_manager,
            resolve_targets,
            start,
            end,
            tangent_lock,
            weight_lock,
        )

    def delete_keys(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
    ) -> None:
        """Delete existing keys across nodes as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate key deletion node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(
                dict.fromkeys(
                    _literal_attribute(value) for value in attributes
                )
            )
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
            matched: set[str] = set()
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "A key deletion node is not available in the scene."
                    )
                targets, names = _collect_targets(
                    handle.object(),
                    attrs,
                    include_channel_box,
                    layer,
                    layer_name,
                    root_name,
                    allow_missing=True,
                )
                found.extend(targets)
                matched.update(names)
            if attrs is not None:
                missing = tuple(
                    attribute
                    for attribute in attrs
                    if attribute not in matched
                )
                if missing:
                    joined = ", ".join(repr(value) for value in missing)
                    raise ValueError(
                        "Animation attributes do not exist on any selected "
                        f"node: {joined}."
                    )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    tuple(found), automatic=attrs is None
                )
            )

        _keyframe_delete.queue_delete_batch(
            self._modifier_manager,
            resolve_targets,
            start_frame,
            end_frame,
        )

    def reduce_keys(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        tolerance: float,
        preserve_breakdowns: bool = True,
    ) -> None:
        """Reduce existing curves across nodes as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate key reduction node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names or None.")
        attrs = (
            None
            if attributes is None
            else tuple(
                dict.fromkeys(
                    _literal_attribute(value) for value in attributes
                )
            )
        )
        if type(include_channel_box) is not bool:
            raise TypeError("include_channel_box must be a bool.")
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_target.Target, ...]:
            layer, layer_name, root_name = _resolve_layer(layer_handle)
            found: list[tuple[_keyframe_target.Target, om.MPlug]] = []
            matched: set[str] = set()
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "A key reduction node is not available in the scene."
                    )
                targets, names = _collect_targets(
                    handle.object(),
                    attrs,
                    include_channel_box,
                    layer,
                    layer_name,
                    root_name,
                    allow_missing=True,
                )
                found.extend(targets)
                matched.update(names)
            if attrs is not None:
                missing = tuple(
                    attribute
                    for attribute in attrs
                    if attribute not in matched
                )
                if missing:
                    joined = ", ".join(repr(value) for value in missing)
                    raise ValueError(
                        "Animation attributes do not exist on any selected "
                        f"node: {joined}."
                    )
            return tuple(
                target
                for target, _ in _existing_curve_targets(
                    tuple(found), automatic=attrs is None
                )
            )

        _keyframe_reduce.queue_reduce_batch(
            self._modifier_manager,
            resolve_targets,
            start_frame,
            end_frame,
            tolerance,
            preserve_breakdowns,
        )

    def euler_filter(
        self,
        nodes: Iterable[NodeOperator | om.MObject | str],
        start_frame: float | None = None,
        end_frame: float | None = None,
    ) -> None:
        """Filter synchronized rotation keys across nodes as one atomic edit."""
        from ._core import NodeOperator

        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        try:
            values = tuple(nodes)
        except TypeError as exc:
            raise TypeError("nodes must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("nodes must contain at least one node.")
        node_handles: list[om.MObjectHandle] = []
        unique_handles: set[om.MObjectHandle] = set()
        for value in values:
            handle = om.MObjectHandle(node_object(value))
            if handle in unique_handles:
                raise ValueError("Duplicate Euler filter node.")
            unique_handles.add(handle)
            node_handles.append(handle)

        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        handles = tuple(node_handles)
        layer_handle = self._layer_handle

        def resolve_targets() -> tuple[_keyframe_euler.RotationTarget, ...]:
            layer, _, _ = _resolve_layer(layer_handle)
            targets: list[_keyframe_euler.RotationTarget] = []
            for handle in handles:
                if not handle.isAlive() or not handle.isValid():
                    raise RuntimeError(
                        "An Euler filter node is not available in the scene."
                    )
                targets.append(_rotation_target(handle.object(), layer))
            return tuple(targets)

        _keyframe_euler.queue_filter(
            self._modifier_manager,
            resolve_targets,
            start,
            end,
        )


__all__ = ("NodeKeyframeManager", "NodesKeyframeManager")
