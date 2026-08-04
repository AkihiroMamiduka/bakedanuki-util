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


def test_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_average import (
        BdDbl3Average,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl3_average_multi import (
        BdDbl3AverageMulti,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_average import BdDblAverage
    from bd_util.maya.node.operator.node.dg.bd_dbl_average_multi import (
        BdDblAverageMulti,
    )

    assert BdDblAverage.NODE_TYPE == "bdDbl_Average"
    assert BdDblAverage.input1.long_name == "input1"
    assert BdDblAverage.i1.short_name == "i1"
    assert BdDblAverage.input2.long_name == "input2"
    assert BdDblAverage.o.short_name == "o"

    assert BdDblAverageMulti.NODE_TYPE == "bdDbl_AverageMulti"
    assert BdDblAverageMulti.input.long_name == "input"
    assert BdDblAverageMulti.i.short_name == "i"

    assert BdDbl3Average.NODE_TYPE == "bdDbl3_Average"
    assert BdDbl3Average.input1.input1X.short_name == "i1x"
    assert BdDbl3Average.input2.input2Z.long_name == "input2Z"
    assert BdDbl3Average.output.outputY.short_name == "oy"

    assert BdDbl3AverageMulti.NODE_TYPE == "bdDbl3_AverageMulti"
    assert BdDbl3AverageMulti.input.inputX.short_name == "ix"
    assert BdDbl3AverageMulti.output.outputZ.short_name == "oz"


@pytest.mark.parametrize(
    ("node_type", "type_id"),
    (
        ("bdDbl3_AverageMulti", 0x0007F02F),
        ("bdDbl3_Average", 0x0007F030),
        ("bdDbl_AverageMulti", 0x0007F031),
        ("bdDbl_Average", 0x0007F032),
    ),
)
def test_defaults_and_type_ids(maya_cmds, maya_om, node_type, type_id):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == type_id

    if node_type.startswith("bdDbl3_"):
        assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
            (0.0, 0.0, 0.0)
        )
    else:
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)


def test_fixed_scalar_returns_arithmetic_mean(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Average()
    node.input1.set(-2.0)
    node.input2.set(8.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(3.0)


def test_fixed_double3_averages_each_component(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Average()
    node.input1.set((-2.0, 4.0, 10.0))
    node.input2.set((8.0, -2.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((3.0, 1.0, 6.0))


def test_multi_empty_is_zero_and_single_element_is_unchanged(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDbl_AverageMulti()
    vector = nodes.create.bdDbl3_AverageMulti()
    modifier_manager.do_it_dg()

    assert scalar.output.get() == pytest.approx(0.0)
    assert vector.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))

    maya_cmds.setAttr(f"{scalar.name}.input[8]", -3.5)
    maya_cmds.setAttr(
        f"{vector.name}.input[8]",
        -3.5,
        2.0,
        7.0,
        type="double3",
    )
    assert scalar.output.get() == pytest.approx(-3.5)
    assert vector.output.get().as_tuple() == pytest.approx((-3.5, 2.0, 7.0))


def test_multi_counts_only_existing_sparse_elements(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_AverageMulti()
    node.input[2].set(2.0)
    node.input[9].set(4.0)
    node.input[20].set(12.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(6.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(7.0)


def test_multi_accumulates_in_logical_index_order(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_AverageMulti")
    maya_cmds.setAttr(f"{node}.input[20]", 1.0)
    maya_cmds.setAttr(f"{node}.input[9]", -1.0e16)
    maya_cmds.setAttr(f"{node}.input[2]", 1.0e16)

    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(1.0 / 3.0)


def test_double3_multi_averages_each_component(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_AverageMulti()
    node.input[2].set((1.0, 10.0, -1.0))
    node.input[9].set((3.0, 20.0, 1.0))
    node.input[20].set((8.0, 30.0, 6.0))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((4.0, 20.0, 2.0))


def test_simple_sum_uses_normal_overflow_behavior(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    fixed = maya_cmds.createNode("bdDbl_Average")
    maya_cmds.setAttr(f"{fixed}.input1", sys.float_info.max)
    maya_cmds.setAttr(f"{fixed}.input2", sys.float_info.max)
    assert math.isinf(maya_cmds.getAttr(f"{fixed}.output"))

    multi = maya_cmds.createNode("bdDbl_AverageMulti")
    maya_cmds.setAttr(f"{multi}.input[2]", sys.float_info.max)
    maya_cmds.setAttr(f"{multi}.input[9]", sys.float_info.max)
    assert math.isinf(maya_cmds.getAttr(f"{multi}.output"))


@pytest.mark.parametrize("node_type", ("bdDbl_Average", "bdDbl_AverageMulti"))
def test_nan_propagates(maya_cmds, node_type):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    if node_type.endswith("Multi"):
        maya_cmds.setAttr(f"{node}.input[2]", 1.0)
        maya_cmds.setAttr(f"{node}.input[9]", float("nan"))
    else:
        maya_cmds.setAttr(f"{node}.input1", 1.0)
        maya_cmds.setAttr(f"{node}.input2", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


def test_opposite_infinities_return_nan(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_AverageMulti")
    maya_cmds.setAttr(f"{node}.input[2]", float("inf"))
    maya_cmds.setAttr(f"{node}.input[9]", float("-inf"))
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDbl_Average")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0)
        maya_cmds.setAttr(f"{fixed}.input2", 6.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(4.0)
        maya_cmds.setAttr(f"{fixed}.input2", 10.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(6.0)

        multi = maya_cmds.createNode("bdDbl3_AverageMulti")
        maya_cmds.setAttr(
            f"{multi}.input[2]",
            2.0,
            4.0,
            6.0,
            type="double3",
        )
        maya_cmds.setAttr(
            f"{multi}.input[9]",
            4.0,
            8.0,
            12.0,
            type="double3",
        )
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (3.0, 6.0, 9.0)
        )
        maya_cmds.setAttr(f"{multi}.input[9].inputY", 12.0)
        assert maya_cmds.getAttr(f"{multi}.outputY") == pytest.approx(8.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connections_existing_accessors_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Average(name="fixed")
    multi = nodes.create.bdDbl_AverageMulti(name="multi")
    fixed.input1.set(2.0)
    fixed.input2.set(6.0)
    fixed.output.connect(multi.input[2])
    multi.input[9].set(8.0)
    modifier_manager.do_it_dg()

    assert multi.output.get() == pytest.approx(6.0)
    assert type(nodes.existing.bdDbl_Average(fixed.name)) is type(fixed)
    assert type(nodes.existing.bdDbl_AverageMulti(multi.name)) is type(multi)

    scene_path = tmp_path / "bd_average.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded_nodes.existing.bdDbl_AverageMulti(
        "multi"
    ).output.get() == pytest.approx(6.0)
