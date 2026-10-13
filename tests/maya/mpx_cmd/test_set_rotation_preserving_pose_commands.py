# coding: utf-8
"""姿勢を維持する回転設定コマンドの実行と Undo を検証する。"""

from __future__ import annotations

import math
from collections.abc import Sequence

import pytest

pytestmark = pytest.mark.maya


@pytest.fixture(scope="module")
def util_rotation_commands_plugin():
    """テストで読み込んだ正式プラグインを Undo 解放後に解除する。"""
    cmds = pytest.importorskip("maya.cmds")
    yield
    cmds.flushUndo()
    if cmds.pluginInfo("bdUtilCommands", query=True, loaded=True):
        cmds.unloadPlugin("bdUtilCommands")


def _set_xyz(cmds, node: str, attribute: str, values: Sequence[float]) -> None:
    """回転属性群の XYZ を表示単位で設定する。"""
    cmds.setAttr(f"{node}.{attribute}", *values, type="double3")


def _xyz(cmds, node: str, attribute: str) -> tuple[float, float, float]:
    """回転属性群の XYZ を表示単位で取得する。"""
    return tuple(cmds.getAttr(f"{node}.{attribute}")[0])


def _matrix(cmds, node: str, *, world: bool = False) -> tuple[float, ...]:
    """ノードの local または world 行列を取得する。"""
    return tuple(
        cmds.xform(
            node,
            query=True,
            matrix=True,
            worldSpace=world,
            objectSpace=not world,
        )
    )


def _assert_close(actual: Sequence[float], expected: Sequence[float]) -> None:
    """回転成分または行列の数値を許容誤差内で比較する。"""
    assert len(actual) == len(expected)
    assert all(
        math.isclose(left, right, rel_tol=1.0e-8, abs_tol=1.0e-8)
        for left, right in zip(actual, expected)
    )


@pytest.mark.parametrize(
    ("target", "compensate_with"),
    (
        ("rotate", "rotateAxis"),
        ("rotate", "jointOrient"),
        ("rotateAxis", "rotate"),
        ("rotateAxis", "jointOrient"),
        ("jointOrient", "rotate"),
        ("jointOrient", "rotateAxis"),
    ),
)
def test_joint_pairs_keep_local_and_child_world_pose_with_one_undo(
    util_rotation_commands_plugin,
    new_scene,
    maya_cmds,
    target: str,
    compensate_with: str,
) -> None:
    """Joint の六通りすべてで第三属性と姿勢を維持して戻せる。"""
    from bd_util.maya.mpx_cmd import set_rotation_preserving_pose

    node = maya_cmds.createNode("joint", name="rotationTarget")
    child = maya_cmds.createNode("joint", name="rotationChild", parent=node)
    maya_cmds.setAttr(f"{node}.rotateOrder", 4)
    _set_xyz(maya_cmds, node, "rotate", (17.0, -23.0, 41.0))
    _set_xyz(maya_cmds, node, "rotateAxis", (8.0, -7.0, 6.0))
    _set_xyz(maya_cmds, node, "jointOrient", (-3.0, 5.0, 9.0))
    _set_xyz(maya_cmds, child, "rotate", (3.0, 4.0, 5.0))
    third = (
        set(("rotate", "rotateAxis", "jointOrient"))
        - {target, compensate_with}
    ).pop()
    original_target = _xyz(maya_cmds, node, target)
    original_third = _xyz(maya_cmds, node, third)
    local = _matrix(maya_cmds, node)
    child_world = _matrix(maya_cmds, child, world=True)
    maya_cmds.flushUndo()

    assert set_rotation_preserving_pose(
        [node],
        (32.0, 11.0, -28.0),
        target=target,
        compensate_with=compensate_with,
    ) == [f"|{node}"]
    _assert_close(_xyz(maya_cmds, node, target), (32.0, 11.0, -28.0))
    _assert_close(_xyz(maya_cmds, node, third), original_third)
    _assert_close(_matrix(maya_cmds, node), local)
    _assert_close(_matrix(maya_cmds, child, world=True), child_world)

    maya_cmds.undo()
    _assert_close(_xyz(maya_cmds, node, target), original_target)
    _assert_close(_matrix(maya_cmds, node), local)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    maya_cmds.redo()
    _assert_close(_xyz(maya_cmds, node, target), (32.0, 11.0, -28.0))
    _assert_close(_matrix(maya_cmds, child, world=True), child_world)


