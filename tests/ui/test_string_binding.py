# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util.ui import (
    PythonStringAttributeStore,
    StringBinding,
    StringLabel,
    StringLineEdit,
    StringViewModel,
    qt,
)


@dataclass
class Data:
    """文字列属性を持つテスト用正本。"""

    name: str = "初期値"


@dataclass
class MutableStore:
    """通知なしの編集可否変更と失敗を再現する正本。"""

    value: str = "initial"
    is_available: bool = True
    is_writable: bool = True
    fail_write: bool = False
    fail_read: bool = False
    writes: int = 0

    def read(self) -> str:
        """現在値または読込み失敗を返す。"""
        if self.fail_read:
            raise RuntimeError("読込み失敗")
        return self.value

    def write(self, value: str) -> str:
        """要求回数を数え、成功時だけ正本を変更する。"""
        self.writes += 1
        if self.fail_write:
            raise ValueError("書込み失敗")
        self.value = value
        return self.value


class KeyReceiver(qt.QWidget):
    """子入力欄から漏れたキー通知を記録する親Widget。"""

    def __init__(self) -> None:
        """キーごとの伝播記録を準備する。"""
        super().__init__()
        self.keys: list[tuple[qt.QEvent.Type, int]] = []

    def event(self, event: qt.QEvent) -> bool:
        """子から到達したキーの種類と値を記録する。"""
        if event.type() in (
            qt.QEvent.Type.ShortcutOverride,
            qt.QEvent.Type.KeyPress,
            qt.QEvent.Type.KeyRelease,
        ) and isinstance(event, qt.QtGui.QKeyEvent):
            self.keys.append((event.type(), event.key()))
        return super().event(event)


def flush() -> None:
    """遅延破棄とqueued signalを処理する。"""
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def edit(line: StringLineEdit, value: str) -> None:
    """ユーザー入力で発生するtextEditedを再現する。"""
    line.setText(value)
    line.textEdited.emit(value)


def press_key(line: StringLineEdit, key: qt.Qt.Key) -> None:
    """押下と解放を送り、欄内で受理されたことを確認する。"""
    for event_type in (
        qt.QEvent.Type.ShortcutOverride,
        qt.QEvent.Type.KeyPress,
        qt.QEvent.Type.KeyRelease,
    ):
        event = qt.QtGui.QKeyEvent(
            event_type, key, qt.Qt.KeyboardModifier.NoModifier
        )
        event.setAccepted(False)
        qt.QApplication.sendEvent(line, event)
        assert event.isAccepted()


def focus_in(line: StringLineEdit) -> None:
    """フォーカス取得通知を送って操作前の再読込みを行う。"""
    event = qt.QtGui.QFocusEvent(qt.QEvent.Type.FocusIn)
    qt.QApplication.sendEvent(line, event)


def test_python_store_preserves_exact_str_and_rejects_other_types(
    qt_application,
):
    """暗黙変換をせず、空文字やUnicodeをそのまま扱う。"""
    data = Data()
    store = PythonStringAttributeStore(data, "name")
    binding = StringBinding(store)
    values = []
    binding.changed.connect(values.append)
    try:
        assert binding.value == "初期値"
        assert binding.set_value("かな😀")
        assert data.name == binding.value == "かな😀"
        assert binding.set_value("")
        assert data.name == binding.value == ""
        assert not binding.set_value("")
        assert values == ["かな😀", ""]
        with pytest.raises(TypeError):
            binding.set_value(None)
        assert data.name == ""
        data.name = 3
        with pytest.raises(TypeError):
            binding.refresh()
        assert not binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_line_edit_commit_conflict_and_shared_views(qt_application):
    """入力を確定まで保持し、競合時は明示操作だけで上書きする。"""
    data = Data()
    binding = StringBinding.from_attribute(data, "name")
    first = StringLineEdit(binding)
    second = StringLineEdit(binding.view_model)
    label = StringLabel(binding)
    try:
        edit(first, "入力中")
        assert data.name == "初期値"
        assert second.text() == label.text() == "初期値"
        first.returnPressed.emit()
        assert data.name == binding.value == "入力中"
        assert second.text() == label.text() == "入力中"
        edit(first, "保留")
        data.name = "外部変更"
        binding.refresh()
        assert first.text() == "保留"
        assert first.hasConflict()
        assert second.text() == label.text() == "外部変更"
        first.editingFinished.emit()
        assert data.name == "外部変更"
        first.returnPressed.emit()
        assert data.name == "保留"
        assert not first.hasConflict()
        edit(first, "破棄")
        event = qt.QtGui.QKeyEvent(
            qt.QEvent.Type.KeyPress,
            qt.Qt.Key.Key_Escape,
            qt.Qt.KeyboardModifier.NoModifier,
        )
        qt.QApplication.sendEvent(first, event)
        assert first.text() == "保留"
        assert data.name == "保留"
    finally:
        first.deleteLater()
        second.deleteLater()
        label.deleteLater()
        binding.dispose()
        flush()


