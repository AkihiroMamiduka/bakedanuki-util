# coding: utf-8
from __future__ import annotations


def test_children_returns_direct_concrete_nodes_in_child_index_order(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint
    from bd_util.maya.node.operator.node.dag.unknown_dag import UnknownDag

    root_name = maya_cmds.createNode("transform", name="root")
    joint_name = maya_cmds.createNode(
        "joint",
        name="joint_child",
        parent=root_name,
    )
    maya_cmds.createNode(
        "transform",
        name="grandchild",
        parent=joint_name,
    )
    maya_cmds.createNode(
        "mesh",
        name="meshShape",
        parent=root_name,
    )
    maya_cmds.createNode(
        "unknownDag",
        name="unknown_child",
        parent=root_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    children = root.children()

    assert tuple(type(child) for child in children) == (
        Joint,
        Mesh,
        UnknownDag,
    )
    assert tuple(child.full_path for child in children) == (
        "|root|joint_child",
        "|root|meshShape",
        "|root|unknown_child",
    )
    assert all(
        child.modifier_manager is nodes.modifier_manager for child in children
    )
    assert all(child.m_obj != root.m_obj for child in children)
    assert all(child.name != "grandchild" for child in children)


def test_children_reads_executed_scene_state_without_cache(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    old_parent_name = maya_cmds.createNode(
        "transform",
        name="old_parent",
    )
    reparented_name = maya_cmds.createNode(
        "transform",
        name="reparented_child",
        parent=old_parent_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    pending_child = nodes.create.transform(
        name="pending_child",
        parent=root,
    )
    reparented_child = nodes.existing.transform(reparented_name)
    reparented_child.set_parent(root)

    assert root.children() == ()

    nodes.modifier_manager.do_it_dag()

    first_result = root.children()
    assert len(first_result) == 2
    assert first_result[0].m_obj == pending_child.m_obj
    assert first_result[1].m_obj == reparented_child.m_obj

    maya_cmds.createNode(
        "joint",
        name="external_child",
        parent=root_name,
    )

    second_result = root.children()
    assert tuple(child.name for child in second_result) == (
        "pending_child",
        "reparented_child",
        "external_child",
    )
    assert second_result is not first_result


def test_children_supports_instanced_child_with_mobject_semantics(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent_a_name = maya_cmds.createNode("transform", name="parent_a")
    parent_b_name = maya_cmds.createNode("transform", name="parent_b")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=parent_a_name,
    )
    maya_cmds.parent(child_name, parent_b_name, addObject=True)
    nodes = bdu.Nodes()
    parent_a = nodes.existing.transform(parent_a_name)
    parent_b = nodes.existing.transform(parent_b_name)

    child_from_a = parent_a.children()[0]
    child_from_b = parent_b.children()[0]

    assert child_from_a.m_obj == child_from_b.m_obj
    assert child_from_a.is_instanced is True
    assert child_from_b.is_instanced is True
    assert child_from_a.modifier_manager is nodes.modifier_manager
    assert child_from_b.modifier_manager is nodes.modifier_manager


def test_ancestors_returns_direct_parent_to_root_with_concrete_nodes(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint

    root_name = maya_cmds.createNode("transform", name="root")
    joint_name = maya_cmds.createNode(
        "joint",
        name="joint_parent",
        parent=root_name,
    )
    transform_name = maya_cmds.createNode(
        "transform",
        name="transform_parent",
        parent=joint_name,
    )
    shape_name = maya_cmds.createNode(
        "mesh",
        name="meshShape",
        parent=transform_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    shape = nodes.existing.mesh(shape_name)

    ancestors = shape.ancestors()

    assert tuple(type(ancestor) for ancestor in ancestors) == (
        Transform,
        Joint,
        Transform,
    )
    assert tuple(ancestor.full_path for ancestor in ancestors) == (
        "|root|joint_parent|transform_parent",
        "|root|joint_parent",
        "|root",
    )
    assert all(
        ancestor.modifier_manager is nodes.modifier_manager
        for ancestor in ancestors
    )
    assert all(ancestor.m_obj != shape.m_obj for ancestor in ancestors)
    assert root.ancestors() == ()


def test_ancestors_reads_executed_scene_state_without_cache(
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
    pending_root = nodes.create.transform(name="pending_root")
    root.set_parent(pending_root)

    assert tuple(ancestor.name for ancestor in child.ancestors()) == ("root",)

    nodes.modifier_manager.do_it_dag()

    first_result = child.ancestors()
    assert tuple(ancestor.name for ancestor in first_result) == (
        "root",
        "pending_root",
    )

    external_root_name = maya_cmds.createNode(
        "transform",
        name="external_root",
    )
    maya_cmds.parent("pending_root", external_root_name)

    second_result = child.ancestors()
    assert tuple(ancestor.name for ancestor in second_result) == (
        "root",
        "pending_root",
        "external_root",
    )
    assert second_result is not first_result


def test_ancestors_uses_held_path_for_instanced_node(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    root_a_name = maya_cmds.createNode("transform", name="root_a")
    parent_a_name = maya_cmds.createNode(
        "transform",
        name="parent_a",
        parent=root_a_name,
    )
    root_b_name = maya_cmds.createNode("transform", name="root_b")
    parent_b_name = maya_cmds.createNode(
        "transform",
        name="parent_b",
        parent=root_b_name,
    )
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=parent_a_name,
    )
    maya_cmds.parent(child_name, parent_b_name, addObject=True)
    child_path = maya_cmds.ls(child_name, long=True, allPaths=True)[1]
    nodes = bdu.Nodes()
    child = nodes.existing.transform(child_path)

    selected_path_names = child.full_path.lstrip("|").split("|")
    expected_ancestor_names = tuple(reversed(selected_path_names[:-1]))
    ancestors = child.ancestors()

    assert child.is_instanced is True
    assert tuple(ancestor.name for ancestor in ancestors) == (
        expected_ancestor_names
    )
    assert all(
        ancestor.modifier_manager is nodes.modifier_manager
        for ancestor in ancestors
    )
