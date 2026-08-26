# coding: utf-8
from __future__ import annotations

import pytest


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def test_get_relative_matrix_returns_src_in_dst_space(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    src = maya_cmds.createNode("transform", name="src")
    dst = maya_cmds.createNode("transform", name="dst")
    maya_cmds.setAttr(f"{src}.translate", 7.0, 8.0, 9.0)
    maya_cmds.setAttr(f"{src}.rotate", 10.0, 20.0, 30.0)
    maya_cmds.setAttr(f"{dst}.translate", 3.0, 4.0, 5.0)
    maya_cmds.setAttr(f"{dst}.rotate", 15.0, 25.0, 35.0)
    nodes = bdu.Nodes()
    src_dag = nodes.existing.transform(src)
    dst_dag = nodes.existing.transform(dst)

    relative = src_dag.get_relative_matrix(dst_dag)
    src_world = src_dag.wm[0].get()
    dst_world_inverse = dst_dag.wim[0].get()
    expected = src_world * dst_world_inverse

    _assert_matrix_close(relative.matrix, expected.matrix)
    _assert_matrix_close(
        dst_dag.get_relative_matrix(dst_dag).matrix,
        maya_om.MMatrix(),
    )


def test_get_local_matrix_handles_offset_parent_matrix(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="dst_parent")
    dst = maya_cmds.createNode("transform", name="dst", parent=parent)
    src = maya_cmds.createNode("transform", name="src")
    maya_cmds.setAttr(f"{parent}.translate", 3.0, 4.0, 5.0)
    maya_cmds.setAttr(f"{parent}.rotate", 15.0, 25.0, 35.0)
    maya_cmds.setAttr(f"{src}.translate", 7.0, 8.0, 9.0)
    maya_cmds.setAttr(f"{src}.rotate", 10.0, 20.0, 30.0)
    offset_parent = maya_om.MTransformationMatrix()
    offset_parent.setTranslation(
        maya_om.MVector(2.0, 3.0, 4.0),
        maya_om.MSpace.kTransform,
    )
    offset_parent.setRotation(maya_om.MEulerRotation(0.2, 0.3, 0.4))
    maya_cmds.setAttr(
        f"{dst}.offsetParentMatrix",
        *list(offset_parent.asMatrix()),
        type="matrix",
    )
    nodes = bdu.Nodes()
    src_dag = nodes.existing.transform(src)
    dst_dag = nodes.existing.transform(dst)

    local = src_dag.get_local_matrix(dst_dag)
    src_world = src_dag.wm[0].get()
    dst_parent_inverse = dst_dag.pim[0].get()
    dst_parent = dst_dag.pm[0].get()
    expected = src_world * dst_parent_inverse

    _assert_matrix_close(local.matrix, expected.matrix)
    _assert_matrix_close(
        local.matrix * dst_parent.matrix,
        src_world.matrix,
    )


def test_dag_matrix_methods_use_dag_path_instance_number(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    parent_a = maya_cmds.createNode("transform", name="parent_a")
    parent_b = maya_cmds.createNode("transform", name="parent_b")
    src = maya_cmds.createNode("transform", name="src", parent=parent_a)
    instance_parent = maya_cmds.instance(src)[0]
    maya_cmds.parent(instance_parent, parent_b)
    maya_cmds.setAttr(f"{parent_a}.translateX", 1.0)
    maya_cmds.setAttr(f"{parent_b}.translateX", 10.0)
    maya_cmds.setAttr(f"{src}.translateX", 2.0)
    src_paths = maya_cmds.ls(src, long=True, allPaths=True)
    assert len(src_paths) == 2

    selection = maya_om.MSelectionList()
    selection.add(src_paths[1])
    second_path = selection.getDagPath(0)
    assert second_path.instanceNumber() == 1

    dst = maya_cmds.createNode("transform", name="dst")
    nodes = bdu.Nodes()
    src_dag = nodes.existing.transform(src_paths[1])
    src_dag._dag_path = second_path
    dst_dag = nodes.existing.transform(dst)

    relative = src_dag.get_relative_matrix(dst_dag)
    src_world = src_dag.wm[1].get()
    dst_world_inverse = dst_dag.wim[0].get()
    expected = src_world * dst_world_inverse

    _assert_matrix_close(relative.matrix, expected.matrix)


def test_dag_matrix_methods_require_dag_destination(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    transform = maya_cmds.createNode("transform", name="transform")
    plus_minus_average = maya_cmds.createNode(
        "plusMinusAverage",
        name="plus_minus_average",
    )
    nodes = bdu.Nodes()
    dag = nodes.existing.transform(transform)
    dg = nodes.existing.plusMinusAverage(plus_minus_average)

    with pytest.raises(TypeError, match="dst_dag must be DAG"):
        dag.get_relative_matrix(dg)
    with pytest.raises(TypeError, match="dst_dag must be DAG"):
        dag.get_local_matrix(dg)
