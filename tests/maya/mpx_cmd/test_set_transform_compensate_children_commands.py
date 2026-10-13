# coding: utf-8
"""子を維持してXYZを設定する正式コマンドとUndoを検証する。"""

from __future__ import annotations

import math

import pytest

pytestmark = pytest.mark.maya


@pytest.fixture(scope="module")
def util_set_commands_plugin():
    """テスト後にUndo履歴を解放し、正式プラグインを解除する。"""
    cmds = pytest.importorskip("maya.cmds")
    yield
    cmds.flushUndo()
    if cmds.pluginInfo("bdUtilCommands", query=True, loaded=True):
        cmds.unloadPlugin("bdUtilCommands")


def _world_matrix(cmds, node: str) -> tuple[float, ...]:
    """子の姿勢と位置を含むworld行列を返す。"""
    return tuple(cmds.xform(node, query=True, matrix=True, worldSpace=True))


def _orientation_dot(values, matrix) -> float:
    """固定XYZの目標と実行後world姿勢のquaternion内積を返す。"""
    from maya.api import OpenMaya as om

    radians = tuple(math.radians(value) for value in values)
    expected = om.MEulerRotation(
        *radians, om.MEulerRotation.kXYZ
    ).asQuaternion()
    actual = om.MTransformationMatrix(om.MMatrix(matrix)).rotation(
        asQuaternion=True
    )
    return abs(
        expected.x * actual.x
        + expected.y * actual.y
        + expected.z * actual.z
        + expected.w * actual.w
    )


@pytest.mark.parametrize(
    ("attribute", "facade_name"),
    (
        ("translate", "set_translate_compensate_children"),
        ("rotate", "set_rotate_compensate_children"),
        ("rotateAxis", "set_rotate_axis_compensate_children"),
        ("jointOrient", "set_joint_orient_compensate_children"),
    ),
)
def test_four_commands_preserve_child_world_and_undo_once(
    util_set_commands_plugin,
    new_scene,
    maya_cmds,
    attribute: str,
    facade_name: str,
) -> None:
    """4属性の設定で子world行列を保ち、親子を一回のUndoで戻す。"""
    from bd_util.maya import mpx_cmd

    parent = maya_cmds.createNode("joint", name="target")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.{attribute}", 2.0, -3.0, 4.0, type="double3")
    maya_cmds.setAttr(f"{child}.translate", 5.0, 6.0, 7.0, type="double3")
    maya_cmds.setAttr(f"{child}.rotate", 8.0, 9.0, 10.0, type="double3")
    before_child = _world_matrix(maya_cmds, child)
    before_parent = tuple(maya_cmds.getAttr(f"{parent}.{attribute}")[0])
    maya_cmds.flushUndo()

    facade = getattr(mpx_cmd, facade_name)
    assert facade((parent,), (12.0, 13.0, 14.0)) == [f"|{parent}"]
    assert tuple(
        maya_cmds.getAttr(f"{parent}.{attribute}")[0]
    ) == pytest.approx((12.0, 13.0, 14.0))
    assert _world_matrix(maya_cmds, child) == pytest.approx(before_child)
    maya_cmds.undo()
    assert tuple(
        maya_cmds.getAttr(f"{parent}.{attribute}")[0]
    ) == pytest.approx(before_parent)
    assert _world_matrix(maya_cmds, child) == pytest.approx(before_child)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_world_noop_and_tiny_explicit_translation(
    util_set_commands_plugin, new_scene, maya_cmds
) -> None:
    """Worldの同値入力はUndo不要で、微小な明示移動は反映する。"""
    from bd_util.maya.mpx_cmd import (
        set_rotate_compensate_children,
        set_translate_compensate_children,
    )

    node = maya_cmds.createNode("transform")
    maya_cmds.flushUndo()
    assert (
        set_translate_compensate_children(
            (node,), (0.0, 0.0, 0.0), space="world"
        )
        == []
    )
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert (
        set_rotate_compensate_children(
            (node,), (360.0, 0.0, 0.0), space="world"
        )
        == []
    )
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)

    assert set_translate_compensate_children(
        (node,), (1.0e-13, 0.0, 0.0), space="world"
    ) == [f"|{node}"]
    assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(
        1.0e-13, rel=0.0, abs=1.0e-15
    )
    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(0.0)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_multiple_targets_roll_back_when_later_child_is_locked(
    util_set_commands_plugin, new_scene, maya_cmds
) -> None:
    """後続ノードの補償が失敗したら先行ノードも復旧する。"""
    from bd_util.maya.mpx_cmd import set_translate_compensate_children

    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("joint", name="second")
    child = maya_cmds.createNode("joint", name="lockedChild", parent=second)
    maya_cmds.setAttr(f"{child}.translateX", lock=True)
    maya_cmds.flushUndo()

    with pytest.raises(RuntimeError):
        set_translate_compensate_children((first, second), (10.0, 20.0, 30.0))
    assert tuple(maya_cmds.getAttr(f"{first}.translate")[0]) == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert tuple(maya_cmds.getAttr(f"{second}.translate")[0]) == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_world_rotation_uses_fixed_xyz_with_non_xyz_rotate_order(
    util_set_commands_plugin, new_scene, maya_cmds
) -> None:
    """world目標を固定XYZで解釈し、Jointの回転順と子補償を扱う。"""
    from bd_util.maya.mpx_cmd import set_rotate_compensate_children

    parent = maya_cmds.createNode("transform", name="worldParent")
    joint = maya_cmds.createNode("joint", name="worldTarget", parent=parent)
    child = maya_cmds.createNode("joint", name="worldChild", parent=joint)
    maya_cmds.setAttr(f"{parent}.rotate", 12.0, -18.0, 23.0, type="double3")
    maya_cmds.setAttr(f"{joint}.rotateOrder", 4)
    maya_cmds.setAttr(f"{joint}.rotateAxis", 3.0, 5.0, 7.0, type="double3")
    maya_cmds.setAttr(f"{joint}.jointOrient", -4.0, 6.0, 9.0, type="double3")
    child_before = _world_matrix(maya_cmds, child)
    goal = (20.0, -30.0, 40.0)
    maya_cmds.flushUndo()

    assert set_rotate_compensate_children(
        (joint,),
        goal,
        space="world",
        joint_child_compensation_attr="jointOrient",
    ) == [f"|{parent}|{joint}"]
    assert _orientation_dot(goal, _world_matrix(maya_cmds, joint)) == (
        pytest.approx(1.0, abs=1.0e-8)
    )
    assert _world_matrix(maya_cmds, child) == pytest.approx(child_before)
    maya_cmds.undo()
    assert _world_matrix(maya_cmds, child) == pytest.approx(child_before)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_display_linear_unit_is_converted_to_centimeters(
    util_set_commands_plugin, new_scene, maya_cmds
) -> None:
    """表示単位mの入力をcmの属性値へ変換する。"""
    from bd_util import Nodes
    from bd_util.maya.mpx_cmd import set_translate_compensate_children

    node = maya_cmds.createNode("transform")
    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="m")
        assert set_translate_compensate_children(
            (node,), (2.0, 0.0, 0.0), input_unit="display"
        ) == [f"|{node}"]
        assert Nodes().existing.transform(node).translate.get().x == (
            pytest.approx(200.0)
        )
    finally:
        maya_cmds.flushUndo()
        maya_cmds.currentUnit(linear=previous_unit)
