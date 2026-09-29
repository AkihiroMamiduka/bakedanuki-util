# coding: utf-8
from maya import cmds

from bd_util._sample.maya.ui.string_sample import maya_plugs
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import StringLineEdit, qt


def flush() -> None:
    """Maya通知とQtの遅延処理を進める。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def edit(line: qt.QLineEdit, value: str) -> None:
    """ユーザー入力時に発生するtextEditedを再現する。"""
    line.setText(value)
    line.textEdited.emit(value)


def test_group_sample_mixed_empty_and_draft_conflict(
    qt_application, maya_standalone
):
    """混在を値と分離し、後続の外部変更中は入力を保護する。"""
    joints = [cmds.createNode("joint") for _ in range(2)]
    cmds.setAttr(joints[0] + ".otherType", "first", type="string")
    cmds.setAttr(joints[1] + ".otherType", "second", type="string")
    window = maya_plugs.show(joints)
    try:
        assert window.line_edit.text() == "first"
        assert window.label.text() == "first"
        assert "混在" in window.state_label.text()
        edit(window.line_edit, "draft")
        cmds.setAttr(joints[1] + ".otherType", "external", type="string")
        flush()
        assert window.line_edit.hasConflict()
        assert window.line_edit.text() == "draft"
        window.line_edit.editingFinished.emit()
        assert cmds.getAttr(joints[0] + ".otherType") == "first"
        assert cmds.getAttr(joints[1] + ".otherType") == "external"
        window.line_edit.returnPressed.emit()
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "draft",
            "draft",
        ]
        assert "一致" in window.state_label.text()
        window.clear_button.click()
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "",
            "",
        ]
        cmds.setAttr(joints[1] + ".otherType", "other", type="string")
        flush()
        assert window.binding.is_mixed
        window.align_button.click()
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "",
            "",
        ]
        registries = window.findChildren(MayaCallbackRegistry)
        assert len(registries) == 1
        window.close()
        flush()
        assert not qt.isValid(window)
        assert registries[0].callback_ids == ()
        cmds.select(joints)
        reopened = maya_plugs.show_selected()
        assert reopened.binding.target_count == 2
    finally:
        maya_plugs.dispose()
        cmds.delete(joints)
        flush()


def test_group_line_edit_follows_value_changes_but_keeps_state_only_draft(
    qt_application, maya_standalone
):
    """後続値変更でも入力を破棄し、lockだけの通知では維持する。"""
    joints = [cmds.createNode("joint") for _ in range(2)]
    cmds.setAttr(joints[0] + ".otherType", "first", type="string")
    cmds.setAttr(joints[1] + ".otherType", "second", type="string")
    window = maya_plugs.show(joints)
    line = StringLineEdit(
        window.binding, window, follow_source_during_edit=True
    )
    try:
        edit(line, "draft")
        cmds.setAttr(joints[1] + ".otherType", lock=True)
        flush()
        assert line.text() == "draft"
        assert not line.hasConflict()
        cmds.setAttr(joints[1] + ".otherType", lock=False)
        flush()
        assert line.text() == "draft"
        cmds.setAttr(joints[1] + ".otherType", "external", type="string")
        flush()
        assert line.text() == "first"
        assert not line.hasConflict()
        line.editingFinished.emit()
        assert cmds.getAttr(joints[1] + ".otherType") == "external"

        edit(line, "another draft")
        cmds.setAttr(joints[0] + ".otherType", "updated", type="string")
        flush()
        assert line.text() == "updated"
        line.editingFinished.emit()
        assert cmds.getAttr(joints[0] + ".otherType") == "updated"
    finally:
        maya_plugs.dispose()
        cmds.delete(joints)
        flush()
