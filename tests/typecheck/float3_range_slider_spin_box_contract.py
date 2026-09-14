# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import (
    Float3Binding,
    Float3RangeSliderSpinBox,
    Float3ViewModel,
    FloatRangeSliderSpinBox,
    FloatSpinBox,
    FloatStepSpinBox,
    FloatStepMode,
    qt,
)
from bd_util.ui.binding import Float3RangeSliderSpinBox as BindingView
from bd_util.ui.binding.float3 import Float3RangeSliderSpinBox as PackageView
from bd_util.ui.binding.float3.view import Float3RangeSliderSpinBox as View
from bd_util.maya.ui import MayaFloat3Binding, MayaFloat3PlugBinding


@dataclass
class Data:
    value: tuple[float, float, float] = (1, 2, 3)


owner = qt.QWidget()
binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
view = Float3RangeSliderSpinBox(
    binding,
    owner,
    minimum=(-10, -20, -30),
    maximum=[10, 20, 30],
    steps=2000,
    decimals=3,
    single_step=15,
    step_mode="multiplicative",
    step_increment=15,
    slider_width=None,
    minimum_width=60,
    maximum_width=60,
    value_width=130,
    step_width=80,
    minimum_enabled=True,
    maximum_enabled=False,
    value_enabled=True,
    step_enabled=True,
    minimum_show_buttons=False,
    maximum_show_buttons=False,
    value_show_buttons=False,
    step_show_buttons=True,
    minimum_decimals=0,
    maximum_decimals=2,
    minimum_show_unit=False,
    maximum_show_unit=True,
    value_show_unit=False,
    step_show_unit=True,
)
assert_type(view.view_model, Float3ViewModel)
assert_type(view.x_editor, FloatRangeSliderSpinBox)
assert_type(view.y_editor, FloatRangeSliderSpinBox)
assert_type(view.z_editor, FloatRangeSliderSpinBox)
assert_type(view.x_spin_box, FloatSpinBox)
assert_type(view.y_spin_box, FloatSpinBox)
assert_type(view.z_spin_box, FloatSpinBox)
assert_type(view.x_editor.minimum_spin_box, qt.QDoubleSpinBox)
assert_type(view.y_editor.maximum_spin_box, qt.QDoubleSpinBox)
assert_type(view.z_editor.step_spin_box, FloatStepSpinBox)
assert_type(view.z_editor.step_spin_box.stepMode(), FloatStepMode)
assert_type(view.x_editor.floatRange(), tuple[float, float])
assert_type(view.y_editor.effectiveFloatRange(), tuple[float, float] | None)
assert_type(view.z_editor.setFloatRange(-50, 50), None)
assert_type(view.x_editor.setSingleStep(0.25), None)
assert_type(view.x_editor.singleStep(), float)
assert_type(
    BindingView(binding, minimum=0, maximum=10), Float3RangeSliderSpinBox
)
assert_type(
    PackageView(binding.view_model, minimum=0, maximum=10),
    Float3RangeSliderSpinBox,
)
assert_type(View(binding, minimum=0, maximum=10), Float3RangeSliderSpinBox)
node = Nodes().existing.transform("pCube1")
assert_type(
    Float3RangeSliderSpinBox(
        MayaFloat3PlugBinding(node.translate), minimum=-100, maximum=100
    ),
    Float3RangeSliderSpinBox,
)
assert_type(
    Float3RangeSliderSpinBox(
        MayaFloat3Binding.from_attribute(
            Data(), "value", maya_plug=node.translate
        ),
        minimum=-100,
        maximum=100,
    ),
    Float3RangeSliderSpinBox,
)
