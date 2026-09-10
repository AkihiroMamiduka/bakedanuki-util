# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from functools import partial

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

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


class _SetKeyframesCommand(_FailAfterExecuteCommand):
    COMMAND_NAME = "bduTestMpxSetKeyframes"

    def execute(self, params: _FailureParams) -> None:
        node = self.nodes.existing.transform(params.node_name)
        node.scale.scaleX.set(2.0)
        self.modifier_manager.do_it_dg()
        node.translate.translateX.keyframe.set(10.0, frame=1.0)
        node.translate.translateY.keyframe.set(20.0, frame=2.0)
        self.modifier_manager.do_it_dg()


class _EditKeyframesCommand(_FailAfterExecuteCommand):
    COMMAND_NAME = "bduTestMpxEditKeyframes"

    def _queue_edits(self, params: _FailureParams) -> None:
        self.nodes.create.transform(name=f"{params.node_name}_dag")
        self.modifier_manager.do_it_dag()
        node = self.nodes.existing.transform(params.node_name)
        node.scaleX.set(2.0)
        self.modifier_manager.do_it_dg()
        keyframe = node.translateX.keyframe
        keyframe.set(5.0, frame=5.0)
        keyframe.insert(frame=2.0)
        keyframe.set_tangent(
            frame=2.0, in_tangent_type="linear", out_tangent_type="linear"
        )
        keyframe.delete_key(frame=3.0)
        node.translateY.keyframe.delete_anim_curve()

    def execute(self, params: _FailureParams) -> None:
        self._queue_edits(params)
        self.modifier_manager.do_it_dg()


class _FailAfterAnimationEditCommand(_EditKeyframesCommand):
    COMMAND_NAME = "bduTestMpxFailAfterAnimationEdit"

    def execute(self, params: _FailureParams) -> None:
        super().execute(params)
        raise RuntimeError("intentional animation command failure")


class _FailDuringAnimationEditCommand(_EditKeyframesCommand):
    COMMAND_NAME = "bduTestMpxFailDuringAnimationEdit"

    def execute(self, params: _FailureParams) -> None:
        self._queue_edits(params)

        def fail_after_edit(change: oma.MAnimCurveChange) -> None:
            curve_name = cmds.listConnections(
                f"{params.node_name}.translateX",
                source=True,
                destination=False,
                type="animCurve",
            )[0]
            selection = om.MSelectionList()
            selection.add(curve_name)
            fn = oma.MFnAnimCurve(selection.getDependNode(0))
            fn.remove(0, change=change)
            raise RuntimeError("intentional animation callback failure")

        self.modifier_manager.queue_anim_curve_change(fail_after_edit)
        self.modifier_manager.do_it_dg()


class _NoOpCommand(MPxCommandBase[None]):
    COMMAND_NAME = "bduTestMpxNoOp"

    def parse_arguments(self, arg_database: om.MArgDatabase) -> None:
        return None

    def execute(self, params: None) -> CommandResult:
        if self.nodes.modifier_manager is not self.modifier_manager:
            raise RuntimeError("MPxCommand Nodes must share ModifierManager.")
        return "no-op"


class _FailDuringExecuteCommand(_FailAfterExecuteCommand):
    COMMAND_NAME = "bduTestMpxFailDuringExecute"

    def execute(self, params: _FailureParams) -> CommandResult | None:
        self.nodes.create.transform(name=f"{params.node_name}_dag")
        self.modifier_manager.do_it_dag()

        target = self.nodes.existing.transform(params.node_name)
        target.translateY.set(12.0)
        modifier = self.modifier_manager.dg_mod
        modifier.pythonCommandToExecute(
            partial(
                cmds.setKeyframe,
                f"{params.node_name}.translateX",
                time=1,
                value=7,
            )
        )
        modifier.pythonCommandToExecute(
            partial(cmds.setKeyframe, "missing_node.translateX", time=1)
        )
        self.modifier_manager.do_it_dg()


COMMAND_TYPES = (
    _SetKeyframesCommand,
    _EditKeyframesCommand,
    _FailAfterAnimationEditCommand,
    _FailDuringAnimationEditCommand,
    _FailAfterExecuteCommand,
    _FailDuringExecuteCommand,
    _NoOpCommand,
)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
