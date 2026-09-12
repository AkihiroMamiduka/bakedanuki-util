# coding: utf-8
from __future__ import annotations

from math import isfinite
from typing import ClassVar

from .... import qt
from .._validation import require_float
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel
from ._connection import connect_queued_qt_signal
from ._source import resolve_float_view_source


def _require_range(minimum: float, maximum: float) -> tuple[float, float]:
    """有限で昇順の操作範囲を、公開単位の値として検証する。"""
    minimum = require_float(minimum, "minimum")
    maximum = require_float(maximum, "maximum")
    if minimum >= maximum:
        raise ValueError("minimumはmaximum未満にしてください")
    return minimum, maximum


def _require_steps(value: object) -> int:
    """Qtの整数位置に収まる正の分割数を検証する。"""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("stepsには整数を指定してください")
    if not 1 <= value <= 2147483647:
        raise ValueError("stepsは1～2147483647にしてください")
    return value


class FloatSlider(qt.QSlider):
    """公開単位の有限範囲を整数位置へ写像し、確定値を連続編集するView。"""

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
        view_model: FloatViewModel | FloatBinding[FloatValueStore],
        parent: qt.QWidget | None = None,
        *,
        minimum: float,
        maximum: float,
        steps: int = 1000,
        orientation: qt.Qt.Orientation = qt.Qt.Orientation.Horizontal,
    ) -> None:
        """操作範囲と分割数を指定し、BindingまたはViewModelを共有する。"""
        view_model, binding = resolve_float_view_source(view_model)
        float_range = _require_range(minimum, maximum)
        steps = _require_steps(steps)
        if orientation not in (
            qt.Qt.Orientation.Horizontal,
            qt.Qt.Orientation.Vertical,
        ):
            raise ValueError(
                "orientationにはHorizontalまたはVerticalを指定してください"
            )
        if view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")

        # 初期化中のQt eventを避け、Viewだけを保持する構成でも正本を存続させる。
        self._ready = False
        super().__init__(orientation, parent)
        self._view_model = view_model
        self._binding = binding
        self._float_range = float_range
        self._steps = steps
        self._effective_range: tuple[float, float] | None = None
        self._editing = False
        self._interrupted = False
        self.setRange(0, steps)
        self.setSingleStep(1)
        self.setPageStep(max(1, steps // 10))
        self.setTracking(True)
        self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
        self._ready = True
        self._render()

        # 確定値の表示と入力を分離し、整数位置への丸めを正本へ戻さない。
        self.valueChanged.connect(self._request_value)
        self.sliderPressed.connect(self._begin_edit)
        self.sliderReleased.connect(self._finish_edit)
        view_model.value.changed.connect(self._update_value)
        view_model.presentation_changed.connect(self._update_presentation)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )
        view_model.edit_finished.connect(self._on_edit_finished)
        view_model.disposed.connect(self._stop_binding)
        connect_queued_qt_signal(view_model.destroyed, self._stop_binding)

    @property
    def view_model(self) -> FloatViewModel:
        """生存中のViewModelを返し、終了後は例外を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        return self._view_model

    def floatRange(self) -> tuple[float, float]:
        """生成時またはsetFloatRangeで指定した公開単位の操作範囲を返す。"""
        return self._float_range

    def setFloatRange(self, minimum: float, maximum: float) -> None:
        """操作範囲だけを変更し、正本の値は変更しない。"""
        float_range = _require_range(minimum, maximum)
        if float_range != self._float_range:
            self._finish_edit()
            self._float_range = float_range
            self._render()

    def effectiveFloatRange(self) -> tuple[float, float] | None:
        """hard limitと交差する有効範囲を返し、操作不可ならNoneを返す。"""
        return self._effective_range

    def _render(self) -> None:
        """表示位置だけを範囲内へ制限し、量子化による書き戻しを防ぐ。"""
        if self._view_model.is_disposed:
            self._stop_binding()
            return
        presentation = self._view_model.presentation
        lower, upper = self._float_range
        if presentation.minimum is not None:
            lower = max(lower, presentation.minimum)
        if presentation.maximum is not None:
            upper = min(upper, presentation.maximum)
        self._effective_range = (lower, upper) if lower < upper else None
        value = self._view_model.value.value
        position = 0
        if self._effective_range is not None:
            value = min(upper, max(lower, value))
            span = upper - lower
            ratio = (
                (value - lower) / span
                if isfinite(span)
                else (value / 2 - lower / 2) / (upper / 2 - lower / 2)
            )
            position = round(ratio * self._steps)
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.setValue(position)
        finally:
            del blocker
        self._update_enabled(self._view_model.set_value_command.can_execute)

    @qt.Slot(int)
    def _request_value(self, position: int) -> None:
        """ユーザーの整数位置を公開値へ変換し、正本の確定値を再表示する。"""
        if self._view_model.is_disposed or self._effective_range is None:
            self._render()
            return
        lower, upper = self._effective_range
        ratio = min(1.0, max(0.0, position / self._steps))
        # 異符号の最大有限値どうしでも、差のoverflowを避けて補間する。
        value = (
            (1 - ratio) * lower + ratio * upper
            if lower < 0 < upper
            else lower + (upper - lower) * ratio
        )
        value = min(upper, max(lower, value))
        try:
            self._view_model.set_value_command.execute(value)
        except Exception:
            self._finish_edit()
            raise
        finally:
            if qt.isValid(self):
                self._render()

    @qt.Slot(float)
    def _update_value(self, _value: float) -> None:
        """丸めやsetter補正後も、最新の確定値を表示する。"""
        self._render()

    @qt.Slot(object)
    def _update_presentation(self, _presentation: object) -> None:
        """単位やhard limitの変更時は編集を終了して再表示する。"""
        self._finish_edit()
        self._render()

    @qt.Slot(bool)
    def _update_enabled(self, can_execute: bool) -> None:
        """書き込み不可または有効範囲なしの場合は操作を終了する。"""
        enabled = can_execute and self._effective_range is not None
        if not enabled:
            self._finish_edit()
        if qt.isValid(self):
            self.setEnabled(enabled)

    @qt.Slot()
    def _begin_edit(self) -> None:
        """入力Viewをownerとして1つの連続編集を開始する。"""
        if (
            not self._editing
            and self.isEnabled()
            and not self._view_model.is_disposed
        ):
            self._editing = self._view_model.begin_edit(self)

    @qt.Slot()
    def _finish_edit(self) -> None:
        """最後に確定した値を維持し、入力とUndoのまとまりを終了する。"""
        if not self._editing:
            return
        self._editing = False
        self._interrupted = True
        if qt.isValid(self):
            self.setRepeatAction(qt.QSlider.SliderAction.SliderNoAction)
            self.setSliderDown(False)
        self._view_model.end_edit(self)

    @qt.Slot()
    def _on_edit_finished(self) -> None:
        """外部からの編集終了要求にも入力状態を揃える。"""
        self._finish_edit()

    @qt.Slot()
    def _stop_binding(self) -> None:
        """ViewModelの明示終了・Qt破棄後の入力を無効にする。"""
        self._finish_edit()
        if qt.isValid(self):
            self.setEnabled(False)

    def mousePressEvent(self, ev: qt.QtGui.QMouseEvent) -> None:
        """つまみと溝の操作を、最初の値変更より前に開始する。"""
        self._interrupted = False
        if ev.button() in (
            qt.Qt.MouseButton.LeftButton,
            qt.Qt.MouseButton.MiddleButton,
        ):
            self._begin_edit()
        super().mousePressEvent(ev)

    def mouseMoveEvent(self, ev: qt.QtGui.QMouseEvent) -> None:
        """途中終了したドラッグからの古い位置入力を無視する。"""
        if not self._interrupted:
            super().mouseMoveEvent(ev)

    def mouseReleaseEvent(self, ev: qt.QtGui.QMouseEvent) -> None:
        """マウスを離した時点で溝のリピートを含む連続編集を終了する。"""
        try:
            super().mouseReleaseEvent(ev)
        finally:
            self._finish_edit()
            self._interrupted = False

    def keyPressEvent(self, ev: qt.QtGui.QKeyEvent) -> None:
        """矢印・Page・Home・Endのリピートを押下中の1操作にまとめる。"""
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
        """キーを実際に離した時点で連続編集を確定する。"""
        super().keyReleaseEvent(event)
        if event.key() in self._EDIT_KEYS and not event.isAutoRepeat():
            self._finish_edit()
            self._interrupted = False

    def wheelEvent(self, e: qt.QtGui.QWheelEvent) -> None:
        """フォーカス中のホイールイベントを1回の編集として適用する。"""
        if not self.hasFocus():
            e.ignore()
            return
        self._begin_edit()
        try:
            super().wheelEvent(e)
        finally:
            self._finish_edit()

    def event(self, event: qt.QEvent) -> bool:
        """非表示・フォーカス喪失・無効化時も、Undoを開いたまま残さない。"""
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
