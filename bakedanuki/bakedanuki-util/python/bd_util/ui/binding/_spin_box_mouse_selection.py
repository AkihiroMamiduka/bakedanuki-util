# coding: utf-8
"""整数と浮動小数点の数値欄でマウスフォーカス時の全選択を共有する。"""

from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from .. import qt


class _QTimerType(Protocol):
    """PySide stub境界で使用する遅延実行の必要最小API。"""

    @staticmethod
    def singleShot(milliseconds: int, callback: Callable[[], None]) -> None:
        """指定時間後にcallbackを一度だけ実行する。"""
        raise NotImplementedError


class SpinBoxMouseFocusSelection(qt.QObject):
    """SpinBoxの初回クリックとドラッグを区別して文字列を全選択する。"""

    def __init__(
        self, spin_box: qt.QtWidgets.QAbstractSpinBox, enabled: bool
    ) -> None:
        """入力欄と同じ寿命でマウス操作を監視する。"""
        if type(enabled) is not bool:
            raise TypeError(
                "select_all_on_mouse_focusにはboolを指定してください"
            )
        super().__init__(spin_box)
        self._spin_box = spin_box
        self.enabled = enabled
        self._select_on_release = False
        self._dragged = False
        spin_box.lineEdit().installEventFilter(self)

    def set_enabled(self, enabled: bool) -> None:
        """初回クリックの全選択を切り替え、無効時の予約を破棄する。"""
        if type(enabled) is not bool:
            raise TypeError("enabledにはboolを指定してください")
        self.enabled = enabled
        if not enabled:
            self.reset()

    def focus_in(self, event: qt.QtGui.QFocusEvent) -> None:
        """マウスで得たフォーカスだけを全選択の候補にする。"""
        self._select_on_release = (
            self.enabled
            and event.reason() == qt.Qt.FocusReason.MouseFocusReason
        )
        self._dragged = False

    def reset(self) -> None:
        """入力文字以外のクリックやフォーカス移動で全選択予約を破棄する。"""
        self._select_on_release = False
        self._dragged = False

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """入力欄の単クリックとドラッグを区別して全選択を予約する。"""
        if not qt.isValid(self) or not qt.isValid(self._spin_box):
            return False
        if watched is self._spin_box.lineEdit():
            event_type = event.type()
            if event_type == qt.QEvent.Type.MouseButtonPress:
                mouse_event = cast(qt.QtGui.QMouseEvent, event)
                if mouse_event.button() == qt.Qt.MouseButton.LeftButton:
                    self._dragged = False
                else:
                    self._select_on_release = False
            elif event_type == qt.QEvent.Type.MouseMove:
                mouse_event = cast(qt.QtGui.QMouseEvent, event)
                if mouse_event.buttons() & qt.Qt.MouseButton.LeftButton:
                    self._dragged = True
            elif event_type == qt.QEvent.Type.MouseButtonRelease:
                mouse_event = cast(qt.QtGui.QMouseEvent, event)
                should_select = (
                    self._select_on_release
                    and not self._dragged
                    and mouse_event.button() == qt.Qt.MouseButton.LeftButton
                )
                self.reset()
                if should_select:
                    cast(_QTimerType, qt.QTimer).singleShot(
                        0, self._select_all
                    )
        return super().eventFilter(watched, event)

    def _select_all(self) -> None:
        """既定のカーソル移動後に生存中の入力文字だけを全選択する。"""
        spin_box = self._spin_box
        if qt.isValid(spin_box) and self.enabled and spin_box.hasFocus():
            spin_box.selectAll()
