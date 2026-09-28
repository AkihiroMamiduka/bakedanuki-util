"""整数フレームへの打ち直し前後でカーブ値の誤差上界を検査する。"""

from __future__ import annotations

import math
from bisect import bisect_left, bisect_right

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ._keyframe_error import Bezier, rounding_slack, within_error
from ._keyframe_reduce import CurveKey, capture_curve_key, curve_segment


def _tail_line(
    keys: tuple[CurveKey, ...], mode: int, *, before: bool, scale: float
) -> tuple[float, float, float] | None:
    key = keys[0] if before else keys[-1]
    if len(keys) == 1 or mode == oma.MFnAnimCurve.kConstant:
        return key.time, key.value * scale, 0.0
    if mode != oma.MFnAnimCurve.kLinear:
        return None
    x, y = key.in_xy if before else key.out_xy
    if not math.isfinite(x) or not math.isfinite(y) or x <= 0:
        return None
    return key.time, key.value * scale, y / x * scale


def _line_value(line: tuple[float, float, float], time: float) -> float:
    anchor_time, anchor_value, slope = line
    return anchor_value + slope * (time - anchor_time)


def _line_segment(
    line: tuple[float, float, float], start: float, end: float
) -> Bezier:
    span = end - start
    start_value, end_value = _line_value(line, start), _line_value(line, end)
    return Bezier(
        (start, start + span / 3, end - span / 3, end),
        (
            start_value,
            start_value + (end_value - start_value) / 3,
            end_value - (end_value - start_value) / 3,
            end_value,
        ),
        linear_x=True,
    )


def _repeated_tail_compatible(
    original: tuple[CurveKey, ...],
    result: tuple[CurveKey, ...],
    original_mode: int,
    result_mode: int,
) -> bool:
    repeated = {
        oma.MFnAnimCurve.kCycle,
        oma.MFnAnimCurve.kCycleRelative,
        oma.MFnAnimCurve.kOscillate,
    }
    return (
        original_mode == result_mode
        and original_mode in repeated
        and (
            original[0].time,
            original[0].value,
            original[-1].time,
            original[-1].value,
        )
        == (
            result[0].time,
            result[0].value,
            result[-1].time,
            result[-1].value,
        )
    )


def _tail_within_error(
    original: tuple[CurveKey, ...],
    result: tuple[CurveKey, ...],
    original_mode: int,
    result_mode: int,
    *,
    before: bool,
    scale: float,
    max_deviation: float,
) -> bool:
    if _repeated_tail_compatible(original, result, original_mode, result_mode):
        return True
    old = _tail_line(original, original_mode, before=before, scale=scale)
    new = _tail_line(result, result_mode, before=before, scale=scale)
    if old is None or new is None or old[2] != new[2]:
        return False
    boundary = (
        min(original[0].time, result[0].time)
        if before
        else max(original[-1].time, result[-1].time)
    )
    old_value, new_value = _line_value(old, boundary), _line_value(
        new, boundary
    )
    return abs(old_value - new_value) <= max_deviation + rounding_slack(
        old_value, new_value
    )


def _segments(
    keys: tuple[CurveKey, ...], weighted: bool, scale: float
) -> tuple[Bezier, ...]:
    return tuple(
        curve_segment(a, b, weighted, scale) for a, b in zip(keys, keys[1:])
    )


def _value_at(
    keys: tuple[CurveKey, ...],
    times: tuple[float, ...],
    segments: tuple[Bezier, ...],
    pre_mode: int,
    post_mode: int,
    time: float,
    scale: float,
) -> float | None:
    index = bisect_left(times, time)
    if index < len(keys) and times[index] == time:
        return keys[index].value * scale
    if index == 0 or index == len(keys):
        line = _tail_line(
            keys,
            pre_mode if index == 0 else post_mode,
            before=index == 0,
            scale=scale,
        )
        return None if line is None else _line_value(line, time)
    segment = segments[index - 1]
    return segment.split(time)[0].y[-1] if segment.supported else None


def _piece(
    keys: tuple[CurveKey, ...],
    times: tuple[float, ...],
    segments: tuple[Bezier, ...],
    pre_mode: int,
    post_mode: int,
    start: float,
    end: float,
    scale: float,
) -> Bezier | None:
    index = bisect_right(times, start) - 1
    if index < 0 or index >= len(segments):
        line = _tail_line(
            keys,
            pre_mode if index < 0 else post_mode,
            before=index < 0,
            scale=scale,
        )
        return None if line is None else _line_segment(line, start, end)
    segment = segments[index]
    return segment.clip(start, end) if segment.supported else None


def within_max_deviation(
    curve: oma.MFnAnimCurve,
    original: tuple[CurveKey, ...],
    original_weighted: bool,
    original_pre_infinity: int,
    original_post_infinity: int,
    max_deviation: float,
) -> bool:
    """元と現在のカーブ値を全時刻で比較し、誤差上限を証明できるか返す。"""
    result = tuple(capture_curve_key(curve, i) for i in range(curve.numKeys))
    if not original or not result:
        return not original and not result
    if any(
        not math.isfinite(number)
        for key in (*original, *result)
        for number in (key.time, key.value, *key.in_xy, *key.out_xy)
    ):
        return False
    scale = (
        180.0 / math.pi if curve.animCurveType == curve.kAnimCurveTA else 1.0
    )
    if len(original) == len(result) == 1:
        old_value, new_value = (
            original[0].value * scale,
            result[0].value * scale,
        )
        return abs(old_value - new_value) <= max_deviation + rounding_slack(
            old_value, new_value
        )
    if len(original) == 1 or len(result) == 1:
        return False

    old_pre, new_pre = original_pre_infinity, curve.preInfinityType
    old_post, new_post = original_post_infinity, curve.postInfinityType
    if not _tail_within_error(
        original,
        result,
        old_pre,
        new_pre,
        before=True,
        scale=scale,
        max_deviation=max_deviation,
    ) or not _tail_within_error(
        original,
        result,
        old_post,
        new_post,
        before=False,
        scale=scale,
        max_deviation=max_deviation,
    ):
        return False

    old_segments = _segments(original, original_weighted, scale)
    new_segments = _segments(result, curve.isWeighted, scale)
    old_times = tuple(key.time for key in original)
    new_times = tuple(key.time for key in result)
    times = tuple(sorted({*old_times, *new_times}))
    for time in times:
        expected = _value_at(
            original, old_times, old_segments, old_pre, old_post, time, scale
        )
        if expected is None:
            return False
        actual = curve.evaluate(om.MTime(time, om.MTime.kSeconds)) * scale
        if abs(actual - expected) > max_deviation + rounding_slack(
            actual, expected
        ):
            return False
    for start, end in zip(times, times[1:]):
        old = _piece(
            original,
            old_times,
            old_segments,
            old_pre,
            old_post,
            start,
            end,
            scale,
        )
        new = _piece(
            result,
            new_times,
            new_segments,
            new_pre,
            new_post,
            start,
            end,
            scale,
        )
        if (
            old is None
            or new is None
            or not within_error(old, new, max_deviation)
        ):
            return False
    return True
