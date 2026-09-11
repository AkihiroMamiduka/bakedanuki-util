"""単純な直接接続カーブのsnapshotと、ModifierManager経由の復元。"""

from __future__ import annotations

import math
from typing import cast

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from .keyframe_data import (
    AnimCurveData,
    CurveTypeName,
    InfinityTypeName,
    KeyData,
    KeyTangentTypeName,
    copy_curve_data,
    weighted_tangent_xy,
)

_CURVES = {
    "animCurveTA": oma.MFnAnimCurve.kAnimCurveTA,
    "animCurveTL": oma.MFnAnimCurve.kAnimCurveTL,
    "animCurveTU": oma.MFnAnimCurve.kAnimCurveTU,
}
_TANGENTS = {
    "fixed": oma.MFnAnimCurve.kTangentFixed,
    "auto": oma.MFnAnimCurve.kTangentAuto,
    "clamped": oma.MFnAnimCurve.kTangentClamped,
    "fast": oma.MFnAnimCurve.kTangentFast,
    "flat": oma.MFnAnimCurve.kTangentFlat,
    "linear": oma.MFnAnimCurve.kTangentLinear,
    "plateau": oma.MFnAnimCurve.kTangentPlateau,
    "slow": oma.MFnAnimCurve.kTangentSlow,
    "spline": oma.MFnAnimCurve.kTangentSmooth,
    "step": oma.MFnAnimCurve.kTangentStep,
    "stepnext": oma.MFnAnimCurve.kTangentStepNext,
    "autocustom": oma.MFnAnimCurve.kTangentAutoCustom,
    "autoease": oma.MFnAnimCurve.kTangentAutoEase,
    "automix": oma.MFnAnimCurve.kTangentAutoMix,
}
_INFINITY = {
    "constant": oma.MFnAnimCurve.kConstant,
    "linear": oma.MFnAnimCurve.kLinear,
    "cycle": oma.MFnAnimCurve.kCycle,
    "cycleRelative": oma.MFnAnimCurve.kCycleRelative,
    "oscillate": oma.MFnAnimCurve.kOscillate,
}


def curve_type_for_plug(plug: om.MPlug) -> CurveTypeName:
    if plug.isArray or plug.isCompound:
        raise RuntimeError("Curve data requires a scalar plug.")
    attr = plug.attribute()
    if not (
        attr.hasFn(om.MFn.kNumericAttribute)
        or attr.hasFn(om.MFn.kUnitAttribute)
    ):
        raise RuntimeError(
            "Curve data requires a numeric, angle or distance plug."
        )
    curve_type = oma.MFnAnimCurve().timedAnimCurveTypeForPlug(plug)
    for name, enum in _CURVES.items():
        if curve_type == enum:
            return cast(CurveTypeName, name)
    raise RuntimeError(
        "Only animCurveTA / TL / TU are supported by curve data."
    )


def _check_editable_plug(plug: om.MPlug) -> None:
    if plug.isLocked:
        raise RuntimeError(
            f"Cannot restore curve data: {plug.name()} is locked."
        )
    if plug.isArray:
        # animCurveのinternal arrayはphysical indexアクセスを受け付けない。
        for i in plug.getExistingArrayAttributeIndices():
            _check_editable_plug(plug.elementByLogicalIndex(i))
    elif plug.isCompound:
        for i in range(plug.numChildren()):
            _check_editable_plug(plug.child(i))


def direct_curve(
    plug: om.MPlug, *, write: bool = False
) -> oma.MFnAnimCurve | None:
    expected = curve_type_for_plug(plug)
    if not om.MItDependencyNodes(om.MFn.kAnimLayer).isDone():
        raise RuntimeError(
            "Curve data does not support scenes with animation layers."
        )
    if write:
        node = om.MFnDependencyNode(plug.node())
        if (
            node.isLocked
            or node.isFromReferencedFile
            or not om.MFnAttribute(plug.attribute()).writable
        ):
            raise RuntimeError(
                "Curve data destination must be writable, local and unlocked."
            )
        _check_editable_plug(plug)
    source = plug.sourceWithConversion()
    if source.isNull:
        return None
    if not source.node().hasFn(om.MFn.kAnimCurve):
        raise RuntimeError(
            "Curve data requires a directly connected animCurve."
        )
    curve = oma.MFnAnimCurve(source.node())
    if (
        curve.animCurveType != _CURVES[expected]
        or source != curve.findPlug("output", False)
        or len(source.connectedTo(False, True)) != 1
        or any(p.isDestination for p in curve.getConnections())
        or (
            expected == "animCurveTA"
            and curve.findPlug("rotationInterpolation", False).asInt() != 1
        )
    ):
        raise RuntimeError(
            "Curve data requires a simple, unshared time-input curve."
        )
    if write:
        if curve.isLocked or curve.isFromReferencedFile:
            raise RuntimeError(
                "Curve data cannot edit locked or referenced curves."
            )
        for i in range(curve.attributeCount()):
            attribute = curve.attribute(i)
            if om.MFnAttribute(attribute).parent.isNull():
                _check_editable_plug(curve.findPlug(attribute, False))
    return curve


def queue_weighted(
    manager: ModifierManager, plug: om.MPlug, weighted: object
) -> None:
    if not isinstance(weighted, bool):
        raise TypeError("weighted must be a bool.")
    curve_type_for_plug(plug)

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = direct_curve(plug, write=True)
        if curve is None:
            raise RuntimeError(
                "No directly connected animCurve to set weighted."
            )
        if curve.isWeighted != weighted:
            curve.setIsWeighted(weighted, change)

    manager.queue_anim_curve_change(edit)


