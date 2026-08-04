# coding: utf-8
from __future__ import annotations

import math
import os
import sys
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


@pytest.mark.parametrize(
    ("node_type", "type_id"),
    (
        ("bdDbl3_WeightedAverageMulti", 0x0007F033),
        ("bdDbl_WeightedAverageMulti", 0x0007F034),
    ),
)
def test_attributes_defaults_and_type_ids(
    modifier_manager,
    maya_cmds,
    maya_om,
    node_type,
    type_id,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    if node_type.startswith("bdDbl3_"):
        node = nodes.create.bdDbl3_WeightedAverageMulti()
    else:
        node = nodes.create.bdDbl_WeightedAverageMulti()
    modifier_manager.do_it_dg()

    assert node.NODE_TYPE == node_type
    assert node.input.long_name == "input"
    assert node.i.short_name == "i"
    assert node.input[2].value.long_name == "value"
    assert node.input[2].v.short_name == "v"
    assert node.input[2].weight.long_name == "weight"
    assert node.input[2].w.short_name == "w"
    assert node.input[2].weight.get() == pytest.approx(0.0)

    if node_type.startswith("bdDbl3_"):
        assert node.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))
        assert node.input[2].value.x.long_name == "valueX"
        assert node.input[2].value.z.short_name == "vz"
        assert node.output.outputZ.short_name == "oz"
    else:
        assert node.output.get() == pytest.approx(0.0)

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == type_id


def test_scalar_normalizes_sparse_inputs_and_removal(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_WeightedAverageMulti(name="weighted_average")
    node.input[2].value.set(10.0)
    node.input[2].weight.set(1.0)
    node.input[9].value.set(20.0)
    node.input[9].weight.set(3.0)
    node.input[20].value.set(100.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(17.5)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(10.0)


def test_double3_uses_one_weight_for_all_components(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_WeightedAverageMulti()
    node.input[2].value.set((2.0, 4.0, 6.0))
    node.input[2].weight.set(1.0)
    node.input[9].value.set((6.0, 12.0, 18.0))
    node.input[9].weight.set(3.0)
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((5.0, 10.0, 15.0))


@pytest.mark.parametrize(
    "node_type",
    ("bdDbl_WeightedAverageMulti", "bdDbl3_WeightedAverageMulti"),
)
def test_empty_and_exact_zero_weight_sum_return_zero(maya_cmds, node_type):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    if node_type.startswith("bdDbl3_"):
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (0.0, 0.0, 0.0)
        )
        maya_cmds.setAttr(
            f"{node}.input[2].value",
            2.0,
            4.0,
            6.0,
            type="double3",
        )
        maya_cmds.setAttr(f"{node}.input[2].weight", 1.0)
        maya_cmds.setAttr(
            f"{node}.input[9].value",
            10.0,
            20.0,
            30.0,
            type="double3",
        )
        maya_cmds.setAttr(f"{node}.input[9].weight", -1.0)
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (0.0, 0.0, 0.0)
        )
    else:
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)
        maya_cmds.setAttr(f"{node}.input[2].value", 2.0)
        maya_cmds.setAttr(f"{node}.input[2].weight", 1.0)
        maya_cmds.setAttr(f"{node}.input[9].value", 10.0)
        maya_cmds.setAttr(f"{node}.input[9].weight", -1.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)


