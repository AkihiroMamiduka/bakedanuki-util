# coding: utf-8
from __future__ import annotations

from .... import qt
from ..._spin_box_mouse_selection import SpinBoxMouseFocusSelection

__all__ = ["MouseFocusSelectAllDoubleSpinBox"]


class MouseFocusSelectAllDoubleSpinBox(qt.QDoubleSpinBox):
    """マウスで入力欄へフォーカスした初回クリックだけ全選択できるSpinBox。"""

    def __init__(
        self,
        parent: qt.QWidget | None = None,
        *,
        select_all_on_mouse_focus: bool = False,
    ) -> None:
        """マウスフォーカス時の全選択設定で初期化する。"""
        if type(select_all_on_mouse_focus) is not bool:
            raise TypeError(
                "select_all_on_mouse_focusにはboolを指定してください"
            )
        super().__init__(parent)
        self._mouse_selection = SpinBoxMouseFocusSelection(
            self, select_all_on_mouse_focus
        )

    def event(self, event: qt.QEvent) -> bool:
        """Enterを数値入力欄で扱い、Mayaのshortcutへ渡さない。"""
        if (
            event.type() == qt.QEvent.Type.ShortcutOverride
            and isinstance(event, qt.QtGui.QKeyEvent)
            and event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter)
        ):
            event.accept()
            return True
        return super().event(event)

    def keyPressEvent(self, event: qt.QtGui.QKeyEvent) -> None:
        """Qtによる値確定後にEnterの押下を受理する。"""
        super().keyPressEvent(event)
        if event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            event.accept()

    def keyReleaseEvent(self, event: qt.QtGui.QKeyEvent) -> None:
        """Enterの解放通知も数値入力欄で受理する。"""
        super().keyReleaseEvent(event)
        if event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            event.accept()

    def select_all_on_mouse_focus(self) -> bool:
        """マウスで初回フォーカスしたときに全選択する設定を返す。"""
        return self._mouse_selection.enabled

    def set_select_all_on_mouse_focus(self, enabled: bool) -> None:
        """マウスで初回フォーカスしたときの全選択を切り替える。"""
        self._mouse_selection.set_enabled(enabled)

    def focusInEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """マウスで得たフォーカスだけ、次の入力欄クリックを全選択候補にする。"""
        self._mouse_selection.focus_in(event)
        super().focusInEvent(event)

    def focusOutEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """フォーカスを失ったら保留中の全選択を破棄する。"""
        self._mouse_selection.reset()
        super().focusOutEvent(event)

    def mousePressEvent(self, event: qt.QtGui.QMouseEvent) -> None:
        """矢印や枠のクリックでは入力文字の自動全選択を行わない。"""
        self._mouse_selection.reset()
        super().mousePressEvent(event)
