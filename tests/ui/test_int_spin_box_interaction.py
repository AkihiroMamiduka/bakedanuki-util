# coding: utf-8
"""整数入力欄のEnter受理と初回クリックの文字選択を検証する。"""

from dataclasses import dataclass

import pytest

from bd_util.ui import IntBinding, IntSpinBox, qt


@dataclass
class Data:
    """入力確定の確認に使用する整数の正本。"""

    value: int = 12345


class Parent(qt.QWidget):
    """子の入力欄から伝播したキーを記録する親Window。"""

    def __init__(self):
        """入力キーの到達履歴を初期化する。"""
        super().__init__()
        self.keys = []

    def event(self, event):
        """Enterの押下と解放が親へ届いたか記録する。"""
        if event.type() in (
            qt.QEvent.Type.ShortcutOverride,
            qt.QEvent.Type.KeyPress,
            qt.QEvent.Type.KeyRelease,
        ) and isinstance(event, qt.QtGui.QKeyEvent):
            self.keys.append(event.key())
        return super().event(event)


def flush():
    """全選択の予約とQtの遅延破棄を処理する。"""
    qt.QApplication.processEvents()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


@pytest.fixture
def panel(qt_application):
    """整数欄とフォーカス移動先を持つWindowを作る。"""
    parent = Parent()
    data = Data()
    binding = IntBinding.from_attribute(data, "value", parent=parent)
    spin = IntSpinBox(binding, parent, select_all_on_mouse_focus=True)
    other = qt.QLineEdit(parent)
    layout = qt.QVBoxLayout(parent)
    layout.addWidget(spin)
    layout.addWidget(other)
    parent.show()
    parent.activateWindow()
    other.setFocus()
    flush()
    yield parent, binding, spin, other
    binding.dispose()
    parent.deleteLater()
    flush()


def mouse(spin, event_type, position, button, held):
    """整数の入力文字へ指定したマウス操作を送る。"""
    line = spin.lineEdit()
    event = qt.QtGui.QMouseEvent(
        event_type,
        qt.QPointF(position),
        qt.QPointF(line.mapToGlobal(position)),
        button,
        held,
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(line, event)


def click(spin):
    """整数の入力文字へドラッグなしの単クリックを送る。"""
    position = spin.lineEdit().rect().center()
    mouse(
        spin,
        qt.QEvent.Type.MouseButtonPress,
        position,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.LeftButton,
    )
    mouse(
        spin,
        qt.QEvent.Type.MouseButtonRelease,
        position,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.NoButton,
    )
    flush()


@pytest.mark.parametrize("key", [qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter])
@pytest.mark.parametrize("child", [False, True])
def test_enter_commits_without_parent_shortcut(panel, key, child):
    """通常EnterとテンキーEnterで確定し、親へキーを渡さない。"""
    parent, binding, spin, _other = panel
    spin.setFocus()
    flush()
    spin.lineEdit().setText("-2147483648")
    target = spin.lineEdit() if child else spin
    for event_type in (
        qt.QEvent.Type.ShortcutOverride,
        qt.QEvent.Type.KeyPress,
        qt.QEvent.Type.KeyRelease,
    ):
        event = qt.QtGui.QKeyEvent(
            event_type, key, qt.Qt.KeyboardModifier.NoModifier
        )
        qt.QApplication.sendEvent(target, event)
        assert event.isAccepted()
    assert binding.value == -(2**31)
    assert parent.keys == []


def test_first_click_selection_and_later_caret(panel):
    """初回文字クリックを全選択し、同じ欄の再クリックはカーソルを置く。"""
    _parent, _binding, spin, _other = panel
    spin.setFocus(qt.Qt.FocusReason.MouseFocusReason)
    flush()
    click(spin)
    assert spin.lineEdit().selectedText() == "12345"
    click(spin)
    assert spin.lineEdit().selectedText() == ""
    assert spin.select_all_on_mouse_focus()
    spin.set_select_all_on_mouse_focus(False)
    assert not spin.select_all_on_mouse_focus()
    with pytest.raises(TypeError):
        spin.set_select_all_on_mouse_focus(1)


def test_initial_drag_and_disabled_option_keep_partial_selection(panel):
    """初回ドラッグと設定無効時には自動全選択を行わない。"""
    _parent, _binding, spin, other = panel
    spin.setFocus(qt.Qt.FocusReason.MouseFocusReason)
    flush()
    position = spin.lineEdit().rect().center()
    mouse(
        spin,
        qt.QEvent.Type.MouseButtonPress,
        position,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.LeftButton,
    )
    mouse(
        spin,
        qt.QEvent.Type.MouseMove,
        position + qt.QPoint(1, 0),
        qt.Qt.MouseButton.NoButton,
        qt.Qt.MouseButton.LeftButton,
    )
    mouse(
        spin,
        qt.QEvent.Type.MouseButtonRelease,
        position + qt.QPoint(1, 0),
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.NoButton,
    )
    flush()
    assert spin.lineEdit().selectedText() != spin.lineEdit().text()
    spin.set_select_all_on_mouse_focus(False)
    other.setFocus()
    flush()
    spin.setFocus(qt.Qt.FocusReason.MouseFocusReason)
    click(spin)
    assert spin.lineEdit().selectedText() != spin.lineEdit().text()


def test_default_selection_and_invalid_option(panel):
    """全選択は明示的な指定だけで有効になり、bool以外は拒否する。"""
    parent, binding, _spin, _other = panel
    default = IntSpinBox(binding, parent)
    assert not default.select_all_on_mouse_focus()
    with pytest.raises(TypeError):
        IntSpinBox(binding, parent, select_all_on_mouse_focus=1)
