# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


OPERATIONS = (
    (0, 2.0, 2.0, 3.0),
    (1, 2.0, 3.0, 3.0),
    (2, 3.0, 2.0, 2.0),
    (3, 2.0, 2.0, 1.0),
    (4, 2.0, 3.0, 3.0),
    (5, 2.0, 2.0, 3.0),
)

NODE_TYPE_IDS = {
    "bdAny_ConditionDbl": 0x0007F02E,
    "bdAny_ConditionDblMulti": 0x0007F02D,
    "bdAny_ConditionDblL": 0x0007F059,
    "bdAny_ConditionDblLMulti": 0x0007F05A,
}

REMOVED_NODE_TYPES = {
    "bdDbl_Condition",
    "bdDbl_ConditionMulti",
    "bdDbl3_Condition",
    "bdDbl3_ConditionMulti",
    "bdDblL_Condition",
    "bdDblL_ConditionMulti",
    "bdDblL3_Condition",
    "bdDblL3_ConditionMulti",
}


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


def _create_numeric_plug(maya_cmds, value, attribute_type="double"):
    node = maya_cmds.createNode("network")
    maya_cmds.addAttr(node, longName="value", attributeType=attribute_type)
    maya_cmds.setAttr(f"{node}.value", value)
    return f"{node}.value"


def _create_string_plug(maya_cmds, value):
    node = maya_cmds.createNode("network")
    maya_cmds.addAttr(node, longName="value", dataType="string")
    maya_cmds.setAttr(f"{node}.value", value, type="string")
    return f"{node}.value"


