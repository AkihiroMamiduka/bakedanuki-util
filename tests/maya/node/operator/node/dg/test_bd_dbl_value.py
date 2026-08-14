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


def test_class_attribute_access_and_default(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_value import (
        BdDblValue,
    )

    assert BdDblValue.NODE_TYPE == "bdDbl_Value"
    assert BdDblValue.value.long_name == "value"
    assert BdDblValue.v.short_name == "v"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Value()
    modifier_manager.do_it_dg()

    assert node.name == "bdDbl_Value1"
    assert node.value.get() == pytest.approx(0.0)


def test_value_is_readable_writable_storable_and_keyable(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Value")
    for flag in ("readable", "writable", "storable", "keyable"):
        assert maya_cmds.attributeQuery(
            "value",
            node=node,
            **{flag: True},
        )

    maya_cmds.setAttr(f"{node}.value", 2.5)
    assert maya_cmds.getAttr(f"{node}.value") == pytest.approx(2.5)


def test_value_can_be_destination_and_source_in_the_same_network(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl_Value(name="source")
    relay = nodes.create.bdDbl_Value(name="relay")
    mult = nodes.create.bdDbl_Multiply(name="mult")
    source.value.set(3.0)
    source.value.connect(relay.value)
    relay.value.connect(mult.input1)
    mult.input2.set(4.0)
    modifier_manager.do_it_dg()

    assert relay.value.get() == pytest.approx(3.0)
    assert mult.output.get() == pytest.approx(12.0)

    source.value.set(5.0)
    modifier_manager.do_it_dg()
    assert relay.value.get() == pytest.approx(5.0)
    assert mult.output.get() == pytest.approx(20.0)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_downstream_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        value = maya_cmds.createNode("bdDbl_Value")
        mult = maya_cmds.createNode("bdDbl_Multiply")
        maya_cmds.connectAttr(f"{value}.value", f"{mult}.input1")
        maya_cmds.setAttr(f"{mult}.input2", 2.0)

        maya_cmds.setAttr(f"{value}.value", 3.0)
        assert maya_cmds.getAttr(f"{mult}.output") == pytest.approx(6.0)

        maya_cmds.setAttr(f"{value}.value", -4.0)
        assert maya_cmds.getAttr(f"{mult}.output") == pytest.approx(-8.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_value_can_drive_animation(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    value = maya_cmds.createNode("bdDbl_Value")
    mult = maya_cmds.createNode("bdDbl_Multiply")
    maya_cmds.connectAttr(f"{value}.value", f"{mult}.input1")
    maya_cmds.setAttr(f"{mult}.input2", 3.0)
    maya_cmds.setKeyframe(value, attribute="value", time=1.0, value=2.0)
    maya_cmds.setKeyframe(value, attribute="value", time=2.0, value=4.0)

    maya_cmds.currentTime(1.0)
    assert maya_cmds.getAttr(f"{mult}.output") == pytest.approx(6.0)
    maya_cmds.currentTime(2.0)
    assert maya_cmds.getAttr(f"{mult}.output") == pytest.approx(12.0)


def test_existing_accessor_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_value import (
        BdDblValue,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Value(name="value")
    node.value.set(7.5)
    modifier_manager.do_it_dg()

    assert isinstance(nodes.existing.bdDbl_Value(node.name), BdDblValue)

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142694

    scene_path = tmp_path / "bd_dbl_value.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl_Value(
        "value"
    ).value.get() == pytest.approx(7.5)
