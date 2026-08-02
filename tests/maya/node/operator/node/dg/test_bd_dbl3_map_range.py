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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_map_range import (
        BdDbl3MapRange,
    )

    assert BdDbl3MapRange.NODE_TYPE == "bdDbl3_MapRange"
    assert BdDbl3MapRange.input.long_name == "input"
    assert BdDbl3MapRange.ix.short_name == "ix"
    assert BdDbl3MapRange.srcMin.long_name == "srcMin"
    assert BdDbl3MapRange.sminy.short_name == "sminy"
    assert BdDbl3MapRange.srcMax.long_name == "srcMax"
    assert BdDbl3MapRange.smaxz.short_name == "smaxz"
    assert BdDbl3MapRange.dstMin.long_name == "dstMin"
    assert BdDbl3MapRange.dminx.short_name == "dminx"
    assert BdDbl3MapRange.dstMax.long_name == "dstMax"
    assert BdDbl3MapRange.dmaxy.short_name == "dmaxy"
    assert BdDbl3MapRange.clamp.long_name == "clamp"
    assert BdDbl3MapRange.c.short_name == "c"
    assert BdDbl3MapRange.output.long_name == "output"
    assert BdDbl3MapRange.oz.short_name == "oz"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_MapRange()
    modifier_manager.do_it_dg()

    zero = (0.0, 0.0, 0.0)
    one = (1.0, 1.0, 1.0)
    assert node.input.get().as_tuple() == pytest.approx(zero)
    assert node.srcMin.get().as_tuple() == pytest.approx(zero)
    assert node.srcMax.get().as_tuple() == pytest.approx(one)
    assert node.dstMin.get().as_tuple() == pytest.approx(zero)
    assert node.dstMax.get().as_tuple() == pytest.approx(one)
    assert node.clamp.get() is True
    assert node.output.get().as_tuple() == pytest.approx(zero)

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F025


def test_maps_component_wise_directional_ranges(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_MapRange")
    maya_cmds.setAttr(f"{node}.input", -5.0, 5.0, 15.0, type="double3")
    maya_cmds.setAttr(f"{node}.srcMin", 0.0, 10.0, 0.0, type="double3")
    maya_cmds.setAttr(f"{node}.srcMax", 10.0, 0.0, 10.0, type="double3")
    maya_cmds.setAttr(f"{node}.dstMin", 0.0, 100.0, 20.0, type="double3")
    maya_cmds.setAttr(f"{node}.dstMax", 1.0, 0.0, 10.0, type="double3")
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (0.0, 50.0, 10.0)
    )


def test_extrapolates_all_components_when_clamp_is_false(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_MapRange")
    maya_cmds.setAttr(f"{node}.input", 15.0, -5.0, 5.0, type="double3")
    maya_cmds.setAttr(f"{node}.srcMax", 10.0, 10.0, 10.0, type="double3")
    maya_cmds.setAttr(f"{node}.clamp", False)
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (1.5, -0.5, 0.5)
    )


def test_zero_width_source_returns_target_minimum_per_component(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_MapRange")
    maya_cmds.setAttr(f"{node}.input", 5.0, 5.0, 5.0, type="double3")
    maya_cmds.setAttr(f"{node}.srcMin", 2.0, -0.0, 0.0, type="double3")
    maya_cmds.setAttr(f"{node}.srcMax", 2.0, 0.0, 10.0, type="double3")
    maya_cmds.setAttr(f"{node}.dstMin", -3.0, -4.0, 0.0, type="double3")
    maya_cmds.setAttr(f"{node}.dstMax", 7.0, 8.0, 100.0, type="double3")
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (-3.0, -4.0, 50.0)
    )


