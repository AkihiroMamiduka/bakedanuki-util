# coding: utf-8
from __future__ import annotations

import pytest


def test_shape_with_transform_creates_named_pair_and_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    from bd_util.maya.node.creator import NodeCreator
    from bd_util.maya.node.modifier import ModifierManager
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh
    from bd_util.maya.node.operator.node.dag.transform._core import Transform

    modifier_manager = ModifierManager()
    node_creator = NodeCreator(modifier_manager=modifier_manager)

    transform, mesh = node_creator.with_transform.mesh(name="mesh")

    assert isinstance(transform, Transform)
    assert isinstance(mesh, Mesh)
    assert transform.modifier_manager is modifier_manager
    assert mesh.modifier_manager is modifier_manager
    assert node_creator.with_transform.modifier_manager is modifier_manager

    modifier_manager.do_it_dag()

    assert transform.full_path == "|mesh"
    assert mesh.full_path == "|mesh|meshShape"
    assert maya_cmds.nodeType(mesh.full_path) == "mesh"
    assert mesh.parent is not None
    assert mesh.parent.m_obj == transform.m_obj

    modifier_manager.undo_it()
    assert not maya_cmds.objExists("mesh")

    modifier_manager.redo_it()
    assert transform.full_path == "|mesh"
    assert mesh.full_path == "|mesh|meshShape"


def test_shape_with_transform_accepts_parent_and_explicit_shape_name(
    new_scene,
    maya_cmds,
):
    from bd_util.maya.node.creator import NodeCreator
    from bd_util.maya.node.operator.node.dag.shape.camera import Camera

    node_creator = NodeCreator()
    group = node_creator.transform(name="group")
    transform, camera = node_creator.with_transform.camera(
        name="camera",
        shape_name="renderCameraShape",
        parent=group,
    )

    node_creator.modifier_manager.do_it_dag()

    assert isinstance(camera, Camera)
    assert transform.full_path == "|group|camera"
    assert camera.full_path == "|group|camera|renderCameraShape"
    assert maya_cmds.listRelatives(
        transform.full_path,
        shapes=True,
        fullPath=True,
    ) == [camera.full_path]


def test_shape_with_transform_supports_dynamic_create(new_scene, maya_cmds):
    from bd_util.maya.node.creator import NodeCreator
    from bd_util.maya.node.operator.node.dag.shape.nurbs_surface import (
        NurbsSurface,
    )

    node_creator = NodeCreator()
    transform, surface = node_creator.with_transform.create(
        "nurbsSurface",
        name="surface",
    )

    node_creator.modifier_manager.do_it_dag()

    assert isinstance(surface, NurbsSurface)
    assert transform.full_path == "|surface"
    assert surface.full_path == "|surface|surfaceShape"
    assert maya_cmds.nodeType(surface.full_path) == "nurbsSurface"


def test_shape_with_transform_exposes_only_creatable_shapes(new_scene):
    from bd_util.maya.node.creator import NodeCreator

    node_creator = NodeCreator()
    creator = node_creator.with_transform
    mesh_creator = creator.mesh

    assert node_creator.with_transform is creator
    assert creator.mesh is mesh_creator
    assert len(creator.available_node_names()) == 80
    assert "mesh" in creator.available_node_names()
    assert "nurbsSurface" in dir(creator)
    assert "plusMinusAverage" not in dir(creator)
    assert "SphereLocator" not in dir(creator)

    with pytest.raises(AttributeError, match="Unsupported shape node type"):
        creator.plusMinusAverage()
    with pytest.raises(AttributeError, match="Unsupported node type"):
        creator.SphereLocator()
