# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued
from .._validation import (
    INT32_MIN,
    INT32_MAX,
    require_slider_range,
    require_step,
)
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel
from .slider_spin_box import IntSliderSpinBox
from .step_spin_box import IntStepMode, IntStepSpinBox, require_step_mode

__all__ = ["IntRangeSliderSpinBox"]


def require_width(value: object, name: str) -> int | None:
    """自動幅またはQtの最大幅以下の正の整数を検証する。"""
    if value is None:
        return None
    if type(value) is not int:
        raise TypeError(f"{name}にはintまたはNoneを指定してください")
    if not 1 <= value <= 16777215:
        raise ValueError(f"{name}は1～16777215にしてください")
    return value


def require_bool(value: object, name: str) -> bool:
    """入力可否とボタン表示を厳密なboolとして検証する。"""
    if type(value) is not bool:
        raise TypeError(f"{name}にはboolを指定してください")
    return value


class IntRangeSliderSpinBox(IntSliderSpinBox):
    """Min・Slider・Max・値・Stepを並べ、View固有の操作設定を編集する。

    Attributes:
        rangeEditRejected: 不正なMin／Max入力を拒否した理由を通知する。
        settingsChanged: 操作範囲または値欄のStepの実変更時に通知する。
    """

    rangeEditRejected = qt.Signal(str)
    settingsChanged = qt.Signal()

    def __init__(
        self,
        view_model: IntViewModel | IntBinding[IntValueStore],
        parent: qt.QWidget | None = None,
        *,
        minimum: int,
        maximum: int,
        steps: int = 1000,
        single_step: int = 1,
        step_mode: IntStepMode = "additive",
        step_increment: int = 1,
        slider_width: int | None = None,
        minimum_width: int | None = None,
        maximum_width: int | None = None,
        value_width: int | None = None,
        step_width: int | None = None,
        minimum_enabled: bool = True,
        maximum_enabled: bool = True,
        value_enabled: bool = True,
        step_enabled: bool = True,
        minimum_show_buttons: bool = True,
        maximum_show_buttons: bool = True,
        value_show_buttons: bool = True,
        step_show_buttons: bool = True,
        value_select_all_on_mouse_focus: bool = False,
    ) -> None:
        """整数の操作範囲と各欄の幅・操作条件を指定する。

        Args:
            view_model: 共有する整数ViewModelまたはBinding。
            parent: このViewを所有するWidget。
            minimum: Sliderの32-bit整数の下限。
            maximum: Sliderの上限。`minimum`より大きくする。
            steps: Sliderの最大分割数。値欄のStepとは独立。
            single_step: 値欄の正の整数刻み幅。既定1。
            step_mode: Step欄の`additive`または`multiplicative`方式。
            step_increment: 加算方式でStep欄自身を増減する正の整数。
            slider_width: Sliderの固定幅。`None`なら伸縮。
            minimum_width: Min欄の固定幅。`None`なら伸縮。
            maximum_width: Max欄の固定幅。`None`なら伸縮。
            value_width: 値欄の固定幅。`None`なら伸縮。
            step_width: Step欄の固定幅。`None`なら伸縮。
            minimum_enabled: Min欄の編集を許すか。
            maximum_enabled: Max欄の編集を許すか。
            value_enabled: 値欄の編集を許すか。
            step_enabled: Step欄の編集を許すか。
            minimum_show_buttons: Min欄の上下ボタンを表示するか。
            maximum_show_buttons: Max欄の上下ボタンを表示するか。
            value_show_buttons: 値欄の上下ボタンを表示するか。
            step_show_buttons: Step欄の上下ボタンを表示するか。
            value_select_all_on_mouse_focus: 値欄の初回文字クリックで全選択するか。

        範囲とStepの変更は正本やMayaのhard limitへ書き込まない。
        Min／Max欄自身の刻み幅は1で、値欄のStepとは独立する。
        """
        widths = tuple(
            require_width(value, name)
            for value, name in (
                (minimum_width, "minimum_width"),
                (slider_width, "slider_width"),
                (maximum_width, "maximum_width"),
                (value_width, "value_width"),
                (step_width, "step_width"),
            )
        )
        flags = tuple(
            require_bool(value, name)
            for value, name in (
                (minimum_enabled, "minimum_enabled"),
                (maximum_enabled, "maximum_enabled"),
                (value_enabled, "value_enabled"),
                (step_enabled, "step_enabled"),
                (minimum_show_buttons, "minimum_show_buttons"),
                (maximum_show_buttons, "maximum_show_buttons"),
                (value_show_buttons, "value_show_buttons"),
                (step_show_buttons, "step_show_buttons"),
            )
        )
        single_step = require_step(single_step)
        step_increment = require_step(step_increment, "step_increment")
        step_mode = require_step_mode(step_mode)
        super().__init__(
            view_model,
            parent,
            minimum=minimum,
            maximum=maximum,
            steps=steps,
            single_step=single_step,
            value_select_all_on_mouse_focus=value_select_all_on_mouse_focus,
        )
        self._minimum_enabled, self._maximum_enabled = flags[:2]
        self._step_enabled = flags[3]
        self._last_settings: tuple[int, int, int] | None = None
        try:
            # 設定欄は正本のCommandへ接続しない
            self.minimum_spin_box = self._create_bound("Slider minimum")
            self.maximum_spin_box = self._create_bound("Slider maximum")
            self.step_spin_box = IntStepSpinBox(
                self,
                value=single_step,
                step_mode=step_mode,
                step_increment=step_increment,
            )
            self._row.insertWidget(0, self.minimum_spin_box)
            self._row.insertWidget(2, self.maximum_spin_box)
            self._row.addWidget(self.step_spin_box)
            buttons = qt.QtWidgets.QAbstractSpinBox.ButtonSymbols
            for spin_box, visible in zip(
                (
                    self.minimum_spin_box,
                    self.maximum_spin_box,
                    self.spin_box,
                    self.step_spin_box,
                ),
                flags[4:],
            ):
                spin_box.setButtonSymbols(
                    buttons.UpDownArrows if visible else buttons.NoButtons
                )
            widgets = (
                self.minimum_spin_box,
                self.slider,
                self.maximum_spin_box,
                self.spin_box,
                self.step_spin_box,
            )
            for widget, width in zip(widgets, widths):
                policy = widget.sizePolicy()
                policy.setHorizontalPolicy(
                    qt.QSizePolicy.Policy.Expanding
                    if width is None
                    else qt.QSizePolicy.Policy.Fixed
                )
                widget.setSizePolicy(policy)
                self._row.setStretchFactor(widget, 1 if width is None else 0)
                if width is not None:
                    widget.setFixedWidth(width)
            if all(width is not None for width in widths):
                self._row.addStretch(1)
            self.spin_box.setInputEnabled(flags[2])
            if not flags[2]:
                self.setFocusProxy(self.slider)
            self._refresh_range()
            self._refresh_step()
            self._notify_settings_changed()
            self.minimum_spin_box.valueChanged.connect(self._request_minimum)
            self.maximum_spin_box.valueChanged.connect(self._request_maximum)
            self.step_spin_box.valueChanged.connect(self._request_step)
            self.slider.intRangeChanged.connect(self._refresh_range)
            self.slider.intRangeChanged.connect(self._notify_settings_changed)
            self.view_model.presentation_changed.connect(self._refresh_range)
            self.view_model.disposed.connect(self._stop_range_editing)
            connect_queued(self.view_model.destroyed, self._stop_range_editing)
            for first, second in zip(widgets, widgets[1:]):
                qt.QWidget.setTabOrder(first, second)
        except Exception:
            self.setParent(None)
            self.deleteLater()
            raise

    def _create_layout(self) -> qt.QHBoxLayout:
        """入力行と範囲の説明領域を作る。"""
        layout = qt.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._row = qt.QHBoxLayout()
        layout.addLayout(self._row)
        self.range_status_label = qt.QLabel(self)
        self.range_status_label.setWordWrap(True)
        self.range_status_label.hide()
        layout.addWidget(self.range_status_label)
        return self._row

    def _create_bound(self, name: str) -> qt.QSpinBox:
        """32-bit整数を確定時だけ通知する範囲欄を作る。"""
        spin_box = qt.QSpinBox(self)
        spin_box.setRange(INT32_MIN, INT32_MAX)
        spin_box.setSingleStep(1)
        spin_box.setKeyboardTracking(False)
        spin_box.setWrapping(False)
        spin_box.setAccessibleName(name)
        spin_box.setToolTip(f"{name}（正本の値は変更しません）")
        return spin_box

    def intRange(self) -> tuple[int, int]:
        """このView固有の操作範囲を返す。"""
        return self.slider.intRange()

    def setIntRange(self, minimum: int, maximum: int) -> None:
        """操作範囲を変更する。不正な範囲では変更前に例外を送出する。"""
        minimum, maximum = require_slider_range(minimum, maximum)
        self.view_model
        self.slider.setIntRange(minimum, maximum)
        self._refresh_range()

    def effectiveIntRange(self) -> tuple[int, int] | None:
        """正本の型・hard limitとの共通部分を返す。操作不能なら`None`。"""
        return self.slider.effectiveIntRange()

    def singleStep(self) -> int:
        """値欄の現在の整数刻み幅を返す。"""
        return self.spin_box.singleStep()

    def setSingleStep(self, single_step: int) -> None:
        """値欄だけのStepを変更し、Step欄と設定通知へ反映する。"""
        single_step = require_step(single_step)
        self.view_model
        self.spin_box.setSingleStep(single_step)
        self._refresh_step()
        self._notify_settings_changed()

    @qt.Slot()
    def _notify_settings_changed(self) -> None:
        """確定した範囲とStepの実変更時だけ通知する。"""
        if self._view_model.is_disposed:
            return
        settings = (*self.intRange(), self.singleStep())
        if settings != self._last_settings:
            self._last_settings = settings
            self.settingsChanged.emit()

    @qt.Slot(int)
    def _request_step(self, value: int) -> None:
        """有効なStep欄からの入力だけをこのViewへ適用する。"""
        if self._view_model.is_disposed:
            self._stop_range_editing()
        elif self._step_enabled:
            self.setSingleStep(value)
        else:
            self._refresh_step()

    def _refresh_step(self) -> None:
        """正本を変更せず、Step欄を値欄の刻み幅へ合わせる。"""
        blocker = qt.QtCore.QSignalBlocker(self.step_spin_box)
        try:
            self.step_spin_box.setValue(self.singleStep())
            self.step_spin_box.setEnabled(self._step_enabled)
        finally:
            del blocker

    @qt.Slot(int)
    def _request_minimum(self, value: int) -> None:
        """Min欄の確定値を要求する。"""
        self._request_bound(value, minimum=True)

    @qt.Slot(int)
    def _request_maximum(self, value: int) -> None:
        """Max欄の確定値を要求する。"""
        self._request_bound(value, minimum=False)

    def _request_bound(self, value: int, *, minimum: bool) -> None:
        """不正なMin／Max入力を元に戻し、拒否理由を表示する。"""
        if self._view_model.is_disposed:
            self._stop_range_editing()
            return
        if not (self._minimum_enabled if minimum else self._maximum_enabled):
            self._refresh_range()
            return
        lower, upper = self.intRange()
        try:
            self.setIntRange(
                value if minimum else lower, upper if minimum else value
            )
        except ValueError:
            self._refresh_range()
            message = (
                "範囲を変更できません：Min < Max の整数を入力してください。"
            )
            self.range_status_label.setText(message)
            self.range_status_label.show()
            self.rangeEditRejected.emit(message)

    @qt.Slot()
    def _refresh_range(self) -> None:
        """要求範囲の表示と、制限に交差した実効範囲の説明を更新する。"""
        if self._view_model.is_disposed:
            self._stop_range_editing()
            return
        lower, upper = self.intRange()
        for spin_box, value, enabled in (
            (self.minimum_spin_box, lower, self._minimum_enabled),
            (self.maximum_spin_box, upper, self._maximum_enabled),
        ):
            blocker = qt.QtCore.QSignalBlocker(spin_box)
            try:
                spin_box.setValue(value)
                spin_box.setEnabled(enabled)
            finally:
                del blocker
        effective = self.effectiveIntRange()
        message = ""
        if effective is None:
            message = "属性の制限内に操作可能なSlider範囲がありません。"
        elif effective != (lower, upper):
            message = (
                f"操作可能範囲：{effective[0]} ～ {effective[1]}（属性の制限）"
            )
        self.range_status_label.setText(message)
        self.range_status_label.setVisible(bool(message))

    @qt.Slot()
    def _stop_range_editing(self) -> None:
        """正本の終了後は設定欄の入力も停止する。"""
        if qt.isValid(self):
            self.minimum_spin_box.setEnabled(False)
            self.maximum_spin_box.setEnabled(False)
            self.step_spin_box.setEnabled(False)
