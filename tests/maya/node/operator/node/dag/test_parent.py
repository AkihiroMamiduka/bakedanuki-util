# coding: utf-8
from __future__ import annotations

import pytest


def _world_matrix(maya_cmds, node: str) -> list[float]:
    return maya_cmds.xform(
        node,
        query=True,
        worldSpace=True,
        matrix=True,
    )


def test_transform_uses_generated_base_class():
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform._generated.transform import (
        GeneratedTransform,
    )

    assert Transform.__base__ is GeneratedTransform
    assert Transform.NODE_TYPE == "transform"
    assert "translate" not in vars(Transform)
    assert "translate" in vars(GeneratedTransform)
    assert Transform.translate.long_name == "translate"


def test_parent_and_parents_return_shared_manager_operators(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent_name = maya_cmds.createNode("transform", name="parent")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=parent_name,
    )
    nodes = bdu.Nodes()
    parent = nodes.existing.transform(parent_name)
    child = nodes.existing.transform(child_name)

    resolved_parent = child.parent

    assert resolved_parent is not None
    assert resolved_parent.m_obj == parent.m_obj
    assert resolved_parent.modifier_manager is nodes.modifier_manager
    assert len(child.parents) == 1
    assert child.parents[0].m_obj == parent.m_obj
    assert parent.parent is None
    assert parent.parents == ()
    assert child.is_instanced is False


def test_parent_rejects_instanced_dag_node(new_scene, maya_cmds):
    import bd_util as bdu

    parent_a = maya_cmds.createNode("transform", name="parent_a")
    parent_b = maya_cmds.createNode("transform", name="parent_b")
    new_parent_name = maya_cmds.createNode("transform", name="new_parent")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=parent_a,
    )
    maya_cmds.parent(child_name, parent_b, addObject=True)
    child_path = maya_cmds.ls(child_name, long=True, allPaths=True)[0]
    nodes = bdu.Nodes()
    child = nodes.existing.transform(child_path)
    new_parent = nodes.existing.transform(new_parent_name)

    assert child.is_instanced is True
    assert {parent.name for parent in child.parents} == {
        parent_a,
        parent_b,
    }
    with pytest.raises(RuntimeError, match="parent is ambiguous"):
        _ = child.parent
    with pytest.raises(RuntimeError, match="set_parent is not supported"):
        child.set_parent(new_parent)
    with pytest.raises(
        RuntimeError,
        match="set_parent_to_world is not supported",
    ):
        child.set_parent_to_world()
    with pytest.raises(RuntimeError, match="cannot be used as parent"):
        new_parent.set_parent(child)


def test_set_parent_preserves_local_transform_and_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent_name = maya_cmds.createNode("transform", name="parent")
    child_name = maya_cmds.createNode("transform", name="child")
    maya_cmds.setAttr(f"{parent_name}.translateX", 10.0)
    maya_cmds.setAttr(f"{child_name}.translateX", 2.0)
    nodes = bdu.Nodes()
    parent = nodes.existing.transform(parent_name)
    child = nodes.existing.transform(child_name)
    assert child.full_path == "|child"

    assert child.set_parent(parent) is child
    nodes.modifier_manager.do_it_dag()

    assert child.full_path == "|parent|child"
    assert maya_cmds.getAttr(f"{child_name}.translateX") == pytest.approx(2.0)
    assert maya_cmds.xform(
        child_name,
        query=True,
        worldSpace=True,
        translation=True,
    ) == pytest.approx([12.0, 0.0, 0.0])

    nodes.modifier_manager.undo_it()
    assert child.full_path == "|child"

    nodes.modifier_manager.redo_it()
    assert child.full_path == "|parent|child"