def test_class_attributes_and_operation_enum(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.attr.define.std.at.typed import (
        TypedAttrOperator,
    )
    from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl import (
        BdAnyConditionDbl,
    )
    from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_l import (
        BdAnyConditionDblL,
    )
    from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_l_multi import (
        BdAnyConditionDblLMulti,
    )
    from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_multi import (
        BdAnyConditionDblMulti,
    )

    assert BdAnyConditionDbl.NODE_TYPE == "bdAny_ConditionDbl"
    assert BdAnyConditionDbl.input.long_name == "input"
    assert BdAnyConditionDbl.op.short_name == "op"
    assert BdAnyConditionDbl.cmp.short_name == "cmp"
    assert BdAnyConditionDbl.extra.long_name == "extra"
    assert BdAnyConditionDbl.ex.short_name == "ex"
    assert BdAnyConditionDbl.extra.logic.short_name == "lgc"
    assert BdAnyConditionDbl.extra.comparison.short_name == "cpr"
    assert BdAnyConditionDbl.extra.compareValue.short_name == "cv"
    assert BdAnyConditionDbl.extra.logic.AND == 0
    assert BdAnyConditionDbl.extra.logic.OR == 1
    assert BdAnyConditionDbl.extra.comparison.GREATER_THAN == 2
    assert BdAnyConditionDbl.tv.short_name == "tv"
    assert BdAnyConditionDbl.fv.short_name == "fv"
    assert isinstance(BdAnyConditionDbl.trueValue, TypedAttrOperator)
    assert isinstance(BdAnyConditionDbl.output, TypedAttrOperator)
    assert BdAnyConditionDbl.operation.GREATER_THAN == 2
    assert BdAnyConditionDbl.operation.name_by_index(3) == "Greater or Equal"

    assert BdAnyConditionDblL.NODE_TYPE == "bdAny_ConditionDblL"
    assert BdAnyConditionDblL.input.ATTR_TYPE == "doubleLinear"
    assert BdAnyConditionDblL.compare.ATTR_TYPE == "doubleLinear"
    assert BdAnyConditionDblL.extra.compareValue.ATTR_TYPE == "doubleLinear"

    assert BdAnyConditionDblMulti.NODE_TYPE == "bdAny_ConditionDblMulti"
    assert BdAnyConditionDblMulti.case.long_name == "case"
    assert BdAnyConditionDblMulti.cs.short_name == "cs"
    assert BdAnyConditionDblMulti.case.operation.long_name == "operation"
    assert BdAnyConditionDblMulti.case.compare.short_name == "cmp"
    assert BdAnyConditionDblMulti.case.extra.long_name == "extra"
    assert BdAnyConditionDblMulti.case.extra.logic.short_name == "lgc"
    assert BdAnyConditionDblMulti.case.extra.comparison.short_name == "cpr"
    assert BdAnyConditionDblMulti.case.extra.compareValue.short_name == "cv"
    assert BdAnyConditionDblMulti.case.value.short_name == "v"
    assert BdAnyConditionDblMulti.elseValue.short_name == "ev"

    assert BdAnyConditionDblLMulti.NODE_TYPE == "bdAny_ConditionDblLMulti"
    assert BdAnyConditionDblLMulti.case.compare.ATTR_TYPE == "doubleLinear"
    assert (
        BdAnyConditionDblLMulti.case.extra.compareValue.ATTR_TYPE
        == "doubleLinear"
    )
    assert isinstance(BdAnyConditionDblLMulti.case.value, TypedAttrOperator)


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_type_ids_attribute_types_and_removed_nodes(
    maya_cmds,
    maya_om,
    node_type,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_object = selection.getDependNode(0)
    assert (
        maya_om.MFnDependencyNode(node_object).typeId.id()
        == NODE_TYPE_IDS[node_type]
    )

    comparison_type = (
        "doubleLinear" if "ConditionDblL" in node_type else "double"
    )
    assert maya_cmds.getAttr(f"{node}.input", type=True) == comparison_type
    compare_plug = (
        f"{node}.case[2].compare"
        if node_type.endswith("Multi")
        else f"{node}.compare"
    )
    assert maya_cmds.getAttr(compare_plug, type=True) == comparison_type

    extra_plug = (
        f"{node}.case[2].extra[3]"
        if node_type.endswith("Multi")
        else f"{node}.extra[3]"
    )
    assert maya_cmds.getAttr(f"{extra_plug}.logic", type=True) == "enum"
    assert maya_cmds.getAttr(f"{extra_plug}.comparison", type=True) == "enum"
    assert (
        maya_cmds.getAttr(f"{extra_plug}.compareValue", type=True)
        == comparison_type
    )

    typed_plugs = (
        ("case[2].value", "elseValue", "output")
        if node_type.endswith("Multi")
        else ("trueValue", "falseValue", "output")
    )
    for attribute_name in typed_plugs:
        selection = maya_om.MSelectionList()
        selection.add(f"{node}.{attribute_name}")
        plug = selection.getPlug(0)
        attribute = plug.attribute()
        assert attribute.apiType() == maya_om.MFn.kTypedAttribute
        assert (
            maya_om.MFnTypedAttribute(attribute).attrType()
            == maya_om.MFnData.kAny
        )

    assert not REMOVED_NODE_TYPES.intersection(maya_cmds.allNodeTypes())


@pytest.mark.parametrize(
    "node_type",
    ("bdAny_ConditionDbl", "bdAny_ConditionDblL"),
)
@pytest.mark.parametrize(
    ("operation", "input_value", "compare_value", "false_input"),
    OPERATIONS,
)
def test_single_supports_all_comparison_operations(
    maya_cmds,
    node_type,
    operation,
    input_value,
    compare_value,
    false_input,
):
    _load_bd_util_nodes(maya_cmds)

    true_value = _create_numeric_plug(maya_cmds, 12.0)
    false_value = _create_numeric_plug(maya_cmds, -4.0)
    output = _create_numeric_plug(maya_cmds, 0.0)
    node = maya_cmds.createNode(node_type)
    maya_cmds.connectAttr(true_value, f"{node}.trueValue")
    maya_cmds.connectAttr(false_value, f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", input_value)
    maya_cmds.setAttr(f"{node}.operation", operation)
    maya_cmds.setAttr(f"{node}.compare", compare_value)

    assert maya_cmds.getAttr(output) == pytest.approx(12.0)
    maya_cmds.setAttr(f"{node}.input", false_input)
    assert maya_cmds.getAttr(output) == pytest.approx(-4.0)


@pytest.mark.parametrize(
    "node_type",
    ("bdAny_ConditionDbl", "bdAny_ConditionDblL"),
)
def test_single_extra_folds_by_logical_index_and_preserves_empty_behavior(
    maya_cmds,
    node_type,
):
    _load_bd_util_nodes(maya_cmds)

    true_value = _create_numeric_plug(maya_cmds, 1.0)
    false_value = _create_numeric_plug(maya_cmds, -1.0)
    output = _create_numeric_plug(maya_cmds, 0.0)
    node = maya_cmds.createNode(node_type)
    maya_cmds.connectAttr(true_value, f"{node}.trueValue")
    maya_cmds.connectAttr(false_value, f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", output)

    maya_cmds.setAttr(f"{node}.input", 5.0)
    maya_cmds.setAttr(f"{node}.operation", 4)
    maya_cmds.setAttr(f"{node}.compare", 4.0)
    assert maya_cmds.getAttr(output) == pytest.approx(-1.0)

    # Create physical index 10 first. Logical order evaluates index 2 first:
    # (False AND False) OR True -> True.
    maya_cmds.setAttr(f"{node}.extra[10].logic", 1)
    maya_cmds.setAttr(f"{node}.extra[10].comparison", 2)
    maya_cmds.setAttr(f"{node}.extra[10].compareValue", 0.0)
    maya_cmds.setAttr(f"{node}.extra[2].logic", 0)
    maya_cmds.setAttr(f"{node}.extra[2].comparison", 2)
    maya_cmds.setAttr(f"{node}.extra[2].compareValue", 10.0)
    assert maya_cmds.getAttr(output) == pytest.approx(1.0)

    maya_cmds.setAttr(f"{node}.extra[10].logic", 0)
    assert maya_cmds.getAttr(output) == pytest.approx(-1.0)

    maya_cmds.removeMultiInstance(f"{node}.extra[2]", b=True)
    maya_cmds.removeMultiInstance(f"{node}.extra[10]", b=True)
    assert maya_cmds.getAttr(output) == pytest.approx(-1.0)


def test_single_preserves_double3_payload(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    true_value = maya_cmds.createNode("transform")
    false_value = maya_cmds.createNode("transform")
    output = maya_cmds.createNode("transform")
    maya_cmds.setAttr(f"{true_value}.translate", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(
        f"{false_value}.translate", -1.0, -2.0, -3.0, type="double3"
    )

    node = maya_cmds.createNode("bdAny_ConditionDbl")
    maya_cmds.connectAttr(f"{true_value}.translate", f"{node}.trueValue")
    maya_cmds.connectAttr(f"{false_value}.translate", f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", f"{output}.translate")
    maya_cmds.setAttr(f"{node}.input", 5.0)
    maya_cmds.setAttr(f"{node}.operation", 2)
    maya_cmds.setAttr(f"{node}.compare", 3.0)

    assert maya_cmds.getAttr(f"{output}.translate")[0] == pytest.approx(
        (1.0, 2.0, 3.0)
    )
    maya_cmds.setAttr(f"{node}.input", 2.0)
    assert maya_cmds.getAttr(f"{output}.translate")[0] == pytest.approx(
        (-1.0, -2.0, -3.0)
    )


def test_linear_comparison_preserves_angle_payload(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    true_value = _create_numeric_plug(maya_cmds, 30.0, "doubleAngle")
    false_value = _create_numeric_plug(maya_cmds, 60.0, "doubleAngle")
    output = _create_numeric_plug(maya_cmds, 0.0, "doubleAngle")
    node = maya_cmds.createNode("bdAny_ConditionDblL")
    maya_cmds.connectAttr(true_value, f"{node}.trueValue")
    maya_cmds.connectAttr(false_value, f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", 3.0)
    maya_cmds.setAttr(f"{node}.operation", 2)
    maya_cmds.setAttr(f"{node}.compare", 2.0)

    assert maya_cmds.getAttr(output) == pytest.approx(30.0)


def test_single_preserves_matrix_payload(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    true_value = maya_cmds.createNode("composeMatrix")
    false_value = maya_cmds.createNode("composeMatrix")
    output = maya_cmds.createNode("decomposeMatrix")
    maya_cmds.setAttr(
        f"{true_value}.inputTranslate", 1.0, 2.0, 3.0, type="double3"
    )
    maya_cmds.setAttr(
        f"{false_value}.inputTranslate", -1.0, -2.0, -3.0, type="double3"
    )

    node = maya_cmds.createNode("bdAny_ConditionDbl")
    maya_cmds.connectAttr(f"{true_value}.outputMatrix", f"{node}.trueValue")
    maya_cmds.connectAttr(f"{false_value}.outputMatrix", f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", f"{output}.inputMatrix")
    maya_cmds.setAttr(f"{node}.input", 5.0)
    maya_cmds.setAttr(f"{node}.operation", 2)
    maya_cmds.setAttr(f"{node}.compare", 3.0)

    assert maya_cmds.getAttr(f"{output}.outputTranslate")[0] == pytest.approx(
        (1.0, 2.0, 3.0)
    )


@pytest.mark.parametrize(
    "node_type",
    ("bdAny_ConditionDblMulti", "bdAny_ConditionDblLMulti"),
)
def test_multi_uses_logical_index_order_and_else_value(maya_cmds, node_type):
    _load_bd_util_nodes(maya_cmds)

    case2 = _create_numeric_plug(maya_cmds, 2.0)
    case10 = _create_numeric_plug(maya_cmds, 10.0)
    else_value = _create_numeric_plug(maya_cmds, -1.0)
    output = _create_numeric_plug(maya_cmds, 0.0)
    node = maya_cmds.createNode(node_type)
    maya_cmds.connectAttr(case2, f"{node}.case[2].value")
    maya_cmds.connectAttr(case10, f"{node}.case[10].value")
    maya_cmds.connectAttr(else_value, f"{node}.elseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", 5.0)
    for index in (10, 2):
        maya_cmds.setAttr(f"{node}.case[{index}].operation", 2)
        maya_cmds.setAttr(f"{node}.case[{index}].compare", 0.0)

    assert maya_cmds.getAttr(output) == pytest.approx(2.0)
    maya_cmds.removeMultiInstance(f"{node}.case[2]", b=True)
    assert maya_cmds.getAttr(output) == pytest.approx(10.0)
    maya_cmds.setAttr(f"{node}.input", -5.0)
    assert maya_cmds.getAttr(output) == pytest.approx(-1.0)


@pytest.mark.parametrize(
    "node_type",
    ("bdAny_ConditionDblMulti", "bdAny_ConditionDblLMulti"),
)
def test_multi_extra_is_evaluated_per_case_in_logical_index_order(
    maya_cmds,
    node_type,
):
    _load_bd_util_nodes(maya_cmds)

    case2 = _create_numeric_plug(maya_cmds, 2.0)
    case10 = _create_numeric_plug(maya_cmds, 10.0)
    else_value = _create_numeric_plug(maya_cmds, -1.0)
    output = _create_numeric_plug(maya_cmds, 0.0)
    node = maya_cmds.createNode(node_type)
    maya_cmds.connectAttr(case2, f"{node}.case[2].value")
    maya_cmds.connectAttr(case10, f"{node}.case[10].value")
    maya_cmds.connectAttr(else_value, f"{node}.elseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", 5.0)

    maya_cmds.setAttr(f"{node}.case[2].operation", 4)
    maya_cmds.setAttr(f"{node}.case[2].compare", 4.0)
    maya_cmds.setAttr(f"{node}.case[2].extra[10].logic", 1)
    maya_cmds.setAttr(f"{node}.case[2].extra[10].comparison", 2)
    maya_cmds.setAttr(f"{node}.case[2].extra[10].compareValue", 0.0)
    maya_cmds.setAttr(f"{node}.case[2].extra[3].logic", 0)
    maya_cmds.setAttr(f"{node}.case[2].extra[3].comparison", 2)
    maya_cmds.setAttr(f"{node}.case[2].extra[3].compareValue", 10.0)

    maya_cmds.setAttr(f"{node}.case[10].operation", 2)
    maya_cmds.setAttr(f"{node}.case[10].compare", 0.0)
    assert maya_cmds.getAttr(output) == pytest.approx(2.0)

    maya_cmds.setAttr(f"{node}.case[2].extra[10].logic", 0)
    assert maya_cmds.getAttr(output) == pytest.approx(10.0)

    maya_cmds.setAttr(f"{node}.case[10].extra[1].logic", 0)
    maya_cmds.setAttr(f"{node}.case[10].extra[1].comparison", 2)
    maya_cmds.setAttr(f"{node}.case[10].extra[1].compareValue", 10.0)
    assert maya_cmds.getAttr(output) == pytest.approx(-1.0)


def test_multi_preserves_string_payload(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    case_value = _create_string_plug(maya_cmds, "matched")
    else_value = _create_string_plug(maya_cmds, "else")
    output = _create_string_plug(maya_cmds, "")
    node = maya_cmds.createNode("bdAny_ConditionDblLMulti")
    maya_cmds.connectAttr(case_value, f"{node}.case[3].value")
    maya_cmds.connectAttr(else_value, f"{node}.elseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", 5.0)
    maya_cmds.setAttr(f"{node}.case[3].operation", 2)
    maya_cmds.setAttr(f"{node}.case[3].compare", 2.0)

    assert maya_cmds.getAttr(output) == "matched"
    maya_cmds.setAttr(f"{node}.input", 1.0)
    assert maya_cmds.getAttr(output) == "else"


@pytest.mark.parametrize(
    ("operation", "expected"),
    ((0, -1.0), (1, 1.0), (2, -1.0), (3, -1.0), (4, -1.0), (5, -1.0)),
)
def test_nan_uses_ieee_comparison_semantics(maya_cmds, operation, expected):
    _load_bd_util_nodes(maya_cmds)

    true_value = _create_numeric_plug(maya_cmds, 1.0)
    false_value = _create_numeric_plug(maya_cmds, -1.0)
    output = _create_numeric_plug(maya_cmds, 0.0)
    node = maya_cmds.createNode("bdAny_ConditionDbl")
    maya_cmds.connectAttr(true_value, f"{node}.trueValue")
    maya_cmds.connectAttr(false_value, f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", float("nan"))
    maya_cmds.setAttr(f"{node}.operation", operation)
    maya_cmds.setAttr(f"{node}.compare", 0.0)

    assert maya_cmds.getAttr(output) == pytest.approx(expected)


def test_infinity_uses_normal_ordering(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    true_value = _create_numeric_plug(maya_cmds, 1.0)
    false_value = _create_numeric_plug(maya_cmds, -1.0)
    output = _create_numeric_plug(maya_cmds, 0.0)
    node = maya_cmds.createNode("bdAny_ConditionDbl")
    maya_cmds.connectAttr(true_value, f"{node}.trueValue")
    maya_cmds.connectAttr(false_value, f"{node}.falseValue")
    maya_cmds.connectAttr(f"{node}.output", output)
    maya_cmds.setAttr(f"{node}.input", math.inf)
    maya_cmds.setAttr(f"{node}.operation", 2)
    maya_cmds.setAttr(f"{node}.compare", 1.0)

    assert maya_cmds.getAttr(output) == pytest.approx(1.0)


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_nested_case_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        case_value = maya_cmds.createNode("transform")
        else_value = maya_cmds.createNode("transform")
        output = maya_cmds.createNode("transform")
        maya_cmds.setAttr(
            f"{case_value}.translate", 1.0, 2.0, 3.0, type="double3"
        )
        maya_cmds.setAttr(
            f"{else_value}.translate", -1.0, -2.0, -3.0, type="double3"
        )

        node = maya_cmds.createNode("bdAny_ConditionDblLMulti")
        maya_cmds.connectAttr(
            f"{case_value}.translate", f"{node}.case[3].value"
        )
        maya_cmds.connectAttr(f"{else_value}.translate", f"{node}.elseValue")
        maya_cmds.connectAttr(f"{node}.output", f"{output}.translate")
        maya_cmds.setAttr(f"{node}.input", 5.0)
        maya_cmds.setAttr(f"{node}.case[3].operation", 2)
        maya_cmds.setAttr(f"{node}.case[3].compare", 3.0)
        maya_cmds.setAttr(f"{node}.case[3].extra[7].logic", 0)
        maya_cmds.setAttr(f"{node}.case[3].extra[7].comparison", 4)
        maya_cmds.setAttr(f"{node}.case[3].extra[7].compareValue", 10.0)
        assert maya_cmds.getAttr(f"{output}.translate")[0] == pytest.approx(
            (1.0, 2.0, 3.0)
        )

        maya_cmds.setAttr(f"{case_value}.translateY", 8.0)
        assert maya_cmds.getAttr(f"{output}.translate")[0] == pytest.approx(
            (1.0, 8.0, 3.0)
        )

        maya_cmds.setAttr(f"{node}.case[3].extra[7].compareValue", 4.0)
        assert maya_cmds.getAttr(f"{output}.translate")[0] == pytest.approx(
            (-1.0, -2.0, -3.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_connections_accessors_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl import (
        BdAnyConditionDbl,
    )
    from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_multi import (
        BdAnyConditionDblMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    true_value = nodes.create.bdDbl_Value(name="true_value")
    false_value = nodes.create.bdDbl_Value(name="false_value")
    case_value = nodes.create.bdDbl_Value(name="case_value")
    else_value = nodes.create.bdDbl_Value(name="else_value")
    result = nodes.create.bdDbl_Value(name="result")
    first = nodes.create.bdAny_ConditionDbl(name="first")
    multi = nodes.create.bdAny_ConditionDblMulti(name="multi")

    true_value.value.set(5.0)
    false_value.value.set(-5.0)
    case_value.value.set(10.0)
    else_value.value.set(-10.0)
    first.input.set(2.0)
    first.operation.set(first.operation.GREATER_THAN)
    first.compare.set(1.0)
    first.extra[3].logic.set(first.extra[3].logic.AND)
    first.extra[3].comparison.set(first.extra[3].comparison.LESS_THAN)
    first.extra[3].compareValue.set(3.0)
    true_value.value.connect(first.trueValue)
    false_value.value.connect(first.falseValue)
    first.output.connect(multi.input)
    multi.case[0].operation.set(multi.case[0].operation.GREATER_THAN)
    multi.case[0].compare.set(3.0)
    multi.case[0].extra[2].logic.set(multi.case[0].extra[2].logic.AND)
    multi.case[0].extra[2].comparison.set(
        multi.case[0].extra[2].comparison.LESS_THAN
    )
    multi.case[0].extra[2].compareValue.set(6.0)
    case_value.value.connect(multi.case[0].value)
    else_value.value.connect(multi.elseValue)
    multi.output.connect(result.value)
    modifier_manager.do_it_dg()

    assert result.value.get() == pytest.approx(10.0)
    assert isinstance(
        nodes.existing.bdAny_ConditionDbl(first.name),
        BdAnyConditionDbl,
    )
    assert isinstance(
        nodes.existing.bdAny_ConditionDblMulti(multi.name),
        BdAnyConditionDblMulti,
    )

    scene_path = tmp_path / "bd_any_condition.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDbl_Value(
        "result"
    ).value.get() == pytest.approx(10.0)
