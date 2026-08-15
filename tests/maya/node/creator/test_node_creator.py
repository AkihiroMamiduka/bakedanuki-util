# coding: utf-8
from __future__ import annotations

import pytest


def test_node_creator_uses_passed_modifier_manager(new_scene, maya_cmds):
    from bd_util.maya.node.creator import NodeCreator
    from bd_util.maya.node.modifier import ModifierManager
    from bd_util.maya.node.operator.node.dg.multiply_divide import (
        MultiplyDivide,
    )
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    modifier_manager = ModifierManager()
    node_creator = NodeCreator(modifier_manager=modifier_manager)

    pma = node_creator.plusMinusAverage(name="plus_minus_ave")
    mult_div = node_creator.multiplyDivide(name="mult_div")
    modifier_manager.do_it_dg()

    assert isinstance(pma, PlusMinusAverage)
    assert isinstance(mult_div, MultiplyDivide)
    assert pma.modifier_manager is modifier_manager
    assert mult_div.modifier_manager is modifier_manager
    assert maya_cmds.objExists("plus_minus_ave")
    assert maya_cmds.objExists("mult_div")


def test_node_creator_creates_transform_nodes(new_scene, maya_cmds):
    from bd_util.maya.node.creator import NodeCreator
    from bd_util.maya.node.modifier import ModifierManager
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint

    modifier_manager = ModifierManager()
    node_creator = NodeCreator(modifier_manager=modifier_manager)

    transform = node_creator.transform(name="created_transform")
    joint = node_creator.joint(name="created_joint")
    modifier_manager.do_it_dag()

    assert isinstance(transform, Transform)
    assert isinstance(joint, Joint)
    assert transform.modifier_manager is modifier_manager
    assert joint.modifier_manager is modifier_manager
    assert maya_cmds.objExists("created_transform")
    assert maya_cmds.objExists("created_joint")


def test_node_creator_creates_modifier_manager(new_scene, maya_cmds):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()
    node = node_creator.plusMinusAverage(name="auto_manager_pma")
    node_creator.modifier_manager.do_it_dg()

    assert node.modifier_manager is node_creator.modifier_manager
    assert maya_cmds.objExists("auto_manager_pma")


def test_node_creator_create_accepts_snake_and_maya_node_type(
    new_scene, maya_cmds
):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()

    pma = node_creator.create("plus_minus_average", name="pma_snake")
    mult_div = node_creator.create("multiplyDivide", name="md_camel")
    transform = node_creator.create("transform", name="created_transform")
    joint = node_creator.create("joint", name="created_joint")
    node_creator.modifier_manager.do_it_dg()
    node_creator.modifier_manager.do_it_dag()

    assert pma.NODE_TYPE == "plusMinusAverage"
    assert mult_div.NODE_TYPE == "multiplyDivide"
    assert transform.NODE_TYPE == "transform"
    assert joint.NODE_TYPE == "joint"
    assert maya_cmds.objExists("pma_snake")
    assert maya_cmds.objExists("md_camel")
    assert maya_cmds.objExists("created_transform")
    assert maya_cmds.objExists("created_joint")


def test_node_creator_caches_creator_and_node_class(new_scene):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()
    creator = node_creator.plusMinusAverage

    assert node_creator.plusMinusAverage is creator
    assert node_creator.__dict__["plusMinusAverage"] is creator
    assert node_creator.node_class(
        "plus_minus_average"
    ) is node_creator.node_class("plusMinusAverage")


def test_node_creator_available_node_names_for_completion(new_scene):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()

    assert "plusMinusAverage" in node_creator.available_node_names()
    assert "transform" in node_creator.available_node_names()
    assert "joint" in node_creator.available_node_names()
    assert "mesh" in node_creator.available_node_names()
    assert {
        "camera",
        "locator",
        "mesh",
        "nurbsCurve",
        "nurbsSurface",
    }.issubset(node_creator.available_node_names())
    assert "ambientLight" not in node_creator.available_node_names()
    assert "aiStandIn" not in node_creator.available_node_names()
    assert "multiplyDivide" in dir(node_creator)
    assert "transform" in dir(node_creator)
    assert "joint" in dir(node_creator)
    assert "mesh" in dir(node_creator)
    assert "and_" in dir(node_creator)


def test_node_creator_creates_opted_in_shape(new_scene, maya_cmds):
    from bd_util.maya.node.creator import NodeCreator
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh

    node_creator = NodeCreator()
    parent = node_creator.transform(name="mesh_parent")
    mesh = node_creator.mesh(name="meshShape", parent=parent)
    node_creator.modifier_manager.do_it_dag()

    assert node_creator.node_class("mesh") is Mesh
    assert isinstance(mesh, Mesh)
    assert "mesh" in dir(node_creator)
    assert mesh.full_path == "|mesh_parent|meshShape"
    assert maya_cmds.nodeType(mesh.full_path) == "mesh"


def test_node_creator_shape_requires_parent(new_scene):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()

    with pytest.raises(TypeError, match="required keyword-only argument"):
        node_creator.mesh()
    with pytest.raises(TypeError, match="parent is required"):
        node_creator.create("mesh")


def test_node_creator_supports_keyword_node_name_alias(new_scene):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()

    assert node_creator.node_class("and_").NODE_TYPE == "and"
    assert node_creator.node_class("or_").NODE_TYPE == "or"
    assert node_creator.node_class("not_").NODE_TYPE == "not"


def test_node_creator_unknown_node_raises_attribute_error(new_scene):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()

    with pytest.raises(AttributeError):
        node_creator.not_existing_node()
    with pytest.raises(AttributeError):
        node_creator.ambientLight()
