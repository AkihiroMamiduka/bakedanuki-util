# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


NODE_TYPE_IDS = {
    "bdDblL_Value": 0x001426B4,
    "bdDblL3_Value": 0x001426B5,
    "bdDblL_Add": 0x001426B6,
    "bdDblL_AddMulti": 0x001426B7,
    "bdDblL3_Add": 0x001426B8,
    "bdDblL3_AddMulti": 0x001426B9,
    "bdDblL_Subtract": 0x001426BA,
    "bdDblL_SubtractMulti": 0x001426BB,
    "bdDblL3_Subtract": 0x001426BC,
    "bdDblL3_SubtractMulti": 0x001426BD,
    "bdDblL_Average": 0x001426BE,
    "bdDblL_AverageMulti": 0x001426BF,
    "bdDblL3_Average": 0x001426C0,
    "bdDblL3_AverageMulti": 0x001426C1,
    "bdDblL_Min": 0x001426C2,
    "bdDblL_MinMulti": 0x001426C3,
    "bdDblL3_Min": 0x001426C4,
    "bdDblL3_MinMulti": 0x001426C5,
    "bdDblL_Max": 0x001426C6,
    "bdDblL_MaxMulti": 0x001426C7,
    "bdDblL3_Max": 0x001426C8,
    "bdDblL3_MaxMulti": 0x001426C9,
    "bdDblL_Clamp": 0x001426CA,
    "bdDblL3_Clamp": 0x001426CB,
    "bdDblL_Abs": 0x001426CC,
    "bdDblL3_Abs": 0x001426CD,
    "bdDblL_Negate": 0x001426CE,
    "bdDblL3_Negate": 0x001426CF,
    "bdDblL_Lerp": 0x001426D0,
    "bdDblL3_Lerp": 0x001426D1,
    "bdDblL_MapRange": 0x001426D2,
    "bdDblL3_MapRange": 0x001426D3,
    "bdDblL_WeightedSumMulti": 0x001426D4,
    "bdDblL3_WeightedSumMulti": 0x001426D5,
    "bdDblL_WeightedAverageMulti": 0x001426D6,
    "bdDblL3_WeightedAverageMulti": 0x001426D7,
}

