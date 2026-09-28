from __future__ import annotations

import math
from bisect import bisect_left, bisect_right
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_target
from ._keyframe_influence import Influence


def checked_time(time: om.MTime, seconds: float) -> om.MTime:
    if not math.isfinite(seconds) or not math.isclose(
        time.asUnits(om.MTime.kSeconds), seconds, rel_tol=1e-12, abs_tol=1e-8
    ):
        raise ValueError(
            "Keyframe time exceeds Maya's representable time range."
        )
    return time


@dataclass(frozen=True)
class CapturedKey:
    """移動するキーの値・接線・ロック状態を復元用に保持する。"""

    value: float | om.MTime
    in_type: int
    out_type: int
    in_tangent: tuple[float | om.MAngle, float]
    out_tangent: tuple[float | om.MAngle, float]
    tangents_locked: bool
    weights_locked: bool
    breakdown: bool


def capture_key(curve: oma.MFnAnimCurve, index: int) -> CapturedKey:
    time_output = curve.animCurveType == oma.MFnAnimCurve.kAnimCurveTT
    return CapturedKey(
        (
            curve.evaluate(curve.input(index))
            if time_output
            else curve.value(index)
        ),
        curve.inTangentType(index),
        curve.outTangentType(index),
        (
            curve.getTangentAngleWeight(index, True)
            if time_output
            else curve.getTangentXY(index, True)
        ),
        (
            curve.getTangentAngleWeight(index, False)
            if time_output
            else curve.getTangentXY(index, False)
        ),
        curve.tangentsLocked(index),
        curve.weightsLocked(index),
        curve.isBreakdown(index),
    )


def _restore_xy_keys(
    curve: oma.MFnAnimCurve,
    keys: tuple[CapturedKey, ...],
    destinations: tuple[om.MTime, ...],
    change: oma.MAnimCurveChange,
) -> None:
    values = om.MDoubleArray()
    in_x, in_y, out_x, out_y = (om.MDoubleArray() for _ in range(4))
    for key in keys:
        assert isinstance(key.value, float)
        values.append(key.value)
        for tangent, xs, ys in (
            (key.in_tangent, in_x, in_y),
            (key.out_tangent, out_x, out_y),
        ):
            x, y = tangent
            assert isinstance(x, float)
            xs.append(x)
            ys.append(y)
    # `setTangent()` は短い weighted 接線を丸めるため、一括挿入で元の XY を保つ。
    curve.addKeysWithTangents(
        om.MTimeArray(destinations),
        values,
        tangentInType=curve.kTangentFixed,
        tangentOutType=curve.kTangentFixed,
        tangentInTypeArray=om.MIntArray([key.in_type for key in keys]),
        tangentOutTypeArray=om.MIntArray([key.out_type for key in keys]),
        tangentInXArray=in_x,
        tangentInYArray=in_y,
        tangentOutXArray=out_x,
        tangentOutYArray=out_y,
        tangentsLockedArray=[key.tangents_locked for key in keys],
        weightsLockedArray=[key.weights_locked for key in keys],
        convertUnits=False,
        keepExistingKeys=True,
        change=change,
    )
    for key, time in zip(keys, destinations):
        index = curve.find(time)
        if index is None:
            raise RuntimeError("Maya did not restore the key.")
        curve.setInTangentType(index, key.in_type, change)
        curve.setOutTangentType(index, key.out_type, change)
        curve.setIsBreakdown(index, key.breakdown, change)


