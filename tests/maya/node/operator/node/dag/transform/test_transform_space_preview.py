# coding: utf-8
"""未適用の移動・回転値をLocal／Worldへ換算するAPIを検証する。"""

from __future__ import annotations

import math

import pytest

pytestmark = pytest.mark.maya


def _world_matrix(cmds, node: str) -> tuple[float, ...]:
    """DAG原点と最終姿勢を含むworld行列を返す。"""
    return tuple(cmds.xform(node, query=True, matrix=True, worldSpace=True))


def _orientation_dot(world_values, world_matrix) -> float:
    """固定XYZ入力の姿勢と行列の姿勢をquaternionで比較する。"""
    from maya.api import OpenMaya as om

    angles = tuple(math.radians(value) for value in world_values)
    expected = om.MEulerRotation(
        *angles, om.MEulerRotation.kXYZ
    ).asQuaternion()
    actual = om.MTransformationMatrix(om.MMatrix(world_matrix)).rotation(
        asQuaternion=True
    )
    return abs(
        expected.x * actual.x
        + expected.y * actual.y
        + expected.z * actual.z
        + expected.w * actual.w
    )


@pytest.mark.parametrize("attribute", ("rotate", "rotateAxis", "jointOrient"))
def test_joint_rotation_preview_matches_applied_world_pose_without_editing(
    new_scene, maya_cmds, attribute: str
) -> None:
    """親の回転・負scale・非XYZ回転順でも未適用値の最終姿勢を予測する。"""
    from bd_util import Nodes

    parent = maya_cmds.createNode("transform", name="previewParent")
    joint = maya_cmds.createNode("joint", name="previewJoint", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotate", 8.0, -12.0, 17.0, type="double3")
    maya_cmds.setAttr(f"{parent}.scale", -1.2, 2.1, 0.8, type="double3")
    maya_cmds.setAttr(f"{joint}.rotateOrder", 4)
    maya_cmds.setAttr(f"{joint}.rotate", 15.0, -25.0, 35.0, type="double3")
    maya_cmds.setAttr(f"{joint}.rotateAxis", 3.0, 5.0, 7.0, type="double3")
    maya_cmds.setAttr(f"{joint}.jointOrient", -4.0, 6.0, 9.0, type="double3")
    original_matrix = _world_matrix(maya_cmds, joint)
    original_value = tuple(maya_cmds.getAttr(f"{joint}.{attribute}")[0])
    operator = Nodes().existing.joint(joint)
    target = (21.0, -14.0, 32.0)

    world_values = operator.convert_transform_space_values(
        attribute, target, from_space="local", to_space="world"
    )
    restored_local = operator.convert_transform_space_values(
        attribute, world_values, from_space="world", to_space="local"
    )
    assert restored_local == pytest.approx(target, abs=1.0e-7)
    assert (
        tuple(maya_cmds.getAttr(f"{joint}.{attribute}")[0]) == original_value
    )
    assert _world_matrix(maya_cmds, joint) == original_matrix

    maya_cmds.setAttr(f"{joint}.{attribute}", *target, type="double3")
    assert _orientation_dot(world_values, _world_matrix(maya_cmds, joint)) == (
        pytest.approx(1.0, abs=1.0e-8)
    )


def test_translation_preview_uses_dag_origin_without_editing(
    new_scene, maya_cmds
) -> None:
    """親の回転・scale下でも未適用のDAG原点を換算する。"""
    from bd_util import Nodes

    parent = maya_cmds.createNode("transform", name="positionParent")
    child = maya_cmds.createNode(
        "transform", name="positionChild", parent=parent
    )
    maya_cmds.setAttr(f"{parent}.translate", 10.0, 20.0, 30.0, type="double3")
    maya_cmds.setAttr(f"{parent}.rotate", 0.0, 0.0, 37.0, type="double3")
    maya_cmds.setAttr(f"{parent}.scale", 1.5, 0.7, 2.0, type="double3")
    before = _world_matrix(maya_cmds, child)
    target = (3.0, 4.0, 5.0)
    operator = Nodes().existing.transform(child)

    world_values = operator.convert_transform_space_values(
        "translate", target, from_space="local", to_space="world"
    )
    assert operator.convert_transform_space_values(
        "translate", world_values, from_space="world", to_space="local"
    ) == pytest.approx(target, abs=1.0e-9)
    assert _world_matrix(maya_cmds, child) == before
    maya_cmds.setAttr(f"{child}.translate", *target, type="double3")
    assert _world_matrix(maya_cmds, child)[12:15] == pytest.approx(
        world_values
    )
