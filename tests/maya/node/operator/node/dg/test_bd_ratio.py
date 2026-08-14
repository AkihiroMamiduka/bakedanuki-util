# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


NODE_TYPE_IDS = {
    "bdDbl_RatioDblL": 0x001426E6,
    "bdDbl3_RatioDblL3": 0x001426E7,
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


def _set_double3(maya_cmds, plug: str, value) -> None:
    maya_cmds.setAttr(plug, *value, type="double3")


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_node_types_are_registered_with_expected_ids(
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


def test_scalar_attribute_contract_defaults_and_ratio(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_RatioDblL")
    assert maya_cmds.getAttr(f"{node}.input", type=True) == "doubleLinear"
    assert maya_cmds.getAttr(f"{node}.base", type=True) == "doubleLinear"
    assert maya_cmds.getAttr(f"{node}.output", type=True) == "double"
    assert maya_cmds.getAttr(f"{node}.input") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.base") == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)

    maya_cmds.setAttr(f"{node}.input", 12.0)
    maya_cmds.setAttr(f"{node}.base", 3.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(4.0)


def test_compound_attribute_contract_defaults_and_component_ratio(
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_RatioDblL3")
    assert maya_cmds.getAttr(f"{node}.input", type=True) == "double3"
    assert maya_cmds.getAttr(f"{node}.base", type=True) == "double3"
    assert maya_cmds.getAttr(f"{node}.output", type=True) == "double3"
    for axis in "XYZ":
        assert (
            maya_cmds.getAttr(f"{node}.input{axis}", type=True)
            == "doubleLinear"
        )
        assert (
            maya_cmds.getAttr(f"{node}.base{axis}", type=True)
            == "doubleLinear"
        )
        assert maya_cmds.getAttr(f"{node}.output{axis}", type=True) == "double"

    assert maya_cmds.getAttr(f"{node}.input")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.base")[0] == pytest.approx(
        (1.0, 1.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )

    _set_double3(maya_cmds, f"{node}.input", (12.0, 20.0, 30.0))
    _set_double3(maya_cmds, f"{node}.base", (3.0, 4.0, 5.0))
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (4.0, 5.0, 6.0)
    )


@pytest.mark.parametrize(
    ("input_value", "base", "expected"),
    (
        (1.0, 0.0, 1.0e9),
        (0.0, 0.0, 0.0),
        (1.0, 5.0e-10, 1.0e9),
        (1.0, -5.0e-10, -1.0e9),
        (1.0, 1.0e-9, 1.0e9),
        (1.0, -1.0e-9, -1.0e9),
        (1.0, 2.0e-9, 5.0e8),
    ),
)
def test_scalar_clamps_small_base_distance_with_sign(
    maya_cmds,
    input_value,
    base,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="cm")
        node = maya_cmds.createNode("bdDbl_RatioDblL")
        maya_cmds.setAttr(f"{node}.input", input_value)
        maya_cmds.setAttr(f"{node}.base", base)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_compound_clamps_small_base_per_component(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="cm")
        node = maya_cmds.createNode("bdDbl3_RatioDblL3")
        _set_double3(maya_cmds, f"{node}.input", (1.0, 2.0, 3.0))
        _set_double3(
            maya_cmds,
            f"{node}.base",
            (0.0, 5.0e-10, -5.0e-10),
        )
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (1.0e9, 2.0e9, -3.0e9)
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_non_finite_values_follow_ieee_arithmetic(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_RatioDblL")
    maya_cmds.setAttr(f"{node}.input", float("inf"))
    maya_cmds.setAttr(f"{node}.base", 2.0)
    assert math.isinf(maya_cmds.getAttr(f"{node}.output"))

    maya_cmds.setAttr(f"{node}.input", 1.0)
    maya_cmds.setAttr(f"{node}.base", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


@pytest.mark.parametrize(
    ("output_child", "expected"),
    (("outputX", 4.0), ("outputY", 5.0), ("outputZ", 6.0)),
)
def test_compound_output_children_can_be_requested_directly(
    maya_cmds,
    output_child,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_RatioDblL3")
    _set_double3(maya_cmds, f"{node}.input", (12.0, 20.0, 30.0))
    _set_double3(maya_cmds, f"{node}.base", (3.0, 4.0, 5.0))
    assert maya_cmds.getAttr(f"{node}.{output_child}") == pytest.approx(
        expected
    )


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_parent_and_child_dirty_updates_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl3_RatioDblL3")
        _set_double3(maya_cmds, f"{node}.input", (12.0, 20.0, 30.0))
        _set_double3(maya_cmds, f"{node}.base", (3.0, 4.0, 5.0))
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (4.0, 5.0, 6.0)
        )

        maya_cmds.setAttr(f"{node}.baseY", 10.0)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(2.0)

        maya_cmds.setAttr(f"{node}.inputZ", 50.0)
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (4.0, 2.0, 10.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_linear_display_unit_does_not_change_ratio(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="cm")
        node = maya_cmds.createNode("bdDbl3_RatioDblL3")
        _set_double3(maya_cmds, f"{node}.input", (200.0, 300.0, 400.0))
        _set_double3(maya_cmds, f"{node}.base", (50.0, 100.0, 200.0))
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (4.0, 3.0, 2.0)
        )

        maya_cmds.currentUnit(linear="m")
        assert maya_cmds.getAttr(f"{node}.input")[0] == pytest.approx(
            (2.0, 3.0, 4.0)
        )
        assert maya_cmds.getAttr(f"{node}.base")[0] == pytest.approx(
            (0.5, 1.0, 2.0)
        )
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (4.0, 3.0, 2.0)
        )

        selection = maya_om.MSelectionList()
        selection.add(f"{node}.inputX")
        selection.add(f"{node}.baseX")
        assert selection.getPlug(0).asMDistance().asCentimeters() == (
            pytest.approx(200.0)
        )
        assert selection.getPlug(1).asMDistance().asCentimeters() == (
            pytest.approx(50.0)
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_translate_inputs_drive_scale_outputs_without_unit_conversion(
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    scalar_input = maya_cmds.createNode("transform")
    scalar_base = maya_cmds.createNode("transform")
    scalar_target = maya_cmds.createNode("transform")
    scalar = maya_cmds.createNode("bdDbl_RatioDblL")
    maya_cmds.setAttr(f"{scalar_input}.translateX", 12.0)
    maya_cmds.setAttr(f"{scalar_base}.translateX", 3.0)
    maya_cmds.connectAttr(f"{scalar_input}.translateX", f"{scalar}.input")
    maya_cmds.connectAttr(f"{scalar_base}.translateX", f"{scalar}.base")
    maya_cmds.connectAttr(f"{scalar}.output", f"{scalar_target}.scaleX")
    assert maya_cmds.getAttr(f"{scalar_target}.scaleX") == pytest.approx(4.0)

    compound_input = maya_cmds.createNode("transform")
    compound_base = maya_cmds.createNode("transform")
    compound_target = maya_cmds.createNode("transform")
    compound = maya_cmds.createNode("bdDbl3_RatioDblL3")
    _set_double3(
        maya_cmds,
        f"{compound_input}.translate",
        (12.0, 20.0, 30.0),
    )
    _set_double3(
        maya_cmds,
        f"{compound_base}.translate",
        (3.0, 4.0, 5.0),
    )
    maya_cmds.connectAttr(f"{compound_input}.translate", f"{compound}.input")
    maya_cmds.connectAttr(f"{compound_base}.translate", f"{compound}.base")
    maya_cmds.connectAttr(f"{compound}.output", f"{compound_target}.scale")
    assert maya_cmds.getAttr(f"{compound_target}.scale")[0] == pytest.approx(
        (4.0, 5.0, 6.0)
    )

    assert not maya_cmds.ls(type="unitConversion")


def test_node_operator_creation_and_existing_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_ratio_dbl_l3 import (
        BdDbl3RatioDblL3,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_ratio_dbl_l import (
        BdDblRatioDblL,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDbl_RatioDblL(name="scalar")
    compound = nodes.create.bdDbl3_RatioDblL3(name="compound")
    scalar.input.set(12.0)
    scalar.base.set(3.0)
    compound.input.set((12.0, 20.0, 30.0))
    compound.base.set((3.0, 4.0, 5.0))
    modifier_manager.do_it_dg()

    assert isinstance(scalar, BdDblRatioDblL)
    assert isinstance(compound, BdDbl3RatioDblL3)
    assert scalar.output.get() == pytest.approx(4.0)
    assert compound.base.baseY.get() == pytest.approx(4.0)
    assert compound.output.get().as_tuple() == pytest.approx((4.0, 5.0, 6.0))
    assert isinstance(nodes.existing.bdDbl_RatioDblL("scalar"), BdDblRatioDblL)
    assert isinstance(
        nodes.existing.bdDbl3_RatioDblL3("compound"),
        BdDbl3RatioDblL3,
    )


def test_ratio_nodes_survive_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDbl_RatioDblL(name="scalar")
    compound = nodes.create.bdDbl3_RatioDblL3(name="compound")
    scalar.input.set(12.0)
    scalar.base.set(3.0)
    compound.input.set((12.0, 20.0, 30.0))
    compound.base.set((3.0, 4.0, 5.0))
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_ratio.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDbl_RatioDblL(
        "scalar"
    ).output.get() == pytest.approx(4.0)
    assert reloaded.existing.bdDbl3_RatioDblL3(
        "compound"
    ).output.get().as_tuple() == pytest.approx((4.0, 5.0, 6.0))
