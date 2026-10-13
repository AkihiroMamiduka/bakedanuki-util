# coding: utf-8
from __future__ import annotations

from pathlib import Path

import pytest

pytestmark = pytest.mark.maya

_PLUGIN_NAME = "bdUtilCommands"


@pytest.fixture(scope="module")
def util_round_commands_plugin():
    """モジュール内で正式プラグインを共有し、最後に安全に解除する。"""
    cmds = pytest.importorskip("maya.cmds")
    yield
    cmds.flushUndo()
    if cmds.pluginInfo(_PLUGIN_NAME, query=True, loaded=True):
        cmds.unloadPlugin(_PLUGIN_NAME)


def test_typed_facade_loads_versioned_plugin_and_uses_maya_undo(
    util_round_commands_plugin, new_scene, maya_cmds
):
    """facade の実行結果とプラグイン配置先、Undo/Redo を確認する。"""
    from bd_util.maya.mpx_cmd.round_transform import round_translate

    node = maya_cmds.createNode("transform", name="roundTarget")
    maya_cmds.setAttr(f"{node}.translateX", 2.675)
    maya_cmds.flushUndo()

    assert round_translate([node], 2) == [f"|{node}"]
    assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(2.68)
    plugin_path = Path(
        maya_cmds.pluginInfo(_PLUGIN_NAME, query=True, path=True)
    ).resolve()
    maya_version = str(maya_cmds.about(version=True)).split(".", 1)[0]
    expected = (
        Path(__file__).resolve().parents[3]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / f"maya{maya_version}"
        / "bdUtilCommands.py"
    ).resolve()
    assert plugin_path == expected

    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(2.675)
    maya_cmds.redo()
    assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(2.68)


def test_rounded_target_is_no_op_for_maya_undo(
    util_round_commands_plugin, new_scene, maya_cmds
):
    """丸め済みのノードは変更結果も Undo 履歴も残さない。"""
    from bd_util.maya.mpx_cmd.round_transform import round_translate

    node = maya_cmds.createNode("transform")
    maya_cmds.setAttr(f"{node}.translateX", 2.68)
    maya_cmds.flushUndo()

    assert round_translate([node], 2) == []
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize(
    ("node_type", "attribute", "facade_name"),
    (
        ("transform", "translate", "round_translate"),
        ("joint", "translate", "round_translate"),
        ("transform", "rotate", "round_rotate"),
        ("joint", "rotate", "round_rotate"),
        ("transform", "rotateAxis", "round_rotate_axis"),
        ("joint", "rotateAxis", "round_rotate_axis"),
        ("joint", "jointOrient", "round_joint_orient"),
    ),
)
def test_round_commands_cover_transform_and_joint_attributes(
    util_round_commands_plugin,
    new_scene,
    maya_cmds,
    node_type,
    attribute,
    facade_name,
):
    """4コマンドが対応する Transform / Joint 属性を四捨五入する。"""
    from bd_util.maya.mpx_cmd import round_transform

    node = maya_cmds.createNode(node_type)
    maya_cmds.setAttr(f"{node}.{attribute}X", 2.675)
    maya_cmds.setAttr(f"{node}.{attribute}Y", -2.675)
    maya_cmds.flushUndo()

    facade = getattr(round_transform, facade_name)
    assert facade([node], 2) == [f"|{node}"]
    assert maya_cmds.getAttr(f"{node}.{attribute}X") == pytest.approx(2.68)
    assert maya_cmds.getAttr(f"{node}.{attribute}Y") == pytest.approx(-2.68)
    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{node}.{attribute}X") == pytest.approx(2.675)
    maya_cmds.redo()
    assert maya_cmds.getAttr(f"{node}.{attribute}X") == pytest.approx(2.68)


def test_raw_maya_command_accepts_explicit_nodes_and_flags(
    util_round_commands_plugin, new_scene, maya_cmds
):
    """公開 Maya コマンドを cmds から直接呼び出せる。"""
    node = maya_cmds.createNode("transform")
    maya_cmds.setAttr(f"{node}.rotateX", 1.235)
    maya_cmds.flushUndo()

    result = maya_cmds.bdRoundRotate(
        node,
        ndigits=2,
        roundingUnit="canonical",
        compensateChildren=False,
        compensateChildTranslate=False,
        jointChildCompensationAttr="rotate",
    )

    assert result in (f"|{node}", [f"|{node}"])
    assert maya_cmds.getAttr(f"{node}.rotateX") == pytest.approx(1.24)
    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{node}.rotateX") == pytest.approx(1.235)


