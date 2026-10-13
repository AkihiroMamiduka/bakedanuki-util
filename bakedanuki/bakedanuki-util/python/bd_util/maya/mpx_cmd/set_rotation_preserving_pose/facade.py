# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, cast

from maya import cmds

from ..round_transform._plugin import ensure_util_commands_plugin_loaded
from .mpx_command import SetRotationPreservingPoseCommand
from .operation import (
    AngleInputUnit,
    RotationAttribute,
    SetRotationPreservingPoseParams,
)


class _SetRotationPreservingPoseCallable(Protocol):
    """動的 Maya コマンド呼び出しの引数を局所的に型付けする。"""

    def __call__(
        self,
        *node_names: str,
        targetAttribute: str,
        compensateWith: str,
        valueX: float,
        valueY: float,
        valueZ: float,
        angleUnit: str,
    ) -> object: ...


def set_rotation_preserving_pose(
    node_names: Sequence[str],
    values: tuple[float, float, float],
    *,
    target: RotationAttribute,
    compensate_with: RotationAttribute,
    angle_unit: AngleInputUnit = "degrees",
) -> list[str]:
    """共通の回転 XYZ を設定し、各ノードの現在の姿勢を一度の Undo で保つ。

    Args:
        node_names: 対象 Transform / Joint の名前。空列は不可。
        values: 全対象へ設定する XYZ の目標値。
        target: 目標値を設定する回転属性群。
        compensate_with: 回転差分を吸収する別の属性群。
        angle_unit: `degrees` は度、`display` は現在の Maya 表示単位。

    Returns:
        値を変更したノードのフル DAG path。変更なしなら空リスト。
    """
    if isinstance(node_names, (str, bytes)):
        raise ValueError("node_names must contain node names, not a string.")
    params = SetRotationPreservingPoseParams(
        node_names=tuple(node_names),
        values=values,
        target=target,
        compensate_with=compensate_with,
        angle_unit=angle_unit,
    )
    ensure_util_commands_plugin_loaded()
    command = cast(
        _SetRotationPreservingPoseCallable,
        getattr(cmds, SetRotationPreservingPoseCommand.COMMAND_NAME),
    )
    result = command(
        *params.node_names,
        targetAttribute=params.target,
        compensateWith=params.compensate_with,
        valueX=params.values[0],
        valueY=params.values[1],
        valueZ=params.values[2],
        angleUnit=params.angle_unit,
    )
    return _decode_result(result)


def _decode_result(raw_result: object) -> list[str]:
    """Maya の stringArray 結果を Python のリストへ正規化する。"""
    if raw_result is None:
        return []
    if isinstance(raw_result, str):
        return [raw_result]
    if isinstance(raw_result, (tuple, list)) and all(
        isinstance(name, str) for name in raw_result
    ):
        return list(raw_result)
    raise TypeError(
        f"Unexpected bdSetRotationPreservingPose result: {raw_result!r}"
    )
