# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


NODE_TYPE = "bdDblL_RightTriangle"
NODE_TYPE_ID = 0x0007F069


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


def test_node_type_id_and_attribute_contract(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(NODE_TYPE)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == NODE_TYPE_ID

    expected_types = {
        "solveFor": "enum",
        "legA": "doubleLinear",
        "legB": "doubleLinear",
        "hypotenuse": "doubleLinear",
        "output": "doubleLinear",
        "isValid": "bool",
    }
    expected_short_names = {
        "solveFor": "sf",
        "legA": "la",
        "legB": "lb",
        "hypotenuse": "h",
        "output": "o",
        "isValid": "iv",
    }
    for attribute, attribute_type in expected_types.items():
        assert (
            maya_cmds.getAttr(f"{node}.{attribute}", type=True)
            == attribute_type
        )
        assert (
            maya_cmds.attributeQuery(
                attribute,
                node=node,
                shortName=True,
            )
            == expected_short_names[attribute]
        )

    assert maya_cmds.attributeQuery(
        "solveFor",
        node=node,
        listEnum=True,
    ) == ["Hypotenuse:LegA:LegB"]
    assert maya_cmds.getAttr(f"{node}.solveFor") == 0
    assert maya_cmds.getAttr(f"{node}.legA") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.legB") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.hypotenuse") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert (
        maya_cmds.attributeQuery("output", node=node, writable=True) is False
    )
    assert (
        maya_cmds.attributeQuery("isValid", node=node, writable=True) is False
    )


