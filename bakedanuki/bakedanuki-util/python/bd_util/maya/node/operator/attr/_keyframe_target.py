"""Resolve a curve separately from key editing and plug-value assignment."""

from __future__ import annotations

from typing import cast

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from .keyframe_data import CurveTypeName


class CurveTarget:
    __slots__ = ("node", "handle", "curve_type")

    def __init__(self, node: object) -> None:
        if not isinstance(node, om.MObject):
            raise TypeError("curve must be an MObject.")
        handle = om.MObjectHandle(node)
        if not handle.isAlive() or not node.hasFn(om.MFn.kAnimCurve):
            raise TypeError("curve must be an animCurve node.")
        name = om.MFnDependencyNode(node).typeName
        if name not in ("animCurveTA", "animCurveTL", "animCurveTU"):
            raise RuntimeError(
                "Explicit curve operations support only animCurveTA / TL / TU."
            )
        # handle.object() is null for a pending MDGModifier-created node.
        self.node = node
        self.handle = handle
        self.curve_type: CurveTypeName = name


class LayerTarget:
    __slots__ = ("plug", "node", "handle")

    def __init__(self, plug: om.MPlug, name: object) -> None:
        if not isinstance(name, str):
            raise TypeError("Animation layer name must be a string.")
        if not name:
            raise ValueError("Animation layer name must not be empty.")
        if any(character in name for character in ".*?[]"):
            raise ValueError("Animation layer name must identify one node.")
        selection = om.MSelectionList()
        try:
            selection.add(name)
            node = selection.getDependNode(0)
        except RuntimeError as exc:
            raise ValueError(
                f"Animation layer does not exist: {name!r}."
            ) from exc
        if selection.length() != 1 or not node.hasFn(om.MFn.kAnimLayer):
            raise ValueError(f"Expected an animation layer: {name!r}.")
        self.plug = plug
        self.node = node
        self.handle = om.MObjectHandle(node)
        if not self.handle.isValid():
            raise ValueError("Animation layer must exist in the scene.")


Target = om.MPlug | CurveTarget | LayerTarget


def base_layer(plug: om.MPlug) -> LayerTarget | None:
    """Resolve the scene's current root layer without creating any layers."""
    if om.MItDependencyNodes(om.MFn.kAnimLayer).isDone():
        return None
    name = cmds.animLayer(query=True, root=True)
    if not isinstance(name, str) or not name:
        raise RuntimeError("The base animation layer is not available.")
    return LayerTarget(plug, name)


def plug_path(plug: om.MPlug) -> str:
    """Use an unambiguous command argument even for duplicate DAG names."""
    node = plug.node()
    name = (
        om.MFnDagNode(node).fullPathName()
        if node.hasFn(om.MFn.kDagNode)
        else om.MFnDependencyNode(node).name()
    )
    attribute = plug.partialName(
        includeNonMandatoryIndices=True,
        includeInstancedIndices=True,
        useAlias=False,
        useFullAttributePath=True,
        useLongNames=True,
    )
    return f"{name}.{attribute}"


def resolve_curve(
    target: Target, *, write: bool = False
) -> oma.MFnAnimCurve | None:
    if isinstance(target, om.MPlug):
        layer = base_layer(target)
        if layer is not None:
            return layer_curve(layer, write=write)
        return channel_curve(target, write=write)
    if isinstance(target, LayerTarget):
        return layer_curve(target, write=write)
    return explicit_curve(target, write=write)


def layer_name(target: LayerTarget, *, write: bool = False) -> str:
    """Revalidate membership without executing pending modifiers or changing UI."""
    if not target.handle.isAlive() or not target.handle.isValid():
        raise RuntimeError(
            "The animation layer is not available in the scene."
        )
    plug = target.plug
    handle = om.MObjectHandle(plug.node())
    if not handle.isAlive() or not handle.isValid():
        raise RuntimeError("The keyframe plug is not available in the scene.")
    _check_channel_plug(plug, write=write)
    layer = om.MFnDependencyNode(target.node)
    name = layer.name()
    if write:
        _check_editable_node(layer)
        if layer.findPlug("lock", False).asBool():
            raise RuntimeError(f"Cannot edit locked animation layer {name}.")
    if name != cmds.animLayer(query=True, root=True) and not _layer_member(
        name, plug
    ):
        raise RuntimeError(
            f"{plug.name()} is not a member of animation layer {name}."
        )
    return name


def _layer_member(name: str, plug: om.MPlug) -> bool:
    members = cast(
        list[str] | None, cmds.animLayer(name, query=True, attribute=True)
    )
    for member in members or ():
        selection = om.MSelectionList()
        selection.add(member)
        if plug_path(selection.getPlug(0)) == plug_path(plug):
            return True
    return False


