"""元カーブとの誤差と手動接線を検査してキー削減を予約する。"""

from __future__ import annotations

import math
from bisect import bisect_left, bisect_right
from collections.abc import Callable
from dataclasses import dataclass

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_snapshot, _keyframe_target
from ._keyframe_error import Bezier, rounding_slack, within_error

_SUPPORTED_TANGENTS = {
    oma.MFnAnimCurve.kTangentFixed,
    oma.MFnAnimCurve.kTangentLinear,
    oma.MFnAnimCurve.kTangentFlat,
    oma.MFnAnimCurve.kTangentSmooth,
    oma.MFnAnimCurve.kTangentStep,
    oma.MFnAnimCurve.kTangentStepNext,
    oma.MFnAnimCurve.kTangentSlow,
    oma.MFnAnimCurve.kTangentFast,
    oma.MFnAnimCurve.kTangentClamped,
    oma.MFnAnimCurve.kTangentPlateau,
    oma.MFnAnimCurve.kTangentAuto,
    oma.MFnAnimCurve.kTangentAutoMix,
    oma.MFnAnimCurve.kTangentAutoEase,
    oma.MFnAnimCurve.kTangentAutoCustom,
}


@dataclass(frozen=True, slots=True)
class _Key:
    time: float
    value: float
    in_type: int
    out_type: int
    in_xy: tuple[float, float]
    out_xy: tuple[float, float]
    tangents_locked: bool
    weights_locked: bool
    breakdown: bool


@dataclass(frozen=True, slots=True)
class _ReductionPlan:
    curve: oma.MFnAnimCurve
    original: tuple[_Key, ...]
    times: tuple[float, ...]
    removed: tuple[float, ...]
    start: float
    end: float
    tolerance: float
    scale: float


def _key(curve: oma.MFnAnimCurve, i: int) -> _Key:
    return _Key(
        curve.input(i).asUnits(om.MTime.kSeconds),
        curve.value(i),
        curve.inTangentType(i),
        curve.outTangentType(i),
        curve.getTangentXY(i, True),
        curve.getTangentXY(i, False),
        curve.tangentsLocked(i),
        curve.weightsLocked(i),
        curve.isBreakdown(i),
    )


def _same_numbers(a: tuple[float, ...], b: tuple[float, ...]) -> bool:
    return all(abs(x - y) <= rounding_slack(x, y) for x, y in zip(a, b))


def _preserved(before: _Key, after: _Key) -> bool:
    if (
        before.time,
        before.value,
        before.in_type,
        before.out_type,
        before.tangents_locked,
        before.weights_locked,
        before.breakdown,
    ) != (
        after.time,
        after.value,
        after.in_type,
        after.out_type,
        after.tangents_locked,
        after.weights_locked,
        after.breakdown,
    ):
        return False
    return (
        before.in_type != oma.MFnAnimCurve.kTangentFixed
        or _same_numbers(before.in_xy, after.in_xy)
    ) and (
        before.out_type != oma.MFnAnimCurve.kTangentFixed
        or _same_numbers(before.out_xy, after.out_xy)
    )


def _segment(a: _Key, b: _Key, weighted: bool, scale: float) -> Bezier:
    span = b.time - a.time
    x = (a.time, a.time + span / 3, b.time - span / 3, b.time)
    if a.out_type in (
        oma.MFnAnimCurve.kTangentStep,
        oma.MFnAnimCurve.kTangentStepNext,
    ):
        value = (
            a.value if a.out_type == oma.MFnAnimCurve.kTangentStep else b.value
        )
        value *= scale
        return Bezier(x, (value, value, value, value), linear_x=True)
    out_x, out_y = a.out_xy
    in_x, in_y = b.in_xy
    valid = span > 0
    if weighted:
        x = (a.time, a.time + out_x / 3, b.time - in_x / 3, b.time)
        valid = valid and all(left <= right for left, right in zip(x, x[1:]))
    elif out_x > 0 and in_x > 0:
        out_y *= span / out_x
        in_y *= span / in_x
    else:
        valid = False
    y = (
        a.value * scale,
        (a.value + out_y / 3) * scale,
        (b.value - in_y / 3) * scale,
        b.value * scale,
    )
    return Bezier(
        x, y, valid and all(math.isfinite(v) for v in (*x, *y)), not weighted
    )


