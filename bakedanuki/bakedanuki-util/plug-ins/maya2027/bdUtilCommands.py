# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import deregister_commands, register_commands
from bd_util.maya.mpx_cmd.round_transform.mpx_command import (
    RoundJointOrientCommand,
    RoundRotateAxisCommand,
    RoundRotateCommand,
    RoundTranslateCommand,
)
from bd_util.maya.mpx_cmd.set_rotation_preserving_pose.mpx_command import (
    SetRotationPreservingPoseCommand,
)

COMMAND_TYPES = (
    RoundTranslateCommand,
    RoundRotateCommand,
    RoundRotateAxisCommand,
    RoundJointOrientCommand,
    SetRotationPreservingPoseCommand,
)


def maya_useNewAPI() -> None:
    """Python API 2.0 のコマンドとして登録する。"""
    return None


def initializePlugin(plugin: om.MObject) -> None:
    """丸めと姿勢維持の回転設定コマンドを登録する。"""
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    """登録済みコマンドを逆順に解除する。"""
    deregister_commands(plugin, COMMAND_TYPES)
