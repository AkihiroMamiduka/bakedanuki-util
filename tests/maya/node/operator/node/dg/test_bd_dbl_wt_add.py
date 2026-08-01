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

    from bd_util.maya.node.operator.node.dg.bd_dbl_wt_add_multi import (
        BdDblWtAddMulti,
    )

    assert BdDblWtAddMulti.NODE_TYPE == "bdDblWtAddMulti"
    assert BdDblWtAddMulti.input.long_name == "input"
    assert BdDblWtAddMulti.i.short_name == "i"
    assert BdDblWtAddMulti.output.long_name == "output"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblWtAddMulti()
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(0.0)
    assert node.input[2].value.long_name == "value"
    assert node.input[2].v.short_name == "v"
    assert node.input[2].weight.long_name == "weight"
    assert node.input[2].w.short_name == "w"

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F01A


def test_sums_sparse_weighted_values_without_normalizing(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblWtAddMulti(name="weighted")
    node.input[2].value.set(10.0)
    node.input[2].weight.set(0.5)
    node.input[9].value.set(4.0)
    node.input[9].weight.set(2.0)
    node.input[20].value.set(3.0)
    node.input[20].weight.set(-1.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(10.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(2.0)


def test_default_weight_contributes_nothing(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDblWtAddMulti()
    node.input[4].value.set(100.0)
    modifier_manager.do_it_dg()

    assert node.input[4].weight.get() == pytest.approx(0.0)
    assert node.output.get() == pytest.approx(0.0)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDblWtAddMulti")
        maya_cmds.setAttr(f"{node}.input[2].value", 4.0)
        maya_cmds.setAttr(f"{node}.input[2].weight", 2.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(8.0)

        maya_cmds.setAttr(f"{node}.input[2].weight", -0.5)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(-2.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)
