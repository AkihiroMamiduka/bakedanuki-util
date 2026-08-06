# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


NODE_TYPE_IDS = {
    "bdDblA_Value": 0x0007F06A,
    "bdDblA_Add": 0x0007F06B,
    "bdDblA_AddMulti": 0x0007F06C,
    "bdDblA_Subtract": 0x0007F06D,
    "bdDblA_SubtractMulti": 0x0007F06E,
    "bdDblA_Negate": 0x0007F06F,
    "bdDblA_Abs": 0x0007F070,
    "bdDblA_Multiply": 0x0007F071,
    "bdDblA_MultiplyMulti": 0x0007F072,
    "bdDblA_Divide": 0x0007F073,
    "bdDblA_DivideMulti": 0x0007F074,
    "bdDblA_Clamp": 0x0007F075,
    "bdDblA_MapRange": 0x0007F076,
    "bdDblA_Lerp": 0x0007F077,
    "bdDblA_Min": 0x0007F078,
    "bdDblA_MinMulti": 0x0007F079,
    "bdDblA_Max": 0x0007F07A,
    "bdDblA_MaxMulti": 0x0007F07B,
}

ANGLE_ATTRIBUTES = {
    "bdDblA_Value": ("value",),
    "bdDblA_Add": ("input1", "input2", "output"),
    "bdDblA_AddMulti": ("input", "output"),
    "bdDblA_Subtract": ("input1", "input2", "output"),
    "bdDblA_SubtractMulti": ("input", "output"),
    "bdDblA_Negate": ("input", "output"),
    "bdDblA_Abs": ("input", "output"),
    "bdDblA_Multiply": ("input", "output"),
    "bdDblA_MultiplyMulti": ("input", "output"),
    "bdDblA_Divide": ("input", "output"),
    "bdDblA_DivideMulti": ("input", "output"),
    "bdDblA_Clamp": ("input", "min", "max", "output"),
    "bdDblA_MapRange": (
        "input",
        "srcMin",
        "srcMax",
        "dstMin",
        "dstMax",
        "output",
    ),
    "bdDblA_Lerp": ("input1", "input2", "output"),
    "bdDblA_Min": ("input1", "input2", "output"),
    "bdDblA_MinMulti": ("input", "output"),
    "bdDblA_Max": ("input1", "input2", "output"),
    "bdDblA_MaxMulti": ("input", "output"),
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


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_node_ids_and_attribute_types(maya_cmds, maya_om, node_type):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == NODE_TYPE_IDS[node_type]
    for attribute in ANGLE_ATTRIBUTES[node_type]:
        if attribute == "input" and node_type in {
            "bdDblA_AddMulti",
            "bdDblA_SubtractMulti",
            "bdDblA_MinMulti",
            "bdDblA_MaxMulti",
        }:
            attribute = "input[0]"
        assert maya_cmds.getAttr(f"{node}.{attribute}", type=True) == (
            "doubleAngle"
        )

    if "Multiply" in node_type or "Divide" in node_type:
        factor = "factor[0]" if node_type.endswith("Multi") else "factor"
        assert maya_cmds.getAttr(f"{node}.{factor}", type=True) == "double"
    if node_type == "bdDblA_Lerp":
        assert maya_cmds.getAttr(f"{node}.weight", type=True) == "double"
    if node_type == "bdDblA_MapRange":
        assert maya_cmds.getAttr(f"{node}.clamp", type=True) == "bool"


@pytest.mark.parametrize(
    ("node_type", "attribute"),
    (
        ("bdDblA_Clamp", "max"),
        ("bdDblA_MapRange", "srcMax"),
        ("bdDblA_MapRange", "dstMax"),
    ),
)
def test_angle_range_maximum_defaults_to_full_rotation(
    maya_cmds,
    node_type,
    attribute,
):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="deg")
        node = maya_cmds.createNode(node_type)

        assert maya_cmds.getAttr(f"{node}.{attribute}") == pytest.approx(360.0)
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