def layer_curve(
    target: LayerTarget, *, write: bool = False
) -> oma.MFnAnimCurve | None:
    name = layer_name(target, write=write)
    curves = cast(
        list[str] | None,
        cmds.animLayer(
            name, query=True, findCurveForPlug=plug_path(target.plug)
        ),
    )
    if not curves:
        if name == cmds.animLayer(query=True, root=True):
            iterator = om.MItDependencyNodes(om.MFn.kAnimLayer)
            while not iterator.isDone():
                layer = om.MFnDependencyNode(iterator.thisNode()).name()
                if _layer_member(layer, target.plug):
                    return None
                iterator.next()
            return channel_curve(target.plug, write=write)
        return None
    selection = om.MSelectionList()
    selection.add(curves[0])
    curve = oma.MFnAnimCurve(selection.getDependNode(0))
    _check_channel_curve(curve, target.plug, write=write)
    return curve


def explicit_curve(
    target: CurveTarget, *, write: bool = False
) -> oma.MFnAnimCurve:
    """Resolve the same scene node, irrespective of its output destinations.

    Input times refer to the curve's own domain, including with a time driver.
    Message connections describe ownership and do not drive curve values.
    """
    if not target.handle.isAlive() or not target.handle.isValid():
        raise RuntimeError(
            "The explicit animCurve is not available in the scene."
        )
    curve = oma.MFnAnimCurve(target.node)
    _check_curve_inputs(curve)
    if write:
        _check_editable_curve(curve)
        _check_owning_layers(curve)
    return curve


def _check_curve_inputs(curve: oma.MFnAnimCurve) -> None:
    if (
        curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTA
        and curve.findPlug("rotationInterpolation", False).asInt() != 1
    ):
        raise RuntimeError(
            "Curve operations require independent scalar rotation interpolation."
        )
    for plug in curve.getConnections():
        if (
            plug.isDestination
            and plug != curve.findPlug("input", False)
            and not plug.attribute().hasFn(om.MFn.kMessageAttribute)
        ):
            raise RuntimeError(
                "Curve operations do not support driven curve attributes."
            )


def channel_curve(
    plug: om.MPlug, *, write: bool = False
) -> oma.MFnAnimCurve | None:
    """Resolve this channel, retaining axes and the pairBlend keying input.

    Driven keys and constraint drivers are not the channel's time animation.
    blendWeighted inputs are searched by logical index; weights are ignored.
    """
    handle = om.MObjectHandle(plug.node())
    if not handle.isAlive() or not handle.isValid():
        raise RuntimeError("The keyframe plug is not available in the scene.")
    _check_channel_plug(plug, write=write)
    pending = [plug]
    visited: set[str] = set()
    while pending:
        destination = pending.pop()
        name = destination.name()
        if name in visited:
            continue
        visited.add(name)
        source = destination.sourceWithConversion()
        if source.isNull:
            continue
        node = om.MFnDependencyNode(source.node())
        attribute = om.MFnAttribute(source.attribute()).name
        if source.node().hasFn(om.MFn.kAnimCurve):
            curve = oma.MFnAnimCurve(source.node())
            if attribute != "output" or not curve.isTimeInput:
                continue
            _check_channel_curve(curve, plug, write=write)
            return curve
        if (
            node.typeName
            in (
                "unitConversion",
                "unitToTimeConversion",
                "timeToUnitConversion",
            )
            and attribute == "output"
        ):
            pending.append(node.findPlug("input", False))
        elif node.typeName == "pairBlend" and attribute in (
            "outTranslateX",
            "outTranslateY",
            "outTranslateZ",
            "outRotateX",
            "outRotateY",
            "outRotateZ",
        ):
            driver = node.findPlug("currentDriver", False).asInt()
            if driver not in (1, 2):
                raise RuntimeError("Unsupported pairBlend currentDriver.")
            pending.append(node.findPlug(f"in{attribute[3:]}{driver}", False))
        elif node.typeName == "blendWeighted" and attribute == "output":
            inputs = node.findPlug("input", False)
            pending.extend(
                inputs.elementByLogicalIndex(index)
                for index in sorted(
                    inputs.getExistingArrayAttributeIndices(), reverse=True
                )
            )
        elif source.node().hasFn(om.MFn.kConstraint):
            continue
        elif node.typeName.startswith("animBlendNode"):
            raise RuntimeError(
                "Channel curve operations require explicit animation layer selection."
            )
        else:
            raise RuntimeError(
                f"Cannot resolve the channel through {source.name()} ({node.typeName}); "
                "use an explicit curve for this connection."
            )
    return None


def _check_channel_curve(
    curve: oma.MFnAnimCurve, plug: om.MPlug, *, write: bool
) -> None:
    if curve.animCurveType != curve.timedAnimCurveTypeForPlug(plug):
        raise RuntimeError(
            f"{plug.name()} requires a time-input curve of the matching type."
        )
    if len(curve.findPlug("output", False).connectedTo(False, True)) != 1:
        raise RuntimeError(
            f"{plug.name()} requires an unshared animation curve."
        )
    _check_curve_inputs(curve)
    if write:
        _check_editable_curve(curve)
        _check_owning_layers(curve)


