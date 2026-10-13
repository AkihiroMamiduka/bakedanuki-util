# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, cast

from maya import cmds

from ...node.operator.node.dag.transform._core import (
    JointChildCompensationAttr,
    TransformSpace,
)
from ..round_transform._plugin import ensure_util_commands_plugin_loaded
from .mpx_command import (
    SetJointOrientCompensateChildrenCommand,
    SetRotateAxisCompensateChildrenCommand,
    SetRotateCompensateChildrenCommand,
    SetTranslateCompensateChildrenCommand,
)
from .operation import InputUnit, SetTransformCompensateChildrenParams


class _SetTranslateCallable(Protocol):
    """動的 Maya コマンドの移動設定引数を局所的に型付けする。"""

    def __call__(
        self,
        *node_names: str,
        valueX: float,
        valueY: float,
        valueZ: float,
        space: str,
        inputUnit: str,
    ) -> object:
        """Maya の移動設定コマンドを呼ぶ。"""
        ...


class _SetRotationCallable(Protocol):
    """動的 Maya コマンドの回転設定引数を局所的に型付けする。"""

    def __call__(
        self,
        *node_names: str,
        valueX: float,
        valueY: float,
        valueZ: float,
        space: str,
        inputUnit: str,
        compensateChildTranslate: bool,
        jointChildCompensationAttr: str,
    ) -> object:
        """Maya の回転設定コマンドを呼ぶ。"""
        ...


def set_translate_compensate_children(
    node_names: Sequence[str],
    values: tuple[float, float, float],
    *,
    space: TransformSpace = "local",
    input_unit: InputUnit = "canonical",
) -> list[str]:
    """子の world 位置を保って `translate` を一度の Undo で設定する。

    Args:
        node_names: 対象 Transform / Joint の名前。空列は不可。
        values: 全対象へ設定する XYZ。`world` では DAG 原点の位置。
        space: `local` は属性値、`world` は world 位置。
        input_unit: `canonical` は cm、`display` は Maya 表示距離単位。

    Returns:
        値を変更したノードのフル DAG path。変更なしなら空リスト。
    """
    params = SetTransformCompensateChildrenParams(
        node_names=_validate_node_names(node_names),
        values=values,
        space=space,
        input_unit=input_unit,
    )
    ensure_util_commands_plugin_loaded()
    command = cast(
        _SetTranslateCallable,
        getattr(cmds, SetTranslateCompensateChildrenCommand.COMMAND_NAME),
    )
    return _decode_result(
        command(
            *params.node_names,
            valueX=params.values[0],
            valueY=params.values[1],
            valueZ=params.values[2],
            space=params.space,
            inputUnit=params.input_unit,
        )
    )


def set_rotate_compensate_children(
    node_names: Sequence[str],
    values: tuple[float, float, float],
    *,
    space: TransformSpace = "local",
    input_unit: InputUnit = "canonical",
    compensate_child_translate: bool = True,
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
) -> list[str]:
    """子の world 姿勢と任意の位置を保って `rotate` を設定する。"""
    return _set_rotation(
        SetRotateCompensateChildrenCommand.COMMAND_NAME,
        node_names,
        values,
        space=space,
        input_unit=input_unit,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )


def set_rotate_axis_compensate_children(
    node_names: Sequence[str],
    values: tuple[float, float, float],
    *,
    space: TransformSpace = "local",
    input_unit: InputUnit = "canonical",
    compensate_child_translate: bool = True,
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
) -> list[str]:
    """子の world 姿勢と任意の位置を保って `rotateAxis` を設定する。"""
    return _set_rotation(
        SetRotateAxisCompensateChildrenCommand.COMMAND_NAME,
        node_names,
        values,
        space=space,
        input_unit=input_unit,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )


def set_joint_orient_compensate_children(
    node_names: Sequence[str],
    values: tuple[float, float, float],
    *,
    space: TransformSpace = "local",
    input_unit: InputUnit = "canonical",
    compensate_child_translate: bool = True,
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
) -> list[str]:
    """子の world 姿勢と任意の位置を保って `jointOrient` を設定する。"""
    return _set_rotation(
        SetJointOrientCompensateChildrenCommand.COMMAND_NAME,
        node_names,
        values,
        space=space,
        input_unit=input_unit,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )


def _set_rotation(
    command_name: str,
    node_names: Sequence[str],
    values: tuple[float, float, float],
    *,
    space: TransformSpace,
    input_unit: InputUnit,
    compensate_child_translate: bool,
    joint_child_compensation_attr: JointChildCompensationAttr,
) -> list[str]:
    """共通の回転入力を検証し、該当 Maya コマンドへ渡す。"""
    params = SetTransformCompensateChildrenParams(
        node_names=_validate_node_names(node_names),
        values=values,
        space=space,
        input_unit=input_unit,
        compensate_child_translate=compensate_child_translate,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )
    ensure_util_commands_plugin_loaded()
    command = cast(_SetRotationCallable, getattr(cmds, command_name))
    return _decode_result(
        command(
            *params.node_names,
            valueX=params.values[0],
            valueY=params.values[1],
            valueZ=params.values[2],
            space=params.space,
            inputUnit=params.input_unit,
            compensateChildTranslate=params.compensate_child_translate,
            jointChildCompensationAttr=params.joint_child_compensation_attr,
        )
    )


def _validate_node_names(node_names: Sequence[str]) -> tuple[str, ...]:
    """空の対象指定と文字列を列として扱う誤用を拒否する。"""
    if isinstance(node_names, (str, bytes)):
        raise ValueError("node_names must contain node names, not a string.")
    return tuple(node_names)


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
    raise TypeError(f"Unexpected bdSet command result: {raw_result!r}")
