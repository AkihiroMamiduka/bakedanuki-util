# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from .... import qt


class _QTimerType(Protocol):
    """PySide stub境界で使用するQTimer classの必要最小API。"""

    @staticmethod
    def singleShot(
        milliseconds: int,
        callback: Callable[[], None],
    ) -> None:
        """指定時間後にcallbackを一度だけ呼び出す。"""
        raise NotImplementedError


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
        self._select_all_on_mouse_focus = select_all_on_mouse_focus
        self._select_on_mouse_release = False
        self._mouse_selection_dragged = False
        self.lineEdit().installEventFilter(self)

    def select_all_on_mouse_focus(self) -> bool:
        """マウスで初回フォーカスしたときに全選択する設定を返す。"""
        return self._select_all_on_mouse_focus

    def set_select_all_on_mouse_focus(self, enabled: bool) -> None:
        """マウスで初回フォーカスしたときの全選択を切り替える。"""
        if type(enabled) is not bool:
            raise TypeError("enabledにはboolを指定してください")
        self._select_all_on_mouse_focus = enabled
        if not enabled:
            self._select_on_mouse_release = False
            self._mouse_selection_dragged = False

    def focusInEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """マウスで得たフォーカスだけ、次の入力欄クリックを全選択候補にする。"""
        self._select_on_mouse_release = (
            self._select_all_on_mouse_focus
            and event.reason() == qt.Qt.FocusReason.MouseFocusReason
        )
        self._mouse_selection_dragged = False
        super().focusInEvent(event)

    def focusOutEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """フォーカスを失ったら保留中の全選択を破棄する。"""
        self._select_on_mouse_release = False
        self._mouse_selection_dragged = False
        super().focusOutEvent(event)

    def mousePressEvent(self, event: qt.QtGui.QMouseEvent) -> None:
        """矢印や枠のクリックでは入力文字の自動全選択を行わない。"""
        self._select_on_mouse_release = False
        self._mouse_selection_dragged = False
        super().mousePressEvent(event)

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """入力欄の単クリックとドラッグを区別して全選択を予約する。"""
        if watched is self.lineEdit():
            event_type = event.type()
            if event_type == qt.QEvent.Type.MouseButtonPress:
                mouse_event = cast(qt.QtGui.QMouseEvent, event)
                if mouse_event.button() == qt.Qt.MouseButton.LeftButton:
                    self._mouse_selection_dragged = False
                else:
                    self._select_on_mouse_release = False
            elif event_type == qt.QEvent.Type.MouseMove:
                mouse_event = cast(qt.QtGui.QMouseEvent, event)
                if mouse_event.buttons() & qt.Qt.MouseButton.LeftButton:
                    self._mouse_selection_dragged = True
            elif event_type == qt.QEvent.Type.MouseButtonRelease:
                mouse_event = cast(qt.QtGui.QMouseEvent, event)
                should_select = (
                    self._select_on_mouse_release
                    and not self._mouse_selection_dragged
                    and mouse_event.button() == qt.Qt.MouseButton.LeftButton
                )
                self._select_on_mouse_release = False
                self._mouse_selection_dragged = False
                if should_select:
                    timer_type = cast(_QTimerType, qt.QTimer)
                    timer_type.singleShot(0, self._select_all_after_click)
        return super().eventFilter(watched, event)

    def _select_all_after_click(self) -> None:
        """既定のカーソル移動後に、生存中の入力文字だけを全選択する。"""
        if (
            qt.isValid(self)
            and self._select_all_on_mouse_focus
            and self.hasFocus()
        ):
            self.selectAll()
