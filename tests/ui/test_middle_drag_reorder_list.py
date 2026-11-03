# coding: utf-8
"""左選択と中ドラッグの分離、行間通知、中断、端スクロールを検証する。"""

from collections.abc import Iterator

import pytest

from bd_util.ui import ListReorderRequest, MiddleDragReorderListWidget, qt


@pytest.fixture
def widget(
    qt_application: qt.QApplication,
) -> Iterator[MiddleDragReorderListWidget]:
    """スクロール可能な縦一覧を表示し、検証後にQt objectを解放する。"""
    del qt_application
    view = MiddleDragReorderListWidget()
    for row in range(80):
        view.addItem(f"row {row}")
    view.resize(260, 170)
    view.show()
    qt.QApplication.processEvents()
    try:
        yield view
    finally:
        view.cancel_reorder()
        view.close()
        view.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


def _point(
    widget: MiddleDragReorderListWidget, row: int, *, before: bool = False
) -> qt.QPoint:
    """表示行の中央か、行の手前へ挿入する座標を返す。"""
    rect = widget.visualItemRect(widget.item(row))
    return (
        qt.QPoint(rect.center().x(), rect.top() + 1)
        if before
        else rect.center()
    )


def _mouse(
    widget: MiddleDragReorderListWidget,
    kind: qt.QEvent.Type,
    position: qt.QPoint,
    button: qt.Qt.MouseButton = qt.Qt.MouseButton.MiddleButton,
    modifiers: qt.Qt.KeyboardModifier = qt.Qt.KeyboardModifier.NoModifier,
) -> None:
    """viewportへ実座標付きの押下・移動・解放を送る。"""
    viewport = widget.viewport()
    event = qt.QtGui.QMouseEvent(
        kind,
        qt.QPointF(position),
        qt.QPointF(viewport.mapToGlobal(position)),
        (
            qt.Qt.MouseButton.NoButton
            if kind == qt.QEvent.Type.MouseMove
            else button
        ),
        (
            qt.Qt.MouseButton.NoButton
            if kind == qt.QEvent.Type.MouseButtonRelease
            else button
        ),
        modifiers,
    )
    qt.QApplication.sendEvent(viewport, event)


def _drag(
    widget: MiddleDragReorderListWidget, origin: int, destination: qt.QPoint
) -> None:
    """中押下から移動、解放までを一つの操作として送る。"""
    _mouse(widget, qt.QEvent.Type.MouseButtonPress, _point(widget, origin))
    _mouse(widget, qt.QEvent.Type.MouseMove, destination)
    _mouse(widget, qt.QEvent.Type.MouseButtonRelease, destination)


def _selected(widget: MiddleDragReorderListWidget) -> tuple[int, ...]:
    """選択中の行番号を一覧の表示順で返す。"""
    return tuple(sorted(widget.row(item) for item in widget.selectedItems()))


def _wait_for_scroll() -> None:
    """Qtのタイマーが複数回進むまでイベント処理を行う。"""
    loop = qt.QtCore.QEventLoop()
    timer = qt.QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(loop.quit)
    timer.start(180)
    loop.exec()


