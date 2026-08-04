# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


OPERATIONS = (
    ("EQUAL", 0, 2.0, 2.0, 3.0),
    ("NOT_EQUAL", 1, 2.0, 3.0, 3.0),
    ("GREATER_THAN", 2, 3.0, 2.0, 2.0),
    ("GREATER_OR_EQUAL", 3, 2.0, 2.0, 1.0),
    ("LESS_THAN", 4, 2.0, 3.0, 3.0),
    ("LESS_OR_EQUAL", 5, 2.0, 2.0, 3.0),
)


def _load_bd_util_nodes(maya_cmds) -> Path:
    default_path = (
        Path(__file__).resolve().parents[6]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / "maya2025"
        / "bdUtilNodes.mll"
    )
    plugin_path = Path(
        os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
    )
    if not plugin_path.is_file():
        pytest.skip(
            "bdUtilNodes.mll is not built. "
            "Run scripts/build-native-maya2025.cmd first."
        )

    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    return plugin_path


def test_class_attributes_and_operation_enum(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_condition import (
        BdDbl3Condition,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl3_condition_multi import (
        BdDbl3ConditionMulti,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_condition import (
        BdDblCondition,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_condition_multi import (
        BdDblConditionMulti,
    )

    assert BdDblCondition.NODE_TYPE == "bdDbl_Condition"
    assert BdDblCondition.input.long_name == "input"
    assert BdDblCondition.op.short_name == "op"
    assert BdDblCondition.cmp.short_name == "cmp"
    assert BdDblCondition.tv.short_name == "tv"
    assert BdDblCondition.fv.short_name == "fv"
    assert BdDblCondition.operation.GREATER_THAN == 2
    assert BdDblCondition.operation.name_by_index(3) == "Greater or Equal"

    assert BdDbl3Condition.NODE_TYPE == "bdDbl3_Condition"
    assert BdDbl3Condition.trueValue.trueValueX.long_name == "trueValueX"
    assert BdDbl3Condition.falseValue.falseValueZ.short_name == "fvz"
    assert BdDbl3Condition.output.outputY.short_name == "oy"

    assert BdDblConditionMulti.NODE_TYPE == "bdDbl_ConditionMulti"
    assert BdDblConditionMulti.case.long_name == "case"
    assert BdDblConditionMulti.cs.short_name == "cs"
    assert BdDblConditionMulti.case.operation.long_name == "operation"
    assert BdDblConditionMulti.case.compare.short_name == "cmp"
    assert BdDblConditionMulti.case.value.short_name == "v"
    assert BdDblConditionMulti.elseValue.short_name == "ev"

    assert BdDbl3ConditionMulti.NODE_TYPE == "bdDbl3_ConditionMulti"
    assert BdDbl3ConditionMulti.case.value.long_name == "value"
    assert BdDbl3ConditionMulti.elseValue.elseValueY.short_name == "evy"


@pytest.mark.parametrize(
    ("node_type", "type_id"),
    (
        ("bdDbl3_ConditionMulti", 0x0007F02B),
        ("bdDbl3_Condition", 0x0007F02C),
        ("bdDbl_ConditionMulti", 0x0007F02D),
        ("bdDbl_Condition", 0x0007F02E),
    ),
)
def test_defaults_and_type_ids(maya_cmds, maya_om, node_type, type_id):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_object = selection.getDependNode(0)
    assert maya_om.MFnDependencyNode(node_object).typeId.id() == type_id
    assert maya_cmds.getAttr(f"{node}.input") == pytest.approx(0.0)

    if node_type.endswith("ConditionMulti"):
        assert maya_cmds.getAttr(f"{node}.elseValue") == (
            pytest.approx(0.0)
            if node_type.startswith("bdDbl_")
            else [pytest.approx((0.0, 0.0, 0.0))]
        )
    else:
        assert maya_cmds.getAttr(f"{node}.compare") == pytest.approx(0.0)
        assert maya_cmds.getAttr(f"{node}.operation") == 0
        if node_type.startswith("bdDbl_"):
            assert maya_cmds.getAttr(f"{node}.trueValue") == pytest.approx(0.0)
            assert maya_cmds.getAttr(f"{node}.falseValue") == pytest.approx(
                0.0
            )
        else:
            assert maya_cmds.getAttr(f"{node}.trueValue")[0] == pytest.approx(
                (0.0, 0.0, 0.0)
            )
            assert maya_cmds.getAttr(f"{node}.falseValue")[0] == pytest.approx(
                (0.0, 0.0, 0.0)
            )


@pytest.mark.parametrize(
    (
        "operation_name",
        "operation",
        "input_value",
        "compare_value",
        "false_input",
    ),
    OPERATIONS,
)
def test_single_supports_all_comparison_operations(
    modifier_manager,
    maya_cmds,
    operation_name,
    operation,
    input_value,
    compare_value,
    false_input,
):
    del operation_name
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Condition()
    node.input.set(input_value)
    node.operation.set(operation)
    node.compare.set(compare_value)
    node.trueValue.set(12.0)
    node.falseValue.set(-4.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(12.0)

    node.input.set(false_input)
    modifier_manager.do_it_dg()
    assert node.output.get() == pytest.approx(-4.0)


def test_single_double3_selects_whole_value(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Condition()
    node.input.set(5.0)
    node.operation.set(node.operation.GREATER_THAN)
    node.compare.set(3.0)
    node.trueValue.set((1.0, 2.0, 3.0))
    node.falseValue.set((-1.0, -2.0, -3.0))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 2.0, 3.0))

    node.input.set(2.0)
    modifier_manager.do_it_dg()
    assert node.output.get().as_tuple() == pytest.approx((-1.0, -2.0, -3.0))


def test_multi_uses_logical_index_order_and_first_match(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_ConditionMulti()
    node.input.set(5.0)
    node.case[10].operation.set(node.case[10].operation.LESS_THAN)
    node.case[10].compare.set(10.0)
    node.case[10].value.set(10.0)
    node.case[2].operation.set(node.case[2].operation.GREATER_THAN)
    node.case[2].compare.set(0.0)
    node.case[2].value.set(2.0)
    node.elseValue.set(-1.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(2.0)

    maya_cmds.removeMultiInstance(f"{node.name}.case[2]", b=True)
    assert node.output.get() == pytest.approx(10.0)

    maya_cmds.setAttr(f"{node.name}.input", 20.0)
    assert node.output.get() == pytest.approx(-1.0)


def test_empty_multi_returns_else_value(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDbl_ConditionMulti()
    vector = nodes.create.bdDbl3_ConditionMulti()
    scalar.elseValue.set(7.0)
    vector.elseValue.set((7.0, 8.0, 9.0))
    modifier_manager.do_it_dg()

    assert scalar.output.get() == pytest.approx(7.0)
    assert vector.output.get().as_tuple() == pytest.approx((7.0, 8.0, 9.0))


def test_double3_multi_selects_case_value(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_ConditionMulti()
    node.input.set(-2.0)
    node.case[4].operation.set(node.case[4].operation.LESS_THAN)
    node.case[4].compare.set(0.0)
    node.case[4].value.set((1.0, 2.0, 3.0))
    node.elseValue.set((-1.0, -2.0, -3.0))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 2.0, 3.0))


@pytest.mark.parametrize(
    ("operation", "expected"),
    ((0, -1.0), (1, 1.0), (2, -1.0), (3, -1.0), (4, -1.0), (5, -1.0)),
)
def test_nan_uses_ieee_comparison_semantics(maya_cmds, operation, expected):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Condition")
    maya_cmds.setAttr(f"{node}.input", float("nan"))
    maya_cmds.setAttr(f"{node}.operation", operation)
    maya_cmds.setAttr(f"{node}.compare", 0.0)
    maya_cmds.setAttr(f"{node}.trueValue", 1.0)
    maya_cmds.setAttr(f"{node}.falseValue", -1.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)


def test_infinity_uses_normal_ordering(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Condition")
    maya_cmds.setAttr(f"{node}.input", math.inf)
    maya_cmds.setAttr(f"{node}.operation", 2)
    maya_cmds.setAttr(f"{node}.compare", 1.0)
    maya_cmds.setAttr(f"{node}.trueValue", 1.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(1.0)


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_nested_case_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl3_ConditionMulti")
        maya_cmds.setAttr(f"{node}.input", 2.0)
        maya_cmds.setAttr(f"{node}.case[3].operation", 2)
        maya_cmds.setAttr(f"{node}.case[3].compare", 1.0)
        maya_cmds.setAttr(
            f"{node}.case[3].value",
            1.0,
            2.0,
            3.0,
            type="double3",
        )
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (1.0, 2.0, 3.0)
        )

        maya_cmds.setAttr(f"{node}.case[3].compare", 5.0)
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (0.0, 0.0, 0.0)
        )

        maya_cmds.setAttr(f"{node}.case[3].compare", 1.0)
        maya_cmds.setAttr(f"{node}.case[3].valueY", 8.0)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(8.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connections_existing_accessors_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    first = nodes.create.bdDbl_Condition(name="first")
    multi = nodes.create.bdDbl_ConditionMulti(name="multi")
    first.input.set(2.0)
    first.operation.set(first.operation.GREATER_THAN)
    first.compare.set(1.0)
    first.trueValue.set(5.0)
    first.output.connect(multi.input)
    multi.case[0].operation.set(multi.case[0].operation.GREATER_THAN)
    multi.case[0].compare.set(3.0)
    multi.case[0].value.set(10.0)
    multi.elseValue.set(-10.0)
    modifier_manager.do_it_dg()

    assert multi.output.get() == pytest.approx(10.0)
    assert type(nodes.existing.bdDbl_Condition(first.name)) is type(first)
    assert type(nodes.existing.bdDbl_ConditionMulti(multi.name)) is type(multi)

    scene_path = tmp_path / "bd_condition.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded_nodes.existing.bdDbl_ConditionMulti(
        "multi"
    ).output.get() == pytest.approx(10.0)