def _copy_keys(curve: oma.MFnAnimCurve, keys: tuple[_Key, ...]) -> None:
    for key in keys:
        curve.addKey(
            om.MTime(key.time, om.MTime.kSeconds),
            key.value,
            curve.kTangentFixed,
            curve.kTangentFixed,
        )
    for i, key in enumerate(keys):
        curve.setTangentsLocked(i, False)
        curve.setWeightsLocked(i, False)
        curve.setTangent(i, *key.in_xy, True, convertUnits=False)
        curve.setTangent(i, *key.out_xy, False, convertUnits=False)
        curve.setInTangentType(i, key.in_type)
        curve.setOutTangentType(i, key.out_type)
        curve.setIsBreakdown(i, key.breakdown)
    for i, key in enumerate(keys):
        curve.setWeightsLocked(i, key.weights_locked)
        curve.setTangentsLocked(i, key.tangents_locked)


def _compare(
    curve: oma.MFnAnimCurve,
    keys: list[_Key],
    original: tuple[_Key, ...],
    original_times: tuple[float, ...],
    original_segments: tuple[Bezier, ...],
    scale: float,
    start: float,
    end: float,
    tolerance: float,
) -> bool:
    for a, b in zip(keys, keys[1:]):
        segment = _segment(a, b, curve.isWeighted, scale)
        first = max(0, bisect_right(original_times, a.time) - 1)
        stop = min(len(original_segments), bisect_left(original_times, b.time))
        for i in range(first, stop):
            source = original_segments[i]
            left, right = max(a.time, source.x[0]), min(b.time, source.x[-1])
            if source == segment:
                continue
            if not source.supported or not segment.supported:
                return False
            bounds = sorted(
                {left, right, *(t for t in (start, end) if left < t < right)}
            )
            for low, high in zip(bounds, bounds[1:]):
                limit = tolerance if low >= start and high <= end else 0.0
                if not within_error(
                    source.clip(low, high), segment.clip(low, high), limit
                ):
                    return False
        # step / stepnext区間の片側極限とは別に、実在キー時刻の値も比較する。
        for i in range(
            bisect_left(original_times, a.time),
            bisect_right(original_times, b.time),
        ):
            key = original[i]
            actual = (
                curve.evaluate(om.MTime(key.time, om.MTime.kSeconds)) * scale
            )
            expected = key.value * scale
            limit = tolerance if start <= key.time <= end else 0.0
            if abs(actual - expected) > limit + rounding_slack(
                actual, expected
            ):
                return False
    return True


def _linear_infinity_preserved(
    curve: oma.MFnAnimCurve, original: tuple[_Key, ...]
) -> bool:
    for index, xy, mode, is_in in (
        (0, original[0].in_xy, curve.preInfinityType, True),
        (
            curve.numKeys - 1,
            original[-1].out_xy,
            curve.postInfinityType,
            False,
        ),
    ):
        if mode == curve.kLinear:
            current = curve.getTangentXY(index, is_in)
            if not _same_numbers(
                (math.atan2(xy[1], xy[0]),),
                (math.atan2(current[1], current[0]),),
            ):
                return False
    return True