def test_transform_set_parent_can_preserve_world_transform(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent_name = maya_cmds.createNode("transform", name="parent")
    child_name = maya_cmds.createNode("transform", name="child")
    maya_cmds.setAttr(f"{parent_name}.translateX", 10.0)
    maya_cmds.setAttr(f"{child_name}.translateX", 2.0)
    expected_world = _world_matrix(maya_cmds, child_name)
    nodes = bdu.Nodes()
    parent = nodes.existing.transform(parent_name)
    child = nodes.existing.transform(child_name)

    assert (
        child.set_parent(
            parent,
            preserve_world_transform=True,
        )
        is child
    )
    nodes.modifier_manager.do_it_dag()

    assert child.full_path == "|parent|child"
    assert _world_matrix(maya_cmds, child_name) == pytest.approx(
        expected_world
    )
    assert maya_cmds.getAttr(f"{child_name}.translateX") == pytest.approx(-8.0)

    nodes.modifier_manager.undo_it()
    assert child.full_path == "|child"
    assert _world_matrix(maya_cmds, child_name) == pytest.approx(
        expected_world
    )

    nodes.modifier_manager.redo_it()
    assert child.full_path == "|parent|child"
    assert _world_matrix(maya_cmds, child_name) == pytest.approx(
        expected_world
    )


@pytest.mark.parametrize(
    ("preserve_world_transform", "expected_world_x"),
    (
        (False, 2.0),
        (True, 12.0),
    ),
)
def test_transform_set_parent_to_world(
    new_scene,
    maya_cmds,
    preserve_world_transform,
    expected_world_x,
):
    import bd_util as bdu

    parent_name = maya_cmds.createNode("transform", name="parent")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=parent_name,
    )
    maya_cmds.setAttr(f"{parent_name}.translateX", 10.0)
    maya_cmds.setAttr(f"{child_name}.translateX", 2.0)
    nodes = bdu.Nodes()
    child = nodes.existing.transform(child_name)

    assert (
        child.set_parent_to_world(
            preserve_world_transform=preserve_world_transform,
        )
        is child
    )
    nodes.modifier_manager.do_it_dag()

    assert child.parent is None
    assert child.full_path == "|child"
    assert maya_cmds.xform(
        child_name,
        query=True,
        worldSpace=True,
        translation=True,
    ) == pytest.approx([expected_world_x, 0.0, 0.0])

    nodes.modifier_manager.undo_it()
    assert child.full_path == "|parent|child"

    nodes.modifier_manager.redo_it()
    assert child.full_path == "|child"
    assert maya_cmds.xform(
        child_name,
        query=True,
        worldSpace=True,
        translation=True,
    ) == pytest.approx([expected_world_x, 0.0, 0.0])


def test_create_accepts_parent_and_full_path_is_not_cached(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="parent")
    child = nodes.create.transform(name="child", parent=parent)
    generic_child = nodes.create.create(
        "transform",
        name="generic_child",
        parent=parent,
    )

    assert child.full_path == ""
    mod.do_it_dag()

    assert child.full_path == "|parent|child"
    assert generic_child.full_path == "|parent|generic_child"
    assert child.parent is not None
    assert child.parent.m_obj == parent.m_obj
    assert maya_cmds.listRelatives(child.name, parent=True) == [parent.name]


def test_dag_create_accepts_parent_for_shape(new_scene, maya_cmds):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="parent")
    shape = Mesh.create(
        mod,
        name="meshShape",
        parent=parent,
    )

    mod.do_it_dag()

    assert isinstance(shape, Mesh)
    assert shape.full_path == "|parent|meshShape"
    assert maya_cmds.nodeType(shape.full_path) == "mesh"
    assert shape.parent is not None
    assert shape.parent.m_obj == parent.m_obj


def test_preserve_world_transform_supports_uncommitted_parent(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    child_name = maya_cmds.createNode("transform", name="child")
    maya_cmds.setAttr(f"{child_name}.translate", 1.0, 2.0, 3.0)
    expected_world = _world_matrix(maya_cmds, child_name)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="parent")
    child = nodes.existing.transform(child_name)

    child.set_parent(parent, preserve_world_transform=True)
    mod.do_it_dag()

    assert child.full_path == "|parent|child"
    assert _world_matrix(maya_cmds, child_name) == pytest.approx(
        expected_world
    )


