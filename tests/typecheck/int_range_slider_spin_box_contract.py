# coding: utf-8
"""整数複合Sliderと保存APIの戻り値・子Viewの型を固定する。"""

from typing import assert_type

from bd_util.ui import (
    IntBinding,
    IntRangeSliderSpinBox,
    IntSlider,
    IntSliderSpinBox,
    IntSliderSpinBoxOrder,
    IntSpinBox,
    IntStepSpinBox,
    IntViewModel,
    UiStateManager,
    qt,
)
from bd_util.ui.binding import IntRangeSliderSpinBox as BindingRange
from bd_util.ui.binding.int import IntSliderSpinBox as IntegerSlider
from bd_util.ui.binding.int.view import IntRangeSliderSpinBox as ViewRange
from bd_util._sample.maya.ui.int_sample import range_slider as sample


class Data:
    """型契約用の整数正本。"""

    value: int = 42


binding = IntBinding.from_attribute(Data(), "value")
basic = IntSliderSpinBox(binding, minimum=0, maximum=100)
editor = IntRangeSliderSpinBox(binding, minimum=-100, maximum=100)
assert_type(BindingRange, type[IntRangeSliderSpinBox])
assert_type(ViewRange, type[IntRangeSliderSpinBox])
assert_type(IntegerSlider, type[IntSliderSpinBox])
assert_type(basic.layoutOrder(), IntSliderSpinBoxOrder)
assert_type(editor.view_model, IntViewModel)
assert_type(editor.slider, IntSlider)
assert_type(editor.spin_box, IntSpinBox)
assert_type(editor.minimum_spin_box, qt.QSpinBox)
assert_type(editor.maximum_spin_box, qt.QSpinBox)
assert_type(editor.step_spin_box, IntStepSpinBox)
assert_type(editor.intRange(), tuple[int, int])
assert_type(editor.effectiveIntRange(), tuple[int, int] | None)
assert_type(editor.setIntRange(0, 100), None)
assert_type(editor.singleStep(), int)
assert_type(editor.setSingleStep(10), None)
assert_type(editor.settingsChanged, qt.QtCore.SignalInstance)
assert_type(editor.rangeEditRejected, qt.QtCore.SignalInstance)


def register(manager: UiStateManager) -> None:
    """manager経由で整数Viewを明示登録できることを確認する。"""
    assert_type(
        manager.register_int_range_slider_spin_box("int", editor), None
    )


window = sample.show()
assert_type(window, sample.IntRangeSliderWindow)
assert_type(window.python_editor, IntRangeSliderSpinBox)
assert_type(window.simple_editor, IntSliderSpinBox)
assert_type(sample.show_demo(), sample.IntRangeSliderWindow)
assert_type(sample.dispose(), None)
