# coding: utf-8
from __future__ import annotations

from typing import ClassVar, cast

from maya.api import OpenMaya as om

from ..base import CommandResult, MPxCommandBase
from ...node.operator.node.dag.transform._core import (
    JointChildCompensationAttr,
    TransformSpace,
)
from .operation import (
    InputUnit,
    SetKind,
    SetTransformCompensateChildrenParams,
    apply_set_transform_compensate_children,
)


class _SetTransformCompensateChildrenCommand(
    MPxCommandBase[SetTransformCompensateChildrenParams]
):
    """NodeOperator の子補償設定を Maya Undo に登録する共通コマンド。"""

    SET_KIND: ClassVar[SetKind]

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        """対象ノード、目標 XYZ、入力空間と子補償条件を定義する。"""
        syntax = om.MSyntax()
        syntax.setObjectType(om.MSyntax.kStringObjects, 1)
        syntax.useSelectionAsDefault(False)
        syntax.addFlag("-vx", "-valueX", om.MSyntax.kDouble)
        syntax.addFlag("-vy", "-valueY", om.MSyntax.kDouble)
        syntax.addFlag("-vz", "-valueZ", om.MSyntax.kDouble)
        syntax.addFlag("-sp", "-space", om.MSyntax.kString)
        syntax.addFlag("-iu", "-inputUnit", om.MSyntax.kString)
        if cls.SET_KIND != "translate":
            syntax.addFlag(
                "-ct", "-compensateChildTranslate", om.MSyntax.kBoolean
            )
            syntax.addFlag(
                "-jc", "-jointChildCompensationAttr", om.MSyntax.kString
            )
        return syntax

    def parse_arguments(
        self, arg_database: om.MArgDatabase
    ) -> SetTransformCompensateChildrenParams:
        """Maya 引数を検証済みの子補償設定へ変換する。"""
        required = ("-valueX", "-valueY", "-valueZ")
        missing = tuple(
            flag for flag in required if not arg_database.isFlagSet(flag)
        )
        if missing:
            raise ValueError(
                "Required flags were not provided: " + ", ".join(missing)
            )
        space = (
            arg_database.flagArgumentString("-space", 0)
            if arg_database.isFlagSet("-space")
            else "local"
        )
        input_unit = (
            arg_database.flagArgumentString("-inputUnit", 0)
            if arg_database.isFlagSet("-inputUnit")
            else "canonical"
        )
        compensate_child_translate = (
            arg_database.flagArgumentBool("-compensateChildTranslate", 0)
            if self.SET_KIND != "translate"
            and arg_database.isFlagSet("-compensateChildTranslate")
            else True
        )
        child_attr = (
            arg_database.flagArgumentString("-jointChildCompensationAttr", 0)
            if self.SET_KIND != "translate"
            and arg_database.isFlagSet("-jointChildCompensationAttr")
            else "rotate"
        )
        return SetTransformCompensateChildrenParams(
            node_names=tuple(arg_database.getObjectStrings()),
            values=(
                arg_database.flagArgumentDouble("-valueX", 0),
                arg_database.flagArgumentDouble("-valueY", 0),
                arg_database.flagArgumentDouble("-valueZ", 0),
            ),
            space=cast(TransformSpace, space),
            input_unit=cast(InputUnit, input_unit),
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=cast(
                JointChildCompensationAttr, child_attr
            ),
        )

    def execute(
        self, params: SetTransformCompensateChildrenParams
    ) -> CommandResult:
        """親から子へ確定し、すべてを一度の Maya Undo にまとめる。"""
        return apply_set_transform_compensate_children(
            self.nodes, self.SET_KIND, params
        )


class SetTranslateCompensateChildrenCommand(
    _SetTransformCompensateChildrenCommand
):
    """子の world 位置を保つ `translate` 設定コマンド。"""

    COMMAND_NAME = "bdSetTranslateCompensateChildren"
    SET_KIND = "translate"


class SetRotateCompensateChildrenCommand(
    _SetTransformCompensateChildrenCommand
):
    """子の world 姿勢と任意の位置を保つ `rotate` 設定コマンド。"""

    COMMAND_NAME = "bdSetRotateCompensateChildren"
    SET_KIND = "rotate"


class SetRotateAxisCompensateChildrenCommand(
    _SetTransformCompensateChildrenCommand
):
    """子の world 姿勢と任意の位置を保つ `rotateAxis` 設定コマンド。"""

    COMMAND_NAME = "bdSetRotateAxisCompensateChildren"
    SET_KIND = "rotateAxis"


class SetJointOrientCompensateChildrenCommand(
    _SetTransformCompensateChildrenCommand
):
    """子の world 姿勢と任意の位置を保つ `jointOrient` 設定コマンド。"""

    COMMAND_NAME = "bdSetJointOrientCompensateChildren"
    SET_KIND = "jointOrient"
