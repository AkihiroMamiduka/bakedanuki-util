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

    from bd_util.maya.node.operator.node.dg.bd_dbl_lerp import (
        BdDblLerp,
    )

    assert BdDblLerp.NODE_TYPE == "bdDblLerp"
    assert BdDblLerp.input1.long_name == "input1"
    assert BdDblLerp.i2.short_name == "i2"
    assert BdDblLerp.weight.long_name == "weight"
    assert BdDblLerp.w.short_name == "w"
    assert BdDblLerp.output.long_name == "output"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblLerp()
    modifier_manager.do_it_dg()

    assert node.input1.get() == pytest.approx(0.0)
    assert node.input2.get() == pytest.approx(0.0)
    assert node.weight.get() == pytest.approx(0.0)
    assert node.output.get() == pytest.approx(0.0)
    assert maya_cmds.attributeQuery("weight", node=node.name, min=True) == [
        0.0
    ]
    assert maya_cmds.attributeQuery("weight", node=node.name, max=True) == [
        1.0
    ]

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F018


@pytest.mark.parametrize(
    ("weight", "expected"),
    [(0.0, 10.0), (0.25, 12.5), (1.0, 20.0)],
)
def test_interpolates_between_inputs(
    modifier_manager,
    maya_cmds,
    weight,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblLerp(name="lerp")
    node.input1.set(10.0)
    node.input2.set(20.0)
    node.weight.set(weight)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(expected)


@pytest.mark.parametrize(
    ("source_weight", "expected"),
    [(-2.0, 10.0), (2.0, 20.0)],
)
def test_connected_weight_is_clamped(
    maya_cmds,
    source_weight,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDblLerp")
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(source, longName="weight", attributeType="double")
    maya_cmds.setAttr(f"{node}.input1", 10.0)
    maya_cmds.setAttr(f"{node}.input2", 20.0)
    maya_cmds.connectAttr(f"{source}.weight", f"{node}.weight")
    maya_cmds.setAttr(f"{source}.weight", source_weight)

    assert maya_cmds.getAttr(f"{node}.weight") == pytest.approx(source_weight)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDblLerp")
        maya_cmds.setAttr(f"{node}.input1", 4.0)
        maya_cmds.setAttr(f"{node}.input2", 12.0)
        maya_cmds.setAttr(f"{node}.weight", 0.25)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(6.0)

        maya_cmds.setAttr(f"{node}.input2", 20.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(8.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)
