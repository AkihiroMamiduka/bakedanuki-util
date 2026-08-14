# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


NODE_TYPE_IDS = {
    "bdConditionDblExtra_Compose": 0x001426DA,
    "bdConditionDblLExtra_Compose": 0x001426DB,
    "bdConditionDblCase_Compose": 0x001426DC,
    "bdConditionDblLCase_Compose": 0x001426DD,
    "bdConditionDblAExtra_Compose": 0x00142705,
    "bdConditionDblACase_Compose": 0x00142706,
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


def _assert_typed_any(maya_om, plug_name):
    selection = maya_om.MSelectionList()
    selection.add(plug_name)
    attribute = selection.getPlug(0).attribute()
    assert attribute.apiType() == maya_om.MFn.kTypedAttribute
    assert (
        maya_om.MFnTypedAttribute(attribute).attrType() == maya_om.MFnData.kAny
    )


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_type_ids_and_public_attribute_structure(
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
        "doubleLinear"
        if "DblL" in node_type
        else "doubleAngle" if "DblA" in node_type else "double"
    )
    assert maya_cmds.getAttr(f"{node}.output", type=True) == "TdataCompound"
    assert not maya_cmds.attributeQuery("output", node=node, writable=True)

    if "Extra" in node_type:
        assert maya_cmds.getAttr(f"{node}.logic", type=True) == "enum"
        assert maya_cmds.getAttr(f"{node}.comparison", type=True) == "enum"
        assert (
            maya_cmds.getAttr(f"{node}.compareValue", type=True)
            == comparison_type
        )
        assert maya_cmds.attributeQuery(
            "output",
            node=node,
            listChildren=True,
        ) == [
            "outputLogic",
            "outputComparison",
            "outputCompareValue",
        ]
        assert (
            maya_cmds.getAttr(f"{node}.outputCompareValue", type=True)
            == comparison_type
        )
        return

    assert maya_cmds.getAttr(f"{node}.operation", type=True) == "enum"
    assert maya_cmds.getAttr(f"{node}.compare", type=True) == comparison_type
    assert maya_cmds.attributeQuery("extra", node=node, multi=True)
    assert (
        maya_cmds.getAttr(f"{node}.extra[3].compareValue", type=True)
        == comparison_type
    )
    assert maya_cmds.attributeQuery(
        "output",
        node=node,
        listChildren=True,
    ) == [
        "outputOperation",
        "outputCompare",
        "outputExtra",
        "outputValue",
    ]
    assert maya_cmds.attributeQuery("outputExtra", node=node, multi=True)
    assert (
        maya_cmds.getAttr(
            f"{node}.output.outputExtra[3].outputCompareValue",
            type=True,
        )
        == comparison_type
    )
    _assert_typed_any(maya_om, f"{node}.value")
    _assert_typed_any(maya_om, f"{node}.outputValue")


@pytest.mark.parametrize(
    ("compose_type", "condition_type"),
    (
        ("bdConditionDblExtra_Compose", "bdAny_ConditionDbl"),
        ("bdConditionDblLExtra_Compose", "bdAny_ConditionDblL"),
        ("bdConditionDblAExtra_Compose", "bdAny_ConditionDblA"),
    ),
)
def test_extra_compose_connects_one_output_to_one_extra_element(
    maya_cmds,
    compose_type,
    condition_type,
):
    _load_bd_util_nodes(maya_cmds)

    true_value = _create_numeric_plug(maya_cmds, 1.0)
    false_value = _create_numeric_plug(maya_cmds, -1.0)
    result = _create_numeric_plug(maya_cmds, 0.0)
    compose = maya_cmds.createNode(compose_type)
    condition = maya_cmds.createNode(condition_type)

    maya_cmds.setAttr(f"{condition}.input", 5.0)
    maya_cmds.setAttr(f"{condition}.operation", 4)
    maya_cmds.setAttr(f"{condition}.compare", 4.0)
    maya_cmds.setAttr(f"{compose}.logic", 1)
    maya_cmds.setAttr(f"{compose}.comparison", 2)
    maya_cmds.setAttr(f"{compose}.compareValue", 0.0)
    maya_cmds.connectAttr(true_value, f"{condition}.trueValue")
    maya_cmds.connectAttr(false_value, f"{condition}.falseValue")
    maya_cmds.connectAttr(f"{compose}.output", f"{condition}.extra[7]")
    maya_cmds.connectAttr(f"{condition}.output", result)

    assert maya_cmds.getAttr(result) == pytest.approx(1.0)
    maya_cmds.setAttr(f"{compose}.logic", 0)
    assert maya_cmds.getAttr(result) == pytest.approx(-1.0)


@pytest.mark.parametrize(
    ("extra_type", "case_type", "condition_type"),
    (
        (
            "bdConditionDblExtra_Compose",
            "bdConditionDblCase_Compose",
            "bdAny_ConditionDblMulti",
        ),
        (
            "bdConditionDblLExtra_Compose",
            "bdConditionDblLCase_Compose",
            "bdAny_ConditionDblLMulti",
        ),
        (
            "bdConditionDblAExtra_Compose",
            "bdConditionDblACase_Compose",
            "bdAny_ConditionDblAMulti",
        ),
    ),
)
def test_case_compose_copies_sparse_extras_and_typed_any_value(
    maya_cmds,
    extra_type,
    case_type,
    condition_type,
):
    _load_bd_util_nodes(maya_cmds)

    extra2 = maya_cmds.createNode(extra_type)
    extra10 = maya_cmds.createNode(extra_type)
    case = maya_cmds.createNode(case_type)
    condition = maya_cmds.createNode(condition_type)
    case_value = _create_numeric_plug(maya_cmds, 42.0)
    else_value = _create_numeric_plug(maya_cmds, -42.0)
    result = _create_numeric_plug(maya_cmds, 0.0)

    maya_cmds.setAttr(f"{condition}.input", 5.0)
    maya_cmds.setAttr(f"{case}.operation", 4)
    maya_cmds.setAttr(f"{case}.compare", 4.0)

    maya_cmds.setAttr(f"{extra10}.logic", 1)
    maya_cmds.setAttr(f"{extra10}.comparison", 2)
    maya_cmds.setAttr(f"{extra10}.compareValue", 0.0)
    maya_cmds.setAttr(f"{extra2}.logic", 0)
    maya_cmds.setAttr(f"{extra2}.comparison", 2)
    maya_cmds.setAttr(f"{extra2}.compareValue", 10.0)

    maya_cmds.connectAttr(f"{extra10}.output", f"{case}.extra[10]")
    maya_cmds.connectAttr(f"{extra2}.output", f"{case}.extra[2]")
    maya_cmds.connectAttr(case_value, f"{case}.value")
    maya_cmds.connectAttr(f"{case}.output", f"{condition}.case[5]")
    maya_cmds.connectAttr(else_value, f"{condition}.elseValue")
    maya_cmds.connectAttr(f"{condition}.output", result)

    assert maya_cmds.getAttr(result) == pytest.approx(42.0)
    assert maya_cmds.getAttr(
        f"{condition}.case[5].extra[2].compareValue"
    ) == pytest.approx(10.0)
    assert maya_cmds.getAttr(
        f"{condition}.case[5].extra[10].compareValue"
    ) == pytest.approx(0.0)

    maya_cmds.setAttr(f"{extra10}.logic", 0)
    assert maya_cmds.getAttr(result) == pytest.approx(-42.0)
    maya_cmds.setAttr(f"{extra10}.logic", 1)
    maya_cmds.setAttr(case_value, 84.0)
    assert maya_cmds.getAttr(result) == pytest.approx(84.0)

    maya_cmds.disconnectAttr(f"{extra2}.output", f"{case}.extra[2]")
    maya_cmds.removeMultiInstance(f"{case}.extra[2]", b=True)
    assert maya_cmds.getAttr(
        f"{condition}.case[5].extra",
        multiIndices=True,
    ) == [10]
    maya_cmds.disconnectAttr(f"{extra10}.output", f"{case}.extra[10]")
    maya_cmds.removeMultiInstance(f"{case}.extra[10]", b=True)
    assert (
        maya_cmds.getAttr(
            f"{condition}.case[5].extra",
            multiIndices=True,
        )
        is None
    )


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_case_compose_preserves_double3_and_dirties_in_all_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        extra = maya_cmds.createNode("bdConditionDblLExtra_Compose")
        case = maya_cmds.createNode("bdConditionDblLCase_Compose")
        condition = maya_cmds.createNode("bdAny_ConditionDblLMulti")
        case_value = maya_cmds.createNode("transform")
        else_value = maya_cmds.createNode("transform")
        result = maya_cmds.createNode("transform")

        maya_cmds.setAttr(
            f"{case_value}.translate",
            1.0,
            2.0,
            3.0,
            type="double3",
        )
        maya_cmds.setAttr(
            f"{else_value}.translate",
            -1.0,
            -2.0,
            -3.0,
            type="double3",
        )
        maya_cmds.setAttr(f"{condition}.input", 5.0)
        maya_cmds.setAttr(f"{case}.operation", 2)
        maya_cmds.setAttr(f"{case}.compare", 3.0)
        maya_cmds.setAttr(f"{extra}.logic", 0)
        maya_cmds.setAttr(f"{extra}.comparison", 4)
        maya_cmds.setAttr(f"{extra}.compareValue", 10.0)

        maya_cmds.connectAttr(f"{extra}.output", f"{case}.extra[3]")
        maya_cmds.connectAttr(f"{case_value}.translate", f"{case}.value")
        maya_cmds.connectAttr(f"{case}.output", f"{condition}.case[2]")
        maya_cmds.connectAttr(
            f"{else_value}.translate",
            f"{condition}.elseValue",
        )
        maya_cmds.connectAttr(f"{condition}.output", f"{result}.translate")

        assert maya_cmds.getAttr(f"{result}.translate")[0] == pytest.approx(
            (1.0, 2.0, 3.0)
        )
        maya_cmds.setAttr(f"{case_value}.translateY", 8.0)
        assert maya_cmds.getAttr(f"{result}.translate")[0] == pytest.approx(
            (1.0, 8.0, 3.0)
        )
        maya_cmds.setAttr(f"{extra}.compareValue", 4.0)
        assert maya_cmds.getAttr(f"{result}.translate")[0] == pytest.approx(
            (-1.0, -2.0, -3.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_connections_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_condition_dbl_case_compose import (
        BdConditionDblCaseCompose,
    )
    from bd_util.maya.node.operator.node.dg.bd_condition_dbl_extra_compose import (
        BdConditionDblExtraCompose,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    extra = nodes.create.bdConditionDblExtra_Compose(name="extra")
    case = nodes.create.bdConditionDblCase_Compose(name="case_compose")
    condition = nodes.create.bdAny_ConditionDblMulti(name="condition")
    case_value = nodes.create.bdDbl_Value(name="case_value")
    else_value = nodes.create.bdDbl_Value(name="else_value")
    result = nodes.create.bdDbl_Value(name="result")

    extra.logic.set(extra.logic.AND)
    extra.comparison.set(extra.comparison.LESS_THAN)
    extra.compareValue.set(10.0)
    case.operation.set(case.operation.GREATER_THAN)
    case.compare.set(3.0)
    condition.input.set(5.0)
    case_value.value.set(12.0)
    else_value.value.set(-12.0)
    extra.output.connect(case.extra[3])
    case_value.value.connect(case.value)
    case.output.connect(condition.case[2])
    else_value.value.connect(condition.elseValue)
    condition.output.connect(result.value)
    modifier_manager.do_it_dg()

    assert result.value.get() == pytest.approx(12.0)
    assert isinstance(
        nodes.existing.bdConditionDblExtra_Compose(extra.name),
        BdConditionDblExtraCompose,
    )
    assert isinstance(
        nodes.existing.bdConditionDblCase_Compose(case.name),
        BdConditionDblCaseCompose,
    )

    scene_path = tmp_path / "bd_condition_compose.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDbl_Value(
        "result"
    ).value.get() == pytest.approx(12.0)


def test_angle_condition_node_operator_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    node_types = (
        "bdAny_ConditionDblA",
        "bdAny_ConditionDblAMulti",
        "bdConditionDblAExtra_Compose",
        "bdConditionDblACase_Compose",
    )
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    created = [
        getattr(nodes.create, node_type)(name=f"angle_condition_{index}")
        for index, node_type in enumerate(node_types)
    ]
    modifier_manager.do_it_dg()

    for node_type, node in zip(node_types, created):
        assert node.NODE_TYPE == node_type
        existing = getattr(nodes.existing, node_type)(node.name)
        assert existing.NODE_TYPE == node_type
