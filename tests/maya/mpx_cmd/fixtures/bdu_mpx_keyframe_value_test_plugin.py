from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


class _EditKeyframeValuesCommand(MPxCommandBase[str]):
    COMMAND_NAME = "bduTestMpxEditKeyframeValues"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> str:
        return arg_database.flagArgumentString("-nodeName", 0)

    def execute(self, params: str) -> None:
        node = self.nodes.existing.transform(params)
        node.tx.keyframe.set_values(10, 20, value=3)
        node.tx.keyframe.add_value(10, offset_value=2)
        node.tx.keyframe.scale_value(20, value_scale=-2, pivot_value=1)
        node.ty.keyframe.set_value(10, value=3)
        node.ty.keyframe.add_values(
            10, 20, offset_value=2, interpolate_start=0, interpolate_end=30
        )
        node.ty.keyframe.scale_values(
            12,
            18,
            value_scale=-2,
            pivot_value=1,
            interpolate_start=5,
            interpolate_end=25,
            insert_missing=True,
        )
        self.modifier_manager.do_it_dg()


class _FailAfterEditKeyframeValuesCommand(_EditKeyframeValuesCommand):
    COMMAND_NAME = "bduTestMpxFailAfterEditKeyframeValues"

    def execute(self, params: str) -> None:
        super().execute(params)
        raise RuntimeError("intentional keyframe value failure")


COMMAND_TYPES = (
    _EditKeyframeValuesCommand,
    _FailAfterEditKeyframeValuesCommand,
)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
