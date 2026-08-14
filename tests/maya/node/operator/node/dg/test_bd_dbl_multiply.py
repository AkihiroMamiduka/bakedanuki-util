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

    from bd_util.maya.node.operator.node.dg.bd_dbl_multiply import (
        BdDblMultiply,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_multiply_multi import (
        BdDblMultiplyMulti,
    )

    assert BdDblMultiply.NODE_TYPE == "bdDbl_Multiply"
    assert BdDblMultiply.input1.long_name == "input1"
    assert BdDblMultiply.i1.short_name == "i1"
    assert BdDblMultiply.input2.long_name == "input2"
    assert BdDblMultiply.i2.short_name == "i2"
    assert BdDblMultiply.output.long_name == "output"
    assert BdDblMultiply.o.short_name == "o"

    assert BdDblMultiplyMulti.NODE_TYPE == "bdDbl_MultiplyMulti"
    assert BdDblMultiplyMulti.input.long_name == "input"
    assert BdDblMultiplyMulti.i.short_name == "i"
    assert BdDblMultiplyMulti.output.long_name == "output"
    assert BdDblMultiplyMulti.o.short_name == "o"


def test_default_names_and_values(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Multiply()
    multi = nodes.create.bdDbl_MultiplyMulti()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDbl_Multiply1"
    assert multi.name == "bdDbl_MultiplyMulti1"
    assert fixed.input1.get() == pytest.approx(1.0)
    assert fixed.input2.get() == pytest.approx(1.0)
    assert fixed.output.get() == pytest.approx(1.0)
    assert multi.output.get() == pytest.approx(1.0)


def test_fixed_multiplies_two_inputs(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Multiply(name="mult")
    node.input1.set(-2.5)
    node.input2.set(4.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(-10.0)


def test_multi_multiplies_existing_sparse_elements(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_MultiplyMulti(name="mult")
    node.input[2].set(2.0)
    node.input[9].set(-3.0)
    node.input[20].set(0.5)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(-3.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(1.0)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDbl_Multiply")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0)
        maya_cmds.setAttr(f"{fixed}.input2", 5.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(10.0)

        maya_cmds.setAttr(f"{fixed}.input1", -4.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(-20.0)

        multi = maya_cmds.createNode("bdDbl_MultiplyMulti")
        maya_cmds.setAttr(f"{multi}.input[2]", 3.0)
        maya_cmds.setAttr(f"{multi}.input[9]", 7.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(21.0)

        maya_cmds.setAttr(f"{multi}.input[2]", 0.5)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(3.5)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_fixed_output_participates_in_multi_product(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Multiply(name="fixed")
    multi = nodes.create.bdDbl_MultiplyMulti(name="multi")
    fixed.input1.set(2.0)
    fixed.input2.set(5.0)
    fixed.output.connect(multi.input[2])
    multi.input[7].set(-0.5)
    modifier_manager.do_it_dg()

    assert multi.output.get() == pytest.approx(-5.0)


def test_existing_node_accessors_return_specific_wrappers(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_multiply import (
        BdDblMultiply,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_multiply_multi import (
        BdDblMultiplyMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Multiply(name="fixed")
    multi = nodes.create.bdDbl_MultiplyMulti(name="multi")
    modifier_manager.do_it_dg()

    assert isinstance(nodes.existing.bdDbl_Multiply(fixed.name), BdDblMultiply)
    assert isinstance(
        nodes.existing.bdDbl_MultiplyMulti(multi.name),
        BdDblMultiplyMulti,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Multiply(name="fixed")
    multi = nodes.create.bdDbl_MultiplyMulti(name="multi")
    fixed.input1.set(2.0)
    fixed.input2.set(5.0)
    multi.input[0].set(2.0)
    multi.input[5].set(5.0)
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x00142683
    assert multi_fn.typeId.id() == 0x00142682

    scene_path = tmp_path / "bd_dbl_multiply.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl_Multiply(
        "fixed"
    ).output.get() == pytest.approx(10.0)
    assert existing_nodes.existing.bdDbl_MultiplyMulti(
        "multi"
    ).output.get() == pytest.approx(10.0)
