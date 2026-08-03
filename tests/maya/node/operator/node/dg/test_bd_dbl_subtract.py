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

    from bd_util.maya.node.operator.node.dg.bd_dbl_subtract import (
        BdDblSubtract,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_subtract_multi import (
        BdDblSubtractMulti,
    )

    assert BdDblSubtract.NODE_TYPE == "bdDbl_Subtract"
    assert BdDblSubtract.input1.long_name == "input1"
    assert BdDblSubtract.i1.short_name == "i1"
    assert BdDblSubtract.input2.long_name == "input2"
    assert BdDblSubtract.i2.short_name == "i2"
    assert BdDblSubtract.output.long_name == "output"
    assert BdDblSubtract.o.short_name == "o"

    assert BdDblSubtractMulti.NODE_TYPE == "bdDbl_SubtractMulti"
    assert BdDblSubtractMulti.input.long_name == "input"
    assert BdDblSubtractMulti.i.short_name == "i"
    assert BdDblSubtractMulti.output.long_name == "output"
    assert BdDblSubtractMulti.o.short_name == "o"


def test_defaults_and_fixed_subtraction(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Subtract()
    multi = nodes.create.bdDbl_SubtractMulti()
    fixed.input1.set(10.0)
    fixed.input2.set(3.5)
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDbl_Subtract1"
    assert multi.name == "bdDbl_SubtractMulti1"
    assert fixed.output.get() == pytest.approx(6.5)
    assert multi.output.get() == pytest.approx(0.0)


def test_multi_uses_logical_index_order_and_defined_edge_cases(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_SubtractMulti(name="sub")
    node.input[20].set(1.0)
    node.input[2].set(20.0)
    node.input[9].set(3.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(16.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get() == pytest.approx(2.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(1.0)

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get() == pytest.approx(0.0)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDbl_Subtract")
        maya_cmds.setAttr(f"{fixed}.input1", 10.0)
        maya_cmds.setAttr(f"{fixed}.input2", 3.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(7.0)

        maya_cmds.setAttr(f"{fixed}.input2", 8.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(2.0)

        multi = maya_cmds.createNode("bdDbl_SubtractMulti")
        maya_cmds.setAttr(f"{multi}.input[20]", 1.0)
        maya_cmds.setAttr(f"{multi}.input[2]", 10.0)
        maya_cmds.setAttr(f"{multi}.input[9]", 3.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(6.0)

        maya_cmds.setAttr(f"{multi}.input[9]", 5.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(4.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connection_and_existing_node_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_subtract import (
        BdDblSubtract,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_subtract_multi import (
        BdDblSubtractMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Subtract(name="fixed")
    multi = nodes.create.bdDbl_SubtractMulti(name="multi")
    fixed.input1.set(10.0)
    fixed.input2.set(3.0)
    fixed.output.connect(multi.input[2])
    multi.input[7].set(2.0)
    modifier_manager.do_it_dg()

    assert multi.output.get() == pytest.approx(5.0)
    assert isinstance(nodes.existing.bdDbl_Subtract(fixed.name), BdDblSubtract)
    assert isinstance(
        nodes.existing.bdDbl_SubtractMulti(multi.name),
        BdDblSubtractMulti,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl_Subtract(name="fixed")
    multi = nodes.create.bdDbl_SubtractMulti(name="multi")
    fixed.input1.set(10.0)
    fixed.input2.set(3.0)
    multi.input[20].set(1.0)
    multi.input[2].set(10.0)
    multi.input[9].set(3.0)
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x0007F00C
    assert multi_fn.typeId.id() == 0x0007F00B

    scene_path = tmp_path / "bd_dbl_subtract.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl_Subtract(
        "fixed"
    ).output.get() == pytest.approx(7.0)
    assert existing_nodes.existing.bdDbl_SubtractMulti(
        "multi"
    ).output.get() == pytest.approx(6.0)
