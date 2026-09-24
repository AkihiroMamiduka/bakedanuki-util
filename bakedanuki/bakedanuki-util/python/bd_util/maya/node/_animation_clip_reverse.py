"""AnimationClipを保存範囲の共通時間軸で反転する。sceneは変更しない。"""

from __future__ import annotations

from dataclasses import replace

from ._animation_clip_time import checked_time
from .animation_clip import AnimationClip, LayerSettingData, finite_number
from .operator.attr.keyframe_data import (
    AnimCurveData,
    KeyTangentTypeName,
)

Tangent = tuple[KeyTangentTypeName, tuple[float, float]]


def _reversed_tangent(tangent: Tangent) -> Tangent:
    tangent_type, (x, y) = tangent
    return tangent_type, (x, -y)


def _reversed_step(tangent: Tangent) -> Tangent:
    tangent_type, xy = _reversed_tangent(tangent)
    return ("stepnext" if tangent_type == "step" else "step"), xy


def _is_step(tangent: Tangent) -> bool:
    return tangent[0] in ("step", "stepnext")


def _reversed_interval(
    left_out: Tangent, right_in: Tangent
) -> tuple[Tangent, Tangent]:
    """1区間を反転し、新しい左outと右inを返す。

    step系は左キーのoutだけで区間を決める。未使用側の情報も保持し、
    同じ変換を2回適用すると元データへ戻るようにする。
    """
    if _is_step(left_out):
        return _reversed_step(left_out), _reversed_tangent(right_in)
    if _is_step(right_in):
        # Mayaではincomingのstep系は区間をstep化しない。非標準データでも
        # reversed側のoutへ移して意味を変えず、二重反転で元へ戻す。
        return _reversed_tangent(left_out), _reversed_tangent(right_in)
    return _reversed_tangent(right_in), _reversed_tangent(left_out)


def _curve(
    data: AnimCurveData,
    axis_seconds: float,
    start_seconds: float,
    end_seconds: float,
    clip_start_frame: float,
    clip_end_frame: float,
    clip_rate: float,
) -> AnimCurveData:
    """保存範囲の共通軸でキー・接線・infinity を反転する。

    カーブ固有の時間単位を保ち、Maya の時間精度でキーが重なれば拒否する。
    """

    def reversed_frame(frame: float) -> float:
        source_seconds = finite_number(
            frame * data.seconds_per_frame, "key time in seconds"
        )
        if data.seconds_per_frame == clip_rate:
            # 通常のchannelと同じ単位の設定curveでは、秒への往復だけで生じる
            # 誤差を避ける。反転軸自体は保存clipと同じ物理時刻である。
            result = finite_number(
                clip_start_frame + clip_end_frame - frame,
                "reversed key frame",
            )
        elif source_seconds == start_seconds:
            result_seconds = end_seconds
            result = finite_number(
                result_seconds / data.seconds_per_frame, "reversed key frame"
            )
        elif source_seconds == end_seconds:
            result_seconds = start_seconds
            result = finite_number(
                result_seconds / data.seconds_per_frame, "reversed key frame"
            )
        else:
            result_seconds = finite_number(
                axis_seconds - source_seconds, "reversed key time in seconds"
            )
            result = finite_number(
                result_seconds / data.seconds_per_frame, "reversed key frame"
            )
        checked_time(result * data.seconds_per_frame)
        return result

    source = data.keys
    keys = [
        replace(
            key,
            frame=reversed_frame(key.frame),
            in_tangent_type=key.out_tangent_type,
            out_tangent_type=key.in_tangent_type,
            in_tangent_xy=_reversed_tangent(
                (key.out_tangent_type, key.out_tangent_xy)
            )[1],
            out_tangent_xy=_reversed_tangent(
                (key.in_tangent_type, key.in_tangent_xy)
            )[1],
        )
        for key in reversed(source)
    ]
    count = len(keys)
    for index, (left, right) in enumerate(zip(source, source[1:])):
        out_tangent, in_tangent = _reversed_interval(
            (left.out_tangent_type, left.out_tangent_xy),
            (right.in_tangent_type, right.in_tangent_xy),
        )
        reversed_left = count - index - 2
        reversed_right = reversed_left + 1
        keys[reversed_left] = replace(
            keys[reversed_left],
            out_tangent_type=out_tangent[0],
            out_tangent_xy=out_tangent[1],
        )
        keys[reversed_right] = replace(
            keys[reversed_right],
            in_tangent_type=in_tangent[0],
            in_tangent_xy=in_tangent[1],
        )
    times = tuple(
        checked_time(key.frame * data.seconds_per_frame) for key in keys
    )
    if any(a >= b for a, b in zip(times, times[1:])):
        raise ValueError("Reversed clip keys coincide at Maya time precision.")
    return replace(
        data,
        pre_infinity=data.post_infinity,
        post_infinity=data.pre_infinity,
        keys=tuple(keys),
    )


def reversed_clip(data: AnimationClip) -> AnimationClip:
    """clip の全カーブを秒基準で反転した独立した clip を返す。

    ノード属性とレイヤー設定には、保存範囲の同じ反転軸を使う。
    """
    data = AnimationClip.from_dict(data.to_dict())
    start_seconds = finite_number(
        data.start_frame * data.seconds_per_frame, "start time in seconds"
    )
    end_seconds = finite_number(
        data.end_frame * data.seconds_per_frame, "end time in seconds"
    )
    checked_time(start_seconds)
    checked_time(end_seconds)
    axis_seconds = finite_number(
        start_seconds + end_seconds, "reverse axis in seconds"
    )

    def curve(item: AnimCurveData) -> AnimCurveData:
        return _curve(
            item,
            axis_seconds,
            start_seconds,
            end_seconds,
            data.start_frame,
            data.end_frame,
            data.seconds_per_frame,
        )

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
