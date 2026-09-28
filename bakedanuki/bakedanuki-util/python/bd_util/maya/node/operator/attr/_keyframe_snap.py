"""既存カーブの小数フレームキーを整数フレームへ打ち直す。"""

from __future__ import annotations

import math
from bisect import bisect_left
from collections.abc import Callable
from dataclasses import dataclass

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import (
    _keyframe_move,
    _keyframe_reduce,
    _keyframe_snap_error,
    _keyframe_tangent,
    _keyframe_target,
)


@dataclass(frozen=True, slots=True)
class _SnapPlan:
    curve: oma.MFnAnimCurve
    sources: tuple[om.MTime, ...]
    samples: tuple[tuple[om.MTime, float], ...]
    breakdowns: tuple[bool, ...]
    original: tuple[_keyframe_reduce.CurveKey, ...] | None
    original_weighted: bool
    original_pre_infinity: int
    original_post_infinity: int


def _nearest_frame(time: om.MTime, unit: int) -> om.MTime:
    frame = time.asUnits(unit)
    if not math.isfinite(frame):
        raise ValueError("Keyframe time must be finite.")
    lower = math.floor(frame)
    middle = om.MTime(lower + 0.5, unit)
    # Maya の snapKey と同じく、半フレームはゼロから遠い側へ寄せる。
    rounded = (
        (lower if frame < 0 else lower + 1)
        if time == middle
        else (lower if time < middle else lower + 1)
    )
    return _keyframe_move.checked_time(
        om.MTime(rounded, unit),
        rounded * om.MTime(1, unit).asUnits(om.MTime.kSeconds),
    )


def _plan_curve(
    curve: oma.MFnAnimCurve,
    start: float | None,
    end: float | None,
    unit: int,
    max_deviation: float | None,
    preserve_breakdowns: bool,
) -> _SnapPlan | None:
    times = tuple(curve.input(index) for index in range(curve.numKeys))
    sources: list[om.MTime] = []
    destinations: list[om.MTime] = []
    breakdowns: list[bool] = []
    for index, time in enumerate(times):
        seconds = time.asUnits(om.MTime.kSeconds)
        if (start is not None and seconds < start) or (
            end is not None and seconds > end
        ):
            continue
        breakdown = curve.isBreakdown(index)
        if preserve_breakdowns and breakdown:
            continue
        destination = _nearest_frame(time, unit)
        if destination == time:
            continue
        sources.append(time)
        destinations.append(destination)
        breakdowns.append(breakdown)
    if not sources:
        return None
    if curve.animCurveType not in (
        curve.kAnimCurveTA,
        curve.kAnimCurveTL,
        curve.kAnimCurveTU,
    ):
        raise TypeError("Subframe snapping requires a TA, TL, or TU curve.")
    ordered = sorted(destinations)
    if any(
        index < len(times) and times[index] == destination
        for destination in destinations
        for index in (bisect_left(times, destination),)
    ) or any(a == b for a, b in zip(ordered, ordered[1:])):
        raise ValueError("Subframe keys would collide at an integer frame.")
    samples = tuple((time, curve.evaluate(time)) for time in destinations)
    if any(not math.isfinite(value) for _, value in samples):
        raise ValueError("Sampled animation curve values must be finite.")
    original = (
        tuple(
            _keyframe_reduce.capture_curve_key(curve, i)
            for i in range(curve.numKeys)
        )
        if max_deviation is not None
        else None
    )
    return _SnapPlan(
        curve,
        tuple(sources),
        samples,
        tuple(breakdowns),
        original,
        curve.isWeighted,
        curve.preInfinityType,
        curve.postInfinityType,
    )


def _apply_plan(plan: _SnapPlan, change: oma.MAnimCurveChange) -> None:
    curve = plan.curve
    _keyframe_move.insert_boundaries(
        curve, [time for time, _ in plan.samples], change, plan.samples
    )
    for source in reversed(plan.sources):
        index = curve.find(source)
        if index is None:
            raise RuntimeError(
                "The source subframe key is no longer available."
            )
        curve.remove(index, change)
    for (time, value), breakdown in zip(plan.samples, plan.breakdowns):
        index = curve.find(time)
        if index is None or curve.input(index) != time:
            raise RuntimeError(
                "Maya did not create the requested integer key."
            )
        if breakdown:
            curve.setIsBreakdown(index, True, change)
        if not math.isclose(
            curve.value(index), value, rel_tol=1e-12, abs_tol=1e-10
        ):
            raise RuntimeError("Maya did not retain the sampled key value.")


def _check_deviation(plan: _SnapPlan, max_deviation: float) -> None:
    original = plan.original
    if original is None:
        return
    if not _keyframe_snap_error.within_max_deviation(
        plan.curve,
        original,
        plan.original_weighted,
        plan.original_pre_infinity,
        plan.original_post_infinity,
        max_deviation,
    ):
        raise ValueError("Subframe snapping exceeds max_deviation.")


def queue_snap_subframe_batch(
    manager: ModifierManager,
    resolve_targets: Callable[[], tuple[_keyframe_target.Target, ...]],
    start_frame: float | None,
    end_frame: float | None,
    *,
    preserve_breakdowns: bool,
    max_deviation: object,
) -> None:
    """全カーブを解決・計画した後、一つの変更履歴へ整数化を予約する。"""
    unit = om.MTime.uiUnit()
    start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
    if type(preserve_breakdowns) is not bool:
        raise TypeError("preserve_breakdowns must be a bool.")
    if max_deviation is not None:
        if isinstance(max_deviation, bool) or not isinstance(
            max_deviation, (int, float)
        ):
            raise TypeError("max_deviation must be a number or None.")
        max_deviation = float(max_deviation)
        if not math.isfinite(max_deviation) or max_deviation < 0:
            raise ValueError("max_deviation must be finite and nonnegative.")

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
        plans = tuple(
            plan
            for curve in curves
            if (
                plan := _plan_curve(
                    curve,
                    start,
                    end,
                    unit,
                    max_deviation,
                    preserve_breakdowns,
                )
            )
            is not None
        )

        def edit(change: oma.MAnimCurveChange) -> None:
            for plan in plans:
                _apply_plan(plan, change)
            if max_deviation is not None:
                for plan in plans:
                    _check_deviation(plan, max_deviation)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)
