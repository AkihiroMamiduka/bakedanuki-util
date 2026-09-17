from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util import AnimationClip
from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    register_commands,
    deregister_commands,
)


class _RestoreClipCommand(MPxCommandBase[tuple[str, str, float, float]]):
    COMMAND_NAME = "bduTestMpxRestoreClip"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-d", "-clipData", om.MSyntax.kString)
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        syntax.addFlag("-o", "-offsetFrames", om.MSyntax.kDouble)
        syntax.addFlag("-s", "-timeScale", om.MSyntax.kDouble)
        return syntax

    def parse_arguments(
        self, arg_database: om.MArgDatabase
    ) -> tuple[str, str, float, float]:
        return (
            arg_database.flagArgumentString("-clipData", 0),
            arg_database.flagArgumentString("-nodeName", 0),
            (
                arg_database.flagArgumentDouble("-offsetFrames", 0)
                if arg_database.isFlagSet("-offsetFrames")
                else 0.0
            ),
            (
                arg_database.flagArgumentDouble("-timeScale", 0)
                if arg_database.isFlagSet("-timeScale")
                else 1.0
            ),
        )

    def execute(self, params: tuple[str, str, float, float]) -> None:
        data, node, offset, scale = params
        AnimationClip.from_json(data).restore(
            self.modifier_manager,
            targets=[node],
            mode="replace_all",
            offset_frames=offset,
            time_scale=scale,
        )
        self.modifier_manager.do_it_dg()


class _FailRestoreClipCommand(_RestoreClipCommand):
    COMMAND_NAME = "bduTestMpxFailRestoreClip"

    def execute(self, params: tuple[str, str, float, float]) -> None:
        super().execute(params)
        raise RuntimeError("intentional animation clip failure")


COMMAND_TYPES = (_RestoreClipCommand, _FailRestoreClipCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
