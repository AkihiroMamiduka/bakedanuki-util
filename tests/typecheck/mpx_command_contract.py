# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import assert_type

from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util._sample.maya.mpx_cmd import (
    CreateTransformsResult,
    SetTransformTranslationResult,
    create_transforms,
    set_transform_translation,
)


@dataclass(frozen=True, slots=True)
class _Params:
    name: str


class _TypedCommand(bdu.MPxCommandBase[_Params]):
    COMMAND_NAME = "bduTypecheckCommand"

    def parse_arguments(self, arg_database: om.MArgDatabase) -> _Params:
        return _Params(name="typed")

    def execute(self, params: _Params) -> bdu.CommandResult:
        self.nodes.create.transform(name=params.name)
        self.modifier_manager.do_it_dag()
        return params.name


command = _TypedCommand()
assert_type(command.nodes, bdu.Nodes)
assert_type(command.modifier_manager, bdu.ModifierManager)

facade_result = create_transforms(prefix="typed", count=3)
assert_type(facade_result, CreateTransformsResult)
assert_type(facade_result.node_names, tuple[str, ...])

translation_result = set_transform_translation(
    node_name="typed",
    translation=(1.0, 2.0, 3.0),
)
assert_type(translation_result, SetTransformTranslationResult)
assert_type(translation_result.node_name, str)
assert_type(translation_result.translation, bdu.DoubleLinear3)
