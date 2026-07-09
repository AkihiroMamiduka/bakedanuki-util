# coding: utf-8
from __future__ import annotations

import pytest


def test_node_creater_can_import_from_bd_util(new_scene):
    from bd_util import ModifierManager, NodeCreater

    modifier_manager = ModifierManager()
    node_creater = NodeCreater(modifier_manager=modifier_manager)

    assert node_creater.modifier_manager is modifier_manager


def test_node_creater_uses_passed_modifier_manager(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater
    from bd_util.maya.node.modifier import ModifierManager
    from bd_util.maya.node.operator.node.dg.multiply_divide import MultiplyDivide
    from bd_util.maya.node.operator.node.dg.plus_minus_average import PlusMinusAverage

    modifier_manager = ModifierManager()
    node_creater = NodeCreater(modifier_manager=modifier_manager)

    pma = node_creater.plusMinusAverage(name="plus_minus_ave")
    mult_div = node_creater.multiplyDivide(name="mult_div")
    modifier_manager.do_it_dg()

    assert isinstance(pma, PlusMinusAverage)
    assert isinstance(mult_div, MultiplyDivide)
    assert pma.modifier_manager is modifier_manager
    assert mult_div.modifier_manager is modifier_manager
    assert maya_cmds.objExists("plus_minus_ave")
    assert maya_cmds.objExists("mult_div")


def test_node_creater_creates_transform_nodes(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater
    from bd_util.maya.node.modifier import ModifierManager
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint

    modifier_manager = ModifierManager()
    node_creater = NodeCreater(modifier_manager=modifier_manager)

    transform = node_creater.transform(name="created_transform")
    joint = node_creater.joint(name="created_joint")
    modifier_manager.do_it_dag()

    assert isinstance(transform, Transform)
    assert isinstance(joint, Joint)
    assert transform.modifier_manager is modifier_manager
    assert joint.modifier_manager is modifier_manager
    assert maya_cmds.objExists("created_transform")
    assert maya_cmds.objExists("created_joint")


def test_node_creater_creates_modifier_manager(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()
    node = node_creater.plusMinusAverage(name="auto_manager_pma")
    node_creater.modifier_manager.do_it_dg()

    assert node.modifier_manager is node_creater.modifier_manager
    assert maya_cmds.objExists("auto_manager_pma")


def test_node_creater_create_accepts_snake_and_maya_node_type(new_scene, maya_cmds):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    pma = node_creater.create("plus_minus_average", name="pma_snake")
    mult_div = node_creater.create("multiplyDivide", name="md_camel")
    transform = node_creater.create("transform", name="created_transform")
    joint = node_creater.create("joint", name="created_joint")
    node_creater.modifier_manager.do_it_dg()
    node_creater.modifier_manager.do_it_dag()

    assert pma.NODE_TYPE == "plusMinusAverage"
    assert mult_div.NODE_TYPE == "multiplyDivide"
    assert transform.NODE_TYPE == "transform"
    assert joint.NODE_TYPE == "joint"
    assert maya_cmds.objExists("pma_snake")
    assert maya_cmds.objExists("md_camel")
    assert maya_cmds.objExists("created_transform")
    assert maya_cmds.objExists("created_joint")


def test_node_creater_caches_creator_and_node_class(new_scene):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    assert node_creater.plusMinusAverage is node_creater.plusMinusAverage
    assert node_creater.node_class("plus_minus_average") is node_creater.node_class(
        "plusMinusAverage"
    )


def test_node_creater_available_node_names_for_completion(new_scene):
    from bd_util.maya.node.creater import NodeCreater

    node_creater = NodeCreater()

    assert "plusMinusAverage" in node_creater.available_node_names()
    assert "transform" in node_creater.available_node_names()
    assert "joint" in node_creater.available_node_names()
    assert "mesh" not in node_creater.available_node_names()
    assert "multiplyDivide" in dir(node_creater)
    assert "transform" in dir(node_creater)
    assert "joint" in dir(node_creater)
    assert "and_" in dir(node_creater)


def test_node_creater_resolves_shape_class_without_creator(new_scene):
    from bd_util.maya.node.creater import NodeCreater
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh

    node_creater = NodeCreater()

    assert node_creater.node_class("mesh") is Mesh
    assert "mesh" not in dir(node_creater)
    with pytest.raises(AttributeError):
        node_creater.mesh()


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
