# coding: utf-8
from __future__ import annotations

import pytest


def test_shape_common_attributes_are_generated_on_shape_base():
    from bd_util.maya.node.operator.node.dag.shape._generated.camera import (
        GeneratedCamera,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.locator import (
        GeneratedLocator,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.mesh import (
        GeneratedMesh,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.nurbs_curve import (
        GeneratedNurbsCurve,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.nurbs_surface import (
        GeneratedNurbsSurface,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.shape import (
        GeneratedShape,
    )

    assert "visibility" in vars(GeneratedShape)
    for node_cls in (
        GeneratedCamera,
        GeneratedLocator,
        GeneratedMesh,
        GeneratedNurbsCurve,
        GeneratedNurbsSurface,
    ):
        assert "visibility" not in vars(node_cls)
        assert node_cls.visibility.long_name == "visibility"


@pytest.mark.parametrize(
    ("node_type", "class_name"),
    (
        ("camera", "Camera"),
        ("locator", "Locator"),
        ("mesh", "Mesh"),
        ("nurbsCurve", "NurbsCurve"),
        ("nurbsSurface", "NurbsSurface"),
    ),
)
def test_nodes_create_opted_in_shape(
    new_scene,
    maya_cmds,
    node_type,
    class_name,
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name=f"{node_type}_parent")
    shape = getattr(nodes.create, node_type)(
        name=f"{node_type}Shape",
        parent=parent,
    )

    assert shape.full_path == ""
    mod.do_it_dag()

    assert type(shape).__name__ == class_name
    assert shape.modifier_manager is mod
    assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
    assert maya_cmds.nodeType(shape.full_path) == node_type
    assert maya_cmds.listRelatives(
        parent.full_path,
        shapes=True,
        fullPath=True,
    ) == [shape.full_path]
    assert shape.parent is not None
    assert shape.parent.m_obj == parent.m_obj


def test_nodes_create_shapes_in_one_modifier_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="shape_parent")
    shapes = [
        nodes.create.camera(name="cameraShape", parent=parent),
        nodes.create.locator(name="locatorShape", parent=parent),
        nodes.create.mesh(name="meshShape", parent=parent),
        nodes.create.nurbsCurve(name="curveShape", parent=parent),
        nodes.create.nurbsSurface(name="surfaceShape", parent=parent),
    ]

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    assert (
        maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        )
        == expected_paths
    )

    mod.undo_it()
    assert not maya_cmds.objExists("shape_parent")

    mod.redo_it()
    assert maya_cmds.objExists("shape_parent")
    assert [shape.full_path for shape in shapes] == expected_paths


def test_generic_create_supports_opted_in_shape(new_scene, maya_cmds):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.nurbs_surface import (
        NurbsSurface,
    )

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="surface_parent")
    surface = nodes.create.create(
        "nurbsSurface",
        name="surfaceShape",
        parent=parent,
    )
    nodes.modifier_manager.do_it_dag()

    assert isinstance(surface, NurbsSurface)
    assert surface.full_path == "|surface_parent|surfaceShape"
    assert maya_cmds.nodeType(surface.full_path) == "nurbsSurface"


def test_shape_parent_must_be_transform(new_scene):
    import bd_util as bdu

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="parent")
    mesh = nodes.create.mesh(name="meshShape", parent=parent)

    with pytest.raises(TypeError, match="parent must be a transform"):
        nodes.create.camera(name="cameraShape", parent=mesh)


def test_uncommitted_shape_parent_must_share_modifier_manager(new_scene):
    import bd_util as bdu

    first_nodes = bdu.Nodes()
    second_nodes = bdu.Nodes()
    parent = first_nodes.create.transform(name="parent")

    with pytest.raises(
        ValueError,
        match="must share the same ModifierManager",
    ):
        second_nodes.create.mesh(name="meshShape", parent=parent)


def test_abstract_shape_is_not_creatable(new_scene):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape._core import Shape

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="parent")

    with pytest.raises(AttributeError, match="Unsupported node type"):
        nodes.create.shape()
    with pytest.raises(AttributeError, match="Unsupported node type"):
        nodes.create.create("shape")
    with pytest.raises(TypeError, match="abstract NodeOperator base class"):
        Shape.create(nodes.modifier_manager, parent=parent)
