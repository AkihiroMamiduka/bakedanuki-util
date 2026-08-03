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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_weighted_sum_multi import (
        BdDbl3WeightedSumMulti,
    )

    assert BdDbl3WeightedSumMulti.NODE_TYPE == "bdDbl3_WeightedSumMulti"
    assert BdDbl3WeightedSumMulti.input.long_name == "input"
    assert BdDbl3WeightedSumMulti.output.long_name == "output"
    assert BdDbl3WeightedSumMulti.oz.short_name == "oz"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_WeightedSumMulti()
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))
    assert node.input[2].value.long_name == "value"
    assert node.input[2].value.x.long_name == "valueX"
    assert node.input[2].v.z.short_name == "vz"
    assert node.input[2].weight.long_name == "weight"

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F019


def test_sums_sparse_weighted_vectors_without_normalizing(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_WeightedSumMulti(name="weighted")
    node.input[2].value.set((2.0, 4.0, 6.0))
    node.input[2].weight.set(0.5)
    node.input[9].value.set((1.0, -2.0, 3.0))
    node.input[9].weight.set(2.0)
    node.input[20].value.set((4.0, 5.0, 6.0))
    node.input[20].weight.set(-1.0)
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((-1.0, -7.0, 3.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((3.0, -2.0, 9.0))


def test_one_scalar_weight_applies_to_all_components(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_WeightedSumMulti()
    node.input[4].value.set((1.0, 2.0, 3.0))
    node.input[4].weight.set(3.0)
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((3.0, 6.0, 9.0))


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_nested_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl3_WeightedSumMulti")
        maya_cmds.setAttr(
            f"{node}.input[2].value",
            2.0,
            4.0,
            6.0,
            type="double3",
        )
        maya_cmds.setAttr(f"{node}.input[2].weight", 0.5)
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (1.0, 2.0, 3.0)
        )

        maya_cmds.setAttr(f"{node}.input[2].valueY", 10.0)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(5.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)
