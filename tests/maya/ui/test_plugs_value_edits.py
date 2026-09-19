# coding: utf-8
"""異種属性行の値入力を、全件事前検証と一つのUndoで適用する。"""

import math

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaBoolValueEdit,
    MayaEnumPlugsBinding,
    MayaEnumValueEdit,
    MayaFloatPlugsBinding,
    MayaFloatValueEdit,
    apply_plugs_values,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.ui import qt


def flush():
    """遅延同期とQObjectの破棄を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def scene(new_scene):
    """三つのnodeと監視ownerを用意し、単位とUndo設定を復元する。"""
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    undo_enabled = cmds.undoInfo(q=True, state=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    yield nodes, owner
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo_enabled)


def float_binding(nodes, owner, attribute="tx"):
    """同名属性の一行を、各nodeへの入力へ接続する。"""
    return MayaFloatPlugsBinding(
        [resolve_float_plug(node, attribute) for node in nodes], parent=owner
    )


def enum_binding(nodes, owner, attribute="rotateOrder"):
    """同じ定義のenum属性を一行の入力へ接続する。"""
    return MayaEnumPlugsBinding(
        [resolve_enum_plug(node, attribute) for node in nodes], parent=owner
    )


def values(nodes, attribute):
    """対象node群の現在値をMayaの表示単位で読む。"""
    return [cmds.getAttr(f"{node}.{attribute}") for node in nodes]


def test_mixed_types_and_units_share_one_undo(scene):
    """公開単位の異種入力を個別変換し、全行を一回でUndoとRedoする。"""
    nodes, owner = scene
    distance = float_binding(nodes, owner)
    angle = float_binding(nodes, owner, "rx")
    number = float_binding(nodes, owner, "sx")
    visible = MayaBoolPlugsBinding(
        [resolve_bool_plug(node, "visibility") for node in nodes],
        parent=owner,
    )
    rotation_order = enum_binding(nodes, owner)
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    cmds.flushUndo()

    assert apply_plugs_values(
        [
            MayaFloatValueEdit(distance, 500.0),
            MayaFloatValueEdit(angle, 90.0),
            MayaFloatValueEdit(number, 5.0),
            MayaBoolValueEdit(visible, False),
            MayaEnumValueEdit(rotation_order, 5),
        ]
    )
    assert values(nodes, "tx") == pytest.approx([5.0] * 3)
    assert values(nodes, "rx") == pytest.approx([math.pi / 2] * 3)
    assert values(nodes, "sx") == [5.0] * 3
    assert values(nodes, "visibility") == [False] * 3
    assert values(nodes, "rotateOrder") == [5] * 3
    assert distance.value == 500.0
    assert angle.value == pytest.approx(90.0)
    assert not any(
        binding.is_mixed
        for binding in (distance, angle, number, visible, rotation_order)
    )

    cmds.undo()
    flush()
    for attribute in ("tx", "rx", "rotateOrder"):
        assert values(nodes, attribute) == [0] * 3
    for attribute in ("sx", "visibility"):
        assert values(nodes, attribute) == [1] * 3
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert distance.value == 500.0
    assert angle.value == pytest.approx(90.0)
    assert number.value == 5.0
    assert visible.value is False
    assert rotation_order.value == 5


def test_later_range_violation_rejects_every_row_before_writing(scene):
    """後の行の後続対象が範囲外なら、先の行も書き込まない。"""
    nodes, owner = scene
    for index, node in enumerate(nodes):
        cmds.addAttr(
            node,
            ln="limited",
            at="doubleLinear",
            minValue=-10,
            maxValue=10 - index * 3,
        )
    first = float_binding(nodes, owner)
    limited = float_binding(nodes, owner, "limited")
    cmds.flushUndo()
    with pytest.raises(ValueError, match="上限"):
        apply_plugs_values(
            [MayaFloatValueEdit(first, 9), MayaFloatValueEdit(limited, 5)]
        )
    assert values(nodes, "tx") == values(nodes, "limited") == [0] * 3
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


@pytest.mark.parametrize("invalid_definition", [False, True])
def test_later_enum_error_rejects_every_row(scene, invalid_definition):
    """enumの未定義入力と途中の定義不一致を、全行の書込み前に拒否する。"""
    nodes, owner = scene
    for node in nodes:
        cmds.addAttr(node, ln="mode", at="enum", enumName="Off=0:On=5")
    first = float_binding(nodes, owner)
    mode = enum_binding(nodes, owner, "mode")
    if invalid_definition:
        cmds.addAttr(nodes[1] + ".mode", edit=True, enumName="Off=0:Other=5")
    cmds.flushUndo()
    with pytest.raises(RuntimeError if invalid_definition else ValueError):
        apply_plugs_values(
            [
                MayaFloatValueEdit(first, 9),
                MayaEnumValueEdit(mode, 5 if invalid_definition else 1),
            ]
        )
    assert values(nodes, "tx") == values(nodes, "mode") == [0] * 3
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_readonly_followers_skip_and_later_representative_blocks(scene):
    """後続のlockと接続は除外し、別行の代表lockでは全行を停止する。"""
    nodes, owner = scene
    first = float_binding(nodes, owner)
    second = float_binding(nodes, owner, "rx")
    cmds.setAttr(nodes[1] + ".tx", lock=True)
    cmds.connectAttr(nodes[1] + ".ty", nodes[2] + ".tx")
    assert apply_plugs_values(
        [MayaFloatValueEdit(first, 4), MayaFloatValueEdit(second, 8)]
    )
    assert values(nodes, "tx") == [4, 0, 0]
    assert values(nodes, "rx") == [8] * 3
    assert first.is_mixed

    cmds.setAttr(nodes[0] + ".rotate", lock=True)
    cmds.flushUndo()
    with pytest.raises(RuntimeError):
        apply_plugs_values(
            [MayaFloatValueEdit(first, 6), MayaFloatValueEdit(second, 12)]
        )
    assert values(nodes, "tx") == [4, 0, 0]
    assert values(nodes, "rx") == [8] * 3
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


@pytest.mark.parametrize("same_binding", [False, True])
def test_duplicate_binding_or_plug_is_rejected_before_writing(
    scene, same_binding
):
    """同じbindingと、別binding内の重複する属性実体を拒否する。"""
    nodes, owner = scene
    first = float_binding(nodes[:2], owner)
    second = first if same_binding else float_binding(nodes[1:], owner)
    cmds.flushUndo()
    with pytest.raises(ValueError):
        apply_plugs_values(
            [MayaFloatValueEdit(first, 4), MayaFloatValueEdit(second, 4)]
        )
    assert values(nodes, "tx") == [0] * 3
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_empty_and_storage_precision_noop_leave_undo_empty(scene):
    """空入力とfloat32格納精度で同値の入力はUndo項目を作らない。"""
    nodes, owner = scene
    for node in nodes:
        cmds.addAttr(node, ln="weight", at="float")
    first = float_binding(nodes, owner)
    weight = float_binding(nodes, owner, "weight")
    weight.set_value(0.1)
    cmds.flushUndo()
    assert not apply_plugs_values([])
    assert not apply_plugs_values(
        [MayaFloatValueEdit(first, 0), MayaFloatValueEdit(weight, 0.1)]
    )
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


@pytest.mark.parametrize("change_definition", [False, True])
def test_later_row_state_change_during_write_restores_previous_rows(
    scene, monkeypatch, change_definition
):
    """先の行の書込み中に後の行が変化したら、直前検証で止めて復旧する。"""
    nodes, owner = scene
    for node in nodes:
        cmds.addAttr(node, ln="mode", at="enum", enumName="Off=0:On=5")
    first = float_binding(nodes, owner)
    mode = enum_binding(nodes, owner, "mode")
    real_set_attr = cmds.setAttr
    changed = False
    mode_writes = []

    def changing_set_attr(path, value):
        """最初の入力に続いて、後の行の代表をlockまたは定義変更する。"""
        nonlocal changed
        if value == 5:
            mode_writes.append(path)
        real_set_attr(path, value)
        if value == 6 and not changed:
            changed = True
            if change_definition:
                cmds.addAttr(
                    nodes[0] + ".mode", edit=True, enumName="Off=0:Other=5"
                )
            else:
                real_set_attr(nodes[0] + ".mode", lock=True)

    monkeypatch.setattr(cmds, "setAttr", changing_set_attr)
    with pytest.raises(ValueError if change_definition else RuntimeError):
        apply_plugs_values(
            [MayaFloatValueEdit(first, 6), MayaEnumValueEdit(mode, 5)]
        )
    assert changed
    assert not mode_writes
    assert values(nodes, "tx") == values(nodes, "mode") == [0] * 3
    assert first.value == 0
    assert not mode.view_model.set_value_command.can_execute
    assert FloatEditUndo._active is None


@pytest.mark.parametrize("restore_fails", [False, True])
def test_later_write_failure_restores_earlier_rows(
    scene, monkeypatch, restore_fails
):
    """後の行で書込み後に失敗しても全行を復旧し、復旧失敗も通知する。"""
    nodes, owner = scene
    first = float_binding(nodes, owner)
    second = float_binding(nodes, owner, "rx")
    first.set_value(2)
    second.set_value(3)
    real_set_attr = cmds.setAttr
    failed = False

    def failing_set_attr(path, value):
        """後の行を一つ変更した直後と、指定時だけ復旧で失敗させる。"""
        nonlocal failed
        if restore_fails and failed and value == 2:
            raise RuntimeError("restore failed")
        real_set_attr(path, value)
        if value == 8 and not failed:
            failed = True
            raise RuntimeError("write failed")

    monkeypatch.setattr(cmds, "setAttr", failing_set_attr)
    with pytest.raises(
        ExceptionGroup if restore_fails else RuntimeError
    ) as captured:
        apply_plugs_values(
            [MayaFloatValueEdit(first, 6), MayaFloatValueEdit(second, 8)]
        )
    expected_first = [6 if restore_fails else 2] * 3
    assert values(nodes, "tx") == expected_first
    assert values(nodes, "rx") == pytest.approx([3] * 3)
    assert first.value == expected_first[0]
    assert second.value == pytest.approx(3)
    if restore_fails:
        assert isinstance(captured.value, ExceptionGroup)
        errors = [str(error) for error in captured.value.exceptions]
        assert any("write failed" in error for error in errors)
        assert any("restore failed" in error for error in errors)
    assert FloatEditUndo._active is None

    # 失敗後の別操作が未終了chunkへ巻き込まれないことを確認する
    monkeypatch.setattr(cmds, "setAttr", real_set_attr)
    cmds.setAttr(nodes[0] + ".ty", 9)
    cmds.undo()
    assert cmds.getAttr(nodes[0] + ".ty") == 0
    assert values(nodes, "tx") == expected_first
