# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar

from .... import qt
from .._connection import connect_queued
from .._validation import require_slider_range, require_step
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel
from ._source import resolve_int_view_source

__all__ = ["IntSlider"]


def _round_ratio(numerator: int, denominator: int) -> int:
    """非負の比率を最寄り整数へ丸め、同点では大きい側を選ぶ。"""
    quotient, remainder = divmod(numerator, denominator)
    return quotient + (2 * remainder >= denominator)


class IntSlider(qt.QSlider):
    """32-bit整数を精度を落とさず整数位置へ写像する連続編集View。"""

    intRangeChanged = qt.Signal(int, int)
    editStarted = qt.Signal()
    editFinished = qt.Signal()

    _EDIT_KEYS: ClassVar[frozenset[qt.Qt.Key]] = frozenset(
        (
            qt.Qt.Key.Key_Left,
            qt.Qt.Key.Key_Right,
            qt.Qt.Key.Key_Up,
            qt.Qt.Key.Key_Down,
            qt.Qt.Key.Key_PageUp,
            qt.Qt.Key.Key_PageDown,
            qt.Qt.Key.Key_Home,
            qt.Qt.Key.Key_End,
        )
    )

    def __init__(
        self,
        view_model: IntViewModel | IntBinding[IntValueStore],
        parent: qt.QWidget | None = None,
        *,
        minimum: int,
        maximum: int,
        steps: int = 1000,
        orientation: qt.Qt.Orientation = qt.Qt.Orientation.Horizontal,
    ) -> None:
        """正本とは独立した範囲を、最大`steps`分割で操作する。

        Args:
            view_model: 共有する整数ViewModelまたはBinding。
            parent: Qtの親Widget。
            minimum: 32-bit整数の下限。`maximum`より小さい値。
            maximum: 32-bit整数の上限。
            steps: 正の32-bit整数の分割数。実効範囲の整数幅以下へ調整する。
            orientation: 水平または垂直方向。

        Raises:
            TypeError: 整数引数が`bool`・小数・文字列などの場合。
            ValueError: 範囲・分割数・方向が不正な場合。
            RuntimeError: 入力元が終了している場合。
        """
        view_model, binding = resolve_int_view_source(view_model)
        int_range = require_slider_range(minimum, maximum)
        steps = require_step(steps, "steps")
        if orientation not in (
            qt.Qt.Orientation.Horizontal,
            qt.Qt.Orientation.Vertical,
        ):
            raise ValueError(
                "orientationにはHorizontalまたはVerticalを指定してください"
            )
        if view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        self._ready = False
        super().__init__(orientation, parent)
        self._view_model = view_model
        self._binding = binding
        self._int_range = int_range
        self._steps = steps
        self._effective_range: tuple[int, int] | None = None
        self._positions = 1
        self._editing = False
        self._wheel_editing = False
        self._interrupted = False
        self._value_request_handler: Callable[[int], bool] | None = None
        self.setSingleStep(1)
        self.setTracking(True)
        self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
        self._ready = True
        self._render()

        # 表示更新の丸めと、利用者による正本への入力を分ける
        self.valueChanged.connect(self._request_value)
        self.sliderPressed.connect(self._begin_edit)
        self.sliderReleased.connect(self._finish_edit)
        view_model.value.changed.connect(self._update_value)
        view_model.presentation_changed.connect(self._update_presentation)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )
        view_model.edit_finished.connect(self._finish_edit)
        view_model.disposed.connect(self._stop_binding)
        connect_queued(view_model.destroyed, self._stop_binding)

    @property
    def view_model(self) -> IntViewModel:
        """生存中の共有ViewModelを返す。終了後は例外を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        return self._view_model

    @property
    def is_wheel_editing(self) -> bool:
        """wheel処理中だけTrueとなり、編集開始・終了通知内でも参照できる。"""
        return self._wheel_editing

    def intRange(self) -> tuple[int, int]:
        """生成時または`setIntRange()`で指定した操作範囲を返す。"""
        return self._int_range

    def setIntRange(self, minimum: int, maximum: int) -> None:
        """正本を変えず操作範囲を変更し、実変更時だけ通知する。"""
        int_range = require_slider_range(minimum, maximum)
        if int_range != self._int_range:
            self._finish_edit()
            self._int_range = int_range
            self._render()
            self.intRangeChanged.emit(*int_range)

    def effectiveIntRange(self) -> tuple[int, int] | None:
        """操作範囲と正本の制限の共通部分を返す。操作不能なら`None`。"""
        return self._effective_range

    def setValueRequestHandler(
        self, handler: Callable[[int], bool] | None
    ) -> None:
        """公開整数を処理したら`True`を返す外部入力先を設定する。"""
        if handler is not None and not callable(handler):
            raise TypeError(
                "handlerには呼出し可能な関数またはNoneを指定してください"
            )
        self._finish_edit()
        self._value_request_handler = handler

    def finish_edit(self) -> None:
        """外部から連続操作を確定終了し、残りの古い入力を停止する。"""
        self._finish_edit()

    def _render(self) -> None:
        """実値を保持したまま、表示位置だけを実効範囲へ制限する。"""
        if self._view_model.is_disposed:
            self._stop_binding()
            return
        lower, upper = self._int_range
        presentation = self._view_model.presentation
        if presentation.minimum is not None:
            lower = max(lower, presentation.minimum)
        if presentation.maximum is not None:
            upper = min(upper, presentation.maximum)
        self._effective_range = (lower, upper) if lower < upper else None
        position = 0
        positions = 1
        if self._effective_range is not None:
            span = upper - lower
            positions = min(self._steps, span)
            value = min(upper, max(lower, self._view_model.value.value))
            position = _round_ratio((value - lower) * positions, span)
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            # 全32-bit範囲の幅もPython整数で扱い、Qtの位置差を範囲内に保つ
            self._positions = positions
            self.setRange(0, positions)
            self.setPageStep(max(1, positions // 10))
            self.setValue(position)
        finally:
            del blocker
        self._update_enabled(self._view_model.set_value_command.can_execute)

    @qt.Slot(int)
    def _request_value(self, position: int) -> None:
        """整数位置を公開整数へ変換し、setter後の実値を再表示する。"""
        if (
            self._view_model.is_disposed
            or self._effective_range is None
            or not self.isEnabled()
        ):
            self._render()
            return
        lower, upper = self._effective_range
        position = min(self._positions, max(0, position))
        value = lower + _round_ratio(
            position * (upper - lower), self._positions
        )
        try:
            handler = self._value_request_handler
            if handler is None or not handler(value):
                self._view_model.set_value_command.execute(value)
        except Exception:
            self._finish_edit()
            raise
        finally:
            if qt.isValid(self):
                self._render()

    @qt.Slot(object)
    def _update_value(self, _value: object) -> None:
        """正本の確定整数を再表示する。"""
        self._render()

    @qt.Slot(object)
    def _update_presentation(self, _presentation: object) -> None:
        """正本の範囲変更では操作を終了して再表示する。"""
        self._finish_edit()
        self._render()

    @qt.Slot(bool)
    def _update_enabled(self, can_execute: bool) -> None:
        """入力不可や操作可能範囲なしの場合に操作を終了する。"""
        enabled = can_execute and self._effective_range is not None
        if not enabled:
            self._finish_edit()
        if qt.isValid(self):
            self.setEnabled(enabled)

    @qt.Slot()
    def _begin_edit(self) -> None:
        """最初の位置変更より前に、入力元の連続編集を開始する。"""
        if (
            not self._editing
            and self.isEnabled()
            and not self._view_model.is_disposed
        ):
            self._editing = (
                True
                if self._value_request_handler is not None
                else self._view_model.begin_edit(self)
            )
            if self._editing:
                self.editStarted.emit()

    @qt.Slot()
    def _finish_edit(self) -> None:
        """最後の確定値を維持し、入力とUndoの操作単位を閉じる。"""
        if not self._editing:
            return
        self._editing = False
        self._interrupted = True
        if qt.isValid(self):
            self.setRepeatAction(qt.QSlider.SliderAction.SliderNoAction)
            self.setSliderDown(False)
        if self._value_request_handler is None:
            self._view_model.end_edit(self)
        if qt.isValid(self):
            self.editFinished.emit()

    @qt.Slot()
    def _stop_binding(self) -> None:
        """入力元の明示終了やQt破棄後に操作を停止する。"""
        self._finish_edit()
        if qt.isValid(self):
            self.setEnabled(False)

    def mousePressEvent(self, ev: qt.QtGui.QMouseEvent) -> None:
        """つまみと溝の入力を、最初の値変更より前に開始する。"""
        self._interrupted = False
        if ev.button() in (
            qt.Qt.MouseButton.LeftButton,
            qt.Qt.MouseButton.MiddleButton,
        ):
            self._begin_edit()
        super().mousePressEvent(ev)

    def mouseMoveEvent(self, ev: qt.QtGui.QMouseEvent) -> None:
        """途中終了したドラッグから届く古い位置変更を無視する。"""
        if not self._interrupted:
            super().mouseMoveEvent(ev)

    def mouseReleaseEvent(self, ev: qt.QtGui.QMouseEvent) -> None:
        """マウス解放で、溝のリピートを含む操作を終了する。"""
        try:
            super().mouseReleaseEvent(ev)
        finally:
            self._finish_edit()
            self._interrupted = False

    def keyPressEvent(self, ev: qt.QtGui.QKeyEvent) -> None:
        """矢印・Page・Home・Endを一操作にまとめ、Escで確定終了する。"""
        if ev.key() == qt.Qt.Key.Key_Escape:
            self._finish_edit()
            ev.accept()
            return
        if ev.key() in self._EDIT_KEYS:
            if self._interrupted and ev.isAutoRepeat():
                return
            self._interrupted = False
            self._begin_edit()
        super().keyPressEvent(ev)

    def keyReleaseEvent(self, event: qt.QtGui.QKeyEvent) -> None:
        """リピートではないキー解放で操作を終了する。"""
        super().keyReleaseEvent(event)
        if event.key() in self._EDIT_KEYS and not event.isAutoRepeat():
            self._finish_edit()
            self._interrupted = False

    def wheelEvent(self, e: qt.QtGui.QWheelEvent) -> None:
        """フォーカス中のホイール一イベントを一操作として適用する。"""
        if not self.hasFocus():
            e.ignore()
            return
        previous = self._wheel_editing
        self._wheel_editing = True
        try:
            self._begin_edit()
            try:
                super().wheelEvent(e)
            finally:
                self._finish_edit()
        finally:
            self._wheel_editing = previous

    def event(self, event: qt.QEvent) -> bool:
        """非表示・フォーカス喪失・無効化でも連続編集を終了する。"""
        if self._ready and event.type() in (
            qt.QEvent.Type.Hide,
            qt.QEvent.Type.HideToParent,
            qt.QEvent.Type.Close,
            qt.QEvent.Type.FocusOut,
            qt.QEvent.Type.WindowDeactivate,
            qt.QEvent.Type.UngrabMouse,
            qt.QEvent.Type.EnabledChange,
        ):
            if (
                event.type() != qt.QEvent.Type.EnabledChange
                or not self.isEnabled()
            ):
                self._finish_edit()
        return super().event(event)
