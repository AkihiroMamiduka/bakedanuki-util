# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


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


def test_attributes_defaults_and_type_id(modifier_manager, maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_map_range import (
        BdDblMapRange,
    )

    assert BdDblMapRange.NODE_TYPE == "bdDbl_MapRange"
    assert BdDblMapRange.input.long_name == "input"
    assert BdDblMapRange.i.short_name == "i"
    assert BdDblMapRange.srcMin.long_name == "srcMin"
    assert BdDblMapRange.smin.short_name == "smin"
    assert BdDblMapRange.srcMax.long_name == "srcMax"
    assert BdDblMapRange.smax.short_name == "smax"
    assert BdDblMapRange.dstMin.long_name == "dstMin"
    assert BdDblMapRange.dmin.short_name == "dmin"
    assert BdDblMapRange.dstMax.long_name == "dstMax"
    assert BdDblMapRange.dmax.short_name == "dmax"
    assert BdDblMapRange.clamp.long_name == "clamp"
    assert BdDblMapRange.c.short_name == "c"
    assert BdDblMapRange.output.long_name == "output"
    assert BdDblMapRange.o.short_name == "o"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_MapRange()
    modifier_manager.do_it_dg()

    assert node.input.get() == pytest.approx(0.0)
    assert node.srcMin.get() == pytest.approx(0.0)
    assert node.srcMax.get() == pytest.approx(1.0)
    assert node.dstMin.get() == pytest.approx(0.0)
    assert node.dstMax.get() == pytest.approx(1.0)
    assert node.clamp.get() is True
    assert node.output.get() == pytest.approx(0.0)
    for attribute_name in (
        "input",
        "srcMin",
        "srcMax",
        "dstMin",
        "dstMax",
    ):
        assert not maya_cmds.attributeQuery(
            attribute_name,
            node=node.name,
            minExists=True,
        )
        assert not maya_cmds.attributeQuery(
            attribute_name,
            node=node.name,
            maxExists=True,
        )

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F026


@pytest.mark.parametrize(
    (
        "input_value",
        "source_minimum",
        "source_maximum",
        "target_minimum",
        "target_maximum",
        "should_clamp",
        "expected",
    ),
    (
        (5.0, 0.0, 10.0, 0.0, 100.0, True, 50.0),
        (-5.0, 0.0, 10.0, 0.0, 100.0, True, 0.0),
        (15.0, 0.0, 10.0, 0.0, 100.0, True, 100.0),
        (5.0, 10.0, 0.0, 0.0, 100.0, True, 50.0),
        (10.0, 10.0, 0.0, 0.0, 100.0, True, 0.0),
        (0.0, 10.0, 0.0, 0.0, 100.0, True, 100.0),
        (2.5, 0.0, 10.0, 100.0, 0.0, True, 75.0),
        (15.0, 0.0, 10.0, 0.0, 100.0, False, 150.0),
        (-5.0, 0.0, 10.0, 0.0, 100.0, False, -50.0),
    ),
)
def test_maps_directional_ranges_and_optional_extrapolation(
    maya_cmds,
    input_value,
    source_minimum,
    source_maximum,
    target_minimum,
    target_maximum,
    should_clamp,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_MapRange")
    maya_cmds.setAttr(f"{node}.input", input_value)
    maya_cmds.setAttr(f"{node}.srcMin", source_minimum)
    maya_cmds.setAttr(f"{node}.srcMax", source_maximum)
    maya_cmds.setAttr(f"{node}.dstMin", target_minimum)
    maya_cmds.setAttr(f"{node}.dstMax", target_maximum)
    maya_cmds.setAttr(f"{node}.clamp", should_clamp)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)


@pytest.mark.parametrize(
    ("source_minimum", "source_maximum"),
    ((2.0, 2.0), (-0.0, 0.0)),
)
def test_zero_width_source_returns_target_minimum(
    maya_cmds,
    source_minimum,
    source_maximum,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_MapRange")
    maya_cmds.setAttr(f"{node}.input", 50.0)
    maya_cmds.setAttr(f"{node}.srcMin", source_minimum)
    maya_cmds.setAttr(f"{node}.srcMax", source_maximum)
    maya_cmds.setAttr(f"{node}.dstMin", -3.0)
    maya_cmds.setAttr(f"{node}.dstMax", 7.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(-3.0)


@pytest.mark.parametrize(
    "nan_attribute",
    (
        "input",
        "srcMin",
        "srcMax",
        "dstMin",
        "dstMax",
    ),
)
def test_nan_propagates_from_each_numeric_input(maya_cmds, nan_attribute):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_MapRange")
    maya_cmds.setAttr(f"{node}.input", 0.5)
    maya_cmds.setAttr(f"{node}.srcMin", 0.0)
    maya_cmds.setAttr(f"{node}.srcMax", 1.0)
    maya_cmds.setAttr(f"{node}.dstMin", 0.0)
    maya_cmds.setAttr(f"{node}.dstMax", 1.0)
    maya_cmds.setAttr(f"{node}.{nan_attribute}", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


@pytest.mark.parametrize(
    ("input_value", "should_clamp", "expected"),
    (
        (float("inf"), True, 5.0),
        (float("-inf"), True, -5.0),
        (float("inf"), False, float("inf")),
        (float("-inf"), False, float("-inf")),
    ),
)
def test_infinite_input_uses_clamp_or_extrapolation(
    maya_cmds,
    input_value,
    should_clamp,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_MapRange")
    maya_cmds.setAttr(f"{node}.input", input_value)
    maya_cmds.setAttr(f"{node}.srcMin", 0.0)
    maya_cmds.setAttr(f"{node}.srcMax", 1.0)
    maya_cmds.setAttr(f"{node}.dstMin", -5.0)
    maya_cmds.setAttr(f"{node}.dstMax", 5.0)
    maya_cmds.setAttr(f"{node}.clamp", should_clamp)
    assert maya_cmds.getAttr(f"{node}.output") == expected


def test_infinite_target_endpoints_are_exact_and_midpoint_is_nan(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_MapRange")
    maya_cmds.setAttr(f"{node}.srcMin", 0.0)
    maya_cmds.setAttr(f"{node}.srcMax", 1.0)
    maya_cmds.setAttr(f"{node}.dstMin", float("-inf"))
    maya_cmds.setAttr(f"{node}.dstMax", float("inf"))

    maya_cmds.setAttr(f"{node}.input", 0.0)
    assert maya_cmds.getAttr(f"{node}.output") == float("-inf")
    maya_cmds.setAttr(f"{node}.input", 1.0)
    assert maya_cmds.getAttr(f"{node}.output") == float("inf")
    maya_cmds.setAttr(f"{node}.input", 0.5)
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


def test_target_endpoint_signed_zero_is_preserved(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_MapRange")
    maya_cmds.setAttr(f"{node}.srcMin", 0.0)
    maya_cmds.setAttr(f"{node}.srcMax", 1.0)
    maya_cmds.setAttr(f"{node}.dstMin", -0.0)
    maya_cmds.setAttr(f"{node}.dstMax", 0.0)

    maya_cmds.setAttr(f"{node}.input", 0.0)
    minimum_output = maya_cmds.getAttr(f"{node}.output")
    assert math.copysign(1.0, minimum_output) == -1.0

    maya_cmds.setAttr(f"{node}.input", 1.0)
    maximum_output = maya_cmds.getAttr(f"{node}.output")
    assert math.copysign(1.0, maximum_output) == 1.0


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl_MapRange")
        maya_cmds.setAttr(f"{node}.input", 15.0)
        maya_cmds.setAttr(f"{node}.srcMin", 0.0)
        maya_cmds.setAttr(f"{node}.srcMax", 10.0)
        maya_cmds.setAttr(f"{node}.dstMin", 0.0)
        maya_cmds.setAttr(f"{node}.dstMax", 10.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(10.0)

        maya_cmds.setAttr(f"{node}.clamp", False)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(15.0)

        maya_cmds.setAttr(f"{node}.srcMin", 20.0)
        maya_cmds.setAttr(f"{node}.srcMax", 0.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(2.5)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connections_existing_accessor_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl_MapRange(name="source_map_range")
    target = nodes.create.bdDbl_MapRange(name="target_map_range")
    source.input.set(5.0)
    source.srcMin.set(0.0)
    source.srcMax.set(10.0)
    source.output.connect(target.input)
    target.dstMin.set(10.0)
    target.dstMax.set(20.0)
    modifier_manager.do_it_dg()

    assert target.output.get() == pytest.approx(15.0)
    existing = nodes.existing.bdDbl_MapRange(target.name)
    assert type(existing) is type(target)

    scene_path = tmp_path / "bd_dbl_map_range.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDbl_MapRange(
        "target_map_range"
    ).output.get() == pytest.approx(15.0)