def restore_keys(
    curve: oma.MFnAnimCurve,
    keys: tuple[CapturedKey, ...],
    destinations: tuple[om.MTime, ...],
    change: oma.MAnimCurveChange,
) -> None:
    if not keys:
        return
    time_output = curve.animCurveType == curve.kAnimCurveTT
    if not time_output:
        _restore_xy_keys(curve, keys, destinations, change)
        return
    indices = [
        curve.addKey(
            time, key.value, curve.kTangentFixed, curve.kTangentFixed, change
        )
        for key, time in zip(keys, destinations)
    ]
    for index, key in zip(indices, keys):
        curve.setTangentsLocked(index, False, change)
        curve.setWeightsLocked(index, False, change)
        for is_in, tangent in (
            (True, key.in_tangent),
            (False, key.out_tangent),
        ):
            # TT カーブは生の XY だと時間精度を失うため、角度と weight を渡す。
            curve.setTangent(
                index, *tangent, is_in, change=change, convertUnits=time_output
            )
        curve.setInTangentType(index, key.in_type, change)
        curve.setOutTangentType(index, key.out_type, change)
        curve.setIsBreakdown(index, key.breakdown, change)
    for index, key in zip(indices, keys):
        curve.setWeightsLocked(index, key.weights_locked, change)
        curve.setTangentsLocked(index, key.tangents_locked, change)
        for is_in, tangent, tangent_type in (
            (True, key.in_tangent, key.in_type),
            (False, key.out_tangent, key.out_type),
        ):
            if tangent_type != curve.kTangentFixed or not curve.isWeighted:
                continue
            angle, weight = curve.getTangentAngleWeight(index, is_in)
            expected_angle, expected_weight = tangent
            assert isinstance(expected_angle, om.MAngle)
            if not math.isclose(
                angle.asRadians(), expected_angle.asRadians(), abs_tol=1e-7
            ) or not math.isclose(
                weight, expected_weight, rel_tol=1e-6, abs_tol=1e-10
            ):
                raise RuntimeError(
                    "Maya cannot represent the restored weighted time tangent."
                )


def insert_boundaries(
    curve: oma.MFnAnimCurve,
    times: list[om.MTime],
    change: oma.MAnimCurveChange,
    samples: tuple[tuple[om.MTime, float | om.MTime], ...] | None = None,
) -> None:
    # 範囲外のキーを追加すると cycle infinity の周期が変わるため、先に値を採取する。
    if samples is None:
        samples = tuple((time, curve.evaluate(time)) for time in times)
    for time, _ in samples:
        curve.insertKey(time, False, change)
    for time, value in samples:
        index = curve.find(time)
        if index is None:
            raise RuntimeError(
                "Maya did not insert the requested boundary key."
            )
        if curve.evaluate(time) == value:
            continue
        if isinstance(value, om.MTime):
            curve.addKey(
                time,
                value,
                curve.inTangentType(index),
                curve.outTangentType(index),
                change,
            )
        else:
            curve.setValue(index, value, change)


def _set_inputs(
    curve: oma.MFnAnimCurve,
    indices: range,
    destinations: tuple[om.MTime, ...],
    change: oma.MAnimCurveChange,
) -> None:
    pairs = list(zip(indices, destinations))
    if any(destination > curve.input(index) for index, destination in pairs):
        pairs.reverse()
    for index, destination in pairs:
        if curve.input(index) == destination:
            continue
        curve.setInput(index, destination, change)
        if curve.input(index) != destination:
            raise RuntimeError(
                "Maya did not move the key to the requested time."
            )


@dataclass(frozen=True)
class MoveSelection:
    curve: oma.MFnAnimCurve
    times: tuple[om.MTime, ...]
    core: tuple[om.MTime, ...]
    missing: tuple[om.MTime, ...]
    selected: tuple[om.MTime, ...]


@dataclass(frozen=True)
class _MovePlan:
    selection: MoveSelection
    samples: tuple[tuple[om.MTime, float | om.MTime], ...]
    virtual_times: tuple[om.MTime, ...]
    first: int
    stop: int
    destinations: tuple[om.MTime, ...]
    collisions: tuple[int, ...]
    use_set_inputs: bool


def select_keys(
    curve: oma.MFnAnimCurve,
    influence: Influence,
    insert_missing: bool,
) -> MoveSelection:
    if not curve.numKeys:
        return MoveSelection(curve, (), (), (), ())
    start, end = influence.start, influence.end
    times = tuple(curve.input(i) for i in range(curve.numKeys))
    first = 0 if start is None else bisect_left(times, start)
    stop = len(times) if end is None else bisect_right(times, end)
    core = list(times[first:stop])
    missing: list[om.MTime] = []
    if insert_missing:
        for boundary in influence.boundaries:
            if (
                boundary is not None
                and boundary not in times
                and boundary not in missing
            ):
                missing.append(boundary)
                if (start is not None and boundary == start) or (
                    end is not None and boundary == end
                ):
                    core.insert(bisect_left(core, boundary), boundary)
    low, high = influence.low, influence.high
    first = 0 if low is None else bisect_left(times, low)
    stop = len(times) if high is None else bisect_right(times, high)
    selected = list(times[first:stop])
    for boundary in missing:
        selected.insert(bisect_left(selected, boundary), boundary)
    return MoveSelection(
        curve, times, tuple(core), tuple(missing), tuple(selected)
    )


