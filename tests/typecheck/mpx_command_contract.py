# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import assert_type

from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util._sample.maya.mpx_cmd import (
    CreateTransformsParams,
    CreateTransformsResult,
    SetTransformTranslationParams,
    SetTransformTranslationResult,
    apply_create_transforms,
    apply_set_transform_translation,
    create_transforms,
    set_transform_translation,
)
from bd_util.maya.mpx_cmd.round_transform import (
    round_joint_orient,
    round_rotate,
    round_rotate_axis,
    round_translate,
)
from bd_util.maya.mpx_cmd import set_rotation_preserving_pose


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

assert_type(round_translate(["ctrl"], 2), list[str])
assert_type(round_translate(["ctrl"], 2, rounding_unit="display"), list[str])
assert_type(
    round_rotate(
        ["ctrl"],
        2,
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr="jointOrient",
    ),
    list[str],
)
assert_type(round_rotate_axis(["ctrl"], 2), list[str])
assert_type(round_joint_orient(["joint"], 2), list[str])
assert_type(
    set_rotation_preserving_pose(
        ["joint"],
        (10.0, 20.0, 30.0),
        target="jointOrient",
        compensate_with="rotateAxis",
        angle_unit="display",
    ),
    list[str],
)

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

operation_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
create_operation_result = apply_create_transforms(
    operation_nodes,
    CreateTransformsParams(prefix="operation", count=2),
)
assert_type(create_operation_result, CreateTransformsResult)

translation_operation_result = apply_set_transform_translation(
    operation_nodes,
    SetTransformTranslationParams(
        node_name="operation1",
        translation=bdu.DoubleLinear3(1.0, 2.0, 3.0),
    ),
)
assert_type(
    translation_operation_result,
    SetTransformTranslationResult,
)
