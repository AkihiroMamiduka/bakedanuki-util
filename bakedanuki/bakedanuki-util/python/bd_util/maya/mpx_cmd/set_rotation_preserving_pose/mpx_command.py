# coding: utf-8
from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om

from ..base import CommandResult, MPxCommandBase
from .operation import (
    AngleInputUnit,
    RotationAttribute,
    SetRotationPreservingPoseParams,
    apply_set_rotation_preserving_pose,
)


class SetRotationPreservingPoseCommand(
    MPxCommandBase[SetRotationPreservingPoseParams]
):
    """NodeOperator の姿勢維持設定を Maya Undo に登録するコマンド。"""

    COMMAND_NAME = "bdSetRotationPreservingPose"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        """対象ノードと設定先・補償先・目標値のフラグを定義する。"""
        syntax = om.MSyntax()
        syntax.setObjectType(om.MSyntax.kStringObjects, 1)
        syntax.useSelectionAsDefault(False)
        syntax.addFlag("-ta", "-targetAttribute", om.MSyntax.kString)
        syntax.addFlag("-cw", "-compensateWith", om.MSyntax.kString)
        syntax.addFlag("-vx", "-valueX", om.MSyntax.kDouble)
        syntax.addFlag("-vy", "-valueY", om.MSyntax.kDouble)
        syntax.addFlag("-vz", "-valueZ", om.MSyntax.kDouble)
        syntax.addFlag("-au", "-angleUnit", om.MSyntax.kString)
        return syntax

    def parse_arguments(
        self, arg_database: om.MArgDatabase
    ) -> SetRotationPreservingPoseParams:
        """Maya 引数を検証済みの姿勢維持設定へ変換する。"""
        required = (
            "-targetAttribute",
            "-compensateWith",
            "-valueX",
            "-valueY",
            "-valueZ",
        )
        missing = tuple(
            flag for flag in required if not arg_database.isFlagSet(flag)
        )
        if missing:
            raise ValueError(
                "Required flags were not provided: " + ", ".join(missing)
            )
        angle_unit = (
            arg_database.flagArgumentString("-angleUnit", 0)
            if arg_database.isFlagSet("-angleUnit")
            else "degrees"
        )
        return SetRotationPreservingPoseParams(
            node_names=tuple(arg_database.getObjectStrings()),
            values=(
                arg_database.flagArgumentDouble("-valueX", 0),
                arg_database.flagArgumentDouble("-valueY", 0),
                arg_database.flagArgumentDouble("-valueZ", 0),
            ),
            target=cast(
                RotationAttribute,
                arg_database.flagArgumentString("-targetAttribute", 0),
            ),
            compensate_with=cast(
                RotationAttribute,
                arg_database.flagArgumentString("-compensateWith", 0),
            ),
            angle_unit=cast(AngleInputUnit, angle_unit),
        )

    def execute(
        self, params: SetRotationPreservingPoseParams
    ) -> CommandResult:
        """複数ノードの変更を一つの Maya Undo にまとめる。"""
        return apply_set_rotation_preserving_pose(self.nodes, params)