@pytest.mark.parametrize(
    ("solve_for", "leg_a", "leg_b", "hypotenuse", "expected"),
    (
        (0, 3.0, 4.0, 0.0, 5.0),
        (1, 0.0, 4.0, 5.0, 3.0),
        (2, 3.0, 0.0, 5.0, 4.0),
    ),
)
def test_solves_each_side_of_three_four_five_triangle(
    maya_cmds,
    solve_for,
    leg_a,
    leg_b,
    hypotenuse,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(NODE_TYPE)
    maya_cmds.setAttr(f"{node}.solveFor", solve_for)
    maya_cmds.setAttr(f"{node}.legA", leg_a)
    maya_cmds.setAttr(f"{node}.legB", leg_b)
    maya_cmds.setAttr(f"{node}.hypotenuse", hypotenuse)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


@pytest.mark.parametrize(
    ("solve_for", "leg_a", "leg_b", "hypotenuse", "expected"),
    (
        (0, -3.0, -4.0, 0.0, 5.0),
        (1, 0.0, -4.0, -5.0, 3.0),
        (2, -3.0, 0.0, -5.0, 4.0),
    ),
)
def test_negative_lengths_are_treated_as_magnitudes(
    maya_cmds,
    solve_for,
    leg_a,
    leg_b,
    hypotenuse,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(NODE_TYPE)
    maya_cmds.setAttr(f"{node}.solveFor", solve_for)
    maya_cmds.setAttr(f"{node}.legA", leg_a)
    maya_cmds.setAttr(f"{node}.legB", leg_b)
    maya_cmds.setAttr(f"{node}.hypotenuse", hypotenuse)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_invalid_inverse_returns_zero_and_false(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(NODE_TYPE)
    maya_cmds.setAttr(f"{node}.solveFor", 1)
    maya_cmds.setAttr(f"{node}.hypotenuse", 4.0)
    maya_cmds.setAttr(f"{node}.legB", 5.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)

    maya_cmds.setAttr(f"{node}.hypotenuse", 5.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


@pytest.mark.parametrize("invalid_value", (float("nan"), float("inf")))
def test_non_finite_inputs_return_zero_and_false(
    maya_cmds,
    invalid_value,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(NODE_TYPE)
    maya_cmds.setAttr(f"{node}.legA", invalid_value)
    maya_cmds.setAttr(f"{node}.legB", 4.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False


def test_large_values_are_solved_without_intermediate_overflow(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(NODE_TYPE)
    maya_cmds.setAttr(f"{node}.legA", 3.0e154)
    maya_cmds.setAttr(f"{node}.legB", 4.0e154)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(5.0e154)
    assert maya_cmds.getAttr(f"{node}.isValid") is True

    maya_cmds.setAttr(f"{node}.solveFor", 1)
    maya_cmds.setAttr(f"{node}.hypotenuse", 5.0e154)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(3.0e154)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_mode_and_inputs_dirty_both_outputs(maya_cmds, evaluation_mode):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode(NODE_TYPE)
        maya_cmds.setAttr(f"{node}.legA", 3.0)
        maya_cmds.setAttr(f"{node}.legB", 4.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(5.0)
        assert maya_cmds.getAttr(f"{node}.isValid") is True

        maya_cmds.setAttr(f"{node}.solveFor", 1)
        maya_cmds.setAttr(f"{node}.hypotenuse", 13.0)
        maya_cmds.setAttr(f"{node}.legB", 5.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(12.0)
        assert maya_cmds.getAttr(f"{node}.isValid") is True

        maya_cmds.setAttr(f"{node}.hypotenuse", 4.0)
        assert maya_cmds.getAttr(f"{node}.isValid") is False
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_linear_display_unit_preserves_physical_result(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="cm")
        node = maya_cmds.createNode(NODE_TYPE)
        maya_cmds.setAttr(f"{node}.legA", 300.0)
        maya_cmds.setAttr(f"{node}.legB", 400.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(500.0)

        maya_cmds.currentUnit(linear="m")
        assert maya_cmds.getAttr(f"{node}.legA") == pytest.approx(3.0)
        assert maya_cmds.getAttr(f"{node}.legB") == pytest.approx(4.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(5.0)

        selection = maya_om.MSelectionList()
        selection.add(f"{node}.output")
        assert selection.getPlug(0).asMDistance().asCentimeters() == (
            pytest.approx(500.0)
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_translate_connections_do_not_create_unit_conversion(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    leg_a_source = maya_cmds.createNode("transform")
    leg_b_source = maya_cmds.createNode("transform")
    target = maya_cmds.createNode("transform")
    node = maya_cmds.createNode(NODE_TYPE)
    maya_cmds.setAttr(f"{leg_a_source}.translateX", 3.0)
    maya_cmds.setAttr(f"{leg_b_source}.translateX", 4.0)
    maya_cmds.connectAttr(f"{leg_a_source}.translateX", f"{node}.legA")
    maya_cmds.connectAttr(f"{leg_b_source}.translateX", f"{node}.legB")
    maya_cmds.connectAttr(f"{node}.output", f"{target}.translateX")

    assert maya_cmds.getAttr(f"{target}.translateX") == pytest.approx(5.0)
    assert not maya_cmds.ls(type="unitConversion")


def test_node_operator_creation_and_existing_accessor(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_l_right_triangle import (
        BdDblLRightTriangle,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblL_RightTriangle(name="right_triangle")
    node.solveFor.set(node.solveFor.LEGA)
    node.legB.set(4.0)
    node.hypotenuse.set(5.0)
    modifier_manager.do_it_dg()

    assert isinstance(node, BdDblLRightTriangle)
    assert node.solveFor.name_by_index(node.solveFor.LEGA) == "LegA"
    assert node.output.get() == pytest.approx(3.0)
    assert node.isValid.get() is True
    assert isinstance(
        nodes.existing.bdDblL_RightTriangle("right_triangle"),
        BdDblLRightTriangle,
    )


def test_node_survives_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblL_RightTriangle(name="right_triangle")
    node.solveFor.set(node.solveFor.LEGB)
    node.legA.set(3.0)
    node.hypotenuse.set(5.0)
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_right_triangle.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    loaded_node = reloaded.existing.bdDblL_RightTriangle("right_triangle")
    assert loaded_node.output.get() == pytest.approx(4.0)
    assert loaded_node.isValid.get() is True
