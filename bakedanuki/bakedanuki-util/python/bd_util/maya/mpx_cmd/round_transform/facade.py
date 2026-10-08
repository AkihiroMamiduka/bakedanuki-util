# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, cast

from maya import cmds

from ...node.operator.node.dag.transform._core import (
    JointChildCompensationAttr,
)
from ...rounding import RoundingUnit
from ._plugin import ensure_util_commands_plugin_loaded
from .mpx_command import (
    RoundJointOrientCommand,
    RoundRotateAxisCommand,
    RoundRotateCommand,
    RoundTranslateCommand,
)


class _RoundTranslateCallable(Protocol):
    def __call__(
        self,
        *node_names: str,
        ndigits: int,
        roundingUnit: str,
        compensateChildren: bool,
    ) -> object: ...


class _RoundRotationCallable(Protocol):
    def __call__(
        self,
        *node_names: str,
        ndigits: int,
        roundingUnit: str,
        compensateChildren: bool,
        compensateChildTranslate: bool,
        jointChildCompensationAttr: str,
    ) -> object: ...


def round_translate(
    node_names: Sequence[str],
    ndigits: int = 0,
    *,
    rounding_unit: RoundingUnit = "canonical",
    compensate_children: bool = False,
) -> list[str]:
    """指定ノードの `translate` を一度の Maya Undo で丸める。

    Args:
        node_names: 対象 Transform / Joint の名前。空列は不可。
        ndigits: 小数点以下の桁数。負の桁数も指定できる。
        rounding_unit: `canonical` は cm、`display` は Maya 表示単位。
        compensate_children: 直接の子の world 位置を保持するか。

    Returns:
        値を変更したノードのフル DAG path。変更なしなら空リスト。
    """
    names = _validate_node_names(node_names)
    ensure_util_commands_plugin_loaded()
    command = cast(
        _RoundTranslateCallable,
        getattr(cmds, RoundTranslateCommand.COMMAND_NAME),
    )
    return _decode_result(
        command(
            *names,
            ndigits=ndigits,
            roundingUnit=rounding_unit,
            compensateChildren=compensate_children,
        )
    )


def round_rotate(
    node_names: Sequence[str],
    ndigits: int = 0,
    *,
    rounding_unit: RoundingUnit = "canonical",
    compensate_children: bool = False,
    compensate_child_translate: bool = False,
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
) -> list[str]:
    """指定ノードの `rotate` を一度の Maya Undo で丸める。"""
    return _round_rotation(
        RoundRotateCommand.COMMAND_NAME,
        node_names,
        ndigits,
        rounding_unit=rounding_unit,
        compensate_children=compensate_children,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )


def round_rotate_axis(
    node_names: Sequence[str],
    ndigits: int = 0,
    *,
    rounding_unit: RoundingUnit = "canonical",
    compensate_children: bool = False,
    compensate_child_translate: bool = False,
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
) -> list[str]:
    """指定ノードの `rotateAxis` を一度の Maya Undo で丸める。"""
    return _round_rotation(
        RoundRotateAxisCommand.COMMAND_NAME,
        node_names,
        ndigits,
        rounding_unit=rounding_unit,
        compensate_children=compensate_children,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )


def round_joint_orient(
    node_names: Sequence[str],
    ndigits: int = 0,
    *,
    rounding_unit: RoundingUnit = "canonical",
    compensate_children: bool = False,
    compensate_child_translate: bool = False,
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
) -> list[str]:
    """指定 Joint の `jointOrient` を一度の Maya Undo で丸める。"""
    return _round_rotation(
        RoundJointOrientCommand.COMMAND_NAME,
        node_names,
        ndigits,
        rounding_unit=rounding_unit,
        compensate_children=compensate_children,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )


def _round_rotation(
    command_name: str,
    node_names: Sequence[str],
    ndigits: int,
    *,
    rounding_unit: RoundingUnit,
    compensate_children: bool,
    compensate_child_translate: bool,
    joint_child_compensation_attr: JointChildCompensationAttr,
) -> list[str]:
    """回転系の4フラグを指定して該当 Maya コマンドを呼ぶ。"""
    names = _validate_node_names(node_names)
    ensure_util_commands_plugin_loaded()
    command = cast(_RoundRotationCallable, getattr(cmds, command_name))
    return _decode_result(
        command(
            *names,
            ndigits=ndigits,
            roundingUnit=rounding_unit,
            compensateChildren=compensate_children,
            compensateChildTranslate=compensate_child_translate,
            jointChildCompensationAttr=joint_child_compensation_attr,
        )
    )


def _validate_node_names(node_names: Sequence[str]) -> tuple[str, ...]:
    """呼び出し前に空の対象指定を拒否する。"""
    if isinstance(node_names, (str, bytes)) or not node_names:
        raise ValueError("node_names must contain at least one node name.")
    names = tuple(node_names)
    if any(not isinstance(name, str) or not name for name in names):
        raise ValueError("node_names must contain nonempty node names.")
    return names


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
    raise TypeError(f"Unexpected bdRound command result: {raw_result!r}")
