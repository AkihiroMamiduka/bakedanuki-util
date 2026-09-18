from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util import AnimationClip
from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    register_commands,
    deregister_commands,
)

RestoreParams = tuple[str, str, float, float, float | None, float | None]


class _RestoreClipCommand(MPxCommandBase[RestoreParams]):
    COMMAND_NAME = "bduTestMpxRestoreClip"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-d", "-clipData", om.MSyntax.kString)
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        syntax.addFlag("-o", "-offsetFrames", om.MSyntax.kDouble)
        syntax.addFlag("-s", "-timeScale", om.MSyntax.kDouble)
        syntax.addFlag("-sf", "-startFrame", om.MSyntax.kDouble)
        syntax.addFlag("-ef", "-endFrame", om.MSyntax.kDouble)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> RestoreParams:
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
            (
                arg_database.flagArgumentDouble("-startFrame", 0)
                if arg_database.isFlagSet("-startFrame")
                else None
            ),
            (
                arg_database.flagArgumentDouble("-endFrame", 0)
                if arg_database.isFlagSet("-endFrame")
                else None
            ),
        )

    def execute(self, params: RestoreParams) -> None:
        data, node, offset, scale, start, end = params
        AnimationClip.from_json(data).restore(
            self.modifier_manager,
            targets=[node],
            mode="replace_all",
            start_frame=start,
            end_frame=end,
            offset_frames=offset,
            time_scale=scale,
        )
        self.modifier_manager.do_it_dg()


class _FailRestoreClipCommand(_RestoreClipCommand):
    COMMAND_NAME = "bduTestMpxFailRestoreClip"

    def execute(self, params: RestoreParams) -> None:
        super().execute(params)
        raise RuntimeError("intentional animation clip failure")


COMMAND_TYPES = (_RestoreClipCommand, _FailRestoreClipCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