def _move_offset(
    selections: tuple[MoveSelection, ...],
    influence: Influence,
    offset: om.MTime | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
) -> om.MTime | None:
    if offset is None:
        if to_start is not None:
            destination = to_start
            if influence.start is not None:
                anchor = influence.start
            else:
                anchors = tuple(
                    time for selection in selections for time in selection.core
                )
                if not anchors:
                    return None
                anchor = min(anchors)
        else:
            assert to_end is not None
            destination = to_end
            if influence.end is not None:
                anchor = influence.end
            else:
                anchors = tuple(
                    time for selection in selections for time in selection.core
                )
                if not anchors:
                    return None
                anchor = max(anchors)
        offset = checked_time(
            destination - anchor,
            destination.asUnits(om.MTime.kSeconds)
            - anchor.asUnits(om.MTime.kSeconds),
        )
    return offset


def _plan_move(
    selection: MoveSelection,
    influence: Influence,
    offset: om.MTime,
) -> _MovePlan | None:
    if not selection.selected or offset == om.MTime(0, om.MTime.kSeconds):
        return None
    seconds_offset = offset.asUnits(om.MTime.kSeconds)

    def destination_time(time: om.MTime) -> om.MTime:
        weight = influence.weight(time)
        if weight == 0:
            return time
        shift = (
            offset
            if weight == 1
            else om.MTime(seconds_offset * weight, om.MTime.kSeconds)
        )
        return checked_time(
            time + shift,
            time.asUnits(om.MTime.kSeconds) + seconds_offset * weight,
        )

    destinations = tuple(destination_time(time) for time in selection.selected)
    if any(a >= b for a, b in zip(destinations, destinations[1:])):
        raise ValueError("Moved keys coincide or change order.")

    virtual_times = tuple(sorted((*selection.times, *selection.missing)))
    low, high = influence.low, influence.high
    first = 0 if low is None else bisect_left(virtual_times, low)
    stop = (
        len(virtual_times)
        if high is None
        else bisect_right(virtual_times, high)
    )
    if virtual_times[first:stop] != selection.selected:
        raise RuntimeError(
            "The planned boundary keys do not match the selection."
        )
    collisions: set[int] = set()
    for destination in destinations:
        index = bisect_left(virtual_times, destination)
        if (
            index < len(virtual_times)
            and virtual_times[index] == destination
            and not first <= index < stop
        ):
            collisions.add(index)
    final_times = virtual_times[:first] + destinations + virtual_times[stop:]
    samples = tuple(
        (time, selection.curve.evaluate(time)) for time in selection.missing
    )
    return _MovePlan(
        selection,
        samples,
        virtual_times,
        first,
        stop,
        destinations,
        tuple(sorted(collisions)),
        not collisions
        and all(a < b for a, b in zip(final_times, final_times[1:])),
    )


def _apply_move(plan: _MovePlan, change: oma.MAnimCurveChange) -> None:
    curve = plan.selection.curve
    insert_boundaries(
        curve, list(plan.selection.missing), change, plan.samples
    )
    times = tuple(curve.input(i) for i in range(curve.numKeys))
    if times != plan.virtual_times:
        raise RuntimeError("Maya did not insert the requested boundary keys.")
    first, stop = plan.first, plan.stop
    indices = range(first, stop)
    destinations = plan.destinations
    if plan.use_set_inputs:
        _set_inputs(curve, indices, destinations, change)
        return

    moved = [
        (i, time) for i, time in zip(indices, destinations) if times[i] != time
    ]
    keys = tuple(capture_key(curve, i) for i, _ in moved)
    moved_times = tuple(time for _, time in moved)
    for index in sorted(
        {i for i, _ in moved} | set(plan.collisions), reverse=True
    ):
        curve.remove(index, change)
    restore_keys(curve, keys, moved_times, change)
    if any(curve.find(time) is None for time in destinations):
        raise RuntimeError("Maya did not restore the moved keys.")


