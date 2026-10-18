# coding: utf-8
"""整数Sliderと連続編集の公開型・補完を固定する。"""

from typing import assert_type

from bd_util._sample.maya.ui.int_sample import slider as sample
from bd_util.ui import IntBinding, IntSlider, IntViewModel, qt
from bd_util.ui.binding import IntSlider as BindingSlider
from bd_util.ui.binding.int import IntSlider as IntegerSlider
from bd_util.ui.binding.int.view import IntSlider as ViewSlider


class Data:
    """型契約の整数正本。"""

    value: int = 42


binding = IntBinding.from_attribute(Data(), "value")
slider = IntSlider(binding, minimum=-100, maximum=100)
assert_type(BindingSlider, type[IntSlider])
assert_type(IntegerSlider, type[IntSlider])
assert_type(ViewSlider, type[IntSlider])
assert_type(slider.view_model, IntViewModel)
assert_type(slider.is_wheel_editing, bool)
assert_type(slider.intRange(), tuple[int, int])
assert_type(slider.effectiveIntRange(), tuple[int, int] | None)
assert_type(slider.setIntRange(-10, 10), None)
assert_type(slider.value(), int)
assert_type(slider.setValue(3), None)
assert_type(slider.finish_edit(), None)
assert_type(slider.setValueRequestHandler(None), None)
assert_type(slider.intRangeChanged, qt.QtCore.SignalInstance)
assert_type(slider.editStarted, qt.QtCore.SignalInstance)
assert_type(slider.editFinished, qt.QtCore.SignalInstance)
assert_type(binding.view_model.begin_edit(slider), bool)
assert_type(binding.view_model.is_editing, bool)
assert_type(binding.view_model.end_edit(slider), None)
assert_type(binding.view_model.edit_started, qt.QtCore.SignalInstance)
assert_type(binding.view_model.edit_finished, qt.QtCore.SignalInstance)
window = sample.show()
assert_type(window, sample.IntSliderWindow)
assert_type(window.widget.python_row.slider, IntSlider)
assert_type(sample.show_demo(), sample.IntSliderWindow)
assert_type(sample.dispose(), None)