def test_locked_view_keeps_copy_and_view_model_can_work_without_store(
    qt_application,
):
    """View固有の編集停止とStore未接続のCommandを確認する。"""
    view_model = StringViewModel("one")
    line = StringLineEdit(view_model)
    try:
        line.setInputEnabled(False)
        assert line.isReadOnly()
        assert line.text() == "one"
        assert not line.isInputEnabled()
        assert view_model.set_value_command.execute("two")
        assert line.text() == "two"
        view_model.dispose()
        assert line.isReadOnly()
        with pytest.raises(RuntimeError):
            _ = line.view_model
    finally:
        line.deleteLater()
        view_model.deleteLater()
        flush()


def test_external_value_matching_draft_clears_conflict(qt_application):
    """外部確定値が入力中の文字列と一致したら競合を残さない。"""
    data = Data()
    binding = StringBinding.from_attribute(data, "name")
    line = StringLineEdit(binding)
    try:
        edit(line, "matching")
        data.name = "matching"
        binding.refresh()
        assert line.text() == "matching"
        assert not line.hasConflict()
        line.editingFinished.emit()
        assert data.name == "matching"
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_line_edit_can_follow_external_value_during_edit(qt_application):
    """確定値優先では編集中の外部値を表示し、古い入力を書き戻さない。"""
    data = Data()
    binding = StringBinding.from_attribute(data, "name")
    line = StringLineEdit(binding, follow_source_during_edit=True)
    try:
        edit(line, "入力中")
        binding.refresh()
        assert line.text() == "入力中"
        data.name = "外部変更"
        binding.refresh()
        assert line.text() == "外部変更"
        assert not line.hasConflict()
        line.editingFinished.emit()
        assert data.name == "外部変更"
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_line_edit_request_handler_intercepts_committed_value(qt_application):
    """任意handlerへ確定値を渡し、処理済みなら単行Commandを実行しない。"""
    data = Data()
    binding = StringBinding.from_attribute(data, "name")
    line = StringLineEdit(binding)
    requested: list[str] = []
    try:
        line.setValueRequestHandler(
            lambda value: requested.append(value) or True
        )
        edit(line, "一括入力")
        line.returnPressed.emit()
        assert requested == ["一括入力"]
        assert data.name == line.text() == "初期値"
        line.setValueRequestHandler(None)
        edit(line, "単行入力")
        line.returnPressed.emit()
        assert data.name == "単行入力"
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("key", [qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter])
@pytest.mark.parametrize("case", ["changed", "same", "readonly", "failure"])
def test_enter_is_consumed_without_leaking_to_parent(
    qt_application, key, case
):
    """成功・同名・編集不可・失敗の全てで確定キーを親へ渡さない。"""
    store = MutableStore()
    binding = StringBinding(store)
    parent = KeyReceiver()
    line = StringLineEdit(binding, parent)
    errors: list[str] = []
    line.edit_failed.connect(errors.append)
    try:
        if case == "readonly":
            store.is_writable = False
        if case == "failure":
            store.fail_write = True
        edit(line, "initial" if case == "same" else "changed")
        press_key(line, key)
        assert parent.keys == []
        expected = "changed" if case == "changed" else "initial"
        assert store.value == line.text() == expected
        assert store.writes == int(case in {"changed", "failure"})
        assert errors == (["書込み失敗"] if case == "failure" else [])
    finally:
        parent.deleteLater()
        binding.dispose()
        flush()


