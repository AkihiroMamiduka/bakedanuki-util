"""Resolve a curve separately from key editing and plug-value assignment."""

from __future__ import annotations

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


Target = om.MPlug | CurveTarget


def resolve_curve(
    target: Target, *, write: bool = False
) -> oma.MFnAnimCurve | None:
    if isinstance(target, om.MPlug):
        return direct_curve(target, write=write)
    return explicit_curve(target, write=write)


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
    if (
        curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTA
        and curve.findPlug("rotationInterpolation", False).asInt() != 1
    ):
        raise RuntimeError(
            "Explicit curve operations require independent scalar rotation interpolation."
        )
    for plug in curve.getConnections():
        if (
            plug.isDestination
            and plug != curve.findPlug("input", False)
            and not plug.attribute().hasFn(om.MFn.kMessageAttribute)
        ):
            raise RuntimeError(
                "Explicit curve operations do not support driven curve attributes."
            )
    if write:
        _check_editable_curve(curve)
        _check_owning_layers(curve)
    return curve


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
    """Return a simple direct time-input curve; only an unconnected plug is None.

    Resolve at query time or first edit execution, never across undo/reconnect.
    Layer selection and upstream traversal need their own explicit policies.
    """
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
    if not om.MItDependencyNodes(om.MFn.kAnimLayer).isDone():
        raise RuntimeError(
            "Direct curve operations do not support scenes with animation layers."
        )
    if write:
        _check_editable_node(om.MFnDependencyNode(plug.node()))
        if not om.MFnAttribute(attribute).writable:
            raise RuntimeError(f"{plug.name()} is not writable.")
        _check_editable_plug(plug)
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
