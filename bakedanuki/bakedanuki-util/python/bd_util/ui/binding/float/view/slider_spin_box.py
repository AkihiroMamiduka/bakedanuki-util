# coding: utf-8
from __future__ import annotations

from typing import Literal, TypeAlias

from .... import qt
from .._validation import (
    require_decimals,
    require_float,
    require_slider_range,
    require_slider_steps,
)
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel
from ._source import resolve_float_view_source
from .slider import FloatSlider
from .spin_box import FloatSpinBox

FloatSliderSpinBoxOrder: TypeAlias = Literal["slider_value", "value_slider"]


def _require_layout_order(value: object) -> FloatSliderSpinBoxOrder:
    """Sliderと値欄の並び順を検証する。"""
    if not isinstance(value, str):
        raise TypeError("layout_orderにはstrを指定してください")
    if value not in ("slider_value", "value_slider"):
        raise ValueError(
            "layout_orderは'slider_value'または'value_slider'にしてください"
        )
    return value


class FloatSliderSpinBox(qt.QWidget):
    """同じ正本を編集するFloatSliderとFloatSpinBoxを横に並べるView。"""

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
        layout_order: FloatSliderSpinBoxOrder = "slider_value",
    ) -> None:
        """操作範囲、入力設定、Sliderと値欄の並び順を受け取る。"""
        # 子Widgetを作る前に、両Viewの設定と共有する入力元を検証する。
        view_model, binding = resolve_float_view_source(view_model)
        minimum, maximum = require_slider_range(minimum, maximum)
        steps = require_slider_steps(steps)
        decimals = require_decimals(decimals)
        single_step = require_float(single_step, "single_step")
        layout_order = _require_layout_order(layout_order)
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")
        if view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        self._ready = False
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._layout_order: FloatSliderSpinBoxOrder = layout_order

        # 各Viewが同じViewModelへ入力し、同期・単位・Undoを既存基盤へ委譲する。
        try:
            self.slider = FloatSlider(
                view_model, self, minimum=minimum, maximum=maximum, steps=steps
            )
            self.spin_box = FloatSpinBox(
                view_model, self, decimals=decimals, single_step=single_step
            )
            layout = self._create_layout()
            if layout_order == "slider_value":
                layout.addWidget(self.slider, 1)
                layout.addWidget(self.spin_box)
            else:
                layout.addWidget(self.spin_box)
                layout.addWidget(self.slider, 1)
            self.setSizePolicy(
                qt.QSizePolicy.Policy.Expanding, qt.QSizePolicy.Policy.Fixed
            )
            self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
            self.setFocusProxy(self.spin_box)
            self._ready = True
        except Exception:
            # 表示変換などで生成に失敗した場合も、共有Bindingを残して子を片付ける。
            self.setParent(None)
            self.deleteLater()
            raise

    def _create_layout(self) -> qt.QHBoxLayout:
        """派生Viewでも入力部品を共有できるよう、配置先の行を作る。"""
        layout = qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    @property
    def view_model(self) -> FloatViewModel:
        """共有ViewModelを返し、明示終了・Qt破棄後は例外を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        return self._view_model

    def layoutOrder(self) -> FloatSliderSpinBoxOrder:
        """Sliderと値欄の現在の並び順を返す。"""
        return self._layout_order

    def event(self, event: qt.QEvent) -> bool:
        """子へhide通知が届かない場合も、このViewの連続編集を終了する。"""
        if (
            self._ready
            and event.type()
            in (
                qt.QEvent.Type.Close,
                qt.QEvent.Type.Hide,
                qt.QEvent.Type.HideToParent,
                qt.QEvent.Type.WindowDeactivate,
            )
            and not self._view_model.is_disposed
        ):
            self._view_model.end_edit(self.slider)
        return super().event(event)
