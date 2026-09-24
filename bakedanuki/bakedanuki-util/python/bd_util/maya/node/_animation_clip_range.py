"""復元に使用する区間を保存データから切り出す。sceneは変更しない。"""

from __future__ import annotations

from dataclasses import replace

from maya.api import OpenMaya as om

from .animation_clip import AnimationClip, LayerSettingData, finite_number
from .operator.attr import _keyframe_move, _keyframe_snapshot


def cropped_for_restore(
    data: AnimationClip,
    start_frame: float | None,
    end_frame: float | None,
) -> AnimationClip:
    """保存時間単位で指定した区間へ全カーブを切り出す。

    Args:
        data: 切り出し元の clip。
        start_frame: 使用区間の開始。None は保存範囲の開始。
        end_frame: 使用区間の終了。None は保存範囲の終了。

    Returns:
        境界キーを補完した独立の clip。両端が None なら元の clip。

    Raises:
        ValueError: 区間が逆転、保存範囲外、または Maya の時間精度で潰れる場合。
    """
    if start_frame is None and end_frame is None:
        return data
    start = (
        data.start_frame
        if start_frame is None
        else finite_number(start_frame, "start_frame")
    )
    end = (
        data.end_frame
        if end_frame is None
        else finite_number(end_frame, "end_frame")
    )
    if not data.start_frame <= start <= end <= data.end_frame:
        raise ValueError(
            "Restore source range must be ordered and inside the saved clip range."
        )

    def time(frame: float) -> om.MTime:
        seconds = finite_number(
            frame * data.seconds_per_frame, "source time in seconds"
        )
        return _keyframe_move.checked_time(
            om.MTime(seconds, om.MTime.kSeconds), seconds
        )

    low, high = time(start), time(end)
    if start < end and low >= high:
        raise ValueError(
            "Restore source range collapses at Maya time precision."
        )

    def settings(
        items: tuple[LayerSettingData, ...],
    ) -> tuple[LayerSettingData, ...]:
        return tuple(
            (
                replace(
                    item,
                    curve=_keyframe_snapshot.clip_curve_data(
                        item.curve, start, end, data.seconds_per_frame
                    ),
                )
                if item.curve is not None
                else item
            )
            for item in items
        )

    return replace(
        data,
        start_frame=start,
        end_frame=end,
        clipped=True,
        nodes=tuple(
            replace(
                node,
                channels=tuple(
                    replace(
                        channel,
                        curve=_keyframe_snapshot.clip_curve_data(
                            channel.curve, start, end, data.seconds_per_frame
                        ),
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