def _move(
    curve: oma.MFnAnimCurve,
    influence: Influence,
    offset: om.MTime | None,
    to_start: om.MTime | None,
    to_end: om.MTime | None,
    insert_missing: bool,
    change: oma.MAnimCurveChange,
) -> None:
    selection = select_keys(curve, influence, insert_missing)
    movement = _move_offset((selection,), influence, offset, to_start, to_end)
    if movement is None:
        return
    plan = _plan_move(selection, influence, movement)
    if plan is not None:
        _apply_move(plan, change)


def _capture_options(
    start_frame: float | None,
    end_frame: float | None,
    *,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    insert_missing: bool,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
) -> tuple[Influence, om.MTime | None, om.MTime | None, om.MTime | None]:
    unit = om.MTime.uiUnit()
    if (
        sum(
            v is not None
            for v in (offset_frames, to_start_frame, to_end_frame)
        )
        != 1
    ):
        raise ValueError(
            "Specify exactly one movement: offset or destination."
        )
    if type(insert_missing) is not bool:
        raise TypeError("insert_missing must be a bool.")

    def capture(frame: float | None) -> om.MTime | None:
        if frame is None:
            return None
        value = float(frame)
        if not math.isfinite(value):
            raise ValueError("Keyframe frames and offsets must be finite.")
        return checked_time(
            om.MTime(value, unit),
            value * om.MTime(1, unit).asUnits(om.MTime.kSeconds),
        )

    start, end = capture(start_frame), capture(end_frame)
    offset = capture(offset_frames)
    to_start, to_end = capture(to_start_frame), capture(to_end_frame)

    def capture_fade(value: object, name: str) -> om.MTime | None:
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number.")
        return capture(value)

    influence = Influence(
        start,
        end,
        capture_fade(interpolate_start, "interpolate_start"),
        capture_fade(interpolate_end, "interpolate_end"),
        interpolation,
    )
    return influence, offset, to_start, to_end


def queue_move(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    start_frame: float | None,
    end_frame: float | None,
    *,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    insert_missing: bool,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
) -> None:
    influence, offset, to_start, to_end = _capture_options(
        start_frame,
        end_frame,
        offset_frames=offset_frames,
        to_start_frame=to_start_frame,
        to_end_frame=to_end_frame,
        insert_missing=insert_missing,
        interpolate_start=interpolate_start,
        interpolate_end=interpolate_end,
        interpolation=interpolation,
    )

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = _keyframe_target.resolve_curve(target, write=True)
        if curve is not None:
            _move(
                curve,
                influence,
                offset,
                to_start,
                to_end,
                insert_missing,
                change,
            )

    manager.queue_anim_curve_change(edit)


def queue_move_batch(
    manager: ModifierManager,
    resolve_targets: Callable[[], tuple[_keyframe_target.Target, ...]],
    start_frame: float | None,
    end_frame: float | None,
    *,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    insert_missing: bool,
    interpolate_start: float | None = None,
    interpolate_end: float | None = None,
    interpolation: Literal["linear", "smoothstep"] = "smoothstep",
) -> None:
    """全カーブの移動を計画してから単一の変更履歴へ予約する。"""
    influence, offset, to_start, to_end = _capture_options(
        start_frame,
        end_frame,
        offset_frames=offset_frames,
        to_start_frame=to_start_frame,
        to_end_frame=to_end_frame,
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
            select_keys(curve, influence, insert_missing) for curve in curves
        )
        movement = _move_offset(
            selections, influence, offset, to_start, to_end
        )
        plans = (
            ()
            if movement is None
            else tuple(
                plan
                for selection in selections
                if (plan := _plan_move(selection, influence, movement))
                is not None
            )
        )

        def edit(change: oma.MAnimCurveChange) -> None:
            for plan in plans:
                _apply_move(plan, change)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)
