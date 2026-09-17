from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


class _ScaleKeyframesCommand(MPxCommandBase[str]):
    COMMAND_NAME = "bduTestMpxScaleKeyframes"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> str:
        return arg_database.flagArgumentString("-nodeName", 0)

    def execute(self, params: str) -> None:
        node = self.nodes.existing.transform(params)
        node.tx.keyframe.scale_keys(10, 20, to_start_frame=20, to_end_frame=40)
        node.ty.keyframe.scale_keys(
            12,
            18,
            time_scale=2,
            to_start_frame=20,
            mode="merge",
            insert_missing=True,
        )
        self.modifier_manager.do_it_dg()


class _FailAfterScaleKeyframesCommand(_ScaleKeyframesCommand):
    COMMAND_NAME = "bduTestMpxFailAfterScaleKeyframes"

    def execute(self, params: str) -> None:
        super().execute(params)
        raise RuntimeError("intentional keyframe scaling failure")


COMMAND_TYPES = (_ScaleKeyframesCommand, _FailAfterScaleKeyframesCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
