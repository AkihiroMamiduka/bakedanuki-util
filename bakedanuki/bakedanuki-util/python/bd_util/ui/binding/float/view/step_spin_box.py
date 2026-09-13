# coding: utf-8
from __future__ import annotations

from decimal import Decimal, localcontext
from sys import float_info
from typing import Literal

from .... import qt
from .._validation import require_float

FloatStepMode = Literal["additive", "multiplicative"]


def require_step_mode(value: object) -> FloatStepMode:
    """刻み幅の加算・桁変更モードを検証する。"""
    if value == "additive":
        return "additive"
    if value == "multiplicative":
        return "multiplicative"
    raise ValueError(
        "step_modeは'additive'または'multiplicative'にしてください"
    )


def require_step(value: object, name: str) -> float:
    """Qtで保持できる、正の有限な刻み幅を検証する。"""
    value = require_float(value, name)
    if value < 1e-323:
        raise ValueError(f"{name}は1e-323以上の正の有限値にしてください")
    return value


class FloatStepSpinBox(qt.QDoubleSpinBox):
    """正の刻み幅を加算または10倍・1/10倍で編集する、正本を持たない入力欄。"""

    def __init__(
        self,
        parent: qt.QWidget | None = None,
        *,
        value: float = 0.1,
        step_mode: FloatStepMode = "additive",
        step_increment: float = 1.0,
    ) -> None:
        """初期刻み幅と操作モード、加算モードの増減量を指定する。"""
        value = require_step(value, "value")
        step_mode = require_step_mode(step_mode)
        step_increment = require_step(step_increment, "step_increment")
        super().__init__(parent)
        self._step_mode: FloatStepMode = step_mode
        # 表示桁数から独立して小さい刻み幅を保持し、末尾の0は表示時に省く。
        self.setDecimals(323)
        self.setRange(1e-323, float_info.max)
        self.setSingleStep(step_increment)
        self.setKeyboardTracking(False)
        self.setWrapping(False)
        self.setCorrectionMode(
            qt.QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue
        )
        self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
        self.setAccessibleName("Value step")
        operation = (
            f"add/subtract {step_increment:g}"
            if step_mode == "additive"
            else "multiply/divide by 10"
        )
        self.setToolTip(
            f"Value step ({operation}); the current value is preserved."
        )
        self.setValue(value)

    def stepMode(self) -> FloatStepMode:
        """生成時に選択した増減モードを返す。"""
        return self._step_mode

    def setValue(self, val: float) -> None:
        """不正な刻み幅を黙って丸めず、正の有限値だけを設定する。"""
        super().setValue(require_step(val, "value"))

    def textFromValue(self, val: float) -> str:
        """floatを再現する短い十進表記を、現在のロケールで表示する。"""
        text = format(Decimal(str(val)), "f")
        if "." in text:
            text = text.rstrip("0").rstrip(".")
        return text.replace(".", self.locale().decimalPoint())

    def stepBy(self, steps: int) -> None:
        """未確定入力を確定してから増減し、overflowと0への到達を防ぐ。"""
        if not self.isEnabled() or self.isReadOnly() or not steps:
            return
        self.interpretText()
        # 演算精度を固定し、15→1.5→0.15の不要な誤差を避ける。
        with localcontext() as context:
            context.prec = 28
            value = Decimal(str(self.value()))
            if self._step_mode == "multiplicative":
                value *= Decimal(10) ** max(-632, min(632, steps))
            else:
                value += Decimal(str(self.singleStep())) * steps
                if value <= 0:
                    return
        lower = Decimal(str(self.minimum()))
        upper = Decimal(str(self.maximum()))
        self.setValue(float(max(lower, min(upper, value))))

    def stepEnabled(self) -> qt.QtWidgets.QAbstractSpinBox.StepEnabledFlag:
        """確定可能な入力を含めて、正の範囲で増減できる方向を判定する。"""
        flag = qt.QtWidgets.QAbstractSpinBox.StepEnabledFlag
        flags = flag.StepNone
        if self.isReadOnly():
            return flags
        value = (
            self.valueFromText(self.text())
            if self.hasAcceptableInput()
            else self.value()
        )
        if value < self.maximum():
            flags |= flag.StepUpEnabled
        if value > self.minimum() and (
            self._step_mode == "multiplicative" or value > self.singleStep()
        ):
            flags |= flag.StepDownEnabled
        return flags

    def wheelEvent(self, event: qt.QtGui.QWheelEvent) -> None:
        """スクロール中の誤変更を避け、フォーカス中だけホイール操作を受け付ける。"""
        if not self.hasFocus():
            event.ignore()
            return
        super().wheelEvent(event)
