# coding: utf-8
"""チェックボックスの固定状態入力と通常操作・中断を検証する。"""

from collections.abc import Iterator
from functools import partial
from typing import Protocol, cast

import pytest

from bd_util.ui import CheckBoxSweep, RadioButtonSweep, qt


@pytest.fixture
def panel(qt_application: qt.QApplication) -> Iterator[qt.QWidget]:
    """状態を混在させられる五行のチェックボックスを表示する。"""
    del qt_application
    widget = qt.QWidget()
    widget.resize(180, 180)
    for index in range(5):
        button = qt.QCheckBox("lock", widget)
        button.setGeometry(0, 32 * index, 75, 28)
    widget.show()
    qt.QApplication.processEvents()
    yield widget
    widget.close()
    widget.deleteLater()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


def _mouse(
    origin: qt.QtWidgets.QAbstractButton,
    kind: qt.QEvent.Type,
    target: qt.QtWidgets.QAbstractButton,
) -> None:
    """マウス取得中と同じく、押下元へ移動先の座標を送る。"""
    position = target.mapToGlobal(qt.QPoint(10, target.height() // 2))
    qt.QApplication.sendEvent(
        origin,
        qt.QtGui.QMouseEvent(
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
        ),
    )


class _CheckBoxContainer(Protocol):
    """Qtの子検索を、テストで指定するチェックボックス型へ限定する。"""

    def findChildren(self, kind: type[qt.QCheckBox]) -> list[qt.QCheckBox]:
        """指定したチェックボックス型の子を列挙する。"""
        raise NotImplementedError


def _buttons(panel: qt.QWidget) -> list[qt.QCheckBox]:
    """Qtの型が未確定な列挙結果を、指定したボタン型へ限定する。"""
    return cast(_CheckBoxContainer, panel).findChildren(qt.QCheckBox)


def _sweep(panel: qt.QWidget) -> CheckBoxSweep:
    """パネル内のチェックボックスだけを操作対象に登録する。"""
    sweep = CheckBoxSweep(panel)
    for button in _buttons(panel):
        sweep.add_button(button)
    return sweep


@pytest.mark.parametrize(
    "initial",
    [
        qt.Qt.CheckState.Unchecked,
        qt.Qt.CheckState.Checked,
        qt.Qt.CheckState.PartiallyChecked,
    ],
)
def test_fast_sweep_paints_fixed_state_without_reversing(
    panel: qt.QWidget, initial: qt.Qt.CheckState
) -> None:
    """高速移動で中間行も揃え、同値や往復では再入力しない。"""
    buttons = _buttons(panel)
    expected = (
        qt.Qt.CheckState.Unchecked
        if initial == qt.Qt.CheckState.Checked
        else qt.Qt.CheckState.Checked
    )
    for button, state in zip(
        buttons,
        (
            initial,
            qt.Qt.CheckState.Unchecked,
            qt.Qt.CheckState.Checked,
            qt.Qt.CheckState.PartiallyChecked,
            qt.Qt.CheckState.Unchecked,
        ),
        strict=True,
    ):
        button.setCheckState(state)
    changes = sum(button.checkState() != expected for button in buttons)
    sweep = _sweep(panel)
    calls: list[str] = []
    sweep.started.connect(lambda: calls.append("start"))
    sweep.finished.connect(lambda: calls.append("finish"))
    for button in buttons:
        button.stateChanged.connect(lambda _state=0: calls.append("change"))
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    assert not sweep.is_active
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    assert sweep.is_active
    assert all(button.checkState() == expected for button in buttons)
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert calls == ["start", *(["change"] * changes), "finish"]


def test_callback_owns_sync_and_mixed_rows_are_visited_once(
    panel: qt.QWidget,
) -> None:
    """入力先が混在表示を保持しても、一操作中に同じ行を再要求しない。"""
    buttons = _buttons(panel)
    calls: list[bool] = []
    sweep = CheckBoxSweep(panel)
    buttons[0].setCheckState(qt.Qt.CheckState.PartiallyChecked)
    sweep.add_button(buttons[0], on_change=calls.append)
    sweep.add_button(buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert calls == [True]
    assert buttons[0].checkState() == qt.Qt.CheckState.PartiallyChecked
    assert buttons[-1].isChecked()
    assert not buttons[1].isChecked()


def test_single_click_and_keyboard_remain_standard(panel: qt.QWidget) -> None:
    """なぞりへ移行しない入力は元のclickedとキー操作を維持する。"""
    sweep = _sweep(panel)
    button = _buttons(panel)[0]
    calls: list[bool] = []
    button.clicked.connect(lambda checked=False: calls.append(checked))
    _mouse(button, qt.QEvent.Type.MouseButtonPress, button)
    assert not button.isChecked()
    _mouse(button, qt.QEvent.Type.MouseButtonRelease, button)
    assert calls == [True]
    assert not sweep.is_active
    for kind in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        qt.QApplication.sendEvent(
            button,
            qt.QtGui.QKeyEvent(
                kind, qt.Qt.Key.Key_Space, qt.Qt.KeyboardModifier.NoModifier
            ),
        )
    assert calls == [True, False]


@pytest.mark.parametrize("family", ["check", "radio"])
def test_crossing_another_button_family_does_not_change_it(
    panel: qt.QWidget, family: str
) -> None:
    """開始した種類だけを操作し、隣の種類を横切っても入力しない。"""
    checks = _buttons(panel)
    radio = qt.QRadioButton("ch", panel)
    radio.setGeometry(80, 0, 75, 28)
    radio.show()
    check_sweep = _sweep(panel)
    radio_sweep = RadioButtonSweep(panel)
    radio_sweep.add_button(radio)
    origin, target = (
        (checks[0], radio) if family == "check" else (radio, checks[0])
    )
    _mouse(origin, qt.QEvent.Type.MouseButtonPress, origin)
    _mouse(origin, qt.QEvent.Type.MouseMove, target)
    _mouse(origin, qt.QEvent.Type.MouseButtonRelease, target)
    assert checks[0].isChecked() == (family == "check")
    assert radio.isChecked() == (family == "radio")
    assert not check_sweep.is_active and not radio_sweep.is_active


@pytest.mark.parametrize(
    "action", ["escape", "hide", "focus", "ungrab", "clear", "dispose"]
)
def test_interruption_prevents_late_input(
    panel: qt.QWidget, action: str
) -> None:
    """途中終了後の移動・解放で追加入力や元のクリックを発生させない。"""
    buttons = _buttons(panel)
    sweep = _sweep(panel)
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[1])
    if action == "escape":
        qt.QApplication.sendEvent(
            buttons[0],
            qt.QtGui.QKeyEvent(
                qt.QEvent.Type.KeyPress,
                qt.Qt.Key.Key_Escape,
                qt.Qt.KeyboardModifier.NoModifier,
            ),
        )
    elif action == "hide":
        panel.hide()
    elif action in ("focus", "ungrab"):
        qt.QApplication.sendEvent(
            buttons[0],
            qt.QEvent(
                qt.QEvent.Type.FocusOut
                if action == "focus"
                else qt.QEvent.Type.UngrabMouse
            ),
        )
    elif action == "clear":
        sweep.clear()
    else:
        sweep.dispose()
    assert not sweep.is_active
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert [button.isChecked() for button in buttons] == [
        True,
        True,
        False,
        False,
        False,
    ]


def test_disabled_hidden_targets_and_callback_finish(
    panel: qt.QWidget,
) -> None:
    """無効・非表示は除外し、callback中の終了では後続行を変更しない。"""
    buttons = _buttons(panel)
    sweep = _sweep(panel)
    buttons[1].setEnabled(False)
    buttons[2].hide()
    buttons[3].toggled.connect(sweep.finish)
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    assert [button.isChecked() for button in buttons] == [
        True,
        False,
        False,
        True,
        False,
    ]
    assert not sweep.is_active


@pytest.mark.parametrize("apply_unchanged", [False, True])
@pytest.mark.parametrize("checked", [False, True])
def test_explicit_same_state_requests_once_and_preserves_display(
    panel: qt.QWidget, apply_unchanged: bool, checked: bool
) -> None:
    """同値の後続行も明示指定時だけ要求し、往復で重複入力しない。"""
    buttons = _buttons(panel)
    calls: list[tuple[int, bool]] = []
    sweep = CheckBoxSweep(panel)

    def record(index: int, value: bool) -> None:
        """表示を更新せず、利用側へ届く要求だけを記録する。"""
        calls.append((index, value))

    for index, button in enumerate(buttons):
        button.setChecked(not checked if index == 0 else checked)
        sweep.add_button(
            button,
            on_change=partial(record, index),
            apply_unchanged=apply_unchanged,
        )
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert calls == [
        (index, checked) for index in (range(5) if apply_unchanged else [0])
    ]
    assert [button.isChecked() for button in buttons] == [
        not checked,
        *([checked] * 4),
    ]
    assert not sweep.is_active


def test_group_limits_targets_and_ungrouped_origin_remains_unrestricted(
    panel: qt.QWidget,
) -> None:
    """開始groupで対象を絞り、Noneからの操作は従来の全登録へ適用する。"""
    buttons = _buttons(panel)
    calls: list[tuple[int, bool]] = []
    sweep = CheckBoxSweep(panel)

    def record(index: int, value: bool) -> None:
        """通過した登録先と固定された入力値を記録する。"""
        calls.append((index, value))

    for index, button in enumerate(buttons):
        sweep.add_button(
            button,
            on_change=partial(record, index),
            apply_unchanged=True,
            group="lock" if index % 2 == 0 else "other",
        )
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
    assert calls == [(0, True), (2, True), (4, True)]
    calls.clear()
    sweep.add_button(
        buttons[0], on_change=partial(record, 0), apply_unchanged=True
    )
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
    assert calls == [(index, True) for index in range(5)]


def test_explicit_settings_do_not_intercept_click_and_clear_removes_writer(
    panel: qt.QWidget,
) -> None:
    """明示設定後も単発クリックは標準経路で、clear後は古い入力先を呼ばない。"""
    buttons = _buttons(panel)
    calls: list[bool] = []
    clicks: list[bool] = []
    sweep = CheckBoxSweep(panel)
    for button in buttons:
        sweep.add_button(
            button, on_change=calls.append, apply_unchanged=True, group="lock"
        )
    buttons[0].clicked.connect(lambda checked=False: clicks.append(checked))
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[0])
    assert clicks == [True] and not calls
    sweep.clear()
    for button in buttons:
        sweep.add_button(button)
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonPress, buttons[0])
    _mouse(buttons[0], qt.QEvent.Type.MouseMove, buttons[-1])
    _mouse(buttons[0], qt.QEvent.Type.MouseButtonRelease, buttons[-1])
    assert not calls
    assert all(not button.isChecked() for button in buttons)


def test_apply_unchanged_requires_actual_bool(panel: qt.QWidget) -> None:
    """同値要求の設定をboolに限定し、誤った指定を登録前に拒否する。"""
    button = _buttons(panel)[0]
    sweep = CheckBoxSweep(panel)
    with pytest.raises(TypeError, match="apply_unchanged"):
        sweep.add_button(button, apply_unchanged=cast(bool, 1))
