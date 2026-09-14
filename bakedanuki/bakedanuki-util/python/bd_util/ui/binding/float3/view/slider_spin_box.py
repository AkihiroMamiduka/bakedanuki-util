# coding: utf-8
from collections.abc import Sequence

from .... import qt
from ...float._validation import (
    require_decimals,
    require_float,
    require_slider_steps,
)
from ...float.view.slider_spin_box import FloatSliderSpinBox
from ...float.view_model import FloatViewModel
from ..binding import Float3Binding
from ..store import Float3ValueStore
from ..view_model import Float3ViewModel
from ._slider_spin_box import Float3SliderSpinBoxBase


class Float3SliderSpinBox(Float3SliderSpinBoxBase[FloatSliderSpinBox]):
    """X・Y・Zのスライダーと数値入力を縦3行に並べるView。"""

    def __init__(
        self,
        view_model: Float3ViewModel | Float3Binding[Float3ValueStore],
        parent: qt.QWidget | None = None,
        *,
        minimum: float | Sequence[float],
        maximum: float | Sequence[float],
        steps: int = 1000,
        decimals: int = 6,
        single_step: float = 0.1,
    ) -> None:
        """公開単位の操作範囲を共通値またはXYZ別の値で受け取る。"""
        # 全軸共通の設定を子Widgetの生成前に検証する。
        steps = require_slider_steps(steps)
        decimals = require_decimals(decimals)
        single_step = require_float(single_step, "single_step")
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")

        def create_editor(
            vm: FloatViewModel, owner: qt.QWidget, low: float, high: float
        ) -> FloatSliderSpinBox:
            """共有設定を使い、1軸分の編集欄を作る。"""
            return FloatSliderSpinBox(
                vm,
                owner,
                minimum=low,
                maximum=high,
                steps=steps,
                decimals=decimals,
                single_step=single_step,
            )

        super().__init__(
            view_model,
            parent,
            minimum=minimum,
            maximum=maximum,
            create_editor=create_editor,
        )
