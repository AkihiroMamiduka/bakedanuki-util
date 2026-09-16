"""復元予約時にclipの時間を移す。sceneと元のclipは変更しない。"""

from __future__ import annotations

import math
from dataclasses import replace

from maya.api import OpenMaya as om

from .animation_clip import AnimationClip, LayerSettingData, finite_number
from .operator.attr.keyframe_data import AnimCurveData


def _time(seconds: float) -> om.MTime:
    seconds = finite_number(seconds, "clip time in seconds")
    time = om.MTime(seconds, om.MTime.kSeconds)
    if not math.isclose(
        time.asUnits(om.MTime.kSeconds), seconds, rel_tol=1e-12, abs_tol=1e-8
    ):
        raise ValueError("Clip time exceeds Maya's representable time range.")
    return time


def _shift_curve(data: AnimCurveData, seconds: float) -> AnimCurveData:
    offset = seconds / data.seconds_per_frame
    keys = tuple(replace(key, frame=key.frame + offset) for key in data.keys)
    times = tuple(_time(key.frame * data.seconds_per_frame) for key in keys)
    if any(a >= b for a, b in zip(times, times[1:])):
        raise ValueError("Shifted clip keys coincide at Maya time precision.")
    return replace(data, keys=keys)


def shifted_for_restore(
    data: AnimationClip,
    *,
    offset_frames: float | None,
    to_start_frame: float | None,
    to_end_frame: float | None,
) -> AnimationClip:
    specified = [
        (name, value)
        for name, value in (
            ("offset_frames", offset_frames),
            ("to_start_frame", to_start_frame),
            ("to_end_frame", to_end_frame),
        )
        if value is not None
    ]
    if len(specified) > 1:
        raise ValueError("Specify at most one clip restore time argument.")
    if not specified:
        return data
    name, value = specified[0]
    rate = om.MTime(1, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)
    seconds = finite_number(value, name) * rate
    _time(seconds)
    if name == "to_start_frame":
        seconds -= data.start_frame * data.seconds_per_frame
    elif name == "to_end_frame":
        seconds -= data.end_frame * data.seconds_per_frame
    _time(seconds)
    if seconds == 0:
        return data
    offset = seconds / data.seconds_per_frame
    start = data.start_frame + offset
    end = data.end_frame + offset
    start_time = _time(start * data.seconds_per_frame)
    end_time = _time(end * data.seconds_per_frame)
    if data.start_frame < data.end_frame and start_time >= end_time:
        raise ValueError(
            "Shifted clip range collapses at Maya time precision."
        )

    def settings(
        items: tuple[LayerSettingData, ...],
    ) -> tuple[LayerSettingData, ...]:
        return tuple(
            (
                replace(item, curve=_shift_curve(item.curve, seconds))
                if item.curve is not None
                else item
            )
            for item in items
        )

    return replace(
        data,
        start_frame=start,
        end_frame=end,
        nodes=tuple(
            replace(
                node,
                channels=tuple(
                    replace(
                        channel, curve=_shift_curve(channel.curve, seconds)
                    )
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
