from __future__ import annotations

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


class _RemoveLayerPlugsCommand(MPxCommandBase[str]):
    COMMAND_NAME = "bduTestMpxRemoveLayerPlugs"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-l", "-layerName", om.MSyntax.kString)
        return syntax

    def parse_arguments(self, arg_database: om.MArgDatabase) -> str:
        return arg_database.flagArgumentString("-layerName", 0)

    def execute(self, params: str) -> None:
        layer = self.nodes.existing.animLayer(params)
        layer.remove_plugs(["ctrl.tx", "ctrl.ty"])
        self.modifier_manager.do_it_dg()


class _FailAfterRemoveLayerPlugsCommand(_RemoveLayerPlugsCommand):
    COMMAND_NAME = "bduTestMpxFailAfterRemoveLayerPlugs"

    def execute(self, params: str) -> None:
        super().execute(params)
        raise RuntimeError("intentional animation layer removal failure")


COMMAND_TYPES = (_RemoveLayerPlugsCommand, _FailAfterRemoveLayerPlugsCommand)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
