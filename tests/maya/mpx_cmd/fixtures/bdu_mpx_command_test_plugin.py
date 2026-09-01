# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import (
    CommandResult,
    MPxCommandBase,
    deregister_commands,
    register_commands,
)


@dataclass(frozen=True, slots=True)
class _FailureParams:
    node_name: str


class _FailAfterExecuteCommand(MPxCommandBase[_FailureParams]):
    COMMAND_NAME = "bduTestMpxFailAfterExecute"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        return syntax

    def parse_arguments(
        self,
        arg_database: om.MArgDatabase,
    ) -> _FailureParams:
        node_name = "bdu_mpx_rollback_test"
        if arg_database.isFlagSet("-nodeName"):
            node_name = arg_database.flagArgumentString("-nodeName", 0)
        return _FailureParams(node_name=node_name)

    def execute(self, params: _FailureParams) -> CommandResult | None:
        self.nodes.create.transform(name=params.node_name)
        self.modifier_manager.do_it_dag()

        self.nodes.create.plusMinusAverage(name=f"{params.node_name}_dg")
        self.modifier_manager.do_it_dg()
        raise RuntimeError("intentional MPxCommand failure")


class _NoOpCommand(MPxCommandBase[None]):
    COMMAND_NAME = "bduTestMpxNoOp"

    def parse_arguments(self, arg_database: om.MArgDatabase) -> None:
        return None

    def execute(self, params: None) -> CommandResult:
        if self.nodes.modifier_manager is not self.modifier_manager:
            raise RuntimeError("MPxCommand Nodes must share ModifierManager.")
        return "no-op"


COMMAND_TYPES = (
    _FailAfterExecuteCommand,
    _NoOpCommand,
)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
