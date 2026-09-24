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
    """保存チャンネルのキーを削減した独立の clip を返す。

    Args:
        data: 削減対象の clip。
        start_frame: 対象範囲の開始。None は制限しない。
        end_frame: 対象範囲の終了。None は制限しない。
        tolerance: カーブ値の許容誤差。非負数。
        preserve_breakdowns: breakdown キーを残すか。

    Returns:
        ノードの属性カーブだけを削減した clip。レイヤー設定は維持する。

    Raises:
        ValueError: 範囲が逆転するか、引数が有限数でない場合。
    """
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
