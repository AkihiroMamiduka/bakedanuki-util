# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from .....maya.mpx_cmd import CommandResult, MPxCommandBase
from .operation import CreateTransformsParams, queue_create_transforms


class CreateTransformsCommand(MPxCommandBase[CreateTransformsParams]):
    COMMAND_NAME = "bduSampleCreateTransforms"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-p", "-prefix", om.MSyntax.kString)
        syntax.addFlag("-c", "-count", om.MSyntax.kLong)
        return syntax

    def parse_arguments(
        self,
        arg_database: om.MArgDatabase,
    ) -> CreateTransformsParams:
        prefix = "bduSample"
        if arg_database.isFlagSet("-prefix"):
            prefix = arg_database.flagArgumentString("-prefix", 0)

        count = 2
        if arg_database.isFlagSet("-count"):
            count = arg_database.flagArgumentInt("-count", 0)

        return CreateTransformsParams(prefix=prefix, count=count)

    def execute(
        self,
        params: CreateTransformsParams,
    ) -> CommandResult:
        transforms = queue_create_transforms(self.nodes, params)

        # The command workflow owns evaluation and transaction boundaries.
        self.modifier_manager.do_it_dag()

        return [transform.name for transform in transforms]
