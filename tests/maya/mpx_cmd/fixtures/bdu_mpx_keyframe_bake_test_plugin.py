from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


class _BakeKeyframesCommand(MPxCommandBase[str]):
    COMMAND_NAME = "bduTestMpxBakeKeyframes"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> str:
        return arg_database.flagArgumentString("-nodeName", 0)

    def execute(self, params: str) -> None:
        node = self.nodes.existing.transform(params)
        node.keyframes.bake(1, 5, attributes=["tx"], sample_by=2)
        self.modifier_manager.do_it_dg()


class _FailAfterBakeKeyframesCommand(_BakeKeyframesCommand):
    COMMAND_NAME = "bduTestMpxFailAfterBakeKeyframes"

    def execute(self, params: str) -> None:
        super().execute(params)
        raise RuntimeError("intentional keyframe bake failure")


COMMAND_TYPES = (_BakeKeyframesCommand, _FailAfterBakeKeyframesCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
