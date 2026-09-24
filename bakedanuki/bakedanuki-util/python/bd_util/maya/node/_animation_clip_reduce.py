"""保存チャンネルのキーを削減する。元clipとsceneは変更しない。"""

from __future__ import annotations

from dataclasses import replace

from maya.api import OpenMaya as om

from .animation_clip import AnimationClip, finite_number
from .operator.attr import _keyframe_move, _keyframe_reduce, _keyframe_snapshot


def reduce_keys(
    data: AnimationClip,
    start_frame: float | None,
    end_frame: float | None,
    *,
    tolerance: float,
    preserve_breakdowns: bool,
) -> AnimationClip:
    tolerance = _keyframe_reduce.validate_options(
        tolerance, preserve_breakdowns
    )
    data = replace(data)

    def bound(value: float | None, name: str) -> om.MTime | None:
        if value is None:
            return None
        seconds = finite_number(
            finite_number(value, name) * data.seconds_per_frame, name
        )
        return _keyframe_move.checked_time(
            om.MTime(seconds, om.MTime.kSeconds), seconds
        )

    start, end = bound(start_frame, "start_frame"), bound(
        end_frame, "end_frame"
    )
    if start is not None and end is not None and start > end:
        raise ValueError(
            "start_frame must be less than or equal to end_frame."
        )
    return replace(
        data,
        nodes=tuple(
            replace(
                node,
                channels=tuple(
                    replace(
                        channel,
                        curve=_keyframe_snapshot.reduce_curve_data(
                            channel.curve,
                            start,
                            end,
                            tolerance,
                            preserve_breakdowns,
                        ),
                    )
                    for channel in node.channels
                ),
            )
            for node in data.nodes
        ),
    )