def _check_channel_plug(plug: om.MPlug, *, write: bool) -> None:
    attribute = plug.attribute()
    if (
        plug.isArray
        or plug.isCompound
        or not (
            attribute.hasFn(om.MFn.kNumericAttribute)
            or attribute.hasFn(om.MFn.kUnitAttribute)
            or attribute.hasFn(om.MFn.kEnumAttribute)
        )
    ):
        raise RuntimeError(
            "Keyframe operations require a scalar numeric or unit plug."
        )
    if write:
        _check_editable_node(om.MFnDependencyNode(plug.node()))
        if not om.MFnAttribute(attribute).writable:
            raise RuntimeError(f"{plug.name()} is not writable.")
        _check_editable_plug(plug)


def _check_owning_layers(curve: oma.MFnAnimCurve) -> None:
    """Layer locks are metadata, not necessarily locks on the curve's plugs."""
    iterator = om.MItDependencyNodes(om.MFn.kAnimLayer)
    if iterator.isDone():
        return
    owners: set[str] = set()
    name = curve.name()
    while not iterator.isDone():
        layer_name = om.MFnDependencyNode(iterator.thisNode()).name()
        if name in (
            cmds.animLayer(layer_name, query=True, animCurves=True) or []
        ):
            owners.add(layer_name)
        if name in (
            cmds.animLayer(layer_name, query=True, baseAnimCurves=True) or []
        ):
            root = cmds.animLayer(query=True, root=True)
            if not isinstance(root, str):
                raise RuntimeError(
                    "The base animation layer is not available."
                )
            owners.add(root)
        iterator.next()
    for name in owners:
        selection = om.MSelectionList()
        selection.add(name)
        layer = om.MFnDependencyNode(selection.getDependNode(0))
        _check_editable_node(layer)
        if layer.findPlug("lock", False).asBool():
            raise RuntimeError(
                f"Cannot edit a curve on locked animation layer {name}."
            )


def deletion_connections(
    curve: oma.MFnAnimCurve,
) -> list[tuple[om.MPlug, om.MPlug]]:
    """Validate every connection before any disconnection can be executed."""
    connections: list[tuple[om.MPlug, om.MPlug]] = []
    for plug in curve.getConnections():
        pairs = [(source, plug) for source in plug.connectedTo(True, False)]
        pairs.extend((plug, dest) for dest in plug.connectedTo(False, True))
        for pair in pairs:
            for endpoint in pair:
                _check_editable_node(om.MFnDependencyNode(endpoint.node()))
                _check_editable_plug(endpoint)
            if pair not in connections:
                connections.append(pair)
    return connections


def direct_curve(
    plug: om.MPlug, *, write: bool = False
) -> oma.MFnAnimCurve | None:
    """Check eligibility for the set_key/set_keys API fast path.

    Other connections and scene states use Maya's setKeyframe value resolution.
    """
    _check_channel_plug(plug, write=write)
    if not om.MItDependencyNodes(om.MFn.kAnimLayer).isDone():
        raise RuntimeError(
            "Direct curve operations do not support scenes with animation layers."
        )
    source = plug.sourceWithConversion()
    if source.isNull:
        return None
    if not source.node().hasFn(om.MFn.kAnimCurve):
        raise RuntimeError(
            f"{plug.name()} requires a directly connected animCurve; upstream traversal is not supported."
        )
    curve = oma.MFnAnimCurve(source.node())
    if (
        not curve.isTimeInput
        or curve.animCurveType != curve.timedAnimCurveTypeForPlug(plug)
        or source != curve.findPlug("output", False)
        or len(source.connectedTo(False, True)) != 1
        or any(p.isDestination for p in curve.getConnections())
        or (
            curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTA
            and curve.findPlug("rotationInterpolation", False).asInt() != 1
        )
    ):
        raise RuntimeError(
            f"{plug.name()} requires a simple, unshared time-input curve of the matching type."
        )
    if write:
        _check_editable_curve(curve)
    return curve


def _check_editable_curve(curve: oma.MFnAnimCurve) -> None:
    _check_editable_node(curve)
    for i in range(curve.attributeCount()):
        attribute = curve.attribute(i)
        if om.MFnAttribute(attribute).parent.isNull():
            _check_editable_plug(curve.findPlug(attribute, False))


def _check_editable_node(node: om.MFnDependencyNode) -> None:
    if node.isLocked or node.isFromReferencedFile:
        raise RuntimeError(
            f"Cannot edit locked or referenced node {node.name()}."
        )


def _check_editable_plug(plug: om.MPlug) -> None:
    if plug.isLocked:
        raise RuntimeError(f"Cannot edit locked plug {plug.name()}.")
    if plug.isArray:
        # animCurve internal arrays do not support physical index access.
        for index in plug.getExistingArrayAttributeIndices():
            _check_editable_plug(plug.elementByLogicalIndex(index))
    elif plug.isCompound:
        for index in range(plug.numChildren()):
            _check_editable_plug(plug.child(index))
