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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_value import (
        BdDbl3Value,
    )

    assert BdDbl3Value.NODE_TYPE == "bdDbl3_Value"
    assert BdDbl3Value.value.long_name == "value"
    assert BdDbl3Value.v.short_name == "v"
    assert BdDbl3Value.valueX.long_name == "valueX"
    assert BdDbl3Value.vx.short_name == "vx"
    assert BdDbl3Value.valueY.long_name == "valueY"
    assert BdDbl3Value.vy.short_name == "vy"
    assert BdDbl3Value.valueZ.long_name == "valueZ"
    assert BdDbl3Value.vz.short_name == "vz"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Value()
    modifier_manager.do_it_dg()

    assert node.name == "bdDbl3_Value1"
    assert node.value.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))


def test_value_parent_and_children_are_editable(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Value")
    for attribute in ("value", "valueX", "valueY", "valueZ"):
        for flag in ("readable", "writable", "storable", "keyable"):
            assert maya_cmds.attributeQuery(
                attribute,
                node=node,
                **{flag: True},
            )

    maya_cmds.setAttr(f"{node}.value", 1.0, 2.0, 3.0, type="double3")
    assert maya_cmds.getAttr(f"{node}.value")[0] == pytest.approx(
        (1.0, 2.0, 3.0)
    )

    maya_cmds.setAttr(f"{node}.valueY", 5.0)
    assert maya_cmds.getAttr(f"{node}.value")[0] == pytest.approx(
        (1.0, 5.0, 3.0)
    )


def test_value_can_be_destination_and_source_in_the_same_network(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl3_Value(name="source")
    relay = nodes.create.bdDbl3_Value(name="relay")
    mult = nodes.create.bdDbl3_Multiply(name="mult")
    source.value.set((2.0, 3.0, 4.0))
    source.value.connect(relay.value)
    relay.value.connect(mult.input1)
    mult.input2.set((3.0, 4.0, 5.0))
    modifier_manager.do_it_dg()

    assert relay.value.get().as_tuple() == pytest.approx((2.0, 3.0, 4.0))
    assert mult.output.get().as_tuple() == pytest.approx((6.0, 12.0, 20.0))

    source.value.valueZ.set(6.0)
    modifier_manager.do_it_dg()
    assert relay.value.get().as_tuple() == pytest.approx((2.0, 3.0, 6.0))
    assert mult.output.get().as_tuple() == pytest.approx((6.0, 12.0, 30.0))


def test_child_value_can_drive_scalar_plug(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    value = nodes.create.bdDbl3_Value(name="value")
    mult = nodes.create.bdDbl_Multiply(name="mult")
    value.value.set((2.0, 3.0, 4.0))
    value.value.valueY.connect(mult.input1)
    mult.input2.set(5.0)
    modifier_manager.do_it_dg()

    assert mult.output.get() == pytest.approx(15.0)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_downstream_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        value = maya_cmds.createNode("bdDbl3_Value")
        mult = maya_cmds.createNode("bdDbl3_Multiply")
        maya_cmds.connectAttr(f"{value}.value", f"{mult}.input1")
        maya_cmds.setAttr(f"{mult}.input2", 2.0, 3.0, 4.0, type="double3")

        maya_cmds.setAttr(f"{value}.value", 3.0, 4.0, 5.0, type="double3")
        assert maya_cmds.getAttr(f"{mult}.output")[0] == pytest.approx(
            (6.0, 12.0, 20.0)
        )

        maya_cmds.setAttr(f"{value}.valueX", -2.0)
        assert maya_cmds.getAttr(f"{mult}.output")[0] == pytest.approx(
            (-4.0, 12.0, 20.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_existing_accessor_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_value import (
        BdDbl3Value,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Value(name="value")
    node.value.set((1.5, 2.5, 3.5))
    modifier_manager.do_it_dg()

    assert isinstance(nodes.existing.bdDbl3_Value(node.name), BdDbl3Value)

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F016

    scene_path = tmp_path / "bd_dbl3_value.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl3_Value(
        "value"
    ).value.get().as_tuple() == pytest.approx((1.5, 2.5, 3.5))
