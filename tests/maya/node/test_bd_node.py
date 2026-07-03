# coding: utf-8
from __future__ import annotations

import pytest


def test_bd_node_wraps_existing_dg_node(new_scene, maya_cmds):
    import bd_util
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

    node = bd_util.BDNode("test_plus_minus_ave")

    assert isinstance(node, PlusMinusAverage)
    assert node.name == "test_plus_minus_ave"


def test_bd_node_can_edit_wrapped_node(new_scene, maya_cmds):
    import bd_util

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

    node = bd_util.BDNode("test_plus_minus_ave")
    node.input1D[0].set(10.0)
    node.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr("test_plus_minus_ave.input1D[0]") == 10.0


def test_bd_node_uses_passed_modifier_manager(new_scene, maya_cmds):
    import bd_util

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")
    modifier_manager = bd_util.ModifierManager()

    node = bd_util.BDNode(
        "test_plus_minus_ave",
        modifier_manager=modifier_manager,
    )

    assert node.modifier_manager is modifier_manager


def test_bd_node_wraps_m_object(new_scene, maya_cmds, maya_om):
    import bd_util
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")
    selection = maya_om.MSelectionList()
    selection.add("test_plus_minus_ave")
    m_obj = selection.getDependNode(0)

    node = bd_util.BDNode(m_obj)

    assert isinstance(node, PlusMinusAverage)
    assert node.name == "test_plus_minus_ave"


def test_bd_node_wraps_transform(new_scene, maya_cmds):
    import bd_util
    from bd_util.maya.node.operator.node.dag.transform._core import Transform

    maya_cmds.createNode("transform", name="test_transform")

    node = bd_util.BDNode("test_transform")

    assert isinstance(node, Transform)
    assert node.name == "test_transform"


def test_bd_node_wraps_joint(new_scene, maya_cmds):
    import bd_util
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint

    maya_cmds.createNode("joint", name="test_joint")

    node = bd_util.BDNode("test_joint")

    assert isinstance(node, Joint)
    assert node.NODE_TYPE == "joint"
    assert node.name == "test_joint"


def test_bd_node_unknown_node_raises_value_error(new_scene):
    import bd_util

    with pytest.raises(ValueError):
        bd_util.BDNode("not_existing_node")
