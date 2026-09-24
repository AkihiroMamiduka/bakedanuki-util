"""接線引数の共通処理と複数キーの編集。"""

from __future__ import annotations

import math
from collections.abc import Callable
from typing import ClassVar, Literal, cast

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_target
from .keyframe_data import KeyTangentTypeName

TangentTypeName = Literal[
    "auto",
    "clamped",
    "fast",
    "flat",
    "linear",
    "plateau",
    "slow",
    "spline",
    "step",
    "stepnext",
]
TangentTypeValue = TangentTypeName | int | None


class TangentType:
    auto: ClassVar[int] = oma.MFnAnimCurve.kTangentAuto
    clamped: ClassVar[int] = oma.MFnAnimCurve.kTangentClamped
    fast: ClassVar[int] = oma.MFnAnimCurve.kTangentFast
    flat: ClassVar[int] = oma.MFnAnimCurve.kTangentFlat
    linear: ClassVar[int] = oma.MFnAnimCurve.kTangentLinear
    plateau: ClassVar[int] = oma.MFnAnimCurve.kTangentPlateau
    slow: ClassVar[int] = oma.MFnAnimCurve.kTangentSlow
    spline: ClassVar[int] = oma.MFnAnimCurve.kTangentSmooth
    step: ClassVar[int] = oma.MFnAnimCurve.kTangentStep
    stepnext: ClassVar[int] = oma.MFnAnimCurve.kTangentStepNext


_TANGENT_TYPE_MAP = {
    "auto": TangentType.auto,
    "clamped": TangentType.clamped,
    "fast": TangentType.fast,
    "flat": TangentType.flat,
    "linear": TangentType.linear,
    "plateau": TangentType.plateau,
    "slow": TangentType.slow,
    "spline": TangentType.spline,
    "step": TangentType.step,
    "stepnext": TangentType.stepnext,
}
_VALID_TANGENT_TYPES = set(_TANGENT_TYPE_MAP.values()) | {
    oma.MFnAnimCurve.kTangentGlobal,
}
_TANGENT_TYPE_NAMES = {
    value: name for name, value in _TANGENT_TYPE_MAP.items()
}

Target = tuple[_keyframe_target.Target, om.MPlug]
TargetResolver = Callable[[], tuple[Target, ...]]
LockTargetResolver = Callable[[], tuple[_keyframe_target.Target, ...]]


def to_tangent_type(tangent_type: int | str | None) -> int:
    if tangent_type is None:
        return oma.MFnAnimCurve.kTangentGlobal

    if isinstance(tangent_type, str):
        result = _TANGENT_TYPE_MAP.get(tangent_type.lower())
        if result is not None:
            return result
    elif tangent_type in _VALID_TANGENT_TYPES:
        return tangent_type

    valid_types = ", ".join(sorted(_TANGENT_TYPE_MAP))
    raise ValueError(
        f"Unsupported tangent type: {tangent_type!r}. "
        f"Expected one of: {valid_types}."
    )


def resolve_tangent_types(
    tangent_type: TangentTypeValue,
    in_tangent_type: TangentTypeValue,
    out_tangent_type: TangentTypeValue,
    *,
    default_in: int | None = None,
    default_out: int | None = None,
) -> tuple[int | None, int | None]:
    """共通の接線型に、指定された入出力別の値を上書きして返す。"""
    common = (
        to_tangent_type(tangent_type) if tangent_type is not None else None
    )
    incoming = (
        to_tangent_type(in_tangent_type)
        if in_tangent_type is not None
        else None
    )
    outgoing = (
        to_tangent_type(out_tangent_type)
        if out_tangent_type is not None
        else None
    )

    def side(value: int | None, default: int | None) -> int | None:
        if value is not None:
            return value
        if common is not None:
            return common
        return default

    return side(incoming, default_in), side(outgoing, default_out)


def command_tangent_name(tangent_type: int) -> TangentTypeName | None:
    if tangent_type == oma.MFnAnimCurve.kTangentGlobal:
        return None
    return cast(TangentTypeName, _TANGENT_TYPE_NAMES[tangent_type])


def data_tangent_name(
    tangent_type: int, *, incoming: bool
) -> KeyTangentTypeName:
    if tangent_type != oma.MFnAnimCurve.kTangentGlobal:
        return cast(KeyTangentTypeName, _TANGENT_TYPE_NAMES[tangent_type])
    values = (
        cmds.keyTangent(query=True, g=True, inTangentType=True)
        if incoming
        else cmds.keyTangent(query=True, g=True, outTangentType=True)
    )
    if not isinstance(values, list) or not values:
        raise RuntimeError("The Maya global tangent type is not available.")
    return cast(KeyTangentTypeName, values[0])