def test_left_drag_ctrl_shift_and_keyboard_remain_standard(
    widget: MiddleDragReorderListWidget,
) -> None:
    """左範囲選択とCtrl・Shift・方向キーを並び替えから独立して保つ。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    _mouse(
        widget,
        qt.QEvent.Type.MouseButtonPress,
        _point(widget, 1),
        qt.Qt.MouseButton.LeftButton,
    )
    _mouse(
        widget,
        qt.QEvent.Type.MouseMove,
        _point(widget, 4),
        qt.Qt.MouseButton.LeftButton,
    )
    _mouse(
        widget,
        qt.QEvent.Type.MouseButtonRelease,
        _point(widget, 4),
        qt.Qt.MouseButton.LeftButton,
    )
    assert _selected(widget) == (1, 2, 3, 4)
    for kind in (
        qt.QEvent.Type.MouseButtonPress,
        qt.QEvent.Type.MouseButtonRelease,
    ):
        _mouse(
            widget,
            kind,
            _point(widget, 6),
            qt.Qt.MouseButton.LeftButton,
            qt.Qt.KeyboardModifier.ControlModifier,
        )
    assert _selected(widget) == (1, 2, 3, 4, 6)
    for kind in (
        qt.QEvent.Type.MouseButtonPress,
        qt.QEvent.Type.MouseButtonRelease,
    ):
        _mouse(widget, kind, _point(widget, 2), qt.Qt.MouseButton.LeftButton)
    for kind in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        qt.QApplication.sendEvent(
            widget,
            qt.QtGui.QKeyEvent(
                kind, qt.Qt.Key.Key_Down, qt.Qt.KeyboardModifier.ShiftModifier
            ),
        )
    assert _selected(widget) == (2, 3)
    assert calls == []


def test_middle_drag_preserves_selected_rows_and_notifies_original_gap(
    widget: MiddleDragReorderListWidget,
) -> None:
    """非連続選択を保ち、元の行間を一回通知して項目は変更しない。"""
    widget.setCurrentRow(1)
    widget.item(3).setSelected(True)
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    _drag(widget, 3, _point(widget, 6, before=True))
    assert calls == [ListReorderRequest((1, 3), 6)]
    assert _selected(widget) == (1, 3)
    assert [widget.item(row).text() for row in range(80)] == [
        f"row {row}" for row in range(80)
    ]


def test_middle_press_outside_selection_selects_only_pressed_row(
    widget: MiddleDragReorderListWidget,
) -> None:
    """選択外からの中ドラッグは押した一行だけを対象にする。"""
    widget.setCurrentRow(0)
    widget.item(2).setSelected(True)
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    _drag(widget, 4, _point(widget, 1, before=True))
    assert calls == [ListReorderRequest((4,), 1)]
    assert _selected(widget) == (4,)


def test_click_short_motion_and_unchanged_gap_emit_nothing(
    widget: MiddleDragReorderListWidget,
) -> None:
    """クリックと微小移動、連続選択の元位置への解放は要求しない。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    point = _point(widget, 1)
    _mouse(widget, qt.QEvent.Type.MouseButtonPress, point)
    _mouse(widget, qt.QEvent.Type.MouseMove, point + qt.QPoint(1, 0))
    _mouse(widget, qt.QEvent.Type.MouseButtonRelease, point + qt.QPoint(1, 0))
    widget.item(2).setSelected(True)
    _drag(widget, 1, _point(widget, 3, before=True))
    assert calls == []


def test_top_and_bottom_gaps_include_empty_space(
    widget: MiddleDragReorderListWidget,
) -> None:
    """先頭と最終行後の空白も、元一覧の0と行数で通知する。"""
    widget.clear()
    for text in ("first", "second", "last"):
        widget.addItem(text)
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    _drag(widget, 2, _point(widget, 0, before=True))
    _drag(widget, 0, qt.QPoint(30, widget.viewport().height() - 30))
    assert calls == [ListReorderRequest((2,), 0), ListReorderRequest((0,), 3)]


@pytest.mark.parametrize(
    "outside", [qt.QPoint(-1, 20), qt.QPoint(30, -1), qt.QPoint(30, 500)]
)
def test_outside_release_cancels_and_restores_cursor(
    widget: MiddleDragReorderListWidget, outside: qt.QPoint
) -> None:
    """一覧外への解放では通知せず、利用側のカーソル設定を戻す。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    widget.viewport().setCursor(qt.Qt.CursorShape.CrossCursor)
    _drag(widget, 1, outside)
    assert calls == []
    assert widget.viewport().cursor().shape() == qt.Qt.CursorShape.CrossCursor


@pytest.mark.parametrize(
    "kind",
    [
        qt.QEvent.Type.Hide,
        qt.QEvent.Type.WindowDeactivate,
        qt.QEvent.Type.ApplicationDeactivate,
        qt.QEvent.Type.UngrabMouse,
    ],
)
def test_interruption_prevents_late_drop(
    widget: MiddleDragReorderListWidget, kind: qt.QEvent.Type
) -> None:
    """非表示・非アクティブ化・grab解除後の解放は古い要求を送らない。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    _mouse(widget, qt.QEvent.Type.MouseButtonPress, _point(widget, 1))
    _mouse(widget, qt.QEvent.Type.MouseMove, _point(widget, 5, before=True))
    qt.QApplication.sendEvent(widget, qt.QEvent(kind))
    _mouse(
        widget,
        qt.QEvent.Type.MouseButtonRelease,
        _point(widget, 5, before=True),
    )
    assert calls == []