def test_small_nonzero_weight_sum_is_not_treated_as_zero(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
    maya_cmds.setAttr(f"{node}.input[2].value", 10.0)
    maya_cmds.setAttr(f"{node}.input[2].weight", 1.0e-20)
    maya_cmds.setAttr(f"{node}.input[9].value", 20.0)
    maya_cmds.setAttr(f"{node}.input[9].weight", 2.0e-20)

    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(50.0 / 3.0)


def test_negative_weights_allow_extrapolation(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
    maya_cmds.setAttr(f"{node}.input[2].value", 10.0)
    maya_cmds.setAttr(f"{node}.input[2].weight", 2.0)
    maya_cmds.setAttr(f"{node}.input[9].value", 4.0)
    maya_cmds.setAttr(f"{node}.input[9].weight", -1.0)

    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(16.0)


@pytest.mark.parametrize("ignored_value", (float("nan"), float("inf")))
def test_zero_weight_completely_ignores_nonfinite_value(
    maya_cmds,
    ignored_value,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
    maya_cmds.setAttr(f"{node}.input[2].value", ignored_value)
    maya_cmds.setAttr(f"{node}.input[9].value", 8.0)
    maya_cmds.setAttr(f"{node}.input[9].weight", 2.0)

    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(8.0)


@pytest.mark.parametrize(
    ("value", "weight"),
    ((float("nan"), 1.0), (1.0, float("nan"))),
)
def test_nonzero_nan_input_propagates(maya_cmds, value, weight):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
    maya_cmds.setAttr(f"{node}.input[2].value", value)
    maya_cmds.setAttr(f"{node}.input[2].weight", weight)

    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


def test_simple_accumulation_uses_logical_index_order(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
    maya_cmds.setAttr(f"{node}.input[20].value", 1.0)
    maya_cmds.setAttr(f"{node}.input[20].weight", 1.0)
    maya_cmds.setAttr(f"{node}.input[9].value", -1.0e16)
    maya_cmds.setAttr(f"{node}.input[9].weight", 1.0)
    maya_cmds.setAttr(f"{node}.input[2].value", 1.0e16)
    maya_cmds.setAttr(f"{node}.input[2].weight", 1.0)

    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(1.0 / 3.0)


def test_simple_weighted_sum_uses_normal_overflow_behavior(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
    maya_cmds.setAttr(f"{node}.input[2].value", sys.float_info.max)
    maya_cmds.setAttr(f"{node}.input[2].weight", 2.0)

    assert math.isinf(maya_cmds.getAttr(f"{node}.output"))


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        scalar = maya_cmds.createNode("bdDbl_WeightedAverageMulti")
        maya_cmds.setAttr(f"{scalar}.input[2].value", 4.0)
        maya_cmds.setAttr(f"{scalar}.input[2].weight", 1.0)
        maya_cmds.setAttr(f"{scalar}.input[9].value", 10.0)
        maya_cmds.setAttr(f"{scalar}.input[9].weight", 1.0)
        assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(7.0)
        maya_cmds.setAttr(f"{scalar}.input[9].weight", 3.0)
        assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(8.5)

        vector = maya_cmds.createNode("bdDbl3_WeightedAverageMulti")
        maya_cmds.setAttr(
            f"{vector}.input[2].value",
            2.0,
            4.0,
            6.0,
            type="double3",
        )
        maya_cmds.setAttr(f"{vector}.input[2].weight", 1.0)
        assert maya_cmds.getAttr(f"{vector}.outputY") == pytest.approx(4.0)
        maya_cmds.setAttr(f"{vector}.input[2].valueY", 12.0)
        assert maya_cmds.getAttr(f"{vector}.outputY") == pytest.approx(12.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connections_existing_accessors_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl_Value(name="source")
    weighted = nodes.create.bdDbl_WeightedAverageMulti(name="weighted")
    source.value.set(6.0)
    source.value.connect(weighted.input[2].value)
    weighted.input[2].weight.set(1.0)
    weighted.input[9].value.set(10.0)
    weighted.input[9].weight.set(3.0)
    modifier_manager.do_it_dg()

    assert weighted.output.get() == pytest.approx(9.0)
    assert type(
        nodes.existing.bdDbl_WeightedAverageMulti(weighted.name)
    ) is type(weighted)

    scene_path = tmp_path / "bd_weighted_average.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded_nodes.existing.bdDbl_WeightedAverageMulti(
        "weighted"
    ).output.get() == pytest.approx(9.0)
