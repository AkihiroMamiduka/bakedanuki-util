# coding: utf-8
from __future__ import annotations

import pytest


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


def test_children_filters_by_dag_class_with_inheritance(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint
    from bd_util.maya.node.operator.node.dag.unknown_dag import UnknownDag

    root_name = maya_cmds.createNode("transform", name="root")
    maya_cmds.createNode("joint", name="joint_child", parent=root_name)
    maya_cmds.createNode("mesh", name="meshShape", parent=root_name)
    maya_cmds.createNode(
        "unknownDag",
        name="unknown_child",
        parent=root_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    assert tuple(type(child) for child in root.children(filter_type=None)) == (
        Joint,
        Mesh,
        UnknownDag,
    )
    assert tuple(
        type(child) for child in root.children(filter_type=nodes.types.DAG)
    ) == (Joint, Mesh, UnknownDag)
    assert tuple(
        child.name
        for child in root.children(filter_type=nodes.types.Transform)
    ) == ("joint_child",)
    assert tuple(
        child.name for child in root.children(filter_type=nodes.types.Shape)
    ) == ("meshShape",)
    assert tuple(
        child.name
        for child in root.children(filter_type=nodes.types.UnknownDag)
    ) == ("unknown_child",)
    assert root.children(filter_type=nodes.types.Locator) == ()
    assert tuple(
        child.name for child in root.children(include_shapes=False)
    ) == ("joint_child", "unknown_child")
    assert tuple(
        child.name
        for child in root.children(
            filter_type=nodes.types.DAG,
            include_shapes=False,
        )
    ) == ("joint_child", "unknown_child")
    assert (
        root.children(
            filter_type=nodes.types.Shape,
            include_shapes=False,
        )
        == ()
    )


def test_children_can_exclude_subclasses(new_scene, maya_cmds):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    maya_cmds.createNode(
        "transform",
        name="transform_child",
        parent=root_name,
    )
    maya_cmds.createNode("joint", name="joint_child", parent=root_name)
    maya_cmds.createNode("mesh", name="meshShape", parent=root_name)
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    assert tuple(
        child.name
        for child in root.children(filter_type=nodes.types.Transform)
    ) == ("transform_child", "joint_child")
    assert tuple(
        child.name
        for child in root.children(
            filter_type=nodes.types.Transform,
            include_subclasses=False,
        )
    ) == ("transform_child",)
    assert tuple(
        child.name
        for child in root.children(
            filter_type=nodes.types.Joint,
            include_subclasses=False,
        )
    ) == ("joint_child",)
    assert (
        root.children(
            filter_type=nodes.types.Shape,
            include_subclasses=False,
        )
        == ()
    )
    assert tuple(
        child.name
        for child in root.children(
            filter_type=nodes.types.Mesh,
            include_subclasses=False,
        )
    ) == ("meshShape",)


def test_children_rejects_non_dag_filter_type(new_scene, maya_cmds):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    invalid_filter_types = (
        nodes.types.NodeOperator,
        nodes.types.PlusMinusAverage,
        root,
        (nodes.types.Transform, nodes.types.Shape),
    )
    for filter_type in invalid_filter_types:
        with pytest.raises(
            TypeError,
            match="filter_type must be a DAG NodeOperator class",
        ):
            root.children(filter_type=filter_type)


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
    assert tuple(
        ancestor.name for ancestor in shape.ancestors(filter_type=None)
    ) == ("transform_parent", "joint_parent", "root")
    assert tuple(
        ancestor.name
        for ancestor in shape.ancestors(filter_type=nodes.types.DAG)
    ) == ("transform_parent", "joint_parent", "root")
    assert tuple(
        ancestor.name
        for ancestor in shape.ancestors(filter_type=nodes.types.Transform)
    ) == ("transform_parent", "joint_parent", "root")
    assert tuple(
        ancestor.name
        for ancestor in shape.ancestors(
            filter_type=nodes.types.Transform,
            include_subclasses=False,
        )
    ) == ("transform_parent", "root")
    assert tuple(
        ancestor.name
        for ancestor in shape.ancestors(
            filter_type=nodes.types.Joint,
            include_subclasses=False,
        )
    ) == ("joint_parent",)
    assert shape.ancestors(filter_type=nodes.types.Shape) == ()
    assert shape.ancestors(filter_type=nodes.types.Locator) == ()


def test_ancestors_rejects_non_dag_filter_type(new_scene, maya_cmds):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    child_name = maya_cmds.createNode(
        "transform",
        name="child",
        parent=root_name,
    )
    nodes = bdu.Nodes()
    child = nodes.existing.transform(child_name)

    invalid_filter_types = (
        nodes.types.NodeOperator,
        nodes.types.PlusMinusAverage,
        child,
        (nodes.types.Transform, nodes.types.Shape),
    )
    for filter_type in invalid_filter_types:
        with pytest.raises(
            TypeError,
            match="filter_type must be a DAG NodeOperator class",
        ):
            child.ancestors(filter_type=filter_type)


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


def test_descendants_returns_depth_first_pre_order_with_concrete_nodes(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint
    from bd_util.maya.node.operator.node.dag.unknown_dag import UnknownDag

    root_name = maya_cmds.createNode("transform", name="root")
    first_name = maya_cmds.createNode(
        "joint",
        name="first",
        parent=root_name,
    )
    first_child_name = maya_cmds.createNode(
        "transform",
        name="first_child",
        parent=first_name,
    )
    shape_name = maya_cmds.createNode(
        "mesh",
        name="meshShape",
        parent=first_child_name,
    )
    maya_cmds.createNode(
        "unknownDag",
        name="unknown_child",
        parent=first_name,
    )
    second_name = maya_cmds.createNode(
        "transform",
        name="second",
        parent=root_name,
    )
    maya_cmds.createNode(
        "joint",
        name="second_child",
        parent=second_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    shape = nodes.existing.mesh(shape_name)

    descendants = root.descendants()

    assert tuple(type(descendant) for descendant in descendants) == (
        Joint,
        Transform,
        Mesh,
        UnknownDag,
        Transform,
        Joint,
    )
    assert tuple(descendant.name for descendant in descendants) == (
        "first",
        "first_child",
        "meshShape",
        "unknown_child",
        "second",
        "second_child",
    )
    assert all(
        descendant.modifier_manager is nodes.modifier_manager
        for descendant in descendants
    )
    assert all(descendant.m_obj != root.m_obj for descendant in descendants)
    assert shape.descendants() == ()


def test_descendants_filters_results_without_pruning_subtrees(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint
    from bd_util.maya.node.operator.node.dag.unknown_dag import UnknownDag

    root_name = maya_cmds.createNode("transform", name="root")
    branch_a_name = maya_cmds.createNode(
        "transform",
        name="branch_a",
        parent=root_name,
    )
    maya_cmds.createNode("mesh", name="meshAShape", parent=branch_a_name)
    branch_b_name = maya_cmds.createNode(
        "joint",
        name="branch_b",
        parent=root_name,
    )
    nested_name = maya_cmds.createNode(
        "transform",
        name="nested",
        parent=branch_b_name,
    )
    maya_cmds.createNode("mesh", name="meshBShape", parent=nested_name)
    maya_cmds.createNode(
        "unknownDag",
        name="unknown_child",
        parent=root_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    assert tuple(
        type(descendant) for descendant in root.descendants(filter_type=None)
    ) == (Transform, Mesh, Joint, Transform, Mesh, UnknownDag)
    assert tuple(
        descendant.name
        for descendant in root.descendants(filter_type=nodes.types.DAG)
    ) == (
        "branch_a",
        "meshAShape",
        "branch_b",
        "nested",
        "meshBShape",
        "unknown_child",
    )
    assert tuple(
        descendant.name
        for descendant in root.descendants(filter_type=nodes.types.Transform)
    ) == ("branch_a", "branch_b", "nested")
    assert tuple(
        descendant.name
        for descendant in root.descendants(filter_type=nodes.types.Shape)
    ) == ("meshAShape", "meshBShape")
    assert tuple(
        descendant.name
        for descendant in root.descendants(filter_type=nodes.types.Mesh)
    ) == ("meshAShape", "meshBShape")
    assert tuple(
        descendant.name
        for descendant in root.descendants(filter_type=nodes.types.Joint)
    ) == ("branch_b",)
    assert tuple(
        descendant.name
        for descendant in root.descendants(filter_type=nodes.types.UnknownDag)
    ) == ("unknown_child",)
    assert root.descendants(filter_type=nodes.types.Locator) == ()
    assert tuple(
        descendant.name
        for descendant in root.descendants(
            filter_type=nodes.types.Transform,
            include_subclasses=False,
        )
    ) == ("branch_a", "nested")
    assert tuple(
        descendant.name
        for descendant in root.descendants(
            filter_type=nodes.types.Joint,
            include_subclasses=False,
        )
    ) == ("branch_b",)
    assert (
        root.descendants(
            filter_type=nodes.types.Shape,
            include_subclasses=False,
        )
        == ()
    )
    assert tuple(
        descendant.name
        for descendant in root.descendants(
            filter_type=nodes.types.Mesh,
            include_subclasses=False,
        )
    ) == ("meshAShape", "meshBShape")
    assert tuple(
        descendant.name
        for descendant in root.descendants(include_shapes=False)
    ) == ("branch_a", "branch_b", "nested", "unknown_child")
    assert tuple(
        descendant.name
        for descendant in root.descendants(
            filter_type=nodes.types.DAG,
            include_shapes=False,
        )
    ) == ("branch_a", "branch_b", "nested", "unknown_child")
    assert (
        root.descendants(
            filter_type=nodes.types.Shape,
            include_shapes=False,
        )
        == ()
    )


def test_descendants_rejects_non_dag_filter_type(new_scene, maya_cmds):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    invalid_filter_types = (
        nodes.types.NodeOperator,
        nodes.types.PlusMinusAverage,
        root,
        (nodes.types.Transform, nodes.types.Shape),
    )
    for filter_type in invalid_filter_types:
        with pytest.raises(
            TypeError,
            match="filter_type must be a DAG NodeOperator class",
        ):
            root.descendants(filter_type=filter_type)


@pytest.mark.parametrize(
    "traversal_name",
    ("children", "ancestors", "descendants"),
)
def test_traversal_validates_include_subclasses(
    new_scene,
    maya_cmds,
    traversal_name,
):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    traversal = getattr(root, traversal_name)

    with pytest.raises(
        ValueError,
        match="include_subclasses=False requires filter_type",
    ):
        traversal(include_subclasses=False)

    for include_subclasses in (None, 0, 1, "false"):
        with pytest.raises(
            TypeError,
            match="include_subclasses must be bool",
        ):
            traversal(
                filter_type=nodes.types.Transform,
                include_subclasses=include_subclasses,
            )


@pytest.mark.parametrize("traversal_name", ("children", "descendants"))
def test_shape_filter_validates_include_shapes(
    new_scene,
    maya_cmds,
    traversal_name,
):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    traversal = getattr(root, traversal_name)

    for include_shapes in (None, 0, 1, "false"):
        with pytest.raises(
            TypeError,
            match="include_shapes must be bool",
        ):
            traversal(include_shapes=include_shapes)


def test_descendants_reads_executed_scene_state_without_cache(
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
    maya_cmds.createNode(
        "joint",
        name="reparented_grandchild",
        parent=reparented_name,
    )
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)
    pending_child = nodes.create.transform(
        name="pending_child",
        parent=root,
    )
    nodes.create.joint(
        name="pending_grandchild",
        parent=pending_child,
    )
    reparented_child = nodes.existing.transform(reparented_name)
    reparented_child.set_parent(root)

    assert root.descendants() == ()

    nodes.modifier_manager.do_it_dag()

    first_result = root.descendants()
    assert tuple(descendant.name for descendant in first_result) == (
        "pending_child",
        "pending_grandchild",
        "reparented_child",
        "reparented_grandchild",
    )

    external_child_name = maya_cmds.createNode(
        "transform",
        name="external_child",
        parent=root_name,
    )
    maya_cmds.createNode(
        "mesh",
        name="externalShape",
        parent=external_child_name,
    )

    second_result = root.descendants()
    assert tuple(descendant.name for descendant in second_result) == (
        "pending_child",
        "pending_grandchild",
        "reparented_child",
        "reparented_grandchild",
        "external_child",
        "externalShape",
    )
    assert second_result is not first_result


def test_descendants_revisits_instanced_subtree_for_each_dag_path(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    root_name = maya_cmds.createNode("transform", name="root")
    branch_a_name = maya_cmds.createNode(
        "transform",
        name="branch_a",
        parent=root_name,
    )
    branch_b_name = maya_cmds.createNode(
        "transform",
        name="branch_b",
        parent=root_name,
    )
    instanced_name = maya_cmds.createNode(
        "transform",
        name="instanced_child",
        parent=branch_a_name,
    )
    maya_cmds.createNode(
        "mesh",
        name="instancedShape",
        parent=instanced_name,
    )
    maya_cmds.parent(instanced_name, branch_b_name, addObject=True)
    nodes = bdu.Nodes()
    root = nodes.existing.transform(root_name)

    descendants = root.descendants()

    assert tuple(descendant.name for descendant in descendants) == (
        "branch_a",
        "instanced_child",
        "instancedShape",
        "branch_b",
        "instanced_child",
        "instancedShape",
    )
    assert descendants[1].m_obj == descendants[4].m_obj
    assert descendants[2].m_obj == descendants[5].m_obj
    assert all(
        descendant.modifier_manager is nodes.modifier_manager
        for descendant in descendants
    )

    meshes = root.descendants(filter_type=nodes.types.Mesh)
    assert tuple(mesh.name for mesh in meshes) == (
        "instancedShape",
        "instancedShape",
    )
    assert meshes[0].m_obj == meshes[1].m_obj
