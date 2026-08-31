# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util._sample.maya.mpx_cmd.create_transforms.mpx_command import (
    CreateTransformsCommand,
)
from bd_util._sample.maya.mpx_cmd.set_transform_translation.mpx_command import (
    SetTransformTranslationCommand,
)
from bd_util.maya.mpx_cmd import deregister_commands, register_commands

COMMAND_TYPES = (
    CreateTransformsCommand,
    SetTransformTranslationCommand,
)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
