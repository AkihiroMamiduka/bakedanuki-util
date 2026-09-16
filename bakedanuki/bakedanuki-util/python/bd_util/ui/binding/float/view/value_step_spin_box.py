# coding: utf-8
from __future__ import annotations

from .... import qt
from .._validation import require_decimals
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel
from ._connection import connect_queued_qt_signal
from ._source import resolve_float_view_source
from .spin_box import FloatSpinBox
from .step_spin_box import (
    FloatStepMode,
    FloatStepSpinBox,
    require_step,
    require_step_mode,
)

__all__ = ["FloatValueStepSpinBox"]


def _require_width(value: object, argument_name: str) -> int | None:
    """自動伸縮のNone、またはQtの有効範囲内の固定幅を検証する。"""
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{argument_name}にはintまたはNoneを指定してください")
    if not 1 <= value <= 16777215:
        raise ValueError(f"{argument_name}は1～16777215にしてください")
    return value


class FloatValueStepSpinBox(qt.QWidget):
    """値と表示単位での刻み幅を横に並べ、刻み幅を正本へ書かないView。"""

    settingsChanged = qt.Signal()

    def __init__(
        self,
        view_model: FloatViewModel | FloatBinding[FloatValueStore],
        parent: qt.QWidget | None = None,
        *,
        decimals: int = 6,
        single_step: float = 0.1,
        step_mode: FloatStepMode = "additive",
        step_increment: float = 1.0,
        step_show_unit: bool = False,
        value_width: int | None = None,
        step_width: int = 68,
    ) -> None:
        """共有する入力元と、値・step欄の表示と操作設定を指定する。"""
        # 子Widgetを作る前に入力元と操作設定を検証する
        view_model, binding = resolve_float_view_source(view_model)
        if view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        decimals = require_decimals(decimals)
        single_step = require_step(single_step, "single_step")
        step_mode = require_step_mode(step_mode)
        step_increment = require_step(step_increment, "step_increment")
        if type(step_show_unit) is not bool:
            raise TypeError("step_show_unitにはboolを指定してください")
        value_width = _require_width(value_width, "value_width")
        validated_step_width = _require_width(step_width, "step_width")
        if validated_step_width is None:
            raise TypeError("step_widthにはintを指定してください")
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._step_show_unit = step_show_unit
        self._last_step = single_step

        # 値の編集は既存Viewへ委譲し、stepだけをView内で連動させる
        try:
            self.spin_box = FloatSpinBox(
                view_model, self, decimals=decimals, single_step=single_step
            )
            self.step_spin_box = FloatStepSpinBox(
                self,
                value=single_step,
                step_mode=step_mode,
                step_increment=step_increment,
            )
            self.step_spin_box.setSizePolicy(
                qt.QSizePolicy.Policy.Ignored, qt.QSizePolicy.Policy.Fixed
            )
            if value_width is not None:
                self.spin_box.setFixedWidth(value_width)
            self.step_spin_box.setFixedWidth(validated_step_width)
            layout = qt.QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.spin_box, 1 if value_width is None else 0)
            layout.addWidget(self.step_spin_box)
            if value_width is not None:
                layout.addStretch(1)
            self.setSizePolicy(
                qt.QSizePolicy.Policy.Expanding, qt.QSizePolicy.Policy.Fixed
            )
            self.setFocusProxy(self.spin_box)
            self._refresh_step()
            self.step_spin_box.valueChanged.connect(self._request_step)
            view_model.presentation_changed.connect(self._refresh_step)
            view_model.disposed.connect(self._stop_editing)
            connect_queued_qt_signal(view_model.destroyed, self._stop_editing)
        except Exception:
            # 部分生成したViewだけを破棄し、共有Bindingの寿命は変更しない
            self.setParent(None)
            self.deleteLater()
            raise

    @property
    def view_model(self) -> FloatViewModel:
        """共有ViewModelを返し、終了・Qt破棄後のアクセスを拒否する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        return self._view_model

    def singleStep(self) -> float:
        """値欄の現在の刻み幅を表示単位で返す。"""
        return self.spin_box.singleStep()

    def setSingleStep(self, single_step: float) -> None:
        """正本を変更せず両欄の刻み幅を同期し、変更時だけ通知する。"""
        single_step = require_step(single_step, "single_step")
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        self.spin_box.setSingleStep(single_step)
        self._refresh_step()
        if single_step != self._last_step:
            self._last_step = single_step
            self.settingsChanged.emit()

    @qt.Slot(float)
    def _request_step(self, value: float) -> None:
        """ユーザーによるstep編集を受け、終了後の遅延入力は破棄する。"""
        if self._view_model.is_disposed:
            self._stop_editing()
            return
        self.setSingleStep(value)

    @qt.Slot()
    def _refresh_step(self) -> None:
        """刻み幅の数値を維持し、単位文字と未確定表示を更新する。"""
        if self._view_model.is_disposed:
            self._stop_editing()
            return
        blocker = qt.QtCore.QSignalBlocker(self.step_spin_box)
        try:
            self.step_spin_box.setSuffix(
                self._view_model.presentation.suffix
                if self._step_show_unit
                else ""
            )
            self.step_spin_box.setValue(self.singleStep())
        finally:
            del blocker

    @qt.Slot()
    def _stop_editing(self) -> None:
        """入力元の終了時に両欄を停止し、保留中のstep入力を捨てる。"""
        if not qt.isValid(self):
            return
        blocker = qt.QtCore.QSignalBlocker(self.step_spin_box)
        try:
            self.step_spin_box.setValue(self.singleStep())
            self.step_spin_box.setEnabled(False)
            self.spin_box.setInputEnabled(False)
        finally:
            del blocker
