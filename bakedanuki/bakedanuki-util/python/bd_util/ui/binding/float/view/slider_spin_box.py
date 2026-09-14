# coding: utf-8
from __future__ import annotations

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
    ) -> None:
        """スライダーの公開単位範囲と、SpinBoxの表示・入力設定を受け取る。"""
        # 子Widgetを作る前に、両Viewの設定と共有する入力元を検証する。
        view_model, binding = resolve_float_view_source(view_model)
        minimum, maximum = require_slider_range(minimum, maximum)
        steps = require_slider_steps(steps)
        decimals = require_decimals(decimals)
        single_step = require_float(single_step, "single_step")
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")
        if view_model.is_disposed:
            raise RuntimeError("編集対象のFloatViewModelは終了しています")
        self._ready = False
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model

        # 各Viewが同じViewModelへ入力し、同期・単位・Undoを既存基盤へ委譲する。
        try:
            self.slider = FloatSlider(
                view_model, self, minimum=minimum, maximum=maximum, steps=steps
            )
            self.spin_box = FloatSpinBox(
                view_model, self, decimals=decimals, single_step=single_step
            )
            layout = self._create_layout()
            layout.addWidget(self.slider, 1)
            layout.addWidget(self.spin_box)
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
