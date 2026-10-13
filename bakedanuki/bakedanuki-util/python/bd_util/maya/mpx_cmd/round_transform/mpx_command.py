# coding: utf-8
from __future__ import annotations

from typing import ClassVar, cast

from maya.api import OpenMaya as om

from ..base import CommandResult, MPxCommandBase
from ...node.operator.node.dag.transform._core import (
    JointChildCompensationAttr,
)
from ...rounding import RoundingUnit
from .operation import (
    RoundKind,
    RoundTransformParams,
    apply_round_transform,
)


class _RoundTransformCommand(MPxCommandBase[RoundTransformParams]):
    """NodeOperator の丸めを Maya Undo に登録する共通コマンド。"""

    ROUND_KIND: ClassVar[RoundKind]

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        """対象ノードの明示指定と丸め・補償フラグを受け取る。"""
        syntax = om.MSyntax()
        syntax.setObjectType(om.MSyntax.kStringObjects, 1)
        syntax.useSelectionAsDefault(False)
        syntax.addFlag("-n", "-ndigits", om.MSyntax.kLong)
        syntax.addFlag("-ru", "-roundingUnit", om.MSyntax.kString)
        syntax.addFlag("-cc", "-compensateChildren", om.MSyntax.kBoolean)
        if cls.ROUND_KIND != "translate":
            syntax.addFlag(
                "-ct", "-compensateChildTranslate", om.MSyntax.kBoolean
            )
            syntax.addFlag(
                "-jc", "-jointChildCompensationAttr", om.MSyntax.kString
            )
        return syntax

    def parse_arguments(
        self, arg_database: om.MArgDatabase
    ) -> RoundTransformParams:
        """Maya の引数を検証済みの丸め条件へ変換する。"""
        names = tuple(arg_database.getObjectStrings())
        ndigits = (
            arg_database.flagArgumentInt("-ndigits", 0)
            if arg_database.isFlagSet("-ndigits")
            else 0
        )
        rounding_unit = (
            cast(
                RoundingUnit,
                arg_database.flagArgumentString("-roundingUnit", 0),
            )
            if arg_database.isFlagSet("-roundingUnit")
            else "canonical"
        )
        compensate_children = (
            arg_database.flagArgumentBool("-compensateChildren", 0)
            if arg_database.isFlagSet("-compensateChildren")
            else False
        )
        compensate_child_translate = (
            arg_database.flagArgumentBool("-compensateChildTranslate", 0)
            if self.ROUND_KIND != "translate"
            and arg_database.isFlagSet("-compensateChildTranslate")
            else False
        )
        child_attr = (
            arg_database.flagArgumentString("-jointChildCompensationAttr", 0)
            if self.ROUND_KIND != "translate"
            and arg_database.isFlagSet("-jointChildCompensationAttr")
            else "rotate"
        )
        return RoundTransformParams(
            node_names=names,
            ndigits=ndigits,
            rounding_unit=rounding_unit,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=cast(
                JointChildCompensationAttr, child_attr
            ),
        )

    def execute(self, params: RoundTransformParams) -> CommandResult:
        """選択ノードを親から処理して Undo 可能な結果を返す。"""
        return apply_round_transform(self.nodes, self.ROUND_KIND, params)


class RoundTranslateCommand(_RoundTransformCommand):
    """`translate` の四捨五入コマンド。"""

    COMMAND_NAME = "bdRoundTranslate"
    ROUND_KIND = "translate"


class RoundRotateCommand(_RoundTransformCommand):
    """`rotate` の四捨五入コマンド。"""

    COMMAND_NAME = "bdRoundRotate"
    ROUND_KIND = "rotate"


class RoundRotateAxisCommand(_RoundTransformCommand):
    """`rotateAxis` の四捨五入コマンド。"""

    COMMAND_NAME = "bdRoundRotateAxis"
    ROUND_KIND = "rotateAxis"


class RoundJointOrientCommand(_RoundTransformCommand):
    """`jointOrient` の四捨五入コマンド。"""

    COMMAND_NAME = "bdRoundJointOrient"
    ROUND_KIND = "jointOrient"
