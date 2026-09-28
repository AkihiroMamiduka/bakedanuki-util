from __future__ import annotations

import math
from bisect import bisect_left, bisect_right
from collections.abc import Callable
from dataclasses import dataclass, replace
from typing import Literal

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_move, _keyframe_target
from ._keyframe_influence import Influence


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


def _pivoted_seconds(
    seconds: float, pivot: om.MTime, scale: float, offset: float | None
) -> float:
    pivot_seconds = pivot.asUnits(om.MTime.kSeconds)
    # 倍率が 0 に近い場合の桁落ちを避け、等倍変換も正確に保つ。
    transformed = (
        pivot_seconds + (seconds - pivot_seconds) * scale
        if scale < 0.5
        else seconds + (seconds - pivot_seconds) * (scale - 1)
    )
    return transformed + (0 if offset is None else offset)


def _placement(
    start: om.MTime,
    end: om.MTime,
    time_scale: float | None,
    duration: float | None,
    offset: float | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
    pivot: om.MTime | None,
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
        time_scale = _positive(duration / source_duration, "scale")
        if pivot is not None and _time(duration) == end - start:
            time_scale = 1
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
    if pivot is not None:
        low = _pivoted_seconds(first, pivot, time_scale, offset)
        high = _pivoted_seconds(last, pivot, time_scale, offset)
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
            # TT カーブは生の XY だと時間精度を失うため、角度と weight を使う。
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


@dataclass(frozen=True)
class _ScalePlan:
    selection: _keyframe_move.MoveSelection
    samples: tuple[tuple[om.MTime, float | om.MTime], ...]
    virtual_times: tuple[om.MTime, ...]
    first: int
    stop: int
    destinations: tuple[om.MTime, ...]
    scales: tuple[float, ...]
    updated: tuple[int, ...]
    removed: tuple[int, ...]


def _plan_scale(
    selection: _keyframe_move.MoveSelection,
    influence: Influence,
    source_start: om.MTime,
    source_end: om.MTime,
    scale: float,
    destination_start: om.MTime,
    destination_end: om.MTime,
    offset: float | None,
    pivot: om.MTime | None,
    mode: Literal["replace_range", "merge"],
) -> _ScalePlan | None:
    if not selection.selected:
        return None

    def destination(time: om.MTime, weight: float) -> om.MTime:
        if weight == 0:
            return time
        if weight == 1 and time == source_start:
            return destination_start
        if weight == 1 and time == source_end:
            return destination_end
        seconds = time.asUnits(om.MTime.kSeconds)
        transformed = (
            _pivoted_seconds(seconds, pivot, scale, offset)
            if pivot is not None
            else destination_start.asUnits(om.MTime.kSeconds)
            + (seconds - source_start.asUnits(om.MTime.kSeconds)) * scale
        )
        return _time(
            transformed
            if weight == 1
            else seconds + (transformed - seconds) * weight
        )

    selected = selection.selected
    weights = tuple(influence.weight(time) for time in selected)
    destinations = tuple(
        destination(time, weight) for time, weight in zip(selected, weights)
    )
    if any(a >= b for a, b in zip(destinations, destinations[1:])):
        raise ValueError(
            "Scaled keys coincide or change order at Maya time precision."
        )
    scales = tuple((1 - weight) + weight * scale for weight in weights)
    updated = tuple(
        i
        for i, (time, dest, factor) in enumerate(
            zip(selected, destinations, scales)
        )
        if time != dest or factor != 1
    )
    if not updated:
        return None

    virtual_times = tuple(sorted((*selection.times, *selection.missing)))
    low, high = influence.low, influence.high
    first = 0 if low is None else bisect_left(virtual_times, low)
    stop = (
        len(virtual_times)
        if high is None
        else bisect_right(virtual_times, high)
    )
    if virtual_times[first:stop] != selected:
        raise RuntimeError(
            "The planned boundary keys do not match the selection."
        )
    removed = {first + i for i in updated}
    if mode == "replace_range":
        removed.update(
            i
            for i in range(
                bisect_left(virtual_times, destination_start),
                bisect_right(virtual_times, destination_end),
            )
            if not first <= i < stop
        )
    for time in destinations:
        index = bisect_left(virtual_times, time)
        if (
            index < len(virtual_times)
            and virtual_times[index] == time
            and not first <= index < stop
        ):
            removed.add(index)
    samples = tuple(
        (time, selection.curve.evaluate(time)) for time in selection.missing
    )
    return _ScalePlan(
        selection,
        samples,
        virtual_times,
        first,
        stop,
        destinations,
        scales,
        updated,
        tuple(sorted(removed, reverse=True)),
    )


def _apply_scale(plan: _ScalePlan, change: oma.MAnimCurveChange) -> None:
    curve = plan.selection.curve
    _keyframe_move.insert_boundaries(
        curve, list(plan.selection.missing), change, plan.samples
    )
    times = tuple(curve.input(i) for i in range(curve.numKeys))
    if times != plan.virtual_times:
        raise RuntimeError("Maya did not insert the requested boundary keys.")
    keys: list[_keyframe_move.CapturedKey] = []
    for i in plan.updated:
        key = _keyframe_move.capture_key(curve, plan.first + i)
        factor = plan.scales[i]
        keys.append(_scaled_key(key, factor) if factor != 1 else key)
    for index in plan.removed:
        curve.remove(index, change)
    _keyframe_move.restore_keys(
        curve,
        tuple(keys),
        tuple(plan.destinations[i] for i in plan.updated),
        change,
    )
    if any(curve.find(time) is None for time in plan.destinations):
        raise RuntimeError("Maya did not restore the scaled keys.")


def _plan_scales(
    selections: tuple[_keyframe_move.MoveSelection, ...],
    influence: Influence,
    *,
    time_scale: float | None,
    duration: float | None,
    offset: float | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
    pivot: om.MTime | None,
    mode: Literal["replace_range", "merge"],
) -> tuple[_ScalePlan, ...]:
    if not any(selection.selected for selection in selections):
        return ()
    core = tuple(time for selection in selections for time in selection.core)
    if influence.start is None and not core:
        return ()
    if influence.end is None and not core:
        return ()
    source_start = (
        influence.start if influence.start is not None else min(core)
    )
    source_end = influence.end if influence.end is not None else max(core)
    scale, destination_start, destination_end = _placement(
        source_start,
        source_end,
        time_scale,
        duration,
        offset,
        to_start,
        to_end,
        pivot,
    )
    # 算出した倍率は秒への変換時の丸めだけで 1 と異なる場合がある。
    if (
        (time_scale is None or scale == 1)
        and source_start == destination_start
        and source_end == destination_end
    ):
        return ()
    return tuple(
        plan
        for selection in selections
        if (
            plan := _plan_scale(
                selection,
                influence,
                source_start,
                source_end,
                scale,
                destination_start,
                destination_end,
                offset,
                pivot,
                mode,
            )
        )
        is not None
    )


def _scale(
    curve: oma.MFnAnimCurve,
    influence: Influence,
    *,
    time_scale: float | None,
    duration: float | None,
    offset: float | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
    pivot: om.MTime | None,
    mode: Literal["replace_range", "merge"],
    insert_missing: bool,
    change: oma.MAnimCurveChange,
) -> None:
    selection = _keyframe_move.select_keys(curve, influence, insert_missing)
    plans = _plan_scales(
        (selection,),
        influence,
        time_scale=time_scale,
        duration=duration,
        offset=offset,
        to_start=to_start,
        to_end=to_end,
        pivot=pivot,
        mode=mode,
    )
    for plan in plans:
        _apply_scale(plan, change)


@dataclass(frozen=True)
class _ScaleOptions:
    influence: Influence
    time_scale: float | None
    duration: float | None
    offset: float | None
    to_start: om.MTime | None
    to_end: om.MTime | None
    pivot: om.MTime | None


def _capture_options(
    start_frame: float | None,
    end_frame: float | None,
    *,
    time_scale: float | None,
    duration_frames: float | None,
    pivot_frame: float | None,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    mode: Literal["replace_range", "merge"],
    insert_missing: bool,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
) -> _ScaleOptions:
    fit = to_start_frame is not None and to_end_frame is not None
    if sum((time_scale is not None, duration_frames is not None, fit)) != 1:
        raise ValueError(
            "Specify exactly one of scale, duration, or both target bounds."
        )
    if offset_frames is not None and (
        to_start_frame is not None or to_end_frame is not None
    ):
        raise ValueError("offset cannot be combined with target bounds.")
    if pivot_frame is not None and (
        to_start_frame is not None or to_end_frame is not None
    ):
        raise ValueError("pivot cannot be combined with target bounds.")
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
    to_start, to_end = capture(to_start_frame, "to_start"), capture(
        to_end_frame, "to_end"
    )
    offset_time = capture(offset_frames, "offset")
    pivot = capture(pivot_frame, "pivot")
    offset = (
        None if offset_time is None else offset_time.asUnits(om.MTime.kSeconds)
    )
    duration = (
        None
        if duration_frames is None
        else _positive(duration_frames, "duration") * rate
    )
    if duration is not None:
        _time(duration)
    if time_scale is not None:
        time_scale = _positive(time_scale, "scale")
    influence = Influence(
        start,
        end,
        capture(interpolate_start, "interpolate_start"),
        capture(interpolate_end, "interpolate_end"),
        interpolation,
    )
    if to_start is not None and to_end is not None and to_start >= to_end:
        raise ValueError("to_end must be greater than to_start.")
    if start is not None and end is not None:
        _placement(
            start, end, time_scale, duration, offset, to_start, to_end, pivot
        )
    return _ScaleOptions(
        influence, time_scale, duration, offset, to_start, to_end, pivot
    )


def queue_scale(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    start_frame: float | None,
    end_frame: float | None,
    *,
    time_scale: float | None,
    duration_frames: float | None,
    pivot_frame: float | None,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    mode: Literal["replace_range", "merge"],
    insert_missing: bool,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
) -> None:
    options = _capture_options(
        start_frame,
        end_frame,
        time_scale=time_scale,
        duration_frames=duration_frames,
        pivot_frame=pivot_frame,
        offset_frames=offset_frames,
        to_start_frame=to_start_frame,
        to_end_frame=to_end_frame,
        mode=mode,
        insert_missing=insert_missing,
        interpolate_start=interpolate_start,
        interpolate_end=interpolate_end,
        interpolation=interpolation,
    )

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = _keyframe_target.resolve_curve(target, write=True)
        if curve is not None:
            _scale(
                curve,
                options.influence,
                time_scale=options.time_scale,
                duration=options.duration,
                offset=options.offset,
                to_start=options.to_start,
                to_end=options.to_end,
                pivot=options.pivot,
                mode=mode,
                insert_missing=insert_missing,
                change=change,
            )

    manager.queue_anim_curve_change(edit)


def queue_scale_batch(
    manager: ModifierManager,
    resolve_targets: Callable[[], tuple[_keyframe_target.Target, ...]],
    start_frame: float | None,
    end_frame: float | None,
    *,
    time_scale: float | None,
    duration_frames: float | None,
    pivot_frame: float | None,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    mode: Literal["replace_range", "merge"],
    insert_missing: bool,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
) -> None:
    """全カーブの拡縮を計画してから単一の変更履歴へ予約する。"""
    options = _capture_options(
        start_frame,
        end_frame,
        time_scale=time_scale,
        duration_frames=duration_frames,
        pivot_frame=pivot_frame,
        offset_frames=offset_frames,
        to_start_frame=to_start_frame,
        to_end_frame=to_end_frame,
        mode=mode,
        insert_missing=insert_missing,
        interpolate_start=interpolate_start,
        interpolate_end=interpolate_end,
        interpolation=interpolation,
    )

    def prepare(work: ModifierManager) -> None:
        curves: list[oma.MFnAnimCurve] = []
        handles: set[om.MObjectHandle] = set()
        for target in resolve_targets():
            curve = _keyframe_target.resolve_curve(target, write=True)
            if curve is None:
                continue
            handle = om.MObjectHandle(curve.object())
            if handle not in handles:
                handles.add(handle)
                curves.append(curve)

        selections = tuple(
            _keyframe_move.select_keys(
                curve, options.influence, insert_missing
            )
            for curve in curves
        )
        plans = _plan_scales(
            selections,
            options.influence,
            time_scale=options.time_scale,
            duration=options.duration,
            offset=options.offset,
            to_start=options.to_start,
            to_end=options.to_end,
            pivot=options.pivot,
            mode=mode,
        )

        def edit(change: oma.MAnimCurveChange) -> None:
            for plan in plans:
                _apply_scale(plan, change)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)
