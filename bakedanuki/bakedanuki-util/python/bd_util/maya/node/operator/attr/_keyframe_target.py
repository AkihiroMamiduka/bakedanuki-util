"""Resolve a curve separately from key editing and plug-value assignment."""

from __future__ import annotations

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma


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
        _check_editable_node(curve)
        for i in range(curve.attributeCount()):
            curve_attribute = curve.attribute(i)
            if om.MFnAttribute(curve_attribute).parent.isNull():
                _check_editable_plug(curve.findPlug(curve_attribute, False))
    return curve


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
