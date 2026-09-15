from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


class _MoveKeyframesCommand(MPxCommandBase[str]):
    COMMAND_NAME = "bduTestMpxMoveKeyframes"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> str:
        return arg_database.flagArgumentString("-nodeName", 0)

    def execute(self, params: str) -> None:
        node = self.nodes.existing.transform(params)
        node.tx.keyframe.move_key(10, to_frame=20)
        node.ty.keyframe.move_keys(
            12, 18, to_start_frame=40, insert_missing=True
        )
        self.modifier_manager.do_it_dg()


class _FailAfterMoveKeyframesCommand(_MoveKeyframesCommand):
    COMMAND_NAME = "bduTestMpxFailAfterMoveKeyframes"

    def execute(self, params: str) -> None:
        super().execute(params)
        raise RuntimeError("intentional keyframe move failure")


COMMAND_TYPES = (_MoveKeyframesCommand, _FailAfterMoveKeyframesCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
