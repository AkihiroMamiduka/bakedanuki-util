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


def test_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_divide import (
        BdDblDivide,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_divide_multi import (
        BdDblDivideMulti,
    )

    assert BdDblDivide.NODE_TYPE == "bdDbl_Divide"
    assert BdDblDivide.input1.long_name == "input1"
    assert BdDblDivide.i1.short_name == "i1"
    assert BdDblDivide.input2.long_name == "input2"
    assert BdDblDivide.i2.short_name == "i2"
    assert BdDblDivide.output.long_name == "output"
    assert BdDblDivide.o.short_name == "o"

    assert BdDblDivideMulti.NODE_TYPE == "bdDbl_DivideMulti"
    assert BdDblDivideMulti.input.long_name == "input"
    assert BdDblDivideMulti.i.short_name == "i"
    assert BdDblDivideMulti.output.long_name == "output"
    assert BdDblDivideMulti.o.short_name == "o"


def test_defaults_and_fixed_division(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Divide()
    multi = nodes.create.bdDbl_DivideMulti()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDbl_Divide1"
    assert multi.name == "bdDbl_DivideMulti1"
    assert fixed.input1.get() == pytest.approx(1.0)
    assert fixed.input2.get() == pytest.approx(1.0)
    assert fixed.output.get() == pytest.approx(1.0)
    assert multi.output.get() == pytest.approx(1.0)

    fixed.input1.set(12.0)
    fixed.input2.set(3.0)
    modifier_manager.do_it_dg()
    assert fixed.output.get() == pytest.approx(4.0)


@pytest.mark.parametrize(
    ("numerator", "divisor", "expected"),
    [
        (1.0, 0.0, 1.0e9),
        (0.0, 0.0, 0.0),
        (1.0, 5.0e-10, 1.0e9),
        (1.0, -5.0e-10, -1.0e9),
        (1.0, 1.0e-9, 1.0e9),
        (1.0, -1.0e-9, -1.0e9),
        (1.0, 2.0e-9, 5.0e8),
    ],
)
def test_fixed_clamps_small_divisors_with_sign(
    maya_cmds,
    numerator,
    divisor,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Divide")
    maya_cmds.setAttr(f"{node}.input1", numerator)
    maya_cmds.setAttr(f"{node}.input2", divisor)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)


def test_multi_uses_logical_index_order_and_defined_edge_cases(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_DivideMulti(name="div")
    node.input[20].set(2.0)
    node.input[2].set(120.0)
    node.input[9].set(3.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(20.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get() == pytest.approx(1.5)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(2.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get() == pytest.approx(1.0)


def test_multi_clamps_only_divisor_elements(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_DivideMulti(name="div")
    node.input[2].set(1.0)
    node.input[9].set(0.0)
    node.input[20].set(-5.0e-10)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(-1.0e18)

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get() == pytest.approx(-0.0)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDbl_Divide")
        maya_cmds.setAttr(f"{fixed}.input1", 10.0)
        maya_cmds.setAttr(f"{fixed}.input2", 2.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(5.0)

        maya_cmds.setAttr(f"{fixed}.input2", 0.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(1.0e10)

        multi = maya_cmds.createNode("bdDbl_DivideMulti")
        maya_cmds.setAttr(f"{multi}.input[20]", 2.0)
        maya_cmds.setAttr(f"{multi}.input[2]", 120.0)
        maya_cmds.setAttr(f"{multi}.input[9]", 3.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(20.0)

        maya_cmds.setAttr(f"{multi}.input[9]", 0.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(6.0e10)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connection_and_existing_node_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_divide import (
        BdDblDivide,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_divide_multi import (
        BdDblDivideMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Divide(name="fixed")
    multi = nodes.create.bdDbl_DivideMulti(name="multi")
    fixed.input1.set(12.0)
    fixed.input2.set(3.0)
    fixed.output.connect(multi.input[2])
    multi.input[7].set(2.0)
    modifier_manager.do_it_dg()

    assert multi.output.get() == pytest.approx(2.0)
    assert isinstance(nodes.existing.bdDbl_Divide(fixed.name), BdDblDivide)
    assert isinstance(
        nodes.existing.bdDbl_DivideMulti(multi.name),
        BdDblDivideMulti,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Divide(name="fixed")
    multi = nodes.create.bdDbl_DivideMulti(name="multi")
    fixed.input1.set(12.0)
    fixed.input2.set(3.0)
    multi.input[20].set(2.0)
    multi.input[2].set(120.0)
    multi.input[9].set(3.0)
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x0014268F
    assert multi_fn.typeId.id() == 0x0014268E

    scene_path = tmp_path / "bd_dbl_divide.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl_Divide(
        "fixed"
    ).output.get() == pytest.approx(4.0)
    assert existing_nodes.existing.bdDbl_DivideMulti(
        "multi"
    ).output.get() == pytest.approx(20.0)
