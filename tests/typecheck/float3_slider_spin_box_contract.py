# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import (
    Float3Binding,
    Float3SliderSpinBox,
    Float3ViewModel,
    FloatSlider,
    FloatSliderSpinBox,
    FloatSpinBox,
    qt,
)
from bd_util.ui.binding import Float3SliderSpinBox as BindingView
from bd_util.ui.binding.float3 import Float3SliderSpinBox as PackageView
from bd_util.ui.binding.float3.view import Float3SliderSpinBox as View
from bd_util.maya.ui import MayaFloat3Binding, MayaFloat3PlugBinding
from bd_util._sample.maya.ui.float3_sample import maya_plug, maya_view, minimal


@dataclass
class Data:
    value: tuple[float, float, float] = (1, 2, 3)


owner = qt.QWidget()
binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
view = Float3SliderSpinBox(
    binding,
    owner,
    minimum=(-10, -20, -30),
    maximum=[10, 20, 30],
    steps=2000,
    decimals=3,
    single_step=0.1,
)
assert_type(view.view_model, Float3ViewModel)
assert_type(view.x_editor, FloatSliderSpinBox)
assert_type(view.y_editor, FloatSliderSpinBox)
assert_type(view.z_editor, FloatSliderSpinBox)
assert_type(view.x_editor.slider, FloatSlider)
assert_type(view.x_spin_box, FloatSpinBox)
assert_type(view.y_spin_box, FloatSpinBox)
assert_type(view.z_spin_box, FloatSpinBox)
assert_type(view.y_editor.slider.setFloatRange(-5, 5), None)
assert_type(view.z_spin_box.setSingleStep(0.25), None)
assert_type(BindingView(binding, minimum=0, maximum=10), Float3SliderSpinBox)
assert_type(
    PackageView(binding.view_model, minimum=0, maximum=10), Float3SliderSpinBox
)
assert_type(View(binding, minimum=0, maximum=10), Float3SliderSpinBox)
node = Nodes().existing.transform("pCube1")
assert_type(
    Float3SliderSpinBox(
        MayaFloat3PlugBinding(node.translate), minimum=-100, maximum=100
    ),
    Float3SliderSpinBox,
)
assert_type(
    Float3SliderSpinBox(
        MayaFloat3Binding.from_attribute(
            Data(), "value", maya_plug=node.translate
        ),
        minimum=-100,
        maximum=100,
    ),
    Float3SliderSpinBox,
)
assert_type(maya_plug.show("pCube1").widget.translate, Float3SliderSpinBox)
assert_type(
    maya_view.show("pCube1").widget.linked_translate, Float3SliderSpinBox
)
assert_type(minimal.show().widget.spin_box, Float3SliderSpinBox)