def capture_curve(plug: om.MPlug) -> AnimCurveData | None:
    unit = om.MTime.uiUnit()
    curve = direct_curve(plug)
    if curve is None:
        return None
    tangent_names = {value: name for name, value in _TANGENTS.items()}
    infinity_names = {value: name for name, value in _INFINITY.items()}
    scale = (
        180.0 / math.pi
        if curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTA
        else 1.0
    )
    keys: list[KeyData] = []
    for i in range(curve.numKeys):
        try:
            in_type = tangent_names[curve.inTangentType(i)]
            out_type = tangent_names[curve.outTangentType(i)]
        except KeyError as exc:
            raise RuntimeError(
                "Curve data does not support this custom tangent type."
            ) from exc
        in_x, in_y = curve.getTangentXY(i, True)
        out_x, out_y = curve.getTangentXY(i, False)
        if not curve.isWeighted:
            in_span = (
                (curve.input(i) - curve.input(i - 1)).asUnits(
                    om.MTime.kSeconds
                )
                if i > 0
                else None
            )
            out_span = (
                (curve.input(i + 1) - curve.input(i)).asUnits(
                    om.MTime.kSeconds
                )
                if i + 1 < curve.numKeys
                else None
            )
            in_x, in_y = weighted_tangent_xy((in_x, in_y), in_span)
            out_x, out_y = weighted_tangent_xy((out_x, out_y), out_span)
        keys.append(
            KeyData(
                frame=curve.input(i).asUnits(unit),
                value=curve.value(i) * scale,
                in_tangent_type=cast(KeyTangentTypeName, in_type),
                out_tangent_type=cast(KeyTangentTypeName, out_type),
                in_tangent_xy=(in_x, in_y * scale),
                out_tangent_xy=(out_x, out_y * scale),
                tangents_locked=curve.tangentsLocked(i),
                weights_locked=curve.weightsLocked(i),
                breakdown=curve.isBreakdown(i),
            )
        )
    return AnimCurveData(
        curve_type=curve_type_for_plug(plug),
        seconds_per_frame=om.MTime(1.0, unit).asUnits(om.MTime.kSeconds),
        weighted=curve.isWeighted,
        pre_infinity=cast(
            InfinityTypeName, infinity_names[curve.preInfinityType]
        ),
        post_infinity=cast(
            InfinityTypeName, infinity_names[curve.postInfinityType]
        ),
        keys=tuple(keys),
    )


def queue_restore(
    manager: ModifierManager,
    plug: om.MPlug,
    data: object,
    *,
    replace: bool,
) -> None:
    data = copy_curve_data(data)
    if data.curve_type != curve_type_for_plug(plug):
        raise ValueError(
            "AnimCurveData curve_type does not match the destination plug."
        )
    times = tuple(
        om.MTime(key.frame * data.seconds_per_frame, om.MTime.kSeconds)
        for key in data.keys
    )
    if any(a >= b for a, b in zip(times, times[1:])):
        raise ValueError("KeyData frames coincide at Maya time precision.")
    curve: oma.MFnAnimCurve | None = None
    created = False

    def prepare(modifier: om.MDGModifier) -> None:
        nonlocal curve, created
        curve = direct_curve(plug, write=True)
        if curve is not None:
            return
        obj = modifier.createNode(data.curve_type)
        created_curve = oma.MFnAnimCurve(obj)
        modifier.connect(created_curve.findPlug("output", False), plug)
        curve = created_curve
        created = True

    def restore(change: oma.MAnimCurveChange) -> None:
        if curve is None:
            raise RuntimeError("Curve data destination was not prepared.")
        if replace:
            for i in reversed(range(curve.numKeys)):
                curve.remove(i, change)
        if replace or created:
            weighted = data.weighted if replace else False
            if curve.isWeighted != weighted:
                curve.setIsWeighted(weighted, change)
        scale = math.pi / 180.0 if data.curve_type == "animCurveTA" else 1.0
        indices: list[int] = []
        for key, time in zip(data.keys, times):
            indices.append(
                curve.addKey(
                    time,
                    key.value * scale,
                    oma.MFnAnimCurve.kTangentFixed,
                    oma.MFnAnimCurve.kTangentFixed,
                    change,
                )
            )
        for key, i in zip(data.keys, indices):
            curve.setTangentsLocked(i, False, change)
            curve.setWeightsLocked(i, False, change)
            for is_in, xy, tangent_type in (
                (True, key.in_tangent_xy, key.in_tangent_type),
                (False, key.out_tangent_xy, key.out_tangent_type),
            ):
                curve.setTangent(
                    i,
                    xy[0],
                    xy[1] * scale,
                    is_in,
                    change=change,
                    convertUnits=False,
                )
                setter = (
                    curve.setInTangentType
                    if is_in
                    else curve.setOutTangentType
                )
                setter(i, _TANGENTS[tangent_type], change)
            curve.setIsBreakdown(i, key.breakdown, change)
        for key, i in zip(data.keys, indices):
            curve.setWeightsLocked(i, key.weights_locked, change)
            curve.setTangentsLocked(i, key.tangents_locked, change)
        if replace:
            curve.setPreInfinityType(_INFINITY[data.pre_infinity], change)
            curve.setPostInfinityType(_INFINITY[data.post_infinity], change)

    manager.queue_dg_modifier(prepare)
    manager.queue_anim_curve_change(restore)