def capture_range(
    start_frame: float | None, end_frame: float | None
) -> tuple[float | None, float | None]:
    def seconds(value: float | None) -> float | None:
        if value is None:
            return None
        frame = float(value)
        if not math.isfinite(frame):
            raise ValueError("Keyframe frame must be finite.")
        return om.MTime(frame, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)

    start = seconds(start_frame)
    end = seconds(end_frame)
    if start is not None and end is not None and start > end:
        raise ValueError(
            "start_frame must be less than or equal to end_frame."
        )
    return start, end


def capture_locks(
    tangents_locked: bool | None,
    weights_locked: bool | None,
) -> tuple[bool | None, bool | None]:
    """整数を bool に変換せず、キーごとの接線 lock 値を検証する。"""
    if tangents_locked is not None and type(tangents_locked) is not bool:
        raise TypeError("tangents_locked must be a bool or None.")
    if weights_locked is not None and type(weights_locked) is not bool:
        raise TypeError("weights_locked must be a bool or None.")
    return tangents_locked, weights_locked


def is_discrete(plug: om.MPlug) -> bool:
    attribute = plug.attribute()
    return attribute.hasFn(om.MFn.kEnumAttribute) or (
        attribute.hasFn(om.MFn.kNumericAttribute)
        and om.MFnNumericAttribute(attribute).numericType()
        in (
            om.MFnNumericData.kBoolean,
            om.MFnNumericData.kByte,
            om.MFnNumericData.kChar,
            om.MFnNumericData.kShort,
            om.MFnNumericData.kInt,
            om.MFnNumericData.kLong,
            om.MFnNumericData.kInt64,
        )
    )


def _indices(
    curve: oma.MFnAnimCurve,
    start: float | None,
    end: float | None,
) -> tuple[int, ...]:
    return tuple(
        index
        for index in range(curve.numKeys)
        if (
            (
                start is None
                or curve.input(index).asUnits(om.MTime.kSeconds) >= start
            )
            and (
                end is None
                or curve.input(index).asUnits(om.MTime.kSeconds) <= end
            )
        )
    )


def apply(
    curve: oma.MFnAnimCurve,
    indices: tuple[int, ...],
    in_type: int | None,
    out_type: int | None,
    change: oma.MAnimCurveChange,
) -> None:
    if in_type is not None and out_type is not None:
        curve.setTangentTypes(indices, in_type, out_type, change)
        return
    for index in indices:
        if in_type is not None:
            curve.setInTangentType(index, in_type, change)
        if out_type is not None:
            curve.setOutTangentType(index, out_type, change)


def queue_batch(
    manager: ModifierManager,
    resolve_targets: TargetResolver,
    start: float | None,
    end: float | None,
    in_type: int | None,
    out_type: int | None,
    discrete_type: int | None,
) -> None:
    """選択済みのノードチャンネルへの編集を単一操作として予約する。"""

    def prepare(work: ModifierManager) -> None:
        targets = resolve_targets()

        def edit(change: oma.MAnimCurveChange) -> None:
            plans: list[
                tuple[
                    oma.MFnAnimCurve, tuple[int, ...], int | None, int | None
                ]
            ] = []
            for target, plug in targets:
                if is_discrete(plug):
                    incoming = outgoing = discrete_type
                else:
                    incoming, outgoing = in_type, out_type
                if incoming is None and outgoing is None:
                    continue
                curve = _keyframe_target.resolve_curve(target, write=True)
                if curve is None:
                    continue
                indices = _indices(curve, start, end)
                if indices:
                    plans.append((curve, indices, incoming, outgoing))
            for curve, indices, incoming, outgoing in plans:
                apply(curve, indices, incoming, outgoing, change)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)


def queue_locks(
    manager: ModifierManager,
    resolve_targets: LockTargetResolver,
    start: float | None,
    end: float | None,
    tangents_locked: bool | None,
    weights_locked: bool | None,
) -> None:
    """選択済みカーブの既存キーに対する lock 変更だけを予約する。"""

    def edit(modifier: om.MDGModifier) -> None:
        plans: list[tuple[oma.MFnAnimCurve, tuple[int, ...]]] = []
        for target in resolve_targets():
            curve = _keyframe_target.resolve_curve(target, write=True)
            if curve is None:
                continue
            indices = _indices(curve, start, end)
            if indices:
                plans.append((curve, indices))

        for curve, indices in plans:
            tangent_locks = curve.findPlug("keyTanLocked", False)
            weight_locks = curve.findPlug("keyWeightLocked", False)
            for index in indices:
                if (
                    tangents_locked is not None
                    and curve.tangentsLocked(index) != tangents_locked
                ):
                    modifier.newPlugValueBool(
                        tangent_locks.elementByLogicalIndex(index),
                        tangents_locked,
                    )
                if (
                    weights_locked is not None
                    and curve.weightsLocked(index) != weights_locked
                ):
                    modifier.newPlugValueBool(
                        weight_locks.elementByLogicalIndex(index),
                        weights_locked,
                    )

    # MAnimCurveChange does not restore these two flags in Maya 2025.
    # Their animCurve array plugs provide reliable undo/redo through MDGModifier.
    manager.queue_dg_modifier(edit)