def _plan(
    source: oma.MFnAnimCurve,
    original: tuple[_Key, ...],
    first: int,
    stop: int,
    start: float,
    end: float,
    tolerance: float,
    preserve_breakdowns: bool,
    scale: float,
) -> list[float]:
    original_times = tuple(key.time for key in original)
    segments = tuple(
        _segment(a, b, source.isWeighted, scale)
        for a, b in zip(original, original[1:])
    )
    protected = {original[first].time, original[stop - 1].time}
    for a, b in zip(original, original[1:]):
        if (
            a.out_type in (source.kTangentStep, source.kTangentStepNext)
            and a.value != b.value
        ):
            protected.update((a.time, b.time))
    modified = cmds.file(query=True, modified=True)
    modifier = om.MDGModifier()
    work = oma.MFnAnimCurve(modifier.createNode(source.typeName))
    trial = oma.MAnimCurveChange()
    try:
        work.setIsWeighted(source.isWeighted)
        work.setPreInfinityType(source.preInfinityType)
        work.setPostInfinityType(source.postInfinityType)
        _copy_keys(work, original)
        baseline = {
            key.time: key
            for key in (_key(work, i) for i in range(work.numKeys))
        }
        removed: list[float] = []
        for key in original[first + 1 : stop - 1]:
            if key.time in protected or (
                preserve_breakdowns and key.breakdown
            ):
                continue
            index = work.find(om.MTime(key.time, om.MTime.kSeconds))
            if index is None:
                raise RuntimeError(
                    "A reduction candidate disappeared from the working curve."
                )
            trial = oma.MAnimCurveChange()
            work.remove(index, trial)
            neighbors = [
                _key(work, i)
                for i in range(max(0, index - 2), min(work.numKeys, index + 2))
            ]
            accepted = (
                all(_preserved(baseline[k.time], k) for k in neighbors)
                and _linear_infinity_preserved(work, original)
                and _compare(
                    work,
                    neighbors,
                    original,
                    original_times,
                    segments,
                    scale,
                    start,
                    end,
                    tolerance,
                )
            )
            if accepted:
                removed.append(key.time)
            else:
                trial.undoIt()
        return removed
    finally:
        del trial, work, modifier
        if not modified:
            cmds.file(modified=False)


def _plan_curve(
    curve: oma.MFnAnimCurve,
    start: om.MTime | None,
    end: om.MTime | None,
    tolerance: float,
    preserve_breakdowns: bool,
) -> _ReductionPlan | None:
    if curve.numKeys < 3:
        return None
    original = tuple(_key(curve, i) for i in range(curve.numKeys))
    times = tuple(key.time for key in original)
    low = times[0] if start is None else start.asUnits(om.MTime.kSeconds)
    high = times[-1] if end is None else end.asUnits(om.MTime.kSeconds)
    first, stop = bisect_left(times, low), bisect_right(times, high)
    if stop - first < 3:
        return None
    if any(
        not math.isfinite(value)
        for key in original
        for value in (key.time, key.value, *key.in_xy, *key.out_xy)
    ):
        raise RuntimeError(
            "Key reduction requires finite key values and tangents."
        )
    if any(
        key.in_type not in _SUPPORTED_TANGENTS
        or key.out_type not in _SUPPORTED_TANGENTS
        for key in original
    ):
        raise RuntimeError(
            "Key reduction does not support custom tangent types."
        )
    scale = (
        180.0 / math.pi if curve.animCurveType == curve.kAnimCurveTA else 1.0
    )
    removed = _plan(
        curve,
        original,
        first,
        stop,
        low,
        high,
        tolerance,
        preserve_breakdowns,
        scale,
    )
    if not removed:
        return None
    return _ReductionPlan(
        curve,
        original,
        times,
        tuple(removed),
        low,
        high,
        tolerance,
        scale,
    )


def _apply_plan(plan: _ReductionPlan, change: oma.MAnimCurveChange) -> None:
    curve = plan.curve
    for time in plan.removed:
        index = curve.find(om.MTime(time, om.MTime.kSeconds))
        if index is None:
            raise RuntimeError(
                "A reduction candidate disappeared from the target curve."
            )
        curve.remove(index, change)
    remaining = [_key(curve, i) for i in range(curve.numKeys)]
    source_by_time = {key.time: key for key in plan.original}
    segments = tuple(
        _segment(a, b, curve.isWeighted, plan.scale)
        for a, b in zip(plan.original, plan.original[1:])
    )
    if (
        not all(_preserved(source_by_time[k.time], k) for k in remaining)
        or not _linear_infinity_preserved(curve, plan.original)
        or not _compare(
            curve,
            remaining,
            plan.original,
            plan.times,
            segments,
            plan.scale,
            plan.start,
            plan.end,
            plan.tolerance,
        )
    ):
        raise RuntimeError(
            "Key reduction could not preserve the requested curve error or key metadata."
        )


