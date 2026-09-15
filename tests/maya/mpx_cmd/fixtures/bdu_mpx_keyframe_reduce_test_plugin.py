from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


class _ReduceKeyframesCommand(MPxCommandBase[str]):
    COMMAND_NAME = "bduTestMpxReduceKeyframes"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> str:
        return arg_database.flagArgumentString("-nodeName", 0)

    def execute(self, params: str) -> None:
        node = self.nodes.existing.transform(params)
        node.tx.keyframe.reduce_keys(tolerance=0.01)
        self.modifier_manager.do_it_dg()


class _FailAfterReduceKeyframesCommand(_ReduceKeyframesCommand):
    COMMAND_NAME = "bduTestMpxFailAfterReduceKeyframes"

    def execute(self, params: str) -> None:
        super().execute(params)
        raise RuntimeError("intentional keyframe reduction failure")


COMMAND_TYPES = (_ReduceKeyframesCommand, _FailAfterReduceKeyframesCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