@pytest.mark.parametrize(
    ("nan_attribute", "component"),
    (
        ("inputX", 0),
        ("srcMinY", 1),
        ("srcMaxZ", 2),
        ("dstMinX", 0),
        ("dstMaxY", 1),
    ),
)
def test_nan_propagates_per_component(maya_cmds, nan_attribute, component):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_MapRange")
    maya_cmds.setAttr(f"{node}.input", 0.5, 0.5, 0.5, type="double3")
    maya_cmds.setAttr(f"{node}.{nan_attribute}", float("nan"))
    output = maya_cmds.getAttr(f"{node}.output")[0]
    assert math.isnan(output[component])
    assert tuple(
        value for index, value in enumerate(output) if index != component
    ) == pytest.approx((0.5, 0.5))


def test_infinity_is_clamped_component_wise(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_MapRange")
    maya_cmds.setAttr(
        f"{node}.input",
        float("-inf"),
        float("inf"),
        0.5,
        type="double3",
    )
    maya_cmds.setAttr(f"{node}.dstMin", -5.0, -5.0, -5.0, type="double3")
    maya_cmds.setAttr(f"{node}.dstMax", 5.0, 5.0, 5.0, type="double3")
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (-5.0, 5.0, 0.0)
    )


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl3_MapRange")
        maya_cmds.setAttr(f"{node}.input", -5.0, 5.0, 15.0, type="double3")
        maya_cmds.setAttr(f"{node}.srcMax", 10.0, 10.0, 10.0, type="double3")
        maya_cmds.setAttr(f"{node}.dstMax", 10.0, 10.0, 10.0, type="double3")
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (0.0, 5.0, 10.0)
        )

        maya_cmds.setAttr(f"{node}.inputX", 7.0)
        assert maya_cmds.getAttr(f"{node}.outputX") == pytest.approx(7.0)

        maya_cmds.setAttr(f"{node}.srcMinY", 10.0)
        maya_cmds.setAttr(f"{node}.srcMaxY", 0.0)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(5.0)

        maya_cmds.setAttr(f"{node}.dstMaxZ", 20.0)
        assert maya_cmds.getAttr(f"{node}.outputZ") == pytest.approx(20.0)

        maya_cmds.setAttr(f"{node}.clamp", False)
        assert maya_cmds.getAttr(f"{node}.outputZ") == pytest.approx(30.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_child_dependencies_cover_output_compound(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_MapRange")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    for input_attribute in (
        "input",
        "inputX",
        "inputY",
        "inputZ",
        "srcMin",
        "srcMinX",
        "srcMinY",
        "srcMinZ",
        "srcMax",
        "srcMaxX",
        "srcMaxY",
        "srcMaxZ",
        "dstMin",
        "dstMinX",
        "dstMinY",
        "dstMinZ",
        "dstMax",
        "dstMaxX",
        "dstMaxY",
        "dstMaxZ",
        "clamp",
    ):
        affected = node_fn.getAffectedAttributes(
            node_fn.attribute(input_attribute)
        )
        affected_names = {
            maya_om.MFnAttribute(attribute).name for attribute in affected
        }
        assert affected_names == {"output", "outputX", "outputY", "outputZ"}


def test_connections_existing_accessor_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl3_MapRange(name="source_map_range3")
    target = nodes.create.bdDbl3_MapRange(name="target_map_range3")
    source.input.set((5.0, 2.5, 7.5))
    source.srcMax.set((10.0, 10.0, 10.0))
    source.output.connect(target.input)
    target.dstMin.set((10.0, 20.0, 30.0))
    target.dstMax.set((20.0, 40.0, 50.0))
    modifier_manager.do_it_dg()

    expected = (15.0, 25.0, 45.0)
    assert target.output.get().as_tuple() == pytest.approx(expected)
    existing = nodes.existing.bdDbl3_MapRange(target.name)
    assert type(existing) is type(target)

    scene_path = tmp_path / "bd_dbl3_map_range.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    output = reloaded.existing.bdDbl3_MapRange(
        "target_map_range3"
    ).output.get()
    assert output.as_tuple() == pytest.approx(expected)