def test_full_path_follows_rename_undo_and_redo(new_scene, maya_cmds):
    import bd_util as bdu

    parent_name = maya_cmds.createNode("transform", name="parent")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=parent_name,
    )
    nodes = bdu.Nodes()
    child = nodes.existing.transform(child_name)
    assert child.full_path == "|parent|child"

    child.rename(new_name="renamed")
    nodes.modifier_manager.do_it_dg()

    assert child.full_path == "|parent|renamed"

    nodes.modifier_manager.undo_it()
    assert child.full_path == "|parent|child"

    nodes.modifier_manager.redo_it()
    assert child.full_path == "|parent|renamed"


def test_create_rejects_parent_for_dg_node(new_scene):
    import bd_util as bdu

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="parent")

    with pytest.raises(TypeError, match="only supported for DAG nodes"):
        nodes.create.create("multiplyDivide", parent=parent)


@pytest.mark.parametrize("preserve_world_transform", (False, True))
def test_set_parent_rejects_descendant(
    new_scene,
    maya_cmds,
    preserve_world_transform,
):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=root_name,
    )
    descendant_name = maya_cmds.createNode(
        "transform",
        name="descendant",
        parent=child_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    descendant = nodes.existing.transform(descendant_name)

    with pytest.raises(ValueError, match="parented to its descendant"):
        root.set_parent(
            descendant,
            preserve_world_transform=preserve_world_transform,
        )


@pytest.mark.parametrize("preserve_world_transform", (False, True))
def test_set_parent_rejects_uncommitted_descendant(
    new_scene,
    preserve_world_transform,
):
    import bd_util as bdu

    nodes = bdu.Nodes()
    root = nodes.create.transform(name="test1")
    child = nodes.create.transform(name="test2", parent=root)
    descendant = nodes.create.transform(name="test3", parent=child)

    with pytest.raises(ValueError, match="parented to its descendant"):
        root.set_parent(
            child,
            preserve_world_transform=preserve_world_transform,
        )

    nodes.modifier_manager.do_it_dag()

    assert root.full_path == "|test1"
    assert child.full_path == "|test1|test2"
    assert descendant.full_path == "|test1|test2|test3"


def test_set_parent_rejects_cycle_from_pending_reparent(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    first_name = maya_cmds.createNode("transform", name="first")
    second_name = maya_cmds.createNode("transform", name="second")
    nodes = bdu.Nodes()
    first = nodes.existing.transform(first_name)
    second = nodes.existing.transform(second_name)

    first.set_parent(second)
    with pytest.raises(ValueError, match="parented to its descendant"):
        second.set_parent(first)

    nodes.modifier_manager.do_it_dag()

    assert first.full_path == "|second|first"
    assert second.full_path == "|second"


def test_pending_world_parent_replaces_current_parent_for_cycle_check(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=root_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    child = nodes.existing.transform(child_name)

    child.set_parent_to_world()
    root.set_parent(child)
    nodes.modifier_manager.do_it_dag()

    assert child.full_path == "|child"
    assert root.full_path == "|child|root"


def test_parent_must_be_transform_dag_node(new_scene, maya_cmds):
    import bd_util as bdu

    transform_name, _ = maya_cmds.polyCube(name="cube")
    shape_name = maya_cmds.listRelatives(transform_name, shapes=True)[0]
    child_name = maya_cmds.createNode("transform", name="child")
    nodes = bdu.Nodes()
    shape = nodes.existing.mesh(shape_name)
    child = nodes.existing.transform(child_name)

    with pytest.raises(TypeError, match="parent must be a transform DAG node"):
        child.set_parent(shape)
    assert not hasattr(shape, "set_parent_to_world")


def test_uncommitted_parent_must_share_modifier_manager(new_scene):
    import bd_util as bdu

    first_nodes = bdu.Nodes()
    second_nodes = bdu.Nodes()
    parent = first_nodes.create.transform(name="parent")

    with pytest.raises(
        ValueError, match="must share the same ModifierManager"
    ):
        second_nodes.create.transform(name="child", parent=parent)
