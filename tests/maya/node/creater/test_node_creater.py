# coding: utf-8
from __future__ import annotations

import pytest


def test_node_creater_uses_passed_modifier_manager(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater
    from bd_util.maya.node.modifier import ModifierManager
    from bd_util.maya.node.operator.node.dg.multiply_divide import MultiplyDivide
    from bd_util.maya.node.operator.node.dg.plus_minus_average import PlusMinusAverage

    modifier_manager = ModifierManager()
    node_creater = NodeCreater(modifier_manager=modifier_manager)

    pma = node_creater.plus_minus_average(name="plus_minus_ave")
    mult_div = node_creater.multiply_divide(name="mult_div")
    modifier_manager.do_it_dg()

    assert isinstance(pma, PlusMinusAverage)
    assert isinstance(mult_div, MultiplyDivide)
    assert pma.modifier_manager is modifier_manager
    assert mult_div.modifier_manager is modifier_manager
    assert maya_cmds.objExists("plus_minus_ave")
    assert maya_cmds.objExists("mult_div")


def test_node_creater_creates_modifier_manager(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()
    node = node_creater.plus_minus_average(name="auto_manager_pma")
    node_creater.modifier_manager.do_it_dg()

    assert node.modifier_manager is node_creater.modifier_manager
    assert maya_cmds.objExists("auto_manager_pma")


def test_node_creater_create_accepts_snake_and_maya_node_type(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    pma = node_creater.create("plus_minus_average", name="pma_snake")
    mult_div = node_creater.create("multiplyDivide", name="md_camel")
    node_creater.modifier_manager.do_it_dg()

    assert pma.NODE_TYPE == "plusMinusAverage"
    assert mult_div.NODE_TYPE == "multiplyDivide"
    assert maya_cmds.objExists("pma_snake")
    assert maya_cmds.objExists("md_camel")


def test_node_creater_caches_creator_and_node_class(new_scene):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    assert node_creater.plus_minus_average is node_creater.plus_minus_average
    assert node_creater.node_class("plus_minus_average") is node_creater.node_class(
        "plusMinusAverage"
    )


def test_node_creater_available_node_names_for_completion(new_scene):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    assert "plus_minus_average" in node_creater.available_node_names()
    assert "multiply_divide" in dir(node_creater)
    assert "and_" in dir(node_creater)


def test_node_creater_supports_keyword_node_name_alias(new_scene):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    assert node_creater.node_class("and_").NODE_TYPE == "and"
    assert node_creater.node_class("or_").NODE_TYPE == "or"
    assert node_creater.node_class("not_").NODE_TYPE == "not"


def test_node_creater_unknown_node_raises_attribute_error(new_scene):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    with pytest.raises(AttributeError):
        node_creater.not_existing_node()
