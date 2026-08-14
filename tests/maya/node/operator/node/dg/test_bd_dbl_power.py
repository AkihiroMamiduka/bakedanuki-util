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


def test_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_power import (
        BdDblPower,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_power_multi import (
        BdDblPowerMulti,
    )

    assert BdDblPower.NODE_TYPE == "bdDbl_Power"
    assert BdDblPower.input1.long_name == "input1"
    assert BdDblPower.i1.short_name == "i1"
    assert BdDblPower.input2.long_name == "input2"
    assert BdDblPower.i2.short_name == "i2"
    assert BdDblPower.output.long_name == "output"
    assert BdDblPower.o.short_name == "o"

    assert BdDblPowerMulti.NODE_TYPE == "bdDbl_PowerMulti"
    assert BdDblPowerMulti.input.long_name == "input"
    assert BdDblPowerMulti.i.short_name == "i"
    assert BdDblPowerMulti.output.long_name == "output"
    assert BdDblPowerMulti.o.short_name == "o"


def test_defaults_and_fixed_power(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Power()
    multi = nodes.create.bdDbl_PowerMulti()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDbl_Power1"
    assert multi.name == "bdDbl_PowerMulti1"
    assert fixed.input1.get() == pytest.approx(1.0)
    assert fixed.input2.get() == pytest.approx(1.0)
    assert fixed.output.get() == pytest.approx(1.0)
    assert multi.output.get() == pytest.approx(1.0)

    fixed.input1.set(2.0)
    fixed.input2.set(3.0)
    modifier_manager.do_it_dg()
    assert fixed.output.get() == pytest.approx(8.0)


@pytest.mark.parametrize(
    ("base", "exponent", "expected"),
    [
        (0.0, -1.0, 1.0e9),
        (0.0, -2.0, 1.0e18),
        (0.0, 0.0, 1.0),
        (0.0, 2.0, 0.0),
        (5.0e-10, -1.0, 1.0e9),
        (-5.0e-10, -1.0, -1.0e9),
        (1.0e-9, -1.0, 1.0e9),
        (-1.0e-9, -1.0, -1.0e9),
        (2.0e-9, -1.0, 5.0e8),
    ],
)
def test_fixed_clamps_small_bases_only_for_negative_exponents(
    maya_cmds,
    base,
    exponent,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Power")
    maya_cmds.setAttr(f"{node}.input1", base)
    maya_cmds.setAttr(f"{node}.input2", exponent)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)


def test_negative_base_with_non_integer_exponent_returns_nan(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Power")
    maya_cmds.setAttr(f"{node}.input1", -4.0)
    maya_cmds.setAttr(f"{node}.input2", 0.5)
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


def test_multi_uses_logical_index_order_and_defined_edge_cases(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_PowerMulti(name="pow")
    node.input[20].set(2.0)
    node.input[2].set(2.0)
    node.input[9].set(3.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(64.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get() == pytest.approx(9.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(2.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get() == pytest.approx(1.0)


def test_multi_clamps_current_base_only_for_negative_exponents(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_PowerMulti")
    maya_cmds.setAttr(f"{node}.input[2]", 0.0)
    maya_cmds.setAttr(f"{node}.input[9]", 2.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(0.0)

    maya_cmds.setAttr(f"{node}.input[9]", -1.0)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(1.0e9)

    maya_cmds.setAttr(f"{node}.input[2]", -5.0e-10)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(-1.0e9)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDbl_Power")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0)
        maya_cmds.setAttr(f"{fixed}.input2", 3.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(8.0)

        maya_cmds.setAttr(f"{fixed}.input2", -1.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(0.5)

        maya_cmds.setAttr(f"{fixed}.input1", 0.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(1.0e9)

        multi = maya_cmds.createNode("bdDbl_PowerMulti")
        maya_cmds.setAttr(f"{multi}.input[20]", 2.0)
        maya_cmds.setAttr(f"{multi}.input[2]", 2.0)
        maya_cmds.setAttr(f"{multi}.input[9]", 3.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(64.0)

        maya_cmds.setAttr(f"{multi}.input[9]", 2.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(16.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connection_and_existing_node_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_power import (
        BdDblPower,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_power_multi import (
        BdDblPowerMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Power(name="fixed")
    multi = nodes.create.bdDbl_PowerMulti(name="multi")
    fixed.input1.set(2.0)
    fixed.input2.set(3.0)
    fixed.output.connect(multi.input[2])
    multi.input[7].set(2.0)
    modifier_manager.do_it_dg()

    assert multi.output.get() == pytest.approx(64.0)
    assert isinstance(nodes.existing.bdDbl_Power(fixed.name), BdDblPower)
    assert isinstance(
        nodes.existing.bdDbl_PowerMulti(multi.name),
        BdDblPowerMulti,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Power(name="fixed")
    multi = nodes.create.bdDbl_PowerMulti(name="multi")
    fixed.input1.set(2.0)
    fixed.input2.set(3.0)
    multi.input[20].set(2.0)
    multi.input[2].set(2.0)
    multi.input[9].set(3.0)
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x00142693
    assert multi_fn.typeId.id() == 0x00142692

    scene_path = tmp_path / "bd_dbl_power.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl_Power(
        "fixed"
    ).output.get() == pytest.approx(8.0)
    assert existing_nodes.existing.bdDbl_PowerMulti(
        "multi"
    ).output.get() == pytest.approx(64.0)
