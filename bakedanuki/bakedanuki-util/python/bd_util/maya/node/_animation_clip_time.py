"""復元予約時にclipの時間を拡縮・移動する。sceneと元のclipは変更しない。"""

from __future__ import annotations

import math
from dataclasses import replace

from maya.api import OpenMaya as om

from .animation_clip import AnimationClip, LayerSettingData, finite_number
from .operator.attr.keyframe_data import AnimCurveData


def checked_time(seconds: float) -> om.MTime:
    """秒を Maya で表現できる MTime に変換する。

    Raises:
        ValueError: 値が有限でないか、Maya の表現範囲を超える場合。
    """
    seconds = finite_number(seconds, "clip time in seconds")
    time = om.MTime(seconds, om.MTime.kSeconds)
    if not math.isclose(
        time.asUnits(om.MTime.kSeconds), seconds, rel_tol=1e-12, abs_tol=1e-8
    ):
        raise ValueError("Clip time exceeds Maya's representable time range.")
    return time


def _positive(value: object, name: str) -> float:
    """有限で正の数値を検証する。"""
    number = finite_number(value, name)
    if number <= 0:
        raise ValueError(f"{name} must be positive.")
    return number


def transformed_for_restore(
    data: AnimationClip,
    *,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
    time_scale: float | None,
    duration_frames: float | None,
) -> AnimationClip:
    """復元先の時間位置と長さに合わせて clip の全キーを変換する。

    Args:
        data: 変換元の clip。
        offset_frames: 復元先の UI 時間単位で加える移動量。
        to_start_frame: 復元先の開始時刻。
        to_end_frame: 復元先の終了時刻。
        time_scale: 正の時間倍率。duration_frames とは併用できない。
        duration_frames: 復元先の長さ。time_scale とは併用できない。

    Returns:
        キー時刻と接線 X を変換した独立の clip。指定がなければ元の clip。

    Raises:
        ValueError: 指定の組合せ、長さ、または Maya の時間精度が不正な場合。
    """
    fit_range = to_start_frame is not None and to_end_frame is not None
    if offset_frames is not None and (
        to_start_frame is not None or to_end_frame is not None
    ):
        raise ValueError(
            "offset_frames cannot be combined with target bounds."
        )
    if time_scale is not None and duration_frames is not None:
        raise ValueError("Specify either time_scale or duration_frames.")
    if fit_range and (time_scale is not None or duration_frames is not None):
        raise ValueError(
            "Target bounds cannot be combined with a scale or duration."
        )
    if all(
        value is None
        for value in (
            offset_frames,
            to_start_frame,
            to_end_frame,
            time_scale,
            duration_frames,
        )
    ):
        return data
    rate = om.MTime(1, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)

    def seconds(value: float, name: str) -> float:
        result = finite_number(value, name) * rate
        checked_time(result)
        return result

    source_start = data.start_frame * data.seconds_per_frame
    source_duration = (
        data.end_frame - data.start_frame
    ) * data.seconds_per_frame
    start = (
        source_start
        if to_start_frame is None
        else seconds(to_start_frame, "to_start_frame")
    )
    end = (
        None if to_end_frame is None else seconds(to_end_frame, "to_end_frame")
    )
    scale = 1.0 if time_scale is None else _positive(time_scale, "time_scale")
    if fit_range or duration_frames is not None:
        if source_duration <= 0:
            raise ValueError(
                "Cannot fit a single-time clip to a duration or range."
            )
        duration = (
            end - start
            if fit_range and end is not None
            else _positive(duration_frames, "duration_frames") * rate
        )
        scale = _positive(duration / source_duration, "time_scale")
    duration = finite_number(source_duration * scale, "scaled duration")
    if offset_frames is not None:
        start += seconds(offset_frames, "offset_frames")
    if end is None:
        end = start + duration
    elif not fit_range:
        start = end - duration
    if data.start_frame < data.end_frame and checked_time(
        start
    ) >= checked_time(end):
        raise ValueError(
            "Transformed clip range collapses at Maya time precision."
        )
    checked_time(start)
    checked_time(end)

    def frame(value: float, curve_rate: float) -> float:
        source_first = data.start_frame * (data.seconds_per_frame / curve_rate)
        source_last = data.end_frame * (data.seconds_per_frame / curve_rate)
        # Exact boundary placement also keeps replace_range inclusive.
        if value == source_first:
            return start / curve_rate
        if value == source_last:
            return end / curve_rate
        return (value - source_first) * scale + start / curve_rate

    def curve(item: AnimCurveData) -> AnimCurveData:
        keys = tuple(
            replace(
                key,
                frame=frame(key.frame, item.seconds_per_frame),
                in_tangent_xy=(
                    key.in_tangent_xy[0] * scale,
                    key.in_tangent_xy[1],
                ),
                out_tangent_xy=(
                    key.out_tangent_xy[0] * scale,
                    key.out_tangent_xy[1],
                ),
            )
            for key in item.keys
        )
        times = tuple(
            checked_time(key.frame * item.seconds_per_frame) for key in keys
        )
        if any(a >= b for a, b in zip(times, times[1:])):
            raise ValueError(
                "Transformed clip keys coincide at Maya time precision."
            )
        return replace(item, keys=keys)

    def settings(
        items: tuple[LayerSettingData, ...],
    ) -> tuple[LayerSettingData, ...]:
        return tuple(
            (
                replace(item, curve=curve(item.curve))
                if item.curve is not None
                else item
            )
            for item in items
        )

    return replace(
        data,
        start_frame=start / data.seconds_per_frame,
        end_frame=end / data.seconds_per_frame,
        nodes=tuple(
            replace(
                node,
                channels=tuple(
                    replace(channel, curve=curve(channel.curve))
                    for channel in node.channels
                ),
            )
            for node in data.nodes
        ),
        layers=tuple(
            replace(layer, settings=settings(layer.settings))
            for layer in data.layers
        ),
        root_settings=settings(data.root_settings),
    )
