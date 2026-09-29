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
