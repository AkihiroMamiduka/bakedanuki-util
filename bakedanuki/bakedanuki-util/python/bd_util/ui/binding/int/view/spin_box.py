# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from .... import qt
from ..._spin_box_mouse_selection import SpinBoxMouseFocusSelection
from .._connection import connect_queued, disconnect
from .._validation import INT32_MAX, INT32_MIN, require_int
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel
from ._source import resolve_int_view_source


class IntSpinBox(qt.QSpinBox):
    """符号付き32-bit整数を、精度を落とさず編集する入力欄。"""

    def __init__(
        self,
        view_model: IntViewModel | IntBinding[IntValueStore],
        parent: qt.QWidget | None = None,
        *,
        single_step: int = 1,
        wheel_requires_focus: bool = False,
        select_all_on_mouse_focus: bool = False,
    ) -> None:
        """共有対象、刻み幅とホイール操作条件を指定する。"""
        view_model, binding = resolve_int_view_source(view_model)
        single_step = require_int(single_step, "single_step")
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")
        if type(wheel_requires_focus) is not bool:
            raise TypeError("wheel_requires_focusにはboolを指定してください")
        if type(select_all_on_mouse_focus) is not bool:
            raise TypeError(
                "select_all_on_mouse_focusにはboolを指定してください"
            )
        super().__init__(parent)
        self._mouse_selection = SpinBoxMouseFocusSelection(
            self, select_all_on_mouse_focus
        )
        self._binding = binding
        self._view_model = view_model
        self._input_enabled = True
        self._wheel_requires_focus = wheel_requires_focus
        self._value_request_handler: Callable[[int], bool] | None = None
        self._step_request_handler: Callable[[int], bool] | None = None
        self.setSingleStep(single_step)
        self.setKeyboardTracking(False)
        self.setWrapping(False)
        self.set_wheel_requires_focus(wheel_requires_focus)
        self._render()
        self._update_enabled()
        self._input_connection: qt.QtCore.QMetaObject.Connection | None = (
            self.valueChanged.connect(self._request_value)
        )
        view_model.value.changed.connect(self._update_value)
        view_model.presentation_changed.connect(self._update_presentation)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )
        view_model.disposed.connect(self._disable_binding)
        connect_queued(view_model.destroyed, self._disable_binding)

    @property
    def view_model(self) -> IntViewModel:
        """生存中の表示対象を返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("表示対象のIntViewModelは終了しています")
        return view_model

    def isInputEnabled(self) -> bool:
        """この入力欄固有の操作可否を返す。"""
        return self._input_enabled

    def setInputEnabled(self, enabled: bool) -> None:
        """表示更新を続けながら、この入力欄の操作を切り替える。"""
        if type(enabled) is not bool:
            raise TypeError("enabledにはboolを指定してください")
        self._input_enabled = enabled
        self._update_enabled()

    def wheel_requires_focus(self) -> bool:
        """ホイール操作にフォーカスを要求するか返す。"""
        return self._wheel_requires_focus

    def set_wheel_requires_focus(self, required: bool) -> None:
        """未フォーカス時のホイール操作を切り替える。"""
        if type(required) is not bool:
            raise TypeError("requiredにはboolを指定してください")
        self._wheel_requires_focus = required
        self.setFocusPolicy(
            qt.Qt.FocusPolicy.StrongFocus
            if required
            else qt.Qt.FocusPolicy.WheelFocus
        )

    def setValueRequestHandler(
        self, handler: Callable[[int], bool] | None
    ) -> None:
        """整数の入力を外側で処理する関数を設定する。"""
        if handler is not None and not callable(handler):
            raise TypeError(
                "handlerには呼出し可能な関数またはNoneを指定してください"
            )
        self._value_request_handler = handler

    def setStepRequestHandler(
        self, handler: Callable[[int], bool] | None
    ) -> None:
        """上下操作のstep数を外側で処理する関数を設定する。"""
        if handler is not None and not callable(handler):
            raise TypeError(
                "handlerには呼出し可能な関数またはNoneを指定してください"
            )
        self._step_request_handler = handler

    def stepBy(self, steps: int) -> None:
        """外側で処理済みの上下操作を重ねて適用しない。"""
        handler = self._step_request_handler
        if (
            handler is None
            or not steps
            or not self.isEnabled()
            or self.isReadOnly()
        ):
            super().stepBy(steps)
            return
        try:
            handled = handler(steps)
        finally:
            if qt.isValid(self) and self._valid_view_model() is not None:
                self._render()
        if not handled:
            super().stepBy(steps)

    def wheelEvent(self, event: qt.QtGui.QWheelEvent) -> None:
        """フォーカスが必要な場合は未フォーカスのホイールを親へ渡す。"""
        if self._wheel_requires_focus and not self.hasFocus():
            event.ignore()
            return
        super().wheelEvent(event)

    def event(self, event: qt.QEvent) -> bool:
        """Enterを整数入力欄で扱い、親Windowのshortcutへ渡さない。"""
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
        """Enterの解放通知も整数入力欄で受理する。"""
        super().keyReleaseEvent(event)
        if event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            event.accept()

    def select_all_on_mouse_focus(self) -> bool:
        """マウスで初回フォーカスしたときの全選択設定を返す。"""
        return self._mouse_selection.enabled

    def set_select_all_on_mouse_focus(self, enabled: bool) -> None:
        """マウスで初回フォーカスしたときの全選択を切り替える。"""
        self._mouse_selection.set_enabled(enabled)

    def focusInEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """マウスで得たフォーカスだけを全選択の候補にする。"""
        self._mouse_selection.focus_in(event)
        super().focusInEvent(event)

    def focusOutEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """フォーカスを失ったら全選択の予約を破棄する。"""
        self._mouse_selection.reset()
        super().focusOutEvent(event)

    def mousePressEvent(self, event: qt.QtGui.QMouseEvent) -> None:
        """矢印や枠のクリックでは入力文字を自動選択しない。"""
        self._mouse_selection.reset()
        super().mousePressEvent(event)

    @qt.Slot()
    def _update_enabled(self) -> None:
        """局所設定と正本の編集可否を合わせる。"""
        view_model = self._valid_view_model()
        self.setEnabled(
            self._input_enabled
            and view_model is not None
            and view_model.set_value_command.can_execute
        )

    def _request_value(self, value: int) -> None:
        """入力をCommandへ渡して確定後の値へ表示を戻す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self._disable_binding()
            return
        if not self._input_enabled:
            self._render()
            return
        try:
            handler = self._value_request_handler
            if handler is None or not handler(value):
                view_model.set_value_command.execute(value)
        finally:
            if qt.isValid(self) and self._valid_view_model() is not None:
                self._render()

    def _render(self) -> None:
        """範囲更新による入力signalを抑え、確定値を表示する。"""
        view_model = self.view_model
        value = view_model.value.value
        presentation = view_model.presentation
        minimum = presentation.minimum
        maximum = presentation.maximum
        # 外部変更で境界外になった実値も、Qt側の範囲に含めて表示する。
        lower = min(INT32_MIN if minimum is None else minimum, value)
        upper = max(INT32_MAX if maximum is None else maximum, value)
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.setRange(lower, upper)
            self.setValue(value)
        finally:
            del blocker

    def _update_value(self, _value: object) -> None:
        """最新の確定値を表示する。"""
        self._render()

    def _update_presentation(self, _presentation: object) -> None:
        """最新の入力範囲と確定値を表示する。"""
        self._render()

    def _valid_view_model(self) -> IntViewModel | None:
        """明示終了とC++ object破棄を確認する。"""
        view_model = self._view_model
        return view_model if not view_model.is_disposed else None

    @qt.Slot()
    def _disable_binding(self) -> None:
        """入力接続を解除し、表示欄を無効にする。"""
        disconnect(self._input_connection)
        self._input_connection = None
        if qt.isValid(self):
            self.setEnabled(False)