def test_escape_and_public_cancel_prevent_late_drop(
    widget: MiddleDragReorderListWidget,
) -> None:
    """Escと明示取消の後は解放で通知せず、新しい操作を始められる。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    for escape in (True, False):
        _mouse(widget, qt.QEvent.Type.MouseButtonPress, _point(widget, 1))
        _mouse(
            widget, qt.QEvent.Type.MouseMove, _point(widget, 5, before=True)
        )
        if escape:
            qt.QApplication.sendEvent(
                widget,
                qt.QtGui.QKeyEvent(
                    qt.QEvent.Type.KeyPress,
                    qt.Qt.Key.Key_Escape,
                    qt.Qt.KeyboardModifier.NoModifier,
                ),
            )
        else:
            widget.cancel_reorder()
        _mouse(
            widget,
            qt.QEvent.Type.MouseButtonRelease,
            _point(widget, 5, before=True),
        )
    assert calls == []
    _drag(widget, 1, _point(widget, 5, before=True))
    assert calls == [ListReorderRequest((1,), 5)]


@pytest.mark.parametrize(
    "change", ["insert", "remove", "reset", "text", "selection"]
)
def test_model_or_selection_change_discards_snapshot(
    widget: MiddleDragReorderListWidget, change: str
) -> None:
    """操作中の項目と選択の更新は古い行番号による移動を取り消す。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    destination = _point(widget, 5, before=True)
    _mouse(widget, qt.QEvent.Type.MouseButtonPress, _point(widget, 1))
    _mouse(widget, qt.QEvent.Type.MouseMove, destination)
    if change == "insert":
        widget.insertItem(0, "new")
    elif change == "remove":
        widget.takeItem(0)
    elif change == "reset":
        widget.clear()
    elif change == "text":
        widget.item(1).setText("changed")
    else:
        widget.item(2).setSelected(True)
    _mouse(widget, qt.QEvent.Type.MouseButtonRelease, destination)
    assert calls == []


def test_edge_timer_scrolls_and_cancellation_stops_it(
    widget: MiddleDragReorderListWidget,
) -> None:
    """下端で待つだけで挿入先が進み、取消後はスクロールを止める。"""
    calls: list[object] = []
    widget.reorder_requested.connect(calls.append)
    bottom = qt.QPoint(30, widget.viewport().height() - 2)
    _mouse(widget, qt.QEvent.Type.MouseButtonPress, _point(widget, 1))
    _mouse(widget, qt.QEvent.Type.MouseMove, bottom)
    _wait_for_scroll()
    assert widget.verticalScrollBar().value() > 0
    _mouse(widget, qt.QEvent.Type.MouseButtonRelease, bottom)
    assert len(calls) == 1
    assert isinstance(calls[0], ListReorderRequest)
    assert calls[0].before_row > 10
    stopped = widget.verticalScrollBar().value()
    _wait_for_scroll()
    assert widget.verticalScrollBar().value() == stopped


def test_top_edge_scrolls_back_towards_first_row(
    widget: MiddleDragReorderListWidget,
) -> None:
    """中段からのドラッグは上端で先頭方向へ自動スクロールする。"""
    widget.scrollToItem(
        widget.item(40), qt.QAbstractItemView.ScrollHint.PositionAtCenter
    )
    qt.QApplication.processEvents()
    previous = widget.verticalScrollBar().value()
    _mouse(widget, qt.QEvent.Type.MouseButtonPress, _point(widget, 40))
    _mouse(widget, qt.QEvent.Type.MouseMove, qt.QPoint(30, 2))
    _wait_for_scroll()
    assert widget.verticalScrollBar().value() < previous
    widget.cancel_reorder()


def test_drop_callback_can_rebuild_items_synchronously(
    widget: MiddleDragReorderListWidget,
) -> None:
    """通知内で一覧を再構築しても追加通知や監視の取り残しを起こさない。"""
    calls: list[ListReorderRequest] = []

    def rebuild(request: object) -> None:
        """利用側によるデータ反映と一覧の作り直しを再現する。"""
        assert isinstance(request, ListReorderRequest)
        calls.append(request)
        widget.clear()
        widget.addItem("rebuilt")

    widget.reorder_requested.connect(rebuild)
    _drag(widget, 1, _point(widget, 5, before=True))
    assert calls == [ListReorderRequest((1,), 5)]
    assert widget.count() == 1
