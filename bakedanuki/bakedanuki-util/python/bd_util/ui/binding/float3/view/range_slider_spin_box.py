# coding: utf-8
from collections.abc import Sequence

from .... import qt
from ...float.view.range_slider_spin_box import FloatRangeSliderSpinBox
from ...float.view.step_spin_box import FloatStepMode
from ...float.view_model import FloatViewModel
from ..binding import Float3Binding
from ..store import Float3ValueStore
from ..view_model import Float3ViewModel
from ._slider_spin_box import Float3SliderSpinBoxBase


class Float3RangeSliderSpinBox(
    Float3SliderSpinBoxBase[FloatRangeSliderSpinBox]
):
    """XYZそれぞれに操作範囲・値・stepの編集欄を備えるView。"""

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
        step_mode: FloatStepMode = "additive",
        step_increment: float = 1.0,
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
        minimum_decimals: int = 0,
        maximum_decimals: int = 0,
        minimum_show_unit: bool = False,
        maximum_show_unit: bool = False,
        value_show_unit: bool = False,
        step_show_unit: bool = False,
    ) -> None:
        """軸別の公開単位範囲と、全軸共通の幅・操作・表示設定を指定する。"""

        # 設定の検証と実装はscalar Viewへ委譲し、各軸で独立した状態を持つ。
        def create_editor(
            vm: FloatViewModel, owner: qt.QWidget, low: float, high: float
        ) -> FloatRangeSliderSpinBox:
            """全軸共通の設定を使い、1軸分の範囲付き編集欄を作る。"""
            return FloatRangeSliderSpinBox(
                vm,
                owner,
                minimum=low,
                maximum=high,
                steps=steps,
                decimals=decimals,
                single_step=single_step,
                step_mode=step_mode,
                step_increment=step_increment,
                slider_width=slider_width,
                minimum_width=minimum_width,
                maximum_width=maximum_width,
                value_width=value_width,
                step_width=step_width,
                minimum_enabled=minimum_enabled,
                maximum_enabled=maximum_enabled,
                value_enabled=value_enabled,
                step_enabled=step_enabled,
                minimum_show_buttons=minimum_show_buttons,
                maximum_show_buttons=maximum_show_buttons,
                value_show_buttons=value_show_buttons,
                step_show_buttons=step_show_buttons,
                minimum_decimals=minimum_decimals,
                maximum_decimals=maximum_decimals,
                minimum_show_unit=minimum_show_unit,
                maximum_show_unit=maximum_show_unit,
                value_show_unit=value_show_unit,
                step_show_unit=step_show_unit,
            )

        super().__init__(
            view_model,
            parent,
            minimum=minimum,
            maximum=maximum,
            create_editor=create_editor,
        )

        # どの軸の範囲・stepかを、数値欄のアクセシビリティ名でも区別する。
        for axis, editor in zip(("X", "Y", "Z"), self._editors):
            editor.minimum_spin_box.setAccessibleName(f"{axis} slider minimum")
            editor.maximum_spin_box.setAccessibleName(f"{axis} slider maximum")
            editor.step_spin_box.setAccessibleName(f"{axis} value step")

    def _tab_widgets(
        self, editor: FloatRangeSliderSpinBox
    ) -> tuple[qt.QWidget, ...]:
        """各軸のMin・Slider・Max・値・stepの順にフォーカスを移す。"""
        return (
            editor.minimum_spin_box,
            editor.slider,
            editor.maximum_spin_box,
            editor.spin_box,
            editor.step_spin_box,
        )