def test_parent_child_inputs_are_deduplicated_and_processed_parent_first(
    util_round_commands_plugin, new_scene, maya_cmds
):
    """親の子補償後の local 値を子の丸め入力として使う。"""
    from bd_util.maya.mpx_cmd.round_transform import round_translate

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("transform", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.translateX", 2.675)
    maya_cmds.setAttr(f"{child}.translateX", 1.234)
    maya_cmds.flushUndo()

    changed = round_translate(
        [child, parent, parent, child],
        2,
        compensate_children=True,
    )

    assert changed == [f"|{parent}", f"|{parent}|{child}"]
    assert maya_cmds.getAttr(f"{parent}.translateX") == pytest.approx(2.68)
    assert maya_cmds.getAttr(f"{child}.translateX") == pytest.approx(1.23)
    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{parent}.translateX") == pytest.approx(2.675)
    assert maya_cmds.getAttr(f"{child}.translateX") == pytest.approx(1.234)


def test_later_locked_target_rolls_back_earlier_target(
    util_round_commands_plugin, new_scene, maya_cmds
):
    """複数ノードの途中で失敗した場合は初めの変更も取り消す。"""
    from bd_util.maya.mpx_cmd.round_transform import round_translate

    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    maya_cmds.setAttr(f"{first}.translateX", 2.675)
    maya_cmds.setAttr(f"{second}.translateX", 2.675)
    maya_cmds.setAttr(f"{second}.translateX", lock=True)
    maya_cmds.flushUndo()

    with pytest.raises(RuntimeError):
        round_translate([first, second], 2)

    assert maya_cmds.getAttr(f"{first}.translateX") == pytest.approx(2.675)
    assert maya_cmds.getAttr(f"{second}.translateX") == pytest.approx(2.675)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize(
    ("parent_type", "attribute", "facade_name"),
    (
        ("transform", "rotate", "round_rotate"),
        ("transform", "rotateAxis", "round_rotate_axis"),
        ("joint", "jointOrient", "round_joint_orient"),
    ),
)
@pytest.mark.parametrize(
    "joint_child_compensation_attr", ("rotate", "jointOrient")
)
def test_rotation_commands_keep_joint_child_world_pose(
    util_round_commands_plugin,
    new_scene,
    maya_cmds,
    parent_type,
    attribute,
    facade_name,
    joint_child_compensation_attr,
):
    """回転の丸めと子 Joint の姿勢・位置補償を一回の Undo にまとめる。"""
    from bd_util.maya.mpx_cmd import round_transform

    parent = maya_cmds.createNode(parent_type, name="parent")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.{attribute}Z", 12.345)
    maya_cmds.setAttr(f"{child}.translateX", 2.0)
    maya_cmds.setAttr(f"{child}.translateY", 3.0)
    maya_cmds.setAttr(f"{child}.jointOrientX", 7.0)
    initial_world = maya_cmds.getAttr(f"{child}.worldMatrix[0]")
    maya_cmds.flushUndo()

    facade = getattr(round_transform, facade_name)
    assert facade(
        [parent],
        2,
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr=joint_child_compensation_attr,
    ) == [f"|{parent}"]

    assert maya_cmds.getAttr(f"{parent}.{attribute}Z") == pytest.approx(12.35)
    assert maya_cmds.getAttr(f"{child}.worldMatrix[0]") == pytest.approx(
        initial_world, abs=1.0e-8
    )
    maya_cmds.undo()
    assert maya_cmds.getAttr(f"{parent}.{attribute}Z") == pytest.approx(12.345)
    assert maya_cmds.getAttr(f"{child}.worldMatrix[0]") == pytest.approx(
        initial_world, abs=1.0e-8
    )
    maya_cmds.redo()
    assert maya_cmds.getAttr(f"{child}.worldMatrix[0]") == pytest.approx(
        initial_world, abs=1.0e-8
    )


def test_commands_round_in_current_display_units(
    util_round_commands_plugin, new_scene, maya_cmds
):
    """現在の距離・角度表示単位に合わせて facade が丸める。"""
    from bd_util.maya.mpx_cmd.round_transform import (
        round_rotate,
        round_translate,
    )

    previous_linear = maya_cmds.currentUnit(query=True, linear=True)
    previous_angle = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(linear="in", angle="rad")
        node = maya_cmds.createNode("transform")
        maya_cmds.setAttr(f"{node}.translateX", 1.235)
        maya_cmds.setAttr(f"{node}.rotateY", 1.235)
        maya_cmds.flushUndo()

        assert round_translate([node], 2, rounding_unit="display") == [
            f"|{node}"
        ]
        assert round_rotate([node], 2, rounding_unit="display") == [f"|{node}"]
        assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(1.24)
        assert maya_cmds.getAttr(f"{node}.rotateY") == pytest.approx(1.24)
        maya_cmds.undo()
        maya_cmds.undo()
        assert maya_cmds.getAttr(f"{node}.translateX") == pytest.approx(1.235)
        assert maya_cmds.getAttr(f"{node}.rotateY") == pytest.approx(1.235)
    finally:
        maya_cmds.currentUnit(linear=previous_linear, angle=previous_angle)
