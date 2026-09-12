# coding: utf-8
from __future__ import annotations

from sys import float_info

from .... import qt
from .._validation import require_decimals, require_float, require_slider_range
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel
from ._connection import connect_queued_qt_signal
from .slider_spin_box import FloatSliderSpinBox


def _require_width(value: object, argument_name: str) -> int | None:
    """自動伸縮のNone、またはQtの最大幅以下の正の整数を検証する。"""
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{argument_name}にはintまたはNoneを指定してください")
    if not 1 <= value <= 16777215:
        raise ValueError(f"{argument_name}は1～16777215にしてください")
    return value


def _require_bool(value: object, argument_name: str) -> bool:
    """表示・操作設定にbool以外の暗黙変換が混ざることを防ぐ。"""
    if not isinstance(value, bool):
        raise TypeError(f"{argument_name}にはboolを指定してください")
    return value


class FloatRangeSliderSpinBox(FloatSliderSpinBox):
    """最小値・最大値を表示単位で編集できる、View固有の操作範囲付きView。"""

    rangeEditRejected = qt.Signal(str)

    def __init__(
        self,
        view_model: FloatViewModel | FloatBinding[FloatValueStore],
        parent: qt.QWidget | None = None,
        *,
        minimum: float,
        maximum: float,
        steps: int = 1000,
        decimals: int = 6,
        single_step: float = 0.1,
        slider_width: int | None = None,
        minimum_width: int | None = None,
        maximum_width: int | None = None,
        value_width: int | None = None,
        minimum_enabled: bool = True,
        maximum_enabled: bool = True,
        value_enabled: bool = True,
        minimum_show_buttons: bool = True,
        maximum_show_buttons: bool = True,
        value_show_buttons: bool = True,
        minimum_decimals: int = 0,
        maximum_decimals: int = 0,
    ) -> None:
        """公開単位の範囲と、各部品の固定幅・操作可否・ボタン表示を指定する。"""
        # 不正な表示設定で、親に生成途中のWidgetを残さない。
        slider_width = _require_width(slider_width, "slider_width")
        minimum_width = _require_width(minimum_width, "minimum_width")
        maximum_width = _require_width(maximum_width, "maximum_width")
        value_width = _require_width(value_width, "value_width")
        minimum_enabled = _require_bool(minimum_enabled, "minimum_enabled")
        maximum_enabled = _require_bool(maximum_enabled, "maximum_enabled")
        value_enabled = _require_bool(value_enabled, "value_enabled")
        minimum_show_buttons = _require_bool(
            minimum_show_buttons, "minimum_show_buttons"
        )
        maximum_show_buttons = _require_bool(
            maximum_show_buttons, "maximum_show_buttons"
        )
        value_show_buttons = _require_bool(
            value_show_buttons, "value_show_buttons"
        )
        minimum_decimals = require_decimals(minimum_decimals)
        maximum_decimals = require_decimals(maximum_decimals)
        super().__init__(
            view_model,
            parent,
            minimum=minimum,
            maximum=maximum,
            steps=steps,
            decimals=decimals,
            single_step=single_step,
        )
        self._minimum_enabled = minimum_enabled
        self._maximum_enabled = maximum_enabled
        try:
            # 範囲入力は値のCommandへ接続せず、このSliderの設定だけを編集する。
            self.minimum_spin_box = self._create_bound("Slider minimum")
            self.maximum_spin_box = self._create_bound("Slider maximum")
            self._row.insertWidget(0, self.minimum_spin_box)
            self._row.insertWidget(2, self.maximum_spin_box)

            # 各入力欄のボタン表示を独立させ、未指定幅の部品へ余白を配分する。
            buttons = qt.QtWidgets.QAbstractSpinBox.ButtonSymbols
            for spin_box, show_buttons in (
                (self.minimum_spin_box, minimum_show_buttons),
                (self.maximum_spin_box, maximum_show_buttons),
                (self.spin_box, value_show_buttons),
            ):
                spin_box.setButtonSymbols(
                    buttons.UpDownArrows if show_buttons else buttons.NoButtons
                )
            for widget, width in (
                (self.slider, slider_width),
                (self.minimum_spin_box, minimum_width),
                (self.maximum_spin_box, maximum_width),
                (self.spin_box, value_width),
            ):
                self._configure_width(widget, width)
            if all(
                width is not None
                for width in (
                    slider_width,
                    minimum_width,
                    maximum_width,
                    value_width,
                )
            ):
                self._row.addStretch(1)
            self.spin_box.setInputEnabled(value_enabled)
            if not value_enabled:
                self.setFocusProxy(self.slider)
            self.setMinimumDecimals(minimum_decimals)
            self.setMaximumDecimals(maximum_decimals)
            self.setSingleStep(single_step)
            self.minimum_spin_box.valueChanged.connect(self._request_minimum)
            self.maximum_spin_box.valueChanged.connect(self._request_maximum)

            # 外部APIと単位変更も同じ表示へ集約し、未確定の古い単位入力を破棄する。
            self.slider.floatRangeChanged.connect(self._refresh_range)
            self.view_model.presentation_changed.connect(self._refresh_range)
            self.view_model.disposed.connect(self._stop_range_editing)
            connect_queued_qt_signal(
                self.view_model.destroyed, self._stop_range_editing
            )
            qt.QWidget.setTabOrder(self.minimum_spin_box, self.slider)
            qt.QWidget.setTabOrder(self.slider, self.maximum_spin_box)
            qt.QWidget.setTabOrder(self.maximum_spin_box, self.spin_box)
        except Exception:
            # 範囲の表示変換が失敗しても、共有している正本を終了しない。
            self.setParent(None)
            self.deleteLater()
            raise

    def _create_layout(self) -> qt.QHBoxLayout:
        """入力行の下に、拒否理由や有効範囲を表示する領域を用意する。"""
        layout = qt.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._row = qt.QHBoxLayout()
        layout.addLayout(self._row)
        self.range_status_label = qt.QLabel(self)
        self.range_status_label.setWordWrap(True)
        self.range_status_label.hide()
        layout.addWidget(self.range_status_label)
        return self._row

    def _create_bound(self, name: str) -> qt.QDoubleSpinBox:
        """有限値を入力できる範囲専用SpinBoxを、文字入力の確定待ちで作る。"""
        spin_box = qt.QDoubleSpinBox(self)
        spin_box.setRange(-float_info.max, float_info.max)
        spin_box.setKeyboardTracking(False)
        spin_box.setWrapping(False)
        spin_box.setAccessibleName(name)
        spin_box.setToolTip(f"{name}; the current value is preserved.")
        return spin_box

    def _configure_width(self, widget: qt.QWidget, width: int | None) -> None:
        """指定幅を固定し、未指定の部品には同じ横方向の伸縮比率を設定する。"""
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

    def floatRange(self) -> tuple[float, float]:
        """このViewが保持する、公開単位の操作範囲を返す。"""
        return self.slider.floatRange()

    def setFloatRange(self, minimum: float, maximum: float) -> None:
        """公開単位の範囲を設定し、正本を変更せずに入力欄へ反映する。"""
        minimum, maximum = require_slider_range(minimum, maximum)
        # 範囲を変更する前に、両端を現在の表示単位へ変換できることを確認する。
        presentation = self.view_model.presentation
        presentation.to_display(minimum)
        presentation.to_display(maximum)
        self.slider.setFloatRange(minimum, maximum)
        self._refresh_range()

    def effectiveFloatRange(self) -> tuple[float, float] | None:
        """正本のhard limitを反映した、実際に操作できる公開単位範囲を返す。"""
        return self.slider.effectiveFloatRange()

    def decimals(self) -> int:
        """現在値の表示・入力桁数を返す。"""
        return self.spin_box.decimals()

    def setDecimals(self, decimals: int) -> None:
        """正本の値とMin／Maxの桁数を保持し、現在値の桁数を変更する。"""
        self._set_decimals(self.spin_box, decimals)
        self._refresh_range()
        self._refresh_current_value()

    def minimumDecimals(self) -> int:
        """Minの表示・入力桁数を返す。"""
        return self.minimum_spin_box.decimals()

    def setMinimumDecimals(self, decimals: int) -> None:
        """実際の操作範囲を保持し、Minの桁数と刻み幅を更新する。"""
        self._set_decimals(self.minimum_spin_box, decimals)
        self._refresh_bound_steps()
        self._refresh_range()

    def maximumDecimals(self) -> int:
        """Maxの表示・入力桁数を返す。"""
        return self.maximum_spin_box.decimals()

    def setMaximumDecimals(self, decimals: int) -> None:
        """実際の操作範囲を保持し、Maxの桁数と刻み幅を更新する。"""
        self._set_decimals(self.maximum_spin_box, decimals)
        self._refresh_bound_steps()
        self._refresh_range()

    def _set_decimals(
        self, spin_box: qt.QDoubleSpinBox, decimals: int
    ) -> None:
        """Qtによる丸めの入力通知を抑止して、指定欄の桁数を変更する。"""
        decimals = require_decimals(decimals)
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        blocker = qt.QtCore.QSignalBlocker(spin_box)
        try:
            spin_box.setDecimals(decimals)
        finally:
            del blocker

    def singleStep(self) -> float:
        """現在値の表示単位での刻み幅を返す。"""
        return self.spin_box.singleStep()

    def setSingleStep(self, single_step: float) -> None:
        """現在値の刻み幅を指定し、Min／Maxは各桁数で操作できる幅へ補正する。"""
        single_step = require_float(single_step, "single_step")
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")
        self.spin_box.setSingleStep(single_step)
        self._refresh_bound_steps()

    def _refresh_bound_steps(self) -> None:
        """0桁は1刻み、それ以外は指定刻み幅を表示可能な最小幅以上にする。"""
        for spin_box in (self.minimum_spin_box, self.maximum_spin_box):
            decimals = spin_box.decimals()
            spin_box.setSingleStep(
                1.0
                if decimals == 0
                else max(self.singleStep(), 10.0**-decimals)
            )

    def _refresh_current_value(self) -> None:
        """桁数を増やした場合も、現在値を正本の精度から再表示する。"""
        vm = self.view_model
        presentation = vm.presentation
        blocker = qt.QtCore.QSignalBlocker(self.spin_box)
        try:
            self.spin_box.setRange(
                (
                    -float_info.max
                    if presentation.minimum is None
                    else presentation.to_display(presentation.minimum)
                ),
                (
                    float_info.max
                    if presentation.maximum is None
                    else presentation.to_display(presentation.maximum)
                ),
            )
            self.spin_box.setValue(presentation.to_display(vm.value.value))
        finally:
            del blocker

    @qt.Slot(float)
    def _request_minimum(self, value: float) -> None:
        """表示単位の最小値入力を、このViewの操作範囲へ適用する。"""
        self._request_bound(value, minimum=True)

    @qt.Slot(float)
    def _request_maximum(self, value: float) -> None:
        """表示単位の最大値入力を、このViewの操作範囲へ適用する。"""
        self._request_bound(value, minimum=False)

    def _request_bound(self, value: float, *, minimum: bool) -> None:
        """変更した側だけを確定し、不正な範囲は復元して理由を表示する。"""
        if self._view_model.is_disposed:
            self._stop_range_editing()
            return
        if not (self._minimum_enabled if minimum else self._maximum_enabled):
            self._refresh_range()
            return
        lower, upper = self.floatRange()
        try:
            value = self.view_model.presentation.from_display(value)
            self.setFloatRange(
                value if minimum else lower, upper if minimum else value
            )
        except ValueError:
            self._refresh_range()
            message = "Range unchanged: enter finite values with Min < Max."
            self.range_status_label.setText(message)
            self.range_status_label.show()
            self.rangeEditRejected.emit(message)

    @qt.Slot()
    def _refresh_range(self) -> None:
        """範囲の実値を保持し、単位・表示丸め・hard limitの情報を更新する。"""
        if self._view_model.is_disposed:
            self._stop_range_editing()
            return
        presentation = self.view_model.presentation
        lower, upper = self.floatRange()
        try:
            display_range = (
                presentation.to_display(lower),
                presentation.to_display(upper),
            )
        except ValueError:
            # 表示単位でoverflowした場合は古い単位の入力を止め、APIでの範囲変更を待つ。
            self._stop_range_editing()
            self.minimum_spin_box.clear()
            self.maximum_spin_box.clear()
            self.range_status_label.setText(
                "Range cannot be displayed in the current unit."
            )
            self.range_status_label.show()
            return
        for spin_box, value, enabled in zip(
            (self.minimum_spin_box, self.maximum_spin_box),
            display_range,
            (self._minimum_enabled, self._maximum_enabled),
        ):
            blocker = qt.QtCore.QSignalBlocker(spin_box)
            try:
                spin_box.setSuffix(presentation.suffix)
                spin_box.setValue(value)
                spin_box.setEnabled(enabled)
            finally:
                del blocker

        # 設定範囲とhard limitが異なる場合も、つまみの実際の両端を明示する。
        effective = self.effectiveFloatRange()
        message = ""
        if effective is None:
            message = "No usable slider range within the attribute limits."
        elif effective != (lower, upper):
            start, end = (
                presentation.to_display(value) for value in effective
            )
            message = (
                f"Usable range: {start:.{self.decimals()}f}{presentation.suffix}"
                f" to {end:.{self.decimals()}f}{presentation.suffix} (attribute limits)"
            )
        self.range_status_label.setText(message)
        self.range_status_label.setVisible(bool(message))

    @qt.Slot()
    def _stop_range_editing(self) -> None:
        """正本の終了後は範囲入力も停止し、破棄済みWidgetには触れない。"""
        if qt.isValid(self):
            self.minimum_spin_box.setEnabled(False)
            self.maximum_spin_box.setEnabled(False)