def test_focus_and_commit_refresh_unannounced_source_changes(qt_application):
    """未通知の外部変更は開始時に表示し、確定前にも競合として検出する。"""
    store = MutableStore()
    binding = StringBinding(store)
    line = StringLineEdit(binding)
    try:
        store.value = "before focus"
        focus_in(line)
        assert line.text() == "before focus"
        edit(line, "draft")
        store.value = "external"
        line.editingFinished.emit()
        assert line.text() == "draft"
        assert line.hasConflict()
        assert store.value == "external"
        assert store.writes == 0
        press_key(line, qt.Qt.Key.Key_Return)
        assert store.value == line.text() == "draft"
        assert store.writes == 1
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("explicit", [False, True])
def test_commit_refresh_keeps_follow_source_policy(qt_application, explicit):
    """正本優先なら確定直前に検出した変更でも古い入力を破棄する。"""
    store = MutableStore()
    binding = StringBinding(store)
    line = StringLineEdit(binding, follow_source_during_edit=True)
    try:
        edit(line, "draft")
        store.value = "external"
        if explicit:
            press_key(line, qt.Qt.Key.Key_Return)
        else:
            line.editingFinished.emit()
        assert store.value == line.text() == "external"
        assert not line.hasConflict()
        assert store.writes == 0
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_focus_refresh_recovers_unannounced_write_permission(qt_application):
    """ロック解除後のフォーカス取得で入力を再開できる。"""
    store = MutableStore(is_writable=False)
    binding = StringBinding(store)
    line = StringLineEdit(binding)
    try:
        assert line.isReadOnly()
        store.is_writable = True
        focus_in(line)
        assert not line.isReadOnly()
        edit(line, "changed")
        press_key(line, qt.Qt.Key.Key_Return)
        assert store.value == "changed"
        edit(line, "locked draft")
        store.is_writable = False
        press_key(line, qt.Qt.Key.Key_Return)
        assert line.isReadOnly()
        assert line.text() == store.value == "changed"
        assert store.writes == 1
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_ui_failure_signal_does_not_change_programmatic_exceptions(
    qt_application,
):
    """UI失敗は理由を通知し、直接呼出しの例外契約は維持する。"""
    store = MutableStore(fail_write=True)
    binding = StringBinding(store)
    line = StringLineEdit(binding)
    errors: list[str] = []
    line.edit_failed.connect(errors.append)
    try:
        edit(line, "draft")
        press_key(line, qt.Qt.Key.Key_Return)
        assert errors == ["書込み失敗"]
        assert line.text() == "initial"
        with pytest.raises(ValueError, match="書込み失敗"):
            binding.set_value("direct")
        assert errors == ["書込み失敗"]
        store.fail_read = True
        focus_in(line)
        assert errors == ["書込み失敗", "読込み失敗"]
        assert line.text() == "initial"
        assert line.isReadOnly()
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_request_handler_failure_restores_actual_value(qt_application):
    """任意handlerが変更後に失敗しても最新の正本へ表示を戻す。"""
    store = MutableStore()
    binding = StringBinding(store)
    line = StringLineEdit(binding)
    errors: list[str] = []
    line.edit_failed.connect(errors.append)

    def fail_after_change(_value: str) -> bool:
        """一部変更された正本と失敗を再現する。"""
        store.value = "partially changed"
        raise RuntimeError("handler失敗")

    try:
        line.setValueRequestHandler(fail_after_change)
        edit(line, "draft")
        press_key(line, qt.Qt.Key.Key_Return)
        assert line.text() == binding.value == "partially changed"
        assert errors == ["handler失敗"]
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_edit_checks_do_not_emit_unchanged_store_confirmation(qt_application):
    """入力前確認だけでは同値の再同期要求を発行しない。"""
    store = MutableStore()
    binding = StringBinding(store)
    line = StringLineEdit(binding)
    confirmations: list[str] = []
    binding.view_model.store_refreshed.connect(confirmations.append)
    try:
        focus_in(line)
        assert confirmations == []
        binding.refresh()
        assert confirmations == ["initial"]
        edit(line, "draft")
        press_key(line, qt.Qt.Key.Key_Return)
        assert confirmations == ["initial", "draft"]
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_enter_preserves_qt_validator_before_commit(qt_application):
    """Qtが確定を拒否する入力ではCommandを実行しない。"""
    data = Data("1")
    binding = StringBinding.from_attribute(data, "name")
    line = StringLineEdit(binding)
    line.setValidator(qt.QtGui.QIntValidator(1, 9, line))
    try:
        edit(line, "100")
        press_key(line, qt.Qt.Key.Key_Return)
        assert data.name == "1"
        assert line.text() == "100"
        edit(line, "2")
        press_key(line, qt.Qt.Key.Key_Enter)
        assert data.name == line.text() == "2"
    finally:
        line.deleteLater()
        binding.dispose()
        flush()


def test_focus_refresh_preserves_maya_view_pending_redo(maya_standalone):
    """Mayaとの再同期保留中でも入力開始だけではRedoを消さない。"""
    from maya import cmds

    from bd_util.maya.ui import MayaStringBinding, resolve_string_plug

    class LowercaseStore(MutableStore):
        """Mayaからの入力を補正して再同期保留を再現する正本。"""

        def write(self, value: str) -> str:
            """小文字に補正した文字列を確定する。"""
            return super().write(value.lower())

    cmds.file(new=True, force=True)
    node = cmds.createNode("network")
    cmds.addAttr(node, longName="text", dataType="string")
    store = LowercaseStore()
    binding = MayaStringBinding(
        store, maya_plug=resolve_string_plug(node, "text")
    )
    line = StringLineEdit(binding)
    view = binding.maya_view
    assert view is not None
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        cmds.setAttr(node + ".text", "UPPER", type="string")
        flush()
        assert cmds.getAttr(node + ".text") == "upper"
        cmds.undo()
        flush()
        assert cmds.getAttr(node + ".text") == "UPPER"
        assert store.value == "upper"
        assert not view.is_synchronized
        focus_in(line)
        flush()
        assert line.text() == "upper"
        assert cmds.getAttr(node + ".text") == "UPPER"
        assert not view.is_synchronized
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert cmds.getAttr(node + ".text") == store.value == "upper"
        assert view.is_synchronized
    finally:
        line.deleteLater()
        binding.dispose()
        flush()
        cmds.file(new=True, force=True)
