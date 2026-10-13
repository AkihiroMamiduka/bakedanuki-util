# coding: utf-8
from maya import cmds

from bd_util._sample.maya.ui.string_sample import node_name
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import StringLineEdit, qt


def flush() -> None:
    """Windowとcallbackの通知・遅延終了を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def press_return(line_edit: StringLineEdit) -> None:
    """通常のEnterイベントで文字列を確定する。"""
    for event_type in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        event = qt.QtGui.QKeyEvent(
            event_type,
            qt.Qt.Key.Key_Return,
            qt.Qt.KeyboardModifier.NoModifier,
        )
        qt.QApplication.sendEvent(line_edit, event)


def test_sample_keeps_fixed_target_and_shares_confirmed_name(
    qt_application, maya_standalone
):
    """表示と選択変更はsceneを書き換えず、名前確定だけを共有する。"""
    target = cmds.createNode("network", name="nodeNameSampleTarget")
    other = cmds.createNode("network", name="nodeNameSampleOther")
    target_id = cmds.ls(target, uuid=True)[0]
    cmds.select(other, replace=True)
    selection = cmds.ls(selection=True, long=True)
    node_count = len(cmds.ls())
    undo_name = cmds.undoInfo(query=True, undoName=True)
    window = node_name.show(target)
    try:
        assert isinstance(window.line_edit, StringLineEdit)
        assert window.line_edit.text() == target
        assert window.label.text() == target
        assert cmds.ls(selection=True, long=True) == selection
        assert len(cmds.ls()) == node_count
        assert cmds.undoInfo(query=True, undoName=True) == undo_name
        cmds.select(clear=True)
        assert window.binding.value == target

        requested = "nodeNameSampleRenamed"
        window.line_edit.setText(requested)
        window.line_edit.textEdited.emit(requested)
        press_return(window.line_edit)
        assert cmds.ls(target_id) == [requested]
        assert cmds.objExists(other)
        assert window.label.text() == requested
        assert window.linked_line_edit.text() == requested
        assert not window.error_label.text()
        assert window.isVisible()

        registries = window.findChildren(MayaCallbackRegistry)
        assert len(registries) == 1
        window.close()
        assert all(registry.callback_ids == () for registry in registries)
        flush()
    finally:
        node_name.dispose()
        cmds.delete(cmds.ls(target_id) or [])
        cmds.delete(other)
        flush()


def test_sample_reports_conflicts_errors_and_refreshes_name_lock(
    qt_application, maya_standalone
):
    """競合と入力失敗を表示し、名前lockの明示再読込みに対応する。"""
    target = cmds.createNode("network", name="nodeNameSampleState")
    target_id = cmds.ls(target, uuid=True)[0]
    window = node_name.show(target)
    try:
        window.line_edit.setText("draftName")
        window.line_edit.textEdited.emit("draftName")
        renamed = cmds.rename(target, "nodeNameSampleExternal")
        flush()
        assert window.line_edit.text() == "draftName"
        assert window.line_edit.hasConflict()
        assert "外部変更" in window.conflict_label.text()
        assert window.label.text() == renamed

        window.line_edit.setText("otherNamespace:newName")
        window.line_edit.textEdited.emit("otherNamespace:newName")
        press_return(window.line_edit)
        assert window.error_label.text()
        assert window.line_edit.text() == renamed
        assert window.label.text() == renamed

        cmds.lockNode(renamed, lock=False, lockName=True)
        window.refresh_button.click()
        assert window.line_edit.isReadOnly()
        assert "読み取り専用" in window.status_label.text()
        cmds.lockNode(renamed, lock=False, lockName=False)
        window.refresh_button.click()
        assert not window.line_edit.isReadOnly()
        assert "編集可能" in window.status_label.text()
        assert not window.error_label.text()
    finally:
        node_name.dispose()
        names = cmds.ls(target_id) or []
        if names:
            cmds.lockNode(names[0], lock=False, lockName=False)
            cmds.delete(names)
        flush()