OPERATIONS = (
    "Value",
    "Add",
    "AddMulti",
    "Subtract",
    "SubtractMulti",
    "Average",
    "AverageMulti",
    "Min",
    "MinMulti",
    "Max",
    "MaxMulti",
    "Clamp",
    "Abs",
    "Negate",
    "Lerp",
    "MapRange",
    "WeightedSumMulti",
    "WeightedAverageMulti",
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


def _set_value(maya_cmds, plug: str, value):
    if isinstance(value, tuple):
        maya_cmds.setAttr(plug, *value, type="double3")
        return
    maya_cmds.setAttr(plug, value)


def _get_value(maya_cmds, plug: str, is_compound: bool):
    value = maya_cmds.getAttr(plug)
    if is_compound:
        return value[0]
    return value


def _value(is_compound: bool, scalar: float, compound: tuple[float, ...]):
    return compound if is_compound else scalar


def _configure_operation(maya_cmds, node: str, operation: str, is_compound):
    value = lambda scalar, compound: _value(is_compound, scalar, compound)

    if operation == "Value":
        expected = value(7.0, (7.0, -2.0, 4.0))
        _set_value(maya_cmds, f"{node}.value", expected)
        return "value", expected

    if operation == "Add":
        _set_value(maya_cmds, f"{node}.input1", value(2.0, (1.0, 2.0, 3.0)))
        _set_value(maya_cmds, f"{node}.input2", value(3.0, (4.0, 5.0, 6.0)))
        return "output", value(5.0, (5.0, 7.0, 9.0))

    if operation == "AddMulti":
        _set_value(maya_cmds, f"{node}.input[2]", value(2.0, (1.0, 2.0, 3.0)))
        _set_value(maya_cmds, f"{node}.input[9]", value(3.0, (4.0, 5.0, 6.0)))
        return "output", value(5.0, (5.0, 7.0, 9.0))

    if operation == "Subtract":
        _set_value(maya_cmds, f"{node}.input1", value(8.0, (8.0, 7.0, 6.0)))
        _set_value(maya_cmds, f"{node}.input2", value(3.0, (1.0, 2.0, 3.0)))
        return "output", value(5.0, (7.0, 5.0, 3.0))

    if operation == "SubtractMulti":
        _set_value(
            maya_cmds, f"{node}.input[2]", value(10.0, (10.0, 9.0, 8.0))
        )
        _set_value(maya_cmds, f"{node}.input[7]", value(3.0, (1.0, 2.0, 3.0)))
        _set_value(maya_cmds, f"{node}.input[20]", value(2.0, (2.0, 1.0, 1.0)))
        return "output", value(5.0, (7.0, 6.0, 4.0))

    if operation == "Average":
        _set_value(maya_cmds, f"{node}.input1", value(2.0, (2.0, 4.0, 6.0)))
        _set_value(maya_cmds, f"{node}.input2", value(6.0, (6.0, 8.0, 10.0)))
        return "output", value(4.0, (4.0, 6.0, 8.0))

    if operation == "AverageMulti":
        for index, current in enumerate(
            (
                value(2.0, (2.0, 4.0, 6.0)),
                value(4.0, (4.0, 6.0, 8.0)),
                value(6.0, (6.0, 8.0, 10.0)),
            )
        ):
            _set_value(maya_cmds, f"{node}.input[{index * 3 + 2}]", current)
        return "output", value(4.0, (4.0, 6.0, 8.0))

    if operation in {"Min", "Max"}:
        _set_value(maya_cmds, f"{node}.input1", value(2.0, (2.0, 7.0, -1.0)))
        _set_value(maya_cmds, f"{node}.input2", value(-1.0, (4.0, 3.0, 5.0)))
        expected = {
            "Min": value(-1.0, (2.0, 3.0, -1.0)),
            "Max": value(2.0, (4.0, 7.0, 5.0)),
        }[operation]
        return "output", expected

    if operation in {"MinMulti", "MaxMulti"}:
        values = (
            value(2.0, (2.0, 7.0, -1.0)),
            value(-1.0, (4.0, 3.0, 5.0)),
            value(8.0, (-3.0, 9.0, 2.0)),
        )
        for index, current in zip((2, 9, 20), values):
            _set_value(maya_cmds, f"{node}.input[{index}]", current)
        expected = {
            "MinMulti": value(-1.0, (-3.0, 3.0, -1.0)),
            "MaxMulti": value(8.0, (4.0, 9.0, 5.0)),
        }[operation]
        return "output", expected

    if operation == "Clamp":
        _set_value(maya_cmds, f"{node}.input", value(5.0, (-1.0, 5.0, 10.0)))
        _set_value(maya_cmds, f"{node}.min", value(1.0, (0.0, 0.0, 0.0)))
        _set_value(maya_cmds, f"{node}.max", value(3.0, (2.0, 4.0, 8.0)))
        return "output", value(3.0, (0.0, 4.0, 8.0))

    if operation == "Abs":
        _set_value(maya_cmds, f"{node}.input", value(-4.0, (-4.0, 0.0, 3.0)))
        return "output", value(4.0, (4.0, 0.0, 3.0))

    if operation == "Negate":
        _set_value(maya_cmds, f"{node}.input", value(-4.0, (1.0, -2.0, 3.0)))
        return "output", value(4.0, (-1.0, 2.0, -3.0))

    if operation == "Lerp":
        _set_value(maya_cmds, f"{node}.input1", value(2.0, (2.0, 4.0, 6.0)))
        _set_value(maya_cmds, f"{node}.input2", value(6.0, (6.0, 8.0, 10.0)))
        maya_cmds.setAttr(f"{node}.weight", 0.25)
        return "output", value(3.0, (3.0, 5.0, 7.0))

    if operation == "MapRange":
        _set_value(maya_cmds, f"{node}.input", value(5.0, (5.0, 5.0, 5.0)))
        _set_value(maya_cmds, f"{node}.srcMin", value(0.0, (0.0, 0.0, 0.0)))
        _set_value(
            maya_cmds, f"{node}.srcMax", value(10.0, (10.0, 10.0, 10.0))
        )
        _set_value(
            maya_cmds, f"{node}.dstMin", value(10.0, (10.0, 20.0, 30.0))
        )
        _set_value(
            maya_cmds, f"{node}.dstMax", value(20.0, (20.0, 40.0, 60.0))
        )
        return "output", value(15.0, (15.0, 30.0, 45.0))

    if operation in {"WeightedSumMulti", "WeightedAverageMulti"}:
        _set_value(
            maya_cmds, f"{node}.input[2].value", value(2.0, (2.0, 4.0, 6.0))
        )
        maya_cmds.setAttr(f"{node}.input[2].weight", 1.0)
        _set_value(
            maya_cmds, f"{node}.input[9].value", value(8.0, (8.0, 12.0, 16.0))
        )
        maya_cmds.setAttr(f"{node}.input[9].weight", 3.0)
        expected = {
            "WeightedSumMulti": value(26.0, (26.0, 40.0, 54.0)),
            "WeightedAverageMulti": value(6.5, (6.5, 10.0, 13.5)),
        }[operation]
        return "output", expected

    raise AssertionError(f"Unhandled operation: {operation}")


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_all_node_types_are_registered_with_expected_ids(
    maya_cmds,
    maya_om,
    node_type,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == NODE_TYPE_IDS[node_type]


@pytest.mark.parametrize("type_code", ("bdDblL", "bdDblL3"))
@pytest.mark.parametrize("operation", OPERATIONS)
def test_all_operations_match_existing_numeric_behavior(
    maya_cmds,
    type_code,
    operation,
):
    _load_bd_util_nodes(maya_cmds)

    is_compound = type_code == "bdDblL3"
    node = maya_cmds.createNode(f"{type_code}_{operation}")
    output_name, expected = _configure_operation(
        maya_cmds,
        node,
        operation,
        is_compound,
    )

    assert _get_value(
        maya_cmds,
        f"{node}.{output_name}",
        is_compound,
    ) == pytest.approx(expected)


def test_scalar_and_compound_attributes_use_linear_unit_children(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    scalar = maya_cmds.createNode("bdDblL_Lerp")
    assert maya_cmds.getAttr(f"{scalar}.input1", type=True) == "doubleLinear"
    assert maya_cmds.getAttr(f"{scalar}.input2", type=True) == "doubleLinear"
    assert maya_cmds.getAttr(f"{scalar}.weight", type=True) == "double"
    assert maya_cmds.getAttr(f"{scalar}.output", type=True) == "doubleLinear"

    compound = maya_cmds.createNode("bdDblL3_Lerp")
    assert maya_cmds.getAttr(f"{compound}.input1", type=True) == "double3"
    for child in ("input1X", "input1Y", "input1Z"):
        assert maya_cmds.getAttr(f"{compound}.{child}", type=True) == (
            "doubleLinear"
        )
    assert maya_cmds.getAttr(f"{compound}.weight", type=True) == "double"
    assert maya_cmds.getAttr(f"{compound}.output", type=True) == "double3"
    for child in ("outputX", "outputY", "outputZ"):
        assert maya_cmds.getAttr(f"{compound}.{child}", type=True) == (
            "doubleLinear"
        )

    weighted = maya_cmds.createNode("bdDblL3_WeightedAverageMulti")
    assert (
        maya_cmds.getAttr(
            f"{weighted}.input[2].value",
            type=True,
        )
        == "double3"
    )
    assert (
        maya_cmds.getAttr(
            f"{weighted}.input[2].valueX",
            type=True,
        )
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(
            f"{weighted}.input[2].weight",
            type=True,
        )
        == "double"
    )


def test_linear_display_unit_changes_do_not_change_internal_distance(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="cm")
        scalar = maya_cmds.createNode("bdDblL_Add")
        compound = maya_cmds.createNode("bdDblL3_Add")
        maya_cmds.setAttr(f"{scalar}.input1", 2.0)
        maya_cmds.setAttr(f"{scalar}.input2", 3.0)
        maya_cmds.setAttr(f"{compound}.input1", 1.0, 2.0, 3.0, type="double3")
        maya_cmds.setAttr(f"{compound}.input2", 4.0, 5.0, 6.0, type="double3")

        assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(5.0)
        assert maya_cmds.getAttr(f"{compound}.output")[0] == pytest.approx(
            (5.0, 7.0, 9.0)
        )

        maya_cmds.currentUnit(linear="m")
        assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(0.05)
        assert maya_cmds.getAttr(f"{compound}.output")[0] == pytest.approx(
            (0.05, 0.07, 0.09)
        )

        selection = maya_om.MSelectionList()
        selection.add(f"{scalar}.output")
        selection.add(f"{compound}.outputY")
        assert selection.getPlug(0).asMDistance().asCentimeters() == (
            pytest.approx(5.0)
        )
        assert selection.getPlug(1).asMDistance().asCentimeters() == (
            pytest.approx(7.0)
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_translate_scalar_and_parent_compound_connect_directly(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    scalar_source = maya_cmds.createNode("transform")
    scalar_target = maya_cmds.createNode("transform")
    scalar = maya_cmds.createNode("bdDblL_Add")
    maya_cmds.setAttr(f"{scalar_source}.translateX", 2.0)
    maya_cmds.setAttr(f"{scalar}.input2", 3.0)
    maya_cmds.connectAttr(f"{scalar_source}.translateX", f"{scalar}.input1")
    maya_cmds.connectAttr(f"{scalar}.output", f"{scalar_target}.translateX")
    assert maya_cmds.getAttr(f"{scalar_target}.translateX") == pytest.approx(
        5.0
    )

    compound_source = maya_cmds.createNode("transform")
    compound_target = maya_cmds.createNode("transform")
    compound = maya_cmds.createNode("bdDblL3_Add")
    maya_cmds.setAttr(
        f"{compound_source}.translate",
        1.0,
        2.0,
        3.0,
        type="double3",
    )
    maya_cmds.setAttr(f"{compound}.input2", 4.0, 5.0, 6.0, type="double3")
    maya_cmds.connectAttr(f"{compound_source}.translate", f"{compound}.input1")
    maya_cmds.connectAttr(f"{compound}.output", f"{compound_target}.translate")
    assert maya_cmds.getAttr(f"{compound_target}.translate")[0] == (
        pytest.approx((5.0, 7.0, 9.0))
    )

    assert not maya_cmds.ls(type="unitConversion")


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_parent_and_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDblL3_Add")
        maya_cmds.setAttr(f"{node}.input1", 1.0, 2.0, 3.0, type="double3")
        maya_cmds.setAttr(f"{node}.input2", 4.0, 5.0, 6.0, type="double3")
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(7.0)

        maya_cmds.setAttr(f"{node}.input1Y", 10.0)
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (5.0, 15.0, 9.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_sparse_multi_removal_updates_scalar_and_compound(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    scalar = maya_cmds.createNode("bdDblL_AddMulti")
    maya_cmds.setAttr(f"{scalar}.input[2]", 2.0)
    maya_cmds.setAttr(f"{scalar}.input[9]", 3.0)
    assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(5.0)
    maya_cmds.removeMultiInstance(f"{scalar}.input[2]", b=True)
    assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(3.0)

    compound = maya_cmds.createNode("bdDblL3_AddMulti")
    maya_cmds.setAttr(f"{compound}.input[2]", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{compound}.input[9]", 4.0, 5.0, 6.0, type="double3")
    assert maya_cmds.getAttr(f"{compound}.output")[0] == pytest.approx(
        (5.0, 7.0, 9.0)
    )
    maya_cmds.removeMultiInstance(f"{compound}.input[2]", b=True)
    assert maya_cmds.getAttr(f"{compound}.output")[0] == pytest.approx(
        (4.0, 5.0, 6.0)
    )


def test_node_operator_creation_and_existing_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_l3_add import (
        BdDblL3Add,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_l_add import BdDblLAdd

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDblL_Add(name="scalar")
    compound = nodes.create.bdDblL3_Add(name="compound")
    scalar.input1.set(2.0)
    scalar.input2.set(3.0)
    compound.input1.set((1.0, 2.0, 3.0))
    compound.input2.set((4.0, 5.0, 6.0))
    modifier_manager.do_it_dg()

    assert isinstance(scalar, BdDblLAdd)
    assert isinstance(compound, BdDblL3Add)
    assert scalar.output.get() == pytest.approx(5.0)
    assert compound.output.get().as_tuple() == pytest.approx((5.0, 7.0, 9.0))
    assert compound.input1.input1X.get() == pytest.approx(1.0)
    assert compound.output.outputZ.get() == pytest.approx(9.0)
    assert isinstance(nodes.existing.bdDblL_Add("scalar"), BdDblLAdd)
    assert isinstance(nodes.existing.bdDblL3_Add("compound"), BdDblL3Add)


def test_scalar_and_compound_survive_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDblL_Add(name="scalar")
    compound = nodes.create.bdDblL3_Add(name="compound")
    scalar.input1.set(2.0)
    scalar.input2.set(3.0)
    compound.input1.set((1.0, 2.0, 3.0))
    compound.input2.set((4.0, 5.0, 6.0))

    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_double_linear.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDblL_Add("scalar").output.get() == (
        pytest.approx(5.0)
    )
    assert reloaded.existing.bdDblL3_Add(
        "compound"
    ).output.get().as_tuple() == pytest.approx((5.0, 7.0, 9.0))