@pytest.mark.parametrize(
    ("node_type", "values", "expected"),
    (
        ("bdDblA_Value", {"value": 725.0}, 725.0),
        (
            "bdDblA_Add",
            {"input1": 350.0, "input2": 20.0},
            370.0,
        ),
        (
            "bdDblA_Subtract",
            {"input1": 10.0, "input2": 350.0},
            -340.0,
        ),
        ("bdDblA_Negate", {"input": -450.0}, 450.0),
        ("bdDblA_Abs", {"input": -450.0}, 450.0),
        (
            "bdDblA_Multiply",
            {"input": 90.0, "factor": 2.5},
            225.0,
        ),
        (
            "bdDblA_Divide",
            {"input": 720.0, "factor": 2.0},
            360.0,
        ),
        (
            "bdDblA_Clamp",
            {"input": 450.0, "min": -90.0, "max": 360.0},
            360.0,
        ),
        (
            "bdDblA_MapRange",
            {
                "input": 45.0,
                "srcMin": -90.0,
                "srcMax": 90.0,
                "dstMin": 0.0,
                "dstMax": 360.0,
            },
            270.0,
        ),
        (
            "bdDblA_Lerp",
            {"input1": 350.0, "input2": 10.0, "weight": 0.5},
            180.0,
        ),
        (
            "bdDblA_Min",
            {"input1": -10.0, "input2": 350.0},
            -10.0,
        ),
        (
            "bdDblA_Max",
            {"input1": 370.0, "input2": 10.0},
            370.0,
        ),
    ),
)
def test_fixed_nodes_use_continuous_angle_arithmetic(
    maya_cmds,
    node_type,
    values,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="deg")
        node = maya_cmds.createNode(node_type)
        for attribute, value in values.items():
            maya_cmds.setAttr(f"{node}.{attribute}", value)

        output = "value" if node_type == "bdDblA_Value" else "output"
        assert maya_cmds.getAttr(f"{node}.{output}") == pytest.approx(expected)
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


def test_sparse_angle_multi_nodes(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="deg")

        add = maya_cmds.createNode("bdDblA_AddMulti")
        for index, value in ((20, 20.0), (2, 300.0), (9, 100.0)):
            maya_cmds.setAttr(f"{add}.input[{index}]", value)
        assert maya_cmds.getAttr(f"{add}.output") == pytest.approx(420.0)

        subtract = maya_cmds.createNode("bdDblA_SubtractMulti")
        for index, value in ((20, 10.0), (2, 720.0), (9, 30.0)):
            maya_cmds.setAttr(f"{subtract}.input[{index}]", value)
        assert maya_cmds.getAttr(f"{subtract}.output") == pytest.approx(680.0)

        multiply = maya_cmds.createNode("bdDblA_MultiplyMulti")
        maya_cmds.setAttr(f"{multiply}.input", 30.0)
        maya_cmds.setAttr(f"{multiply}.factor[9]", 2.0)
        maya_cmds.setAttr(f"{multiply}.factor[2]", 3.0)
        assert maya_cmds.getAttr(f"{multiply}.output") == pytest.approx(180.0)

        divide = maya_cmds.createNode("bdDblA_DivideMulti")
        maya_cmds.setAttr(f"{divide}.input", 360.0)
        maya_cmds.setAttr(f"{divide}.factor[9]", 3.0)
        maya_cmds.setAttr(f"{divide}.factor[2]", 2.0)
        assert maya_cmds.getAttr(f"{divide}.output") == pytest.approx(60.0)
        maya_cmds.removeMultiInstance(f"{divide}.factor[9]", b=True)
        maya_cmds.removeMultiInstance(f"{divide}.factor[2]", b=True)
        assert maya_cmds.getAttr(f"{divide}.output") == pytest.approx(360.0)
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


