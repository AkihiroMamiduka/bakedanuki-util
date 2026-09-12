# coding: utf-8
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import (
    FloatBinding,
    FloatSlider,
    FloatSliderSpinBox,
    FloatRangeSliderSpinBox,
    FloatSpinBox,
    FloatViewModel,
    qt,
)
from bd_util.ui.binding import FloatSliderSpinBox as BindingEditor
from bd_util.ui.binding.float import FloatSliderSpinBox as PackageEditor
from bd_util.ui.binding.float.view import FloatSliderSpinBox as ViewEditor
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    MayaFloat3PlugBinding,
)
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData

data = TransformFloatData()
node = Nodes().existing.transform("pCube1")
owner = qt.QWidget()
binding = FloatBinding.from_attribute(data, "translate_x")
editor = FloatSliderSpinBox(
    binding,
    owner,
    minimum=-100,
    maximum=100,
    steps=2000,
    decimals=3,
    single_step=0.1,
)
assert_type(editor.view_model, FloatViewModel)
assert_type(editor.slider, FloatSlider)
assert_type(editor.spin_box, FloatSpinBox)
assert_type(editor.slider.floatRange(), tuple[float, float])
assert_type(editor.slider.setFloatRange(-10, 10), None)
assert_type(editor.spin_box.decimals(), int)
assert_type(editor.spin_box.setDecimals(6), None)
assert_type(editor.spin_box.singleStep(), float)
assert_type(editor.spin_box.setSingleStep(0.25), None)
assert_type(BindingEditor(binding, minimum=0, maximum=1), FloatSliderSpinBox)
assert_type(
    PackageEditor(binding.view_model, minimum=0, maximum=1), FloatSliderSpinBox
)
assert_type(
    ViewEditor(FloatViewModel(), minimum=0, maximum=1), FloatSliderSpinBox
)
assert_type(
    FloatSliderSpinBox(
        MayaFloatPlugBinding(node.translate.translateX),
        minimum=-100,
        maximum=100,
    ),
    FloatSliderSpinBox,
)
assert_type(
    FloatSliderSpinBox(
        MayaFloatBinding.from_attribute(
            data, "translate_x", maya_plug=node.translate.translateX
        ),
        minimum=-100,
        maximum=100,
    ),
    FloatSliderSpinBox,
)
assert_type(
    FloatSliderSpinBox(
        MayaFloat3PlugBinding(node.translate).view_model.x,
        minimum=-100,
        maximum=100,
    ),
    FloatSliderSpinBox,
)
assert_type(
    maya_plug.show("pCube1").widget.translate_x_editor, FloatRangeSliderSpinBox
)
assert_type(
    maya_view.show("pCube1").widget.linked_translate_x_editor,
    FloatRangeSliderSpinBox,
)
assert_type(minimal.show().widget.editor, FloatRangeSliderSpinBox)
