from __future__ import annotations

import math
from bisect import bisect_left, bisect_right
from dataclasses import replace
from typing import Literal

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_move, _keyframe_target
from ._keyframe_influence import Influence


def _number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    try:
        result = float(value)
    except OverflowError as error:
        raise ValueError(f"{name} must be finite.") from error
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite.")
    return result


def _time(seconds: float) -> om.MTime:
    seconds = _number(seconds, "Keyframe time")
    return _keyframe_move.checked_time(
        om.MTime(seconds, om.MTime.kSeconds), seconds
    )


def _scaled_tangents(
    key: _keyframe_move.CapturedKey, scale: float, weighted: bool
) -> _keyframe_move.CapturedKey:
    def tangent(
        item: tuple[float | om.MAngle, float],
    ) -> tuple[float | om.MAngle, float]:
        x, y = item
        time_output = isinstance(x, om.MAngle)
        if isinstance(x, om.MAngle):
            # TT uses angle/weight because native XY loses time precision.
            angle, weight = x.asRadians(), y
            x, y = math.cos(angle) * weight, math.sin(angle) * weight
        y = _number(y * scale, "Scaled tangent Y")
        length = _number(math.hypot(x, y), "Scaled tangent length")
        if time_output:
            return om.MAngle(math.atan2(y, x), om.MAngle.kRadians), (
                length if weighted else 1.0
            )
        if not weighted:
            # Bulk insertion does not normalize nonweighted tangent vectors.
            return (x / length, y / length) if length else (1.0, 0.0)
        return x, y

    return replace(
        key,
        in_tangent=tangent(key.in_tangent),
        out_tangent=tangent(key.out_tangent),
    )


def _set_value(
    curve: oma.MFnAnimCurve,
    index: int,
    value: float | om.MTime,
    change: oma.MAnimCurveChange,
) -> None:
    if isinstance(value, om.MTime):
        locked = curve.tangentsLocked(index)
        weights_locked = curve.weightsLocked(index)
        breakdown = curve.isBreakdown(index)
        curve.addKey(
            curve.input(index),
            value,
            curve.inTangentType(index),
            curve.outTangentType(index),
            change,
        )
        # addKey updates TT values but resets key flags even at an existing time.
        curve.setTangentsLocked(index, locked, change)
        curve.setWeightsLocked(index, weights_locked, change)
        curve.setIsBreakdown(index, breakdown, change)
    else:
        curve.setValue(index, value, change)


def _edit(
    curve: oma.MFnAnimCurve,
    influence: Influence,
    operation: Literal["set", "add", "scale"],
    amount: float,
    pivot: float,
    rate: float,
    insert_missing: bool,
    change: oma.MAnimCurveChange,
) -> None:
    if (
        not curve.numKeys
        or (operation == "add" and amount == 0)
        or (operation == "scale" and amount == 1)
    ):
        return
    times = [curve.input(i) for i in range(curve.numKeys)]
    low, high = influence.low, influence.high
    missing: list[om.MTime] = []
    if insert_missing:
        for time in influence.boundaries:
            if time is not None and time not in times and time not in missing:
                missing.append(time)
    _keyframe_move.insert_boundaries(curve, missing, change)
    if missing:
        times = [curve.input(i) for i in range(curve.numKeys)]
    first = 0 if low is None else bisect_left(times, low)
    stop = len(times) if high is None else bisect_right(times, high)
    if first == stop:
        return
    unit = 1.0
    if curve.animCurveType == curve.kAnimCurveTA:
        unit = math.pi / 180
    elif curve.animCurveType == curve.kAnimCurveTT:
        unit = rate
    if operation != "scale":
        amount = _number(amount * unit, "Value")
    pivot = _number(pivot * unit, "Pivot value")
    updates: list[tuple[int, _keyframe_move.CapturedKey]] = []
    for index in range(first, stop):
        weight = influence.weight(times[index])
        if weight == 0:
            continue
        key = _keyframe_move.capture_key(curve, index)
        old = key.value
        value = (
            old.asUnits(om.MTime.kSeconds)
            if isinstance(old, om.MTime)
            else old
        )
        if operation == "set":
            value = (1 - weight) * value + weight * amount
        elif operation == "add":
            value += weight * amount
        else:
            scale = _number(
                (1 - weight) + weight * amount, "Effective value scale"
            )
            if scale == 1:
                continue
            value = pivot if scale == 0 else pivot + (value - pivot) * scale
            key = _scaled_tangents(key, scale, curve.isWeighted)
        value = _number(value, "Edited key value")
        new_value = _time(value) if isinstance(old, om.MTime) else value
        if operation == "scale" or new_value != old:
            updates.append((index, replace(key, value=new_value)))
    if operation == "scale" and updates:
        # Native bulk overwrite cannot reliably undo existing keys. Reinsert them.
        for index, _ in reversed(updates):
            curve.remove(index, change)
        _keyframe_move.restore_keys(
            curve,
            tuple(key for _, key in updates),
            tuple(times[index] for index, _ in updates),
            change,
        )
    else:
        for index, key in updates:
            _set_value(curve, index, key.value, change)


def queue_value(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    start_frame: float | None,
    end_frame: float | None,
    *,
    operation: Literal["set", "add", "scale"],
    amount: float,
    pivot_value: float = 0,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
    insert_missing: bool = False,
    single: bool = False,
) -> None:
    if single:
        start_frame = end_frame = _number(start_frame, "frame")
    amount = _number(
        amount,
        {"set": "value", "add": "offset_value", "scale": "value_scale"}[
            operation
        ],
    )
    pivot = _number(pivot_value, "pivot_value")
    if type(insert_missing) is not bool:
        raise TypeError("insert_missing must be a bool.")
    rate = om.MTime(1, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)

    def capture(value: float | None, name: str) -> om.MTime | None:
        return None if value is None else _time(_number(value, name) * rate)

    start, end = capture(start_frame, "start_frame"), capture(
        end_frame, "end_frame"
    )
    fade_start = capture(interpolate_start, "interpolate_start")
    fade_end = capture(interpolate_end, "interpolate_end")
    influence = Influence(start, end, fade_start, fade_end, interpolation)

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = _keyframe_target.resolve_curve(target, write=True)
        if curve is not None:
            _edit(
                curve,
                influence,
                operation,
                amount,
                pivot,
                rate,
                insert_missing,
                change,
            )

    manager.queue_anim_curve_change(edit)
