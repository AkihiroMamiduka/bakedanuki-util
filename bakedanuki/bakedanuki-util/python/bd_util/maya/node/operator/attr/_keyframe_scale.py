from __future__ import annotations

import math
from bisect import bisect_left, bisect_right
from dataclasses import replace
from typing import Literal

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_move, _keyframe_target


def _number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite.")
    return value


def _positive(value: object, name: str) -> float:
    value = _number(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be positive.")
    return value


def _time(seconds: float) -> om.MTime:
    seconds = _number(seconds, "Keyframe time")
    return _keyframe_move.checked_time(
        om.MTime(seconds, om.MTime.kSeconds), seconds
    )


def _placement(
    start: om.MTime,
    end: om.MTime,
    time_scale: float | None,
    duration: float | None,
    offset: float | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
) -> tuple[float, om.MTime, om.MTime]:
    first, last = (t.asUnits(om.MTime.kSeconds) for t in (start, end))
    source_duration = last - first
    fit = to_start is not None and to_end is not None
    if fit or duration is not None:
        if source_duration <= 0:
            raise ValueError(
                "Cannot fit a zero-width key range to a duration or range."
            )
        if fit:
            assert to_start is not None and to_end is not None
            duration = to_end.asUnits(om.MTime.kSeconds) - to_start.asUnits(
                om.MTime.kSeconds
            )
        assert duration is not None
        time_scale = _positive(duration / source_duration, "time_scale")
    assert time_scale is not None
    length = _number(source_duration * time_scale, "Scaled duration")
    low = first if to_start is None else to_start.asUnits(om.MTime.kSeconds)
    if offset is not None:
        low += offset
    high = (
        low + length if to_end is None else to_end.asUnits(om.MTime.kSeconds)
    )
    if to_end is not None and not fit:
        low = high - length
    destination_start, destination_end = _time(low), _time(high)
    if start < end and destination_start >= destination_end:
        raise ValueError("Scaled key range collapses at Maya time precision.")
    return time_scale, destination_start, destination_end


def _scaled_key(
    key: _keyframe_move.CapturedKey, scale: float
) -> _keyframe_move.CapturedKey:
    def tangent(
        item: tuple[float | om.MAngle, float],
    ) -> tuple[float | om.MAngle, float]:
        x, y = item
        if isinstance(x, om.MAngle):
            # TT uses angle/weight because native XY loses time precision.
            angle, weight = x.asRadians(), y
            x, y = math.cos(angle) * weight * scale, math.sin(angle) * weight
            weight = _number(math.hypot(x, y), "Scaled tangent weight")
            return om.MAngle(math.atan2(y, x), om.MAngle.kRadians), weight
        return _number(x * scale, "Scaled tangent X"), y

    return replace(
        key,
        in_tangent=tangent(key.in_tangent),
        out_tangent=tangent(key.out_tangent),
    )


def _scale(
    curve: oma.MFnAnimCurve,
    start: om.MTime | None,
    end: om.MTime | None,
    *,
    time_scale: float | None,
    duration: float | None,
    offset: float | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
    mode: Literal["replace_range", "merge"],
    insert_missing: bool,
    change: oma.MAnimCurveChange,
) -> None:
    if not curve.numKeys:
        return
    times = [curve.input(i) for i in range(curve.numKeys)]
    first = 0 if start is None else bisect_left(times, start)
    stop = len(times) if end is None else bisect_right(times, end)
    selected = times[first:stop]
    missing: list[om.MTime] = []
    if insert_missing:
        for boundary in (start, end):
            if boundary is not None and boundary not in selected:
                selected.insert(bisect_left(selected, boundary), boundary)
                missing.append(boundary)
    if not selected:
        return
    source_start = selected[0] if start is None else start
    source_end = selected[-1] if end is None else end
    scale, destination_start, destination_end = _placement(
        source_start,
        source_end,
        time_scale,
        duration,
        offset,
        to_start,
        to_end,
    )
    # Derived scales may differ from one only due to seconds conversion rounding.
    if (
        (time_scale is None or scale == 1)
        and source_start == destination_start
        and source_end == destination_end
    ):
        return

    def destination(time: om.MTime) -> om.MTime:
        if time == source_start:
            return destination_start
        if time == source_end:
            return destination_end
        return _time(
            destination_start.asUnits(om.MTime.kSeconds)
            + (
                time.asUnits(om.MTime.kSeconds)
                - source_start.asUnits(om.MTime.kSeconds)
            )
            * scale
        )

    destinations = tuple(destination(time) for time in selected)
    if any(a >= b for a, b in zip(destinations, destinations[1:])):
        raise ValueError("Scaled keys coincide at Maya time precision.")
    _keyframe_move.insert_boundaries(curve, missing, change)
    times = [curve.input(i) for i in range(curve.numKeys)]
    first = 0 if start is None else bisect_left(times, start)
    stop = len(times) if end is None else bisect_right(times, end)
    if times[first:stop] != selected:
        raise RuntimeError("Maya did not insert the requested boundary keys.")
    keys = tuple(
        _scaled_key(_keyframe_move.capture_key(curve, i), scale)
        for i in range(first, stop)
    )
    removed = set(range(first, stop))
    if mode == "replace_range":
        removed.update(
            range(
                bisect_left(times, destination_start),
                bisect_right(times, destination_end),
            )
        )
    else:
        removed.update(
            index
            for time in destinations
            if (index := curve.find(time)) is not None
        )
    for index in sorted(removed, reverse=True):
        curve.remove(index, change)
    _keyframe_move.restore_keys(curve, keys, destinations, change)
    if any(curve.find(time) is None for time in destinations):
        raise RuntimeError("Maya did not restore the scaled keys.")


def queue_scale(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    start_frame: float | None,
    end_frame: float | None,
    *,
    time_scale: float | None,
    duration_frames: float | None,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    mode: Literal["replace_range", "merge"],
    insert_missing: bool,
) -> None:
    fit = to_start_frame is not None and to_end_frame is not None
    if sum((time_scale is not None, duration_frames is not None, fit)) != 1:
        raise ValueError(
            "Specify exactly one of time_scale, duration_frames, or both target bounds."
        )
    if offset_frames is not None and (
        to_start_frame is not None or to_end_frame is not None
    ):
        raise ValueError(
            "offset_frames cannot be combined with target bounds."
        )
    if mode not in ("replace_range", "merge"):
        raise ValueError("mode must be 'replace_range' or 'merge'.")
    if type(insert_missing) is not bool:
        raise TypeError("insert_missing must be a bool.")
    rate = om.MTime(1, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)

    def capture(value: float | None, name: str) -> om.MTime | None:
        return None if value is None else _time(_number(value, name) * rate)

    start, end = capture(start_frame, "start_frame"), capture(
        end_frame, "end_frame"
    )
    to_start, to_end = capture(to_start_frame, "to_start_frame"), capture(
        to_end_frame, "to_end_frame"
    )
    offset_time = capture(offset_frames, "offset_frames")
    offset = (
        None if offset_time is None else offset_time.asUnits(om.MTime.kSeconds)
    )
    duration = (
        None
        if duration_frames is None
        else _positive(duration_frames, "duration_frames") * rate
    )
    if duration is not None:
        _time(duration)
    if time_scale is not None:
        time_scale = _positive(time_scale, "time_scale")
    if start is not None and end is not None and start > end:
        raise ValueError(
            "start_frame must be less than or equal to end_frame."
        )
    if to_start is not None and to_end is not None and to_start >= to_end:
        raise ValueError("to_end_frame must be greater than to_start_frame.")
    if start is not None and end is not None:
        _placement(start, end, time_scale, duration, offset, to_start, to_end)

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = _keyframe_target.resolve_curve(target, write=True)
        if curve is not None:
            _scale(
                curve,
                start,
                end,
                time_scale=time_scale,
                duration=duration,
                offset=offset,
                to_start=to_start,
                to_end=to_end,
                mode=mode,
                insert_missing=insert_missing,
                change=change,
            )

    manager.queue_anim_curve_change(edit)