def reduce_curve(
    curve: oma.MFnAnimCurve,
    start: om.MTime | None,
    end: om.MTime | None,
    tolerance: float,
    preserve_breakdowns: bool,
    change: oma.MAnimCurveChange,
) -> None:
    plan = _plan_curve(curve, start, end, tolerance, preserve_breakdowns)
    if plan is not None:
        _apply_plan(plan, change)


def validate_options(tolerance: object, preserve_breakdowns: bool) -> float:
    if isinstance(tolerance, bool) or not isinstance(tolerance, (float, int)):
        raise TypeError("tolerance must be a number.")
    tolerance = float(tolerance)
    if not math.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and nonnegative.")
    if type(preserve_breakdowns) is not bool:
        raise TypeError("preserve_breakdowns must be a bool.")
    return tolerance


def _capture_options(
    start_frame: float | None,
    end_frame: float | None,
    tolerance: object,
    preserve_breakdowns: bool,
) -> tuple[om.MTime | None, om.MTime | None, float]:
    tolerance = validate_options(tolerance, preserve_breakdowns)
    unit = om.MTime.uiUnit()

    def capture(frame: float | None) -> om.MTime | None:
        if frame is None:
            return None
        value = float(frame)
        if not math.isfinite(value):
            raise ValueError("Keyframe bounds must be finite.")
        time = om.MTime(value, unit)
        expected = value * om.MTime(1, unit).asUnits(om.MTime.kSeconds)
        if not math.isclose(
            time.asUnits(om.MTime.kSeconds),
            expected,
            rel_tol=1e-12,
            abs_tol=1e-8,
        ):
            raise ValueError(
                "Keyframe bounds exceed Maya's representable time range."
            )
        return time

    start, end = capture(start_frame), capture(end_frame)
    if start is not None and end is not None and start > end:
        raise ValueError(
            "start_frame must be less than or equal to end_frame."
        )
    return start, end, tolerance


def queue_reduce(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    start_frame: float | None,
    end_frame: float | None,
    tolerance: object,
    preserve_breakdowns: bool,
) -> None:
    start, end, tolerance = _capture_options(
        start_frame, end_frame, tolerance, preserve_breakdowns
    )

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = _keyframe_snapshot.resolve_curve(target, write=True)
        if curve is not None:
            reduce_curve(
                curve, start, end, tolerance, preserve_breakdowns, change
            )

    manager.queue_anim_curve_change(edit)


def queue_reduce_batch(
    manager: ModifierManager,
    resolve_targets: Callable[[], tuple[_keyframe_target.Target, ...]],
    start_frame: float | None,
    end_frame: float | None,
    tolerance: object,
    preserve_breakdowns: bool,
) -> None:
    """全対象の処理を組み立てた後、キー削減を単一操作として予約する。"""
    start, end, tolerance = _capture_options(
        start_frame, end_frame, tolerance, preserve_breakdowns
    )

    def prepare(work: ModifierManager) -> None:
        curves: list[oma.MFnAnimCurve] = []
        handles: set[om.MObjectHandle] = set()
        for target in resolve_targets():
            curve = _keyframe_snapshot.resolve_curve(target, write=True)
            if curve is None:
                continue
            handle = om.MObjectHandle(curve.object())
            if handle not in handles:
                handles.add(handle)
                curves.append(curve)

        plans = tuple(
            plan
            for curve in curves
            if (
                plan := _plan_curve(
                    curve, start, end, tolerance, preserve_breakdowns
                )
            )
            is not None
        )

        def edit(change: oma.MAnimCurveChange) -> None:
            for plan in plans:
                _apply_plan(plan, change)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)
