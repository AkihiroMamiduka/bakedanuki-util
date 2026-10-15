# coding: utf-8
from __future__ import annotations

from typing import Literal

from .... import qt
from ..._spin_box_mouse_selection import SpinBoxMouseFocusSelection
from .._validation import INT32_MAX, require_int, require_step

IntStepMode = Literal["additive", "multiplicative"]


def require_step_mode(value: object) -> IntStepMode:
    """整数Step欄の加算・10倍方式を検証する。"""
    if value == "additive":
        return "additive"
    if value == "multiplicative":
        return "multiplicative"
    raise ValueError("step_modeはadditiveまたはmultiplicativeにしてください")


class IntStepSpinBox(qt.QSpinBox):
    """正の整数Stepを加算または10倍・整数除算で編集する入力欄。"""

    def __init__(
        self,
        parent: qt.QWidget | None = None,
        *,
        value: int = 1,
        step_mode: IntStepMode = "additive",
        step_increment: int = 1,
        wheel_requires_focus: bool = True,
        select_all_on_mouse_focus: bool = False,
    ) -> None:
        """整数Stepと操作方式を指定し、正本を持たない欄を作る。

        Args:
            parent: この欄を所有するWidget。
            value: 初期Step。1～2147483647の整数。
            step_mode: `additive`は加算、`multiplicative`は10倍と整数除算。
            step_increment: 加算方式でStep欄自身を増減する正の整数。
            wheel_requires_focus: 未フォーカスのホイールを親へ渡すか。
            select_all_on_mouse_focus: 初回の文字クリックで全選択するか。
        """
        value = require_step(value, "value")
        step_mode = require_step_mode(step_mode)
        step_increment = require_step(step_increment, "step_increment")
        if type(wheel_requires_focus) is not bool:
            raise TypeError("wheel_requires_focusにはboolを指定してください")
        if type(select_all_on_mouse_focus) is not bool:
            raise TypeError(
                "select_all_on_mouse_focusにはboolを指定してください"
            )
        super().__init__(parent)
        self._step_mode: IntStepMode = step_mode
        self._wheel_requires_focus = wheel_requires_focus
        self._mouse_selection = SpinBoxMouseFocusSelection(
            self, select_all_on_mouse_focus
        )
        self.setRange(1, INT32_MAX)
        self.setValue(value)
        self.setSingleStep(step_increment)
        self.setKeyboardTracking(False)
        self.setWrapping(False)
        self.setCorrectionMode(
            qt.QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue
        )
        self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
        self.setAccessibleName("Value step")
        self.setToolTip(
            "正の整数Step。10倍方式の減少は整数除算、下限は1。上限を超える増加は無効。"
        )

    def stepMode(self) -> IntStepMode:
        """生成時に選択した操作方式を返す。"""
        return self._step_mode

    def setValue(self, val: int) -> None:
        """小数・bool・範囲外を丸めず、正の整数Stepだけを設定する。"""
        super().setValue(require_step(val, "value"))

    def setSingleStep(self, val: int) -> None:
        """加算方式の増減量を正の整数として設定する。"""
        super().setSingleStep(require_step(val, "single_step"))

    def stepBy(self, steps: int) -> None:
        """未確定入力を確定後に整数演算し、上限超過では現在値を維持する。"""
        steps = require_int(steps, "steps")
        if not steps or not self.isEnabled() or self.isReadOnly():
            return
        self.interpretText()
        current = self.value()
        if self._step_mode == "multiplicative":
            if steps > 0:
                # 最大10桁なので、巨大なべき乗を作らず増加不能を判定する
                if steps > 9:
                    return
                value = current * 10**steps
            else:
                value = max(1, current // 10 ** min(-steps, 10))
        else:
            value = current + self.singleStep() * steps
        if self.minimum() <= value <= self.maximum():
            self.setValue(value)

    def stepEnabled(self) -> qt.QtWidgets.QAbstractSpinBox.StepEnabledFlag:
        """現在の入力と方式から、実行可能な増減方向だけを有効にする。"""
        flag = qt.QtWidgets.QAbstractSpinBox.StepEnabledFlag
        flags = flag.StepNone
        if self.isReadOnly():
            return flags
        value = (
            self.valueFromText(self.text())
            if self.hasAcceptableInput()
            else self.value()
        )
        if self._step_mode == "multiplicative":
            up = value <= self.maximum() // 10
            down = value > self.minimum()
        else:
            up = value + self.singleStep() <= self.maximum()
            down = value - self.singleStep() >= self.minimum()
        if up:
            flags |= flag.StepUpEnabled
        if down:
            flags |= flag.StepDownEnabled
        return flags

    def wheel_requires_focus(self) -> bool:
        """ホイール操作にフォーカスを必須とするか返す。"""
        return self._wheel_requires_focus

    def set_wheel_requires_focus(self, required: bool) -> None:
        """未フォーカスのホイールを親へ渡す設定を変更する。"""
        if type(required) is not bool:
            raise TypeError("requiredにはboolを指定してください")
        self._wheel_requires_focus = required

    def wheelEvent(self, event: qt.QtGui.QWheelEvent) -> None:
        """設定に従い、未フォーカスのホイールを親へ渡す。"""
        if self._wheel_requires_focus and not self.hasFocus():
            event.ignore()
            return
        super().wheelEvent(event)

    def event(self, event: qt.QEvent) -> bool:
        """Enterのshortcutを整数Step欄で受理する。"""
        if (
            event.type() == qt.QEvent.Type.ShortcutOverride
            and isinstance(event, qt.QtGui.QKeyEvent)
            and event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter)
        ):
            event.accept()
            return True
        return super().event(event)

    def keyPressEvent(self, event: qt.QtGui.QKeyEvent) -> None:
        """値を確定し、Enterの押下を親へ伝播しない。"""
        super().keyPressEvent(event)
        if event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            event.accept()

    def keyReleaseEvent(self, event: qt.QtGui.QKeyEvent) -> None:
        """Enterの解放も欄内で受理する。"""
        super().keyReleaseEvent(event)
        if event.key() in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
            event.accept()

    def select_all_on_mouse_focus(self) -> bool:
        """初回の文字クリックで全選択する設定を返す。"""
        return self._mouse_selection.enabled

    def set_select_all_on_mouse_focus(self, enabled: bool) -> None:
        """初回の文字クリックで全選択する設定を変更する。"""
        self._mouse_selection.set_enabled(enabled)

    def focusInEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """マウスフォーカスを全選択の候補として記録する。"""
        self._mouse_selection.focus_in(event)
        super().focusInEvent(event)

    def focusOutEvent(self, event: qt.QtGui.QFocusEvent) -> None:
        """フォーカス喪失時に全選択の予約を破棄する。"""
        self._mouse_selection.reset()
        super().focusOutEvent(event)

    def mousePressEvent(self, event: qt.QtGui.QMouseEvent) -> None:
        """矢印や枠のクリックで全選択しないよう予約をリセットする。"""
        self._mouse_selection.reset()
        super().mousePressEvent(event)