@pytest.mark.parametrize(
    ("node_type", "values", "expected"),
    (
        ("bdDblA_MinMulti", ((20, 725.0), (2, -10.0), (9, 370.0)), -10.0),
        ("bdDblA_MaxMulti", ((20, -450.0), (2, 10.0), (9, 370.0)), 370.0),
    ),
)
def test_min_max_multi_handles_sparse_single_and_empty_inputs(
    maya_cmds,
    node_type,
    values,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="deg")
        node = maya_cmds.createNode(node_type)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)

        for index, value in values:
            maya_cmds.setAttr(f"{node}.input[{index}]", value)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)

        for index, _ in values:
            maya_cmds.removeMultiInstance(f"{node}.input[{index}]", b=True)
        maya_cmds.setAttr(f"{node}.input[100]", -725.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(-725.0)

        maya_cmds.removeMultiInstance(f"{node}.input[100]", b=True)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


def test_angle_display_unit_does_not_change_internal_value(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="deg")
        node = maya_cmds.createNode("bdDblA_Add")
        maya_cmds.setAttr(f"{node}.input1", 180.0)
        maya_cmds.setAttr(f"{node}.input2", 90.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(270.0)

        selection = maya_om.MSelectionList()
        selection.add(f"{node}.output")
        output_plug = selection.getPlug(0)
        assert output_plug.asMAngle().asRadians() == pytest.approx(
            1.5 * math.pi
        )

        maya_cmds.currentUnit(angle="rad")
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(
            1.5 * math.pi
        )
        assert output_plug.asMAngle().asRadians() == pytest.approx(
            1.5 * math.pi
        )
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


def test_rotate_x_connects_without_unit_conversion(maya_cmds, new_scene):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="deg")
        source = maya_cmds.createNode("transform")
        target = maya_cmds.createNode("transform")
        node = maya_cmds.createNode("bdDblA_Add")
        maya_cmds.setAttr(f"{source}.rotateX", 350.0)
        maya_cmds.setAttr(f"{node}.input2", 20.0)
        maya_cmds.connectAttr(f"{source}.rotateX", f"{node}.input1")
        maya_cmds.connectAttr(f"{node}.output", f"{target}.rotateX")

        assert maya_cmds.getAttr(f"{target}.rotateX") == pytest.approx(370.0)
        assert not maya_cmds.ls(type="unitConversion")
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


def test_node_operator_creation_and_existing_accessor(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_a_add import BdDblAAdd
    from bd_util.maya.node.operator.node.dg.bd_dbl_a_min import BdDblAMin

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    add_node = nodes.create.bdDblA_Add(name="angle_add")
    add_node.input1.set(350.0)
    add_node.input2.set(20.0)
    min_node = nodes.create.bdDblA_Min(name="angle_min")
    min_node.input1.set(-10.0)
    min_node.input2.set(350.0)
    modifier_manager.do_it_dg()

    assert isinstance(add_node, BdDblAAdd)
    assert add_node.output.get() == pytest.approx(370.0)
    assert isinstance(nodes.existing.bdDblA_Add("angle_add"), BdDblAAdd)
    assert isinstance(min_node, BdDblAMin)
    assert min_node.output.get() == pytest.approx(-10.0)
    assert isinstance(nodes.existing.bdDblA_Min("angle_min"), BdDblAMin)


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_in_all_evaluation_modes(maya_cmds, evaluation_mode):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.currentUnit(angle="deg")
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDblA_Add")
        maya_cmds.setAttr(f"{node}.input1", 300.0)
        maya_cmds.setAttr(f"{node}.input2", 20.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(320.0)
        maya_cmds.setAttr(f"{node}.input2", 100.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(400.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)
        maya_cmds.currentUnit(angle=previous_unit)


def test_angle_node_survives_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblA_Subtract(name="angle_subtract")
    node.input1.set(10.0)
    node.input2.set(350.0)
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_double_angle.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDblA_Subtract(
        "angle_subtract"
    ).output.get() == pytest.approx(-340.0)
