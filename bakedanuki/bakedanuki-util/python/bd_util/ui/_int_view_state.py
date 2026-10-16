# coding: utf-8
import json
from dataclasses import dataclass
from typing import ClassVar, cast

from . import qt
from .binding.int._validation import require_slider_range, require_step
from .binding.int.view.range_slider_spin_box import IntRangeSliderSpinBox
from ._ui_state_adapter import UiStateAdapter, require_widget


@dataclass(frozen=True)
class IntRangeStateAdapter(UiStateAdapter):
    """整数ViewのMin・Max・StepだけをJSON整数で保存・復元する。"""

    state_type: ClassVar[str] = "int_range_slider_spin_box"
    _VERSION: ClassVar[int] = 1
    widget: IntRangeSliderSpinBox

    @property
    def state_object(self) -> qt.QObject:
        """状態を所有する整数複合Viewを返す。"""
        return self.widget

    @property
    def is_available(self) -> bool:
        """QtとBindingが共に生存している間だけ保存・復元を許可する。"""
        if not qt.isValid(self.widget):
            return False
        try:
            self.widget.view_model
        except RuntimeError:
            return False
        return all(
            qt.isValid(child)
            for child in (
                self.widget.slider,
                self.widget.spin_box,
                self.widget.minimum_spin_box,
                self.widget.maximum_spin_box,
                self.widget.step_spin_box,
            )
        )

    def require_available(self) -> None:
        """登録対象の型と寿命を検証する。"""
        require_widget(self.widget, IntRangeSliderSpinBox)
        if not self.is_available:
            raise RuntimeError("登録対象のViewまたはBindingは終了しています")

    def save_state(self) -> qt.QtCore.QByteArray:
        """丸めやfloat変換をせず、全設定をJSON整数として取得する。"""
        minimum, maximum = self.widget.intRange()
        data = {
            "version": self._VERSION,
            "minimum": minimum,
            "maximum": maximum,
            "single_step": self.widget.singleStep(),
        }
        return qt.QtCore.QByteArray(
            json.dumps(data, separators=(",", ":")).encode("utf-8")
        )

    def restore_state(
        self, settings: qt.QtCore.QSettings, state_key: str
    ) -> bool:
        """全項目を検証してから一括復元し、最後に一回だけ設定を通知する。"""
        raw = settings.value(state_key)
        if not isinstance(raw, qt.QtCore.QByteArray):
            return False
        try:
            decoded: object = json.loads(bytes(raw.data()))
            if not isinstance(decoded, dict):
                return False
            data = cast(dict[str, object], decoded)
            if (
                type(data.get("version")) is not int
                or data["version"] != self._VERSION
            ):
                return False
            minimum, maximum = require_slider_range(
                data.get("minimum"), data.get("maximum")
            )
            step = require_step(data.get("single_step"))
        except (ValueError, TypeError, OverflowError, UnicodeError):
            return False

        # 中間設定を保存側へ通知せず、範囲変更では進行中の操作も終了する
        previous = (*self.widget.intRange(), self.widget.singleStep())
        blocker = qt.QtCore.QSignalBlocker(self.widget)
        try:
            self.widget.setIntRange(minimum, maximum)
            self.widget.setSingleStep(step)
        finally:
            del blocker
        if previous != (minimum, maximum, step):
            self.widget.settingsChanged.emit()
        return True