@pytest.mark.parametrize(
    ("target", "compensate_with"),
    (("rotate", "rotateAxis"), ("rotateAxis", "rotate")),
)
def test_transform_pairs_keep_local_pose(
    util_rotation_commands_plugin,
    new_scene,
    maya_cmds,
    target: str,
    compensate_with: str,
) -> None:
    """Transform の二通りでも local 行列を保つ。"""
    from bd_util.maya.mpx_cmd import set_rotation_preserving_pose

    node = maya_cmds.createNode("transform")
    _set_xyz(maya_cmds, node, "rotate", (17.0, -23.0, 41.0))
    _set_xyz(maya_cmds, node, "rotateAxis", (8.0, -7.0, 6.0))
    local = _matrix(maya_cmds, node)
    maya_cmds.flushUndo()

    assert set_rotation_preserving_pose(
        [node],
        (32.0, 11.0, -28.0),
        target=target,
        compensate_with=compensate_with,
    ) == [f"|{node}"]
    _assert_close(_xyz(maya_cmds, node, target), (32.0, 11.0, -28.0))
    _assert_close(_matrix(maya_cmds, node), local)
    maya_cmds.undo()
    _assert_close(_matrix(maya_cmds, node), local)


def test_multiple_nodes_use_one_undo_and_noop_does_not_add_history(
    util_rotation_commands_plugin, new_scene, maya_cmds
) -> None:
    """複数対象を一度に戻し、目標と同値なら履歴を増やさない。"""
    from bd_util.maya.mpx_cmd import set_rotation_preserving_pose

    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("joint", name="second")
    for node in (first, second):
        _set_xyz(maya_cmds, node, "rotate", (1.0, 2.0, 3.0))
    maya_cmds.flushUndo()

    assert set_rotation_preserving_pose(
        [first, second, first],
        (4.0, 5.0, 6.0),
        target="rotate",
        compensate_with="rotateAxis",
    ) == [f"|{first}", f"|{second}"]
    maya_cmds.undo()
    for node in (first, second):
        _assert_close(_xyz(maya_cmds, node, "rotate"), (1.0, 2.0, 3.0))
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert (
        set_rotation_preserving_pose(
            [first, second],
            (1.0, 2.0, 3.0),
            target="rotate",
            compensate_with="rotateAxis",
        )
        == []
    )
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_later_locked_target_rolls_back_earlier_node(
    util_rotation_commands_plugin, new_scene, maya_cmds
) -> None:
    """後続ノードのロックで失敗したら先行ノードも復旧する。"""
    from bd_util.maya.mpx_cmd import set_rotation_preserving_pose

    first = maya_cmds.createNode("joint", name="first")
    second = maya_cmds.createNode("joint", name="second")
    _set_xyz(maya_cmds, first, "rotate", (1.0, 2.0, 3.0))
    _set_xyz(maya_cmds, second, "rotate", (1.0, 2.0, 3.0))
    maya_cmds.setAttr(f"{second}.jointOrientX", lock=True)
    first_local = _matrix(maya_cmds, first)
    maya_cmds.flushUndo()

    with pytest.raises(RuntimeError):
        set_rotation_preserving_pose(
            [first, second],
            (4.0, 5.0, 6.0),
            target="rotate",
            compensate_with="jointOrient",
        )
    _assert_close(_xyz(maya_cmds, first, "rotate"), (1.0, 2.0, 3.0))
    _assert_close(_matrix(maya_cmds, first), first_local)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_raw_command_converts_display_angle_unit(
    util_rotation_commands_plugin, new_scene, maya_cmds
) -> None:
    """Maya コマンドから表示角度単位を指定して実行できる。"""
    from bd_util.maya.mpx_cmd import set_rotation_preserving_pose

    node = maya_cmds.createNode("transform")
    original_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="rad")
        set_rotation_preserving_pose(
            [node],
            (0.5, 0.2, -0.3),
            target="rotate",
            compensate_with="rotateAxis",
            angle_unit="display",
        )
        _assert_close(_xyz(maya_cmds, node, "rotate"), (0.5, 0.2, -0.3))
        original_rotate_axis = _xyz(maya_cmds, node, "rotateAxis")
        maya_cmds.flushUndo()
        result = maya_cmds.bdSetRotationPreservingPose(
            node,
            targetAttribute="rotateAxis",
            compensateWith="rotate",
            valueX=0.4,
            valueY=-0.5,
            valueZ=0.6,
            angleUnit="display",
        )
        assert result in (f"|{node}", [f"|{node}"])
        _assert_close(_xyz(maya_cmds, node, "rotateAxis"), (0.4, -0.5, 0.6))
        maya_cmds.undo()
        _assert_close(
            _xyz(maya_cmds, node, "rotateAxis"), original_rotate_axis
        )
    finally:
        maya_cmds.currentUnit(angle=original_unit)


def test_invalid_pair_is_rejected_before_scene_change(
    util_rotation_commands_plugin, new_scene, maya_cmds
) -> None:
    """同一属性の指定を拒否し、シーンと Undo を変更しない。"""
    from bd_util.maya.mpx_cmd import set_rotation_preserving_pose

    node = maya_cmds.createNode("joint")
    maya_cmds.flushUndo()
    with pytest.raises(ValueError):
        set_rotation_preserving_pose(
            [node],
            (1.0, 2.0, 3.0),
            target="rotate",
            compensate_with="rotate",
        )
    _assert_close(_xyz(maya_cmds, node, "rotate"), (0.0, 0.0, 0.0))
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
