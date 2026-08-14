# coding: utf-8
from __future__ import annotations

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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_lerp import (
        BdDbl3Lerp,
    )

    assert BdDbl3Lerp.NODE_TYPE == "bdDbl3_Lerp"
    assert BdDbl3Lerp.input1.long_name == "input1"
    assert BdDbl3Lerp.i1x.short_name == "i1x"
    assert BdDbl3Lerp.input2.long_name == "input2"
    assert BdDbl3Lerp.i2z.short_name == "i2z"
    assert BdDbl3Lerp.weight.long_name == "weight"
    assert BdDbl3Lerp.output.long_name == "output"
    assert BdDbl3Lerp.oy.short_name == "oy"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Lerp()
    modifier_manager.do_it_dg()

    assert node.input1.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))
    assert node.input2.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))
    assert node.weight.get() == pytest.approx(0.0)
    assert node.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142696


def test_interpolates_components_with_one_weight(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Lerp(name="lerp")
    node.input1.set((0.0, 10.0, -10.0))
    node.input2.set((20.0, -10.0, 30.0))
    node.weight.set(0.25)
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((5.0, 5.0, 0.0))


@pytest.mark.parametrize(
    ("source_weight", "expected"),
    [(-1.0, (1.0, 2.0, 3.0)), (3.0, (4.0, 5.0, 6.0))],
)
def test_connected_weight_is_clamped(
    maya_cmds,
    source_weight,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Lerp")
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(source, longName="weight", attributeType="double")
    maya_cmds.setAttr(f"{node}.input1", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{node}.input2", 4.0, 5.0, 6.0, type="double3")
    maya_cmds.connectAttr(f"{source}.weight", f"{node}.weight")
    maya_cmds.setAttr(f"{source}.weight", source_weight)

    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(expected)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl3_Lerp")
        maya_cmds.setAttr(f"{node}.input1", 0.0, 0.0, 0.0, type="double3")
        maya_cmds.setAttr(f"{node}.input2", 4.0, 8.0, 12.0, type="double3")
        maya_cmds.setAttr(f"{node}.weight", 0.5)
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (2.0, 4.0, 6.0)
        )

        maya_cmds.setAttr(f"{node}.input2Y", 12.0)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(6.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)
