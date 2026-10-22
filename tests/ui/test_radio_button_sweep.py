# coding: utf-8
"""なぞり選択の通常操作、経路判定、中断と登録範囲を検証する。"""

from collections.abc import Iterator
from functools import partial
from typing import Protocol, cast

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


class _RadioContainer(Protocol):
    """Qtの子検索を、テストで指定するラジオボタン型へ限定する。"""

    def findChildren(
        self, kind: type[qt.QRadioButton]
    ) -> list[qt.QRadioButton]:
        """指定したラジオボタン型の子を列挙する。"""
        raise NotImplementedError


def _all_buttons(panel: qt.QWidget) -> list[qt.QRadioButton]:
    """Qtの型が未確定な列挙結果を、指定したボタン型へ限定する。"""
    return cast(_RadioContainer, panel).findChildren(qt.QRadioButton)


def _buttons(panel: qt.QWidget, text: str) -> list[qt.QRadioButton]:
    """指定した列のボタンを表示順に返す。"""
    return [button for button in _all_buttons(panel) if button.text() == text]


def _sweep(panel: qt.QWidget) -> RadioButtonSweep:
    """表示範囲内のラジオボタンだけを操作対象に登録する。"""
    sweep = RadioButtonSweep(panel)
    for button in _all_buttons(panel):
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


@pytest.mark.parametrize("apply_unchanged", [False, True])
@pytest.mark.parametrize("column", ["key", "ch"])
def test_explicit_writer_visits_once_without_changing_display(
    panel: qt.QWidget, apply_unchanged: bool, column: str
) -> None:
    """表示同期しない入力先でも一回だけ要求し、同値は明示指定で許可する。"""
    buttons = _buttons(panel, column)
    calls: list[int] = []
    sweep = RadioButtonSweep(panel)
    for index, button in enumerate(buttons):
        sweep.add_button(
            button,
            on_change=partial(calls.append, index),
            apply_unchanged=apply_unchanged,
        )
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    expected = list(range(5)) if column == "ch" or apply_unchanged else []
    assert calls == expected
    assert all(button.isChecked() == (column == "key") for button in buttons)
    assert not sweep.is_active


def test_group_excludes_crossed_columns_and_restarts_from_new_origin(
    panel: qt.QWidget,
) -> None:
    """等しいgroupだけを要求し、横断や往復でも別列へ波及しない。"""
    calls: list[qt.QRadioButton] = []
    sweep = RadioButtonSweep(panel)
    for button in _all_buttons(panel):
        sweep.add_button(
            button,
            on_change=partial(calls.append, button),
            apply_unchanged=True,
            group=[button.text()],
        )
    channels, hidden = _buttons(panel, "ch"), _buttons(panel, "hide")
    _mouse(channels[0], qt.QEvent.Type.MouseButtonPress, channels[0])
    _mouse(channels[0], qt.QEvent.Type.MouseMove, hidden[2])
    _mouse(channels[0], qt.QEvent.Type.MouseMove, channels[-1])
    _mouse(channels[0], qt.QEvent.Type.MouseMove, channels[0])
    _mouse(channels[0], qt.QEvent.Type.MouseButtonRelease, channels[0])
    assert channels[0] in calls and channels[-1] in calls
    assert all(button.text() == "ch" for button in calls)
    assert len(calls) == len(set(calls))
    calls.clear()
    _mouse(hidden[0], qt.QEvent.Type.MouseButtonPress, hidden[0])
    _mouse(hidden[0], qt.QEvent.Type.MouseMove, hidden[-1])
    _mouse(hidden[0], qt.QEvent.Type.MouseButtonRelease, hidden[-1])
    assert calls == hidden


def test_unchanged_click_fallback_and_clear_restore_default_registration(
    panel: qt.QWidget,
) -> None:
    """同値要求はclickedへ委譲でき、再登録時は入力設定を残さない。"""
    buttons = _buttons(panel, "key")
    calls: list[int] = []
    sweep = RadioButtonSweep(panel)
    for index, button in enumerate(buttons):
        button.clicked.connect(lambda _checked=False, i=index: calls.append(i))
        sweep.add_button(button, apply_unchanged=True, group="key")
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert calls == list(range(5))
    sweep.clear()
    calls.clear()
    for button in buttons:
        sweep.add_button(button)
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
    assert not calls


def test_writer_exception_finishes_and_invalid_bool_is_rejected(
    panel: qt.QWidget,
) -> None:
    """明示入力の失敗で操作を閉じ、bool以外の同値指定を登録前に拒否する。"""
    button = _buttons(panel, "key")[0]

    class FailureSweep(RadioButtonSweep):
        """Qtに握りつぶされない経路で入力先の例外を確認する。"""

        def apply_for_test(self, target: qt.QRadioButton) -> None:
            """開始済みのなぞりを再現して対象の入力先を呼ぶ。"""
            self._dragging = True
            self._apply(target)

    sweep = FailureSweep(panel)

    def fail() -> None:
        """入力先からの失敗を再現する。"""
        raise RuntimeError("入力失敗")

    with pytest.raises(TypeError, match="apply_unchanged"):
        sweep.add_button(button, apply_unchanged=cast(bool, 1))
    sweep.add_button(button, on_change=fail, apply_unchanged=True)
    with pytest.raises(RuntimeError, match="入力失敗"):
        sweep.apply_for_test(button)
    assert not sweep.is_active
