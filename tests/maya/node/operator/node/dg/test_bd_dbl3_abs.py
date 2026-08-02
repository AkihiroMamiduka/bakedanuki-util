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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_abs import BdDbl3Abs

    assert BdDbl3Abs.NODE_TYPE == "bdDbl3_Abs"
    assert BdDbl3Abs.input.long_name == "input"
    assert BdDbl3Abs.ix.short_name == "ix"
    assert BdDbl3Abs.iy.short_name == "iy"
    assert BdDbl3Abs.iz.short_name == "iz"
    assert BdDbl3Abs.output.long_name == "output"
    assert BdDbl3Abs.ox.short_name == "ox"
    assert BdDbl3Abs.oy.short_name == "oy"
    assert BdDbl3Abs.oz.short_name == "oz"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Abs()
    modifier_manager.do_it_dg()

    zero = (0.0, 0.0, 0.0)
    assert node.input.get().as_tuple() == pytest.approx(zero)
    assert node.output.get().as_tuple() == pytest.approx(zero)

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F027


def test_returns_component_wise_absolute_value(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Abs")
    maya_cmds.setAttr(f"{node}.input", -1.5, 2.5, -3.5, type="double3")
    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (1.5, 2.5, 3.5)
    )


def test_nan_propagates_per_component(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Abs")
    maya_cmds.setAttr(
        f"{node}.input",
        -1.0,
        float("nan"),
        -3.0,
        type="double3",
    )
    output = maya_cmds.getAttr(f"{node}.output")[0]
    assert output[0] == pytest.approx(1.0)
    assert math.isnan(output[1])
    assert output[2] == pytest.approx(3.0)


def test_infinity_and_signed_zero_are_component_wise(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Abs")
    maya_cmds.setAttr(
        f"{node}.input",
        float("-inf"),
        float("inf"),
        -0.0,
        type="double3",
    )
    output = maya_cmds.getAttr(f"{node}.output")[0]
    assert output[:2] == (float("inf"), float("inf"))
    assert output[2] == 0.0
    assert math.copysign(1.0, output[2]) == 1.0


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl3_Abs")
        maya_cmds.setAttr(f"{node}.input", -1.0, -2.0, -3.0, type="double3")
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (1.0, 2.0, 3.0)
        )

        maya_cmds.setAttr(f"{node}.inputY", 4.5)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(4.5)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_child_dependencies_cover_output_compound(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Abs")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    for input_attribute in ("input", "inputX", "inputY", "inputZ"):
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
    source = nodes.create.bdDbl3_Abs(name="source_abs3")
    target = nodes.create.bdDbl3_Abs(name="target_abs3")
    source.input.set((-1.0, 2.0, -3.0))
    source.output.connect(target.input)
    modifier_manager.do_it_dg()

    expected = (1.0, 2.0, 3.0)
    assert target.output.get().as_tuple() == pytest.approx(expected)
    existing = nodes.existing.bdDbl3_Abs(target.name)
    assert type(existing) is type(target)

    scene_path = tmp_path / "bd_dbl3_abs.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    output = reloaded.existing.bdDbl3_Abs("target_abs3").output.get()
    assert output.as_tuple() == pytest.approx(expected)
