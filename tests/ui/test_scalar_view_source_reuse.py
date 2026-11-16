# coding: utf-8
"""bool・enum・stringの入力欄を、新しい正本へ安全に接続し直す。"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

import pytest

from bd_util.ui import (
    BoolBinding,
    BoolCheckBox,
    BoolViewModel,
    EnumBinding,
    EnumComboBox,
    EnumDefinition,
    EnumViewModel,
    StringBinding,
    StringLineEdit,
    StringViewModel,
    qt,
)


@dataclass
class _BoolStore:
    """書込み回数と編集可否を観察できるboolの正本。"""

    value: bool
    is_available: bool = True
    is_writable: bool = True
    writes: int = 0

    def read(self) -> bool:
        """現在の確定値を返す。"""
        return self.value

    def write(self, value: bool) -> bool:
        """明示入力だけを正本へ保存する。"""
        self.writes += 1
        self.value = value
        return value


@dataclass
class _EnumStore:
    """値と選択肢が異なる接続先の書込みを記録する。"""

    value: int
    definition: EnumDefinition
    is_available: bool = True
    is_writable: bool = True
    writes: int = 0

    def read(self) -> int:
        """現在の確定値を返す。"""
        return self.value

    def write(self, value: int) -> int:
        """明示入力だけを正本へ保存する。"""
        self.writes += 1
        self.value = value
        return value


@dataclass
class _StringStore:
    """文字列下書きの持越しと書込み回数を観察する。"""

    value: str
    is_available: bool = True
    is_writable: bool = True
    writes: int = 0

    def read(self) -> str:
        """現在の確定値を返す。"""
        return self.value

    def write(self, value: str) -> str:
        """明示入力だけを正本へ保存する。"""
        self.writes += 1
        self.value = value
        return value


def _events() -> None:
    """遅延破棄と旧正本から予約されたQt通知を処理する。"""
    for _ in range(3):
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()


class _PopupCloseObserver(qt.QObject):
    """実際のpopup非表示通知から、一度だけ外部処理を実行する。"""

    def __init__(
        self, popup: qt.QWidget, callback: Callable[[], None]
    ) -> None:
        """popupの寿命と同じ監視を用意し、初期表示中は外部処理を止める。"""
        super().__init__(popup)
        self.armed = False
        self.calls = 0
        self._callback = callback
        popup.installEventFilter(self)

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """非表示の開始時に監視を解除し、再入しても処理を繰り返さない。"""
        if self.armed and event.type() == qt.QEvent.Type.Hide:
            self.armed = False
            self.calls += 1
            self._callback()
        return super().eventFilter(watched, event)


@pytest.mark.parametrize("effect", ["dispose", "destroy", "reenter"])
def test_enum_popup_close_keeps_old_or_latest_valid_source(
    qt_application: qt.QApplication,
    effect: Literal["dispose", "destroy", "reenter"],
) -> None:
    """popup終了中の候補失効は拒否し、再入による最新の接続を上書きしない。"""
    del qt_application
    old_store = _EnumStore(
        0, EnumDefinition.from_mapping({0: "旧", 1: "旧次"})
    )
    new_store = _EnumStore(
        10, EnumDefinition.from_mapping({10: "候補", 20: "候補次"})
    )
    latest_store = _EnumStore(
        30, EnumDefinition.from_mapping({30: "最新", 40: "最新次"})
    )
    old, new, latest = (
        EnumBinding(old_store),
        EnumBinding(new_store),
        EnumBinding(latest_store),
    )
    destination = new.view_model
    view = EnumComboBox(old)

    def on_popup_close() -> None:
        """接続を確定する前に候補の終了、Qt破棄または別の接続を発生させる。"""
        if effect == "dispose":
            destination.dispose()
        elif effect == "destroy":
            destination.deleteLater()
            qt.QApplication.sendPostedEvents(
                None, qt.QEvent.Type.DeferredDelete
            )
        else:
            view.set_source(latest)

    observer = _PopupCloseObserver(view.view().window(), on_popup_close)
    try:
        view.show()
        view.showPopup()
        _events()
        assert view.view().isVisible()
        observer.armed = True
        if effect == "reenter":
            view.set_source(new)
            expected, expected_store = latest, latest_store
        else:
            with pytest.raises(RuntimeError):
                view.set_source(new)
            expected, expected_store = old, old_store
        assert observer.calls == 1
        assert not view.view().isVisible()
        assert view.view_model is expected.view_model
        assert view.isEnabled()
        assert view.currentText() == ("最新" if effect == "reenter" else "旧")
        assert old_store.writes == new_store.writes == latest_store.writes == 0

        # 失敗時の旧接続と再入時の最新接続が、終了後も表示を更新する
        expected_store.value = 40 if effect == "reenter" else 1
        expected.refresh()
        assert view.currentText() == (
            "最新次" if effect == "reenter" else "旧次"
        )
        assert old_store.writes == new_store.writes == latest_store.writes == 0
    finally:
        view.deleteLater()
        old.dispose()
        new.dispose()
        latest.dispose()
        _events()


@pytest.mark.parametrize("binding_source", [False, True])
def test_bool_source_replacement_preserves_handler_without_old_notifications(
    qt_application: qt.QApplication, binding_source: bool
) -> None:
    """入力先の交換と旧正本の変更・破棄を、値の書戻しから分離する。"""
    del qt_application
    old_store, new_store = _BoolStore(False), _BoolStore(
        True, is_writable=False
    )
    old, new = BoolBinding(old_store), BoolBinding(new_store)
    view = BoolCheckBox(old)
    requests: list[bool] = []

    def request(value: bool) -> bool:
        """既存handlerが新しい入力にも一度だけ使われることを記録する。"""
        requests.append(value)
        return False

    view.setValueRequestHandler(request)
    invalid = BoolViewModel()
    invalid.dispose()
    try:
        with pytest.raises(RuntimeError):
            view.set_source(invalid)
        assert view.view_model is old.view_model
        view.set_source(new if binding_source else new.view_model)
        assert view.view_model is new.view_model
        assert view.isChecked()
        assert not view.isEnabled()
        assert not old.is_disposed
        assert old_store.writes == new_store.writes == 0
        old_store.value = True
        old.refresh()
        old_store.value = False
        old.refresh()
        assert view.isChecked()
        assert not view.isEnabled()
        old.dispose()
        _events()
        new_store.is_writable = True
        new.refresh()
        assert view.isEnabled()
        view.click()
        assert not new_store.value
        assert requests == [False]
        assert old_store.writes == 0 and new_store.writes == 1
    finally:
        view.deleteLater()
        old.dispose()
        new.dispose()
        invalid.deleteLater()
        _events()


@pytest.mark.parametrize("binding_source", [False, True])
def test_enum_source_replacement_closes_popup_and_loads_new_definition(
    qt_application: qt.QApplication, binding_source: bool
) -> None:
    """開いた旧候補を終了し、新しい飛び番定義へ無書込みで切り替える。"""
    del qt_application
    old_store = _EnumStore(
        0, EnumDefinition.from_mapping({0: "旧", 1: "旧次"})
    )
    new_store = _EnumStore(
        20,
        EnumDefinition.from_mapping({10: "新", 20: "新次"}),
        is_writable=False,
    )
    old, new = EnumBinding(old_store), EnumBinding(new_store)
    view = EnumComboBox(old, wheel_requires_focus=True)
    requests: list[int] = []

    def request(value: int) -> bool:
        """候補の同期ではなく明示入力だけを記録する。"""
        requests.append(value)
        return False

    view.setValueRequestHandler(request)
    invalid = EnumViewModel()
    invalid.dispose()
    try:
        with pytest.raises(RuntimeError):
            view.set_source(invalid)
        assert view.view_model is old.view_model
        view.show()
        view.showPopup()
        _events()
        view.set_source(new if binding_source else new.view_model)
        assert not view.view().isVisible()
        assert view.view_model is new.view_model
        assert view.currentText() == "新次"
        assert [view.itemText(index) for index in range(view.count())] == [
            "新",
            "新次",
        ]
        assert view.wheel_requires_focus()
        assert not view.isEnabled()
        assert not old.is_disposed
        assert old_store.writes == new_store.writes == 0
        old_store.value = 1
        old.refresh()
        assert view.currentText() == "新次"
        assert not view.isEnabled()
        old.dispose()
        _events()
        new_store.is_writable = True
        new.refresh()
        assert view.isEnabled()
        view.setCurrentIndex(0)
        assert requests == [10]
        assert new_store.value == 10
        assert old_store.writes == 0 and new_store.writes == 1
    finally:
        view.deleteLater()
        old.dispose()
        new.dispose()
        invalid.deleteLater()
        _events()


@pytest.mark.parametrize("binding_source", [False, True])
def test_string_source_replacement_discards_draft_conflict_and_text_undo(
    qt_application: qt.QApplication, binding_source: bool
) -> None:
    """旧正本の下書き・競合・入力履歴を新正本へ持ち越さずhandlerを保持する。"""
    del qt_application
    old_store, new_store = _StringStore("旧"), _StringStore(
        "新", is_writable=False
    )
    old, new = StringBinding(old_store), StringBinding(new_store)
    view = StringLineEdit(old, select_all_on_mouse_focus=False)
    requests: list[str] = []

    def request(value: str) -> bool:
        """交換後の確定入力だけを記録する。"""
        requests.append(value)
        return False

    view.setValueRequestHandler(request)
    invalid = StringViewModel()
    invalid.dispose()
    try:
        with pytest.raises(RuntimeError):
            view.set_source(invalid)
        assert view.view_model is old.view_model
        view.setText("旧下書き")
        view.textEdited.emit("旧下書き")
        old_store.value = "旧の外部値"
        old.refresh()
        assert view.hasConflict()
        view.set_source(new if binding_source else new.view_model)
        assert view.view_model is new.view_model
        assert view.text() == "新"
        assert not view.hasConflict()
        assert not view.isUndoAvailable()
        assert not view.select_all_on_mouse_focus()
        assert view.isReadOnly()
        assert not old.is_disposed
        view.editingFinished.emit()
        assert old_store.writes == new_store.writes == 0
        old_store.value = "もう一度外部値"
        old.refresh()
        assert view.text() == "新"
        assert view.isReadOnly()
        old.dispose()
        _events()
        new_store.is_writable = True
        new.refresh()
        assert not view.isReadOnly()
        view.setText("新確定値")
        view.textEdited.emit("新確定値")
        view.returnPressed.emit()
        assert requests == ["新確定値"]
        assert new_store.value == "新確定値"
        assert old_store.writes == 0 and new_store.writes == 1
    finally:
        view.deleteLater()
        old.dispose()
        new.dispose()
        invalid.deleteLater()
        _events()


@pytest.mark.parametrize("kind", ["bool", "enum", "string"])
def test_queued_old_source_destruction_does_not_disable_reconnected_view(
    qt_application: qt.QApplication, kind: Literal["bool", "enum", "string"]
) -> None:
    """既に予約された旧正本の破棄通知を、交換後の入力欄へ適用しない。"""
    del qt_application
    if kind == "bool":
        old = BoolViewModel(False)
        new = BoolViewModel(True)
        view = BoolCheckBox(old)
        old.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        view.set_source(new)
        _events()
        assert view.isEnabled()
        assert view.isChecked()
        view.deleteLater()
        new.deleteLater()
    elif kind == "enum":
        definition = EnumDefinition.from_mapping({0: "旧", 1: "新"})
        old_enum = EnumViewModel(0, definition=definition)
        new_enum = EnumViewModel(1, definition=definition)
        combo = EnumComboBox(old_enum)
        old_enum.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        combo.set_source(new_enum)
        _events()
        assert combo.isEnabled()
        assert combo.currentText() == "新"
        combo.deleteLater()
        new_enum.deleteLater()
    else:
        old_string = StringViewModel("旧")
        new_string = StringViewModel("新")
        line = StringLineEdit(old_string)
        old_string.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        line.set_source(new_string)
        _events()
        assert not line.isReadOnly()
        assert line.text() == "新"
        line.deleteLater()
        new_string.deleteLater()
    _events()


@pytest.mark.parametrize("kind", ["bool", "enum", "string"])
def test_source_replacement_inside_handler_never_writes_to_previous_source(
    qt_application: qt.QApplication, kind: Literal["bool", "enum", "string"]
) -> None:
    """入力handler中の再接続後に、古いCommandを実行しない。"""
    del qt_application
    if kind == "bool":
        old, new = BoolViewModel(False), BoolViewModel(True)
        view = BoolCheckBox(old)

        def request_bool(_value: bool) -> bool:
            """入力処理中に別の正本へ交換する。"""
            view.set_source(new)
            return False

        view.setValueRequestHandler(request_bool)
        view.click()
        assert old.value.value is False
        assert new.value.value is True
        assert view.isChecked()
        view.deleteLater()
        old.deleteLater()
        new.deleteLater()
    elif kind == "enum":
        definition = EnumDefinition.from_mapping({0: "旧", 1: "新"})
        old_enum = EnumViewModel(0, definition=definition)
        new_enum = EnumViewModel(0, definition=definition)
        combo = EnumComboBox(old_enum)

        def request_enum(_value: int) -> bool:
            """入力処理中に別の正本へ交換する。"""
            combo.set_source(new_enum)
            return False

        combo.setValueRequestHandler(request_enum)
        combo.setCurrentIndex(1)
        assert old_enum.value.value == new_enum.value.value == 0
        assert combo.currentIndex() == 0
        combo.deleteLater()
        old_enum.deleteLater()
        new_enum.deleteLater()
    else:
        old_string, new_string = StringViewModel("旧"), StringViewModel("新")
        line = StringLineEdit(old_string)

        def request_string(_value: str) -> bool:
            """入力処理中に別の正本へ交換する。"""
            line.set_source(new_string)
            return False

        line.setValueRequestHandler(request_string)
        line.setText("旧下書き")
        line.textEdited.emit("旧下書き")
        line.returnPressed.emit()
        assert old_string.value.value == "旧"
        assert new_string.value.value == line.text() == "新"
        line.deleteLater()
        old_string.deleteLater()
        new_string.deleteLater()
    _events()
