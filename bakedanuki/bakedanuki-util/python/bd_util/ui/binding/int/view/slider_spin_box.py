# coding: utf-8
from __future__ import annotations

from typing import Literal, TypeAlias

from .... import qt
from .._validation import require_slider_range, require_step
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel
from ._source import resolve_int_view_source
from .slider import IntSlider
from .spin_box import IntSpinBox

__all__ = ["IntSliderSpinBox", "IntSliderSpinBoxOrder"]

IntSliderSpinBoxOrder: TypeAlias = Literal["slider_value", "value_slider"]


def require_layout_order(value: object) -> IntSliderSpinBoxOrder:
    """Sliderと値欄の並び順を検証する。"""
    if not isinstance(value, str):
        raise TypeError("layout_orderにはstrを指定してください")
    if value not in ("slider_value", "value_slider"):
        raise ValueError(
            "layout_orderは'slider_value'または'value_slider'にしてください"
        )
    return value


class IntSliderSpinBox(qt.QWidget):
    """同じ整数正本を編集するSliderと数値欄を横に並べるView。"""

    def __init__(
        self,
        view_model: IntViewModel | IntBinding[IntValueStore],
        parent: qt.QWidget | None = None,
        *,
        minimum: int,
        maximum: int,
        steps: int = 1000,
        single_step: int = 1,
        layout_order: IntSliderSpinBoxOrder = "slider_value",
        value_select_all_on_mouse_focus: bool = False,
    ) -> None:
        """整数の操作範囲と値欄の刻み幅・並び順を指定する。

        Args:
            view_model: 両Viewで共有するViewModelまたはBinding。
            parent: このViewを所有するWidget。
            minimum: Sliderの32-bit整数の下限。
            maximum: Sliderの上限。`minimum`より大きくする。
            steps: Sliderの最大分割数。正の32-bit整数。
            single_step: 値欄の刻み幅。正の32-bit整数。
            layout_order: `slider_value`または`value_slider`。
            value_select_all_on_mouse_focus: 値欄の初回文字クリックで全選択するか。
        """
        # 子Viewの生成前に全設定を検証する
        view_model, binding = resolve_int_view_source(view_model)
        minimum, maximum = require_slider_range(minimum, maximum)
        steps = require_step(steps, "steps")
        single_step = require_step(single_step)
        layout_order = require_layout_order(layout_order)
        if type(value_select_all_on_mouse_focus) is not bool:
            raise TypeError(
                "value_select_all_on_mouse_focusにはboolを指定してください"
            )
        if view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        self._ready = False
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._layout_order: IntSliderSpinBoxOrder = layout_order
        try:
            self.slider = IntSlider(
                view_model, self, minimum=minimum, maximum=maximum, steps=steps
            )
            self.spin_box = IntSpinBox(
                view_model,
                self,
                single_step=single_step,
                select_all_on_mouse_focus=value_select_all_on_mouse_focus,
            )
            layout = self._create_layout()
            widgets = (
                (self.slider, self.spin_box)
                if layout_order == "slider_value"
                else (self.spin_box, self.slider)
            )
            for widget in widgets:
                layout.addWidget(widget, 1 if widget is self.slider else 0)
            self.setSizePolicy(
                qt.QSizePolicy.Policy.Expanding, qt.QSizePolicy.Policy.Fixed
            )
            self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
            self.setFocusProxy(self.spin_box)
            self._ready = True
        except Exception:
            self.setParent(None)
            self.deleteLater()
            raise

    def _create_layout(self) -> qt.QHBoxLayout:
        """派生Viewでも同じ子Viewを並べられる配置先を作る。"""
        layout = qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    @property
    def view_model(self) -> IntViewModel:
        """生存中の共有ViewModelを返す。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        return self._view_model

    def layoutOrder(self) -> IntSliderSpinBoxOrder:
        """Sliderと値欄の並び順を返す。"""
        return self._layout_order

    def event(self, event: qt.QEvent) -> bool:
        """複合Viewの非表示でも所有Sliderの連続操作を終了する。"""
        if self._ready and event.type() in (
            qt.QEvent.Type.Close,
            qt.QEvent.Type.Hide,
            qt.QEvent.Type.HideToParent,
            qt.QEvent.Type.WindowDeactivate,
        ):
            self.slider.finish_edit()
        return super().event(event)
