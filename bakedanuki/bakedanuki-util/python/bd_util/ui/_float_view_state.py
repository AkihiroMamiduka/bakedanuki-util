# coding: utf-8
import json
from dataclasses import dataclass
from typing import ClassVar, cast

from . import qt
from .binding.float._validation import require_float, require_slider_range
from .binding.float.view.range_slider_spin_box import FloatRangeSliderSpinBox
from .binding.float.view.step_spin_box import require_step
from ._ui_state_adapter import UiStateAdapter, require_widget


@dataclass(frozen=True)
class FloatRangeStateAdapter(UiStateAdapter):
    """公開単位の操作範囲と表示単位のstepを、1行ごとに保存・復元する。"""

    state_type: ClassVar[str] = "float_range_slider_spin_box"
    _VERSION: ClassVar[int] = 1
    widget: FloatRangeSliderSpinBox

    @property
    def state_object(self) -> qt.QObject:
        """状態を所有する複合Viewを返す。"""
        return self.widget

    @property
    def is_available(self) -> bool:
        """QtとBindingが共に利用できる間だけ取得・復元を許可する。"""
        if not qt.isValid(self.widget):
            return False
        try:
            self.widget.view_model
        except RuntimeError:
            return False
        return (
            qt.isValid(self.widget.slider)
            and qt.isValid(self.widget.spin_box)
            and qt.isValid(self.widget.step_spin_box)
        )

    def require_available(self) -> None:
        """公開登録APIへ渡されたViewの型と寿命を検証する。"""
        require_widget(self.widget, FloatRangeSliderSpinBox)
        if not self.is_available:
            raise RuntimeError("登録対象のViewまたはBindingは終了しています")

    def save_state(self) -> qt.QtCore.QByteArray:
        """丸め前の設定をJSONへ変換し、既存のQByteArray保存経路へ渡す。"""
        minimum, maximum = self.widget.floatRange()
        data = {
            "version": self._VERSION,
            "unit_kind": self.widget.view_model.presentation.unit_kind,
            "minimum": minimum,
            "maximum": maximum,
            "single_step": self.widget.singleStep(),
        }
        return qt.QtCore.QByteArray(
            json.dumps(data, allow_nan=False, separators=(",", ":")).encode(
                "utf-8"
            )
        )

    def restore_state(
        self, settings: qt.QtCore.QSettings, state_key: str
    ) -> bool:
        """全項目の互換性・範囲を検証してから、正本を変更せずに1行へ適用する。"""
        raw = settings.value(state_key)
        if not isinstance(raw, qt.QtCore.QByteArray):
            return False
        try:
            decoded: object = json.loads(raw.data())
            if not isinstance(decoded, dict):
                return False
            data = cast(dict[str, object], decoded)
            if (
                type(data.get("version")) is not int
                or data["version"] != self._VERSION
            ):
                return False
            presentation = self.widget.view_model.presentation
            if data.get("unit_kind") != presentation.unit_kind:
                return False
            minimum, maximum = require_slider_range(
                require_float(data.get("minimum"), "minimum"),
                require_float(data.get("maximum"), "maximum"),
            )
            step = require_step(data.get("single_step"), "single_step")
            presentation.to_display(minimum)
            presentation.to_display(maximum)
        except (ValueError, TypeError, OverflowError, UnicodeError):
            return False

        # 中間の設定通知を抑止し、行の全設定が揃ってから保存側へ通知する。
        previous = (*self.widget.floatRange(), self.widget.singleStep())
        blocker = qt.QtCore.QSignalBlocker(self.widget)
        try:
            self.widget.setFloatRange(minimum, maximum)
            self.widget.setSingleStep(step)
        finally:
            del blocker
        if previous != (minimum, maximum, step):
            self.widget.settingsChanged.emit()
        return True
