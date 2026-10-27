# coding: utf-8
"""実際の入力eventから、一時画面の表示起点を選ぶ契約を確認する。"""

import pytest

from bd_util.ui import qt
from bd_util.ui.dialog_anchor import DialogAnchorTracker


def _key_press(widget: qt.QWidget) -> None:
    """対象Widgetへ通常処理を妨げないキー入力を送る。"""
    event = qt.QtGui.QKeyEvent(
        qt.QEvent.Type.KeyPress,
        qt.Qt.Key.Key_F1,
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(widget, event)


def _mouse_event(widget: qt.QWidget, kind: qt.QEvent.Type) -> None:
    """対象Widgetへ実際のマウスeventを送る。"""
    event = qt.QtGui.QMouseEvent(
        kind,
        qt.QPointF(2, 2),
        qt.QPointF(widget.mapToGlobal(qt.QPoint(2, 2))),
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(widget, event)


def test_keyboard_anchor_uses_focused_control_in_its_owner(qt_application):
    """所有画面内でキーを押すと、現在focusのある操作部品を起点にする。"""
    root = qt.QWidget()
    root.setGeometry(100, 200, 420, 280)
    button = qt.QPushButton("操作", root)
    button.setGeometry(30, 40, 120, 32)
    tracker = DialogAnchorTracker(root)
    try:
        root.show()
        root.activateWindow()
        button.setFocus()
        qt_application.processEvents()
        assert qt.QApplication.focusWidget() is button
        _key_press(root)
        assert tracker.position() == button.mapToGlobal(button.rect().center())
    finally:
        tracker.dispose()
        root.deleteLater()
        qt_application.processEvents()


@pytest.mark.parametrize(
    "kind",
    (
        qt.QEvent.Type.MouseButtonPress,
        qt.QEvent.Type.MouseButtonRelease,
        qt.QEvent.Type.MouseButtonDblClick,
    ),
)
def test_mouse_anchor_reads_current_cursor_after_each_operation(
    qt_application, monkeypatch, kind
):
    """各マウス入力でキー起点を解除し、返す座標はカーソル位置のコピーにする。"""
    root = qt.QWidget()
    tracker = DialogAnchorTracker(root)
    cursor = qt.QPoint(721, 543)
    monkeypatch.setattr(qt.QCursor, "pos", staticmethod(lambda: cursor))
    try:
        _key_press(root)
        _mouse_event(root, kind)
        position = tracker.position()
        assert position == cursor
        position.setX(-100)
        assert cursor.x() == 721
        cursor.setY(789)
        assert tracker.position() == qt.QPoint(721, 789)
    finally:
        tracker.dispose()
        root.deleteLater()
        qt_application.processEvents()


@pytest.mark.parametrize("popup_kind", ("menu", "combo"))
def test_owned_popup_keyboard_input_is_an_anchor(
    qt_application, monkeypatch, popup_kind
):
    """QMenuとComboBox popupのキー入力も、所有画面の操作として扱う。"""
    root = qt.QWidget()
    tracker = DialogAnchorTracker(root)
    monkeypatch.setattr(
        qt.QApplication, "focusWidget", staticmethod(lambda: None)
    )
    if popup_kind == "menu":
        popup = qt.QMenu(root)
        receiver = popup
    else:
        combo = qt.QComboBox(root)
        combo.addItem("項目")
        receiver = combo.view().viewport()
    try:
        _key_press(receiver)
        assert tracker.position() == receiver.mapToGlobal(
            receiver.rect().center()
        )
    finally:
        tracker.dispose()
        root.deleteLater()
        qt_application.processEvents()


def test_unrelated_window_input_does_not_change_its_anchor(
    qt_application, monkeypatch
):
    """別ツールのキーとマウス入力を、所有画面の入力方法へ反映しない。"""
    root = qt.QWidget()
    other = qt.QWidget()
    tracker = DialogAnchorTracker(root)
    cursor = qt.QPoint(721, 543)
    monkeypatch.setattr(qt.QCursor, "pos", staticmethod(lambda: cursor))
    monkeypatch.setattr(
        qt.QApplication, "focusWidget", staticmethod(lambda: other)
    )
    try:
        _key_press(other)
        assert tracker.position() == cursor
        _key_press(root)
        _mouse_event(other, qt.QEvent.Type.MouseButtonPress)
        assert tracker.position() == root.mapToGlobal(root.rect().center())
    finally:
        tracker.dispose()
        root.deleteLater()
        other.deleteLater()
        qt_application.processEvents()


def test_deleted_key_source_falls_back_to_explicit_control_then_owner(
    qt_application, monkeypatch
):
    """入力元が破棄された場合、明示した部品と所有画面へ起点を補完する。"""
    root = qt.QWidget()
    button = qt.QPushButton(root)
    button.setGeometry(30, 40, 120, 32)
    explicit = qt.QPushButton(root)
    explicit.setGeometry(210, 140, 120, 32)
    tracker = DialogAnchorTracker(root)
    monkeypatch.setattr(
        qt.QApplication, "focusWidget", staticmethod(lambda: None)
    )
    try:
        _key_press(button)
        button.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        assert not qt.isValid(button)
        assert tracker.position(explicit) == explicit.mapToGlobal(
            explicit.rect().center()
        )
        assert tracker.position() == root.mapToGlobal(root.rect().center())
    finally:
        tracker.dispose()
        root.deleteLater()
        qt_application.processEvents()


def test_unhandled_key_propagation_keeps_origin_until_a_new_key(
    qt_application, monkeypatch
):
    """未処理キーの親への伝播と、親自身への次のキー入力を区別する。"""
    root = qt.QWidget()
    button = qt.QPushButton(root)
    button.setGeometry(30, 40, 120, 32)
    tracker = DialogAnchorTracker(root)
    monkeypatch.setattr(
        qt.QApplication, "focusWidget", staticmethod(lambda: None)
    )
    try:
        _key_press(button)
        assert tracker.position() == button.mapToGlobal(button.rect().center())
        _key_press(root)
        assert tracker.position() == root.mapToGlobal(root.rect().center())
    finally:
        tracker.dispose()
        root.deleteLater()
        qt_application.processEvents()


def test_dispose_removes_application_filter_and_can_repeat(
    qt_application, monkeypatch
):
    """終了後は監視を解除し、繰返し終了しても追加eventを受け取らない。"""

    class RecordingTracker(DialogAnchorTracker):
        """所有画面へのキーeventの受信回数だけを記録する。"""

        def __init__(self, source: qt.QWidget) -> None:
            """監視の前に受信回数を初期化する。"""
            self.key_count = 0
            super().__init__(source)

        def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
            """キーeventを数えてから通常の起点判定へ渡す。"""
            if event.type() == qt.QEvent.Type.KeyPress:
                self.key_count += 1
            return super().eventFilter(watched, event)

    root = qt.QWidget()
    tracker = RecordingTracker(root)
    cursor = qt.QPoint(721, 543)
    monkeypatch.setattr(qt.QCursor, "pos", staticmethod(lambda: cursor))
    try:
        _key_press(root)
        assert tracker.key_count == 1
        tracker.dispose()
        tracker.dispose()
        _key_press(root)
        assert tracker.key_count == 1
        assert tracker.position() == cursor
    finally:
        root.deleteLater()
        qt_application.processEvents()


def test_owner_deletion_disposes_tracker_safely(qt_application, monkeypatch):
    """所有画面の破棄後も、保持されたwrapperから安全に終了できる。"""
    root = qt.QWidget()
    tracker = DialogAnchorTracker(root)
    cursor = qt.QPoint(721, 543)
    monkeypatch.setattr(qt.QCursor, "pos", staticmethod(lambda: cursor))
    _key_press(root)
    root.deleteLater()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    assert not qt.isValid(tracker)
    tracker.dispose()
    assert tracker.position() == cursor
