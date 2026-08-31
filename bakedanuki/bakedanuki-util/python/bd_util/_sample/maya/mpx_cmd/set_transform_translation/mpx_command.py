# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from .....maya.mpx_cmd import CommandResult, MPxCommandBase
from .....maya.value import DoubleLinear3
from .operation import (
    SetTransformTranslationParams,
    queue_set_transform_translation,
)


class SetTransformTranslationCommand(
    MPxCommandBase[SetTransformTranslationParams]
):
    COMMAND_NAME = "bduSampleSetTransformTranslation"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-n", "-nodeName", om.MSyntax.kString)
        syntax.addFlag("-tx", "-translateX", om.MSyntax.kDouble)
        syntax.addFlag("-ty", "-translateY", om.MSyntax.kDouble)
        syntax.addFlag("-tz", "-translateZ", om.MSyntax.kDouble)
        return syntax

    def parse_arguments(
        self,
        arg_database: om.MArgDatabase,
    ) -> SetTransformTranslationParams:
        required_flags = (
            "-nodeName",
            "-translateX",
            "-translateY",
            "-translateZ",
        )
        missing_flags = tuple(
            flag for flag in required_flags if not arg_database.isFlagSet(flag)
        )
        if missing_flags:
            raise ValueError(
                "Required flags were not provided: " + ", ".join(missing_flags)
            )

        return SetTransformTranslationParams(
            node_name=arg_database.flagArgumentString("-nodeName", 0),
            translation=DoubleLinear3(
                arg_database.flagArgumentDouble("-translateX", 0),
                arg_database.flagArgumentDouble("-translateY", 0),
                arg_database.flagArgumentDouble("-translateZ", 0),
            ),
        )

    def execute(
        self,
        params: SetTransformTranslationParams,
    ) -> CommandResult:
        transform = queue_set_transform_translation(self.nodes, params)
        current_translation = transform.translate.get().as_tuple()
        if current_translation != params.translation.as_tuple():
            self.modifier_manager.do_it_dg()
        return transform.name
