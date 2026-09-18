# coding: utf-8
"""なぞり選択の通常操作、経路判定、中断と登録範囲を検証する。"""

from collections.abc import Iterator

import pytest

from bd_util.ui import RadioButtonSweep, qt


@pytest.fixture
def panel(qt_application: qt.QApplication) -> Iterator[qt.QWidget]:
    """独立した5行のラジオボタンを表示し、検証後に監視を破棄する。"""
    del qt_application
    widget = qt.QWidget()
    widget.resize(240, 180)
    for index in range(5):
        group = qt.QtWidgets.QButtonGroup(widget)
        for column, text in enumerate(("key", "ch", "hide")):
            button = qt.QRadioButton(text, widget)
            button.setGeometry(80 * column, 32 * index, 75, 28)
            group.addButton(button)
            if column == 0:
                button.setChecked(True)
    widget.show()
    qt.QApplication.processEvents()
    yield widget
    widget.close()
    widget.deleteLater()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


def _buttons(panel: qt.QWidget, text: str) -> list[qt.QRadioButton]:
    """指定した列のボタンを表示順に返す。"""
    return [
        button
        for button in panel.findChildren(qt.QRadioButton)
        if button.text() == text
    ]


def _sweep(panel: qt.QWidget) -> RadioButtonSweep:
    """表示範囲内のラジオボタンだけを操作対象に登録する。"""
    sweep = RadioButtonSweep(panel)
    for button in panel.findChildren(qt.QRadioButton):
        sweep.add_button(button)
    return sweep


def _mouse(
    origin: qt.QRadioButton, kind: qt.QEvent.Type, target: qt.QRadioButton
) -> None:
    """押下元へ送り続けるQtのマウス配送を、移動先の座標で再現する。"""
    position = target.mapToGlobal(qt.QPoint(10, target.height() // 2))
    event = qt.QtGui.QMouseEvent(
        kind,
        qt.QPointF(origin.mapFromGlobal(position)),
        qt.QPointF(position),
        (
            qt.Qt.MouseButton.NoButton
            if kind == qt.QEvent.Type.MouseMove
            else qt.Qt.MouseButton.LeftButton
        ),
        (
            qt.Qt.MouseButton.NoButton
            if kind == qt.QEvent.Type.MouseButtonRelease
            else qt.Qt.MouseButton.LeftButton
        ),
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(origin, event)


def test_fast_sweep_visits_intermediate_rows_once(panel: qt.QWidget) -> None:
    """一回の移動でも途中の行を選択し、滞在やreleaseで重複入力しない。"""
    sweep = _sweep(panel)
    buttons = _buttons(panel, "ch")
    calls: list[str] = []
    sweep.started.connect(lambda: calls.append("start"))
    sweep.finished.connect(lambda: calls.append("finish"))
    for index, button in enumerate(buttons):
        button.clicked.connect(
            lambda _checked=False, i=index: calls.append(str(i))
        )
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    assert not sweep.is_active
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    assert sweep.is_active
    assert all(button.isChecked() for button in buttons)
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
    assert calls == ["start", "0", "1", "2", "3", "4", "finish"]
    assert not sweep.is_active


def test_single_click_and_keyboard_remain_standard(panel: qt.QWidget) -> None:
    """単発クリックはreleaseで選択され、キー入力もそのまま利用できる。"""
    sweep = _sweep(panel)
    button = _buttons(panel, "ch")[0]
    _mouse(button, qt.QEvent.Type.MouseButtonPress, button)
    assert not button.isChecked()
    _mouse(button, qt.QEvent.Type.MouseButtonRelease, button)
    assert button.isChecked()
    assert not sweep.is_active
    hidden = _buttons(panel, "hide")[0]
    for kind in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        qt.QApplication.sendEvent(
            hidden,
            qt.QtGui.QKeyEvent(
                kind, qt.Qt.Key.Key_Space, qt.Qt.KeyboardModifier.NoModifier
            ),
        )
    assert hidden.isChecked()


@pytest.mark.parametrize(
    "kind",
    [qt.QEvent.Type.FocusOut, qt.QEvent.Type.UngrabMouse],
)
def test_interruption_prevents_late_click(
    panel: qt.QWidget, kind: qt.QEvent.Type
) -> None:
    """中断後に押下元へ戻って解放しても、古いクリックを発生させない。"""
    sweep = _sweep(panel)
    buttons = _buttons(panel, "ch")
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[1])
    qt.QApplication.sendEvent(buttons[0], qt.QEvent(kind))
    assert not sweep.is_active
    _buttons(panel, "key")[0].setChecked(True)
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert not buttons[0].isChecked()
    assert buttons[1].isChecked()
    assert not buttons[2].isChecked()


def test_selected_start_disabled_and_unregistered_targets(
    panel: qt.QWidget,
) -> None:
    """選択済みから開始でき、無効・未登録の行は通過しても変更しない。"""
    buttons = _buttons(panel, "ch")
    buttons[0].setChecked(True)
    buttons[1].setEnabled(False)
    sweep = RadioButtonSweep(panel)
    for button in (buttons[0], buttons[1], buttons[3], buttons[4]):
        sweep.add_button(button)
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
    assert [button.isChecked() for button in buttons] == [
        True,
        False,
        False,
        True,
        True,
    ]


def test_scroll_viewport_replacement_and_clipping(panel: qt.QWidget) -> None:
    """viewport差し替え後も使え、表示範囲から外れた行には入力しない。"""
    scroll = qt.QScrollArea()
    scroll.resize(270, 120)
    scroll.setWidget(panel)
    sweep = RadioButtonSweep(scroll)
    buttons = _buttons(panel, "ch")
    for button in buttons:
        sweep.add_button(button)
    scroll.show()
    qt.QApplication.processEvents()
    try:
        # 古いviewportの寿命と、操作補助の寿命を分離して確認する
        contents = scroll.takeWidget()
        scroll.setViewport(qt.QWidget())
        scroll.setWidget(contents)
        qt.QApplication.processEvents()
        _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
        _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
        _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
        assert buttons[0].isChecked()
        assert buttons[1].isChecked()
        assert not buttons[-1].isChecked()
    finally:
        sweep.dispose()
        scroll.takeWidget()
        scroll.close()
        scroll.deleteLater()


def test_end_during_callback_stops_remaining_targets(
    panel: qt.QWidget,
) -> None:
    """入力callbackが操作を終了したら、残りの経路への入力を止める。"""
    sweep = _sweep(panel)
    buttons = _buttons(panel, "ch")
    buttons[1].clicked.connect(sweep.finish)
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    assert [button.isChecked() for button in buttons] == [
        True,
        True,
        False,
        False,
        False,
    ]
    assert not sweep.is_active
