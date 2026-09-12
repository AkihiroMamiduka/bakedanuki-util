# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import (
    FloatBinding,
    FloatRangeSliderSpinBox,
    FloatSlider,
    FloatSpinBox,
    FloatViewModel,
    qt,
)
from bd_util.ui.binding import FloatRangeSliderSpinBox as BindingEditor
from bd_util.ui.binding.float import FloatRangeSliderSpinBox as PackageEditor
from bd_util.ui.binding.float.view import FloatRangeSliderSpinBox as ViewEditor
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    MayaFloat3PlugBinding,
)
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal


@dataclass
class Data:
    value: float = 0.5


owner = qt.QWidget()
data = Data()
binding = FloatBinding.from_attribute(data, "value", parent=owner)
editor = FloatRangeSliderSpinBox(
    binding,
    owner,
    minimum=-10,
    maximum=10,
    steps=1000,
    decimals=4,
    single_step=0.1,
    slider_width=None,
    minimum_width=80,
    maximum_width=80,
    value_width=100,
    minimum_enabled=False,
    maximum_enabled=True,
    value_enabled=False,
    minimum_show_buttons=False,
    maximum_show_buttons=True,
    value_show_buttons=False,
    minimum_decimals=0,
    maximum_decimals=2,
)
assert_type(editor.view_model, FloatViewModel)
assert_type(editor.slider, FloatSlider)
assert_type(editor.spin_box, FloatSpinBox)
assert_type(editor.minimum_spin_box, qt.QDoubleSpinBox)
assert_type(editor.maximum_spin_box, qt.QDoubleSpinBox)
assert_type(editor.range_status_label, qt.QLabel)
assert_type(editor.floatRange(), tuple[float, float])
assert_type(editor.setFloatRange(-1, 1), None)
assert_type(editor.effectiveFloatRange(), tuple[float, float] | None)
assert_type(editor.decimals(), int)
assert_type(editor.setDecimals(6), None)
assert_type(editor.minimumDecimals(), int)
assert_type(editor.setMinimumDecimals(0), None)
assert_type(editor.maximumDecimals(), int)
assert_type(editor.setMaximumDecimals(2), None)
assert_type(editor.spin_box.isInputEnabled(), bool)
assert_type(editor.spin_box.setInputEnabled(False), None)
assert_type(editor.singleStep(), float)
assert_type(editor.setSingleStep(0.25), None)
assert_type(
    BindingEditor(binding, minimum=0, maximum=1), FloatRangeSliderSpinBox
)
assert_type(
    PackageEditor(binding.view_model, minimum=0, maximum=1),
    FloatRangeSliderSpinBox,
)
assert_type(
    ViewEditor(FloatViewModel(), minimum=0, maximum=1, slider_width=160),
    FloatRangeSliderSpinBox,
)
node = Nodes().existing.transform("pCube1")
assert_type(
    FloatRangeSliderSpinBox(
        MayaFloatPlugBinding(node.translate.translateX),
        minimum=-100,
        maximum=100,
    ),
    FloatRangeSliderSpinBox,
)
assert_type(
    FloatRangeSliderSpinBox(
        MayaFloatBinding.from_attribute(
            data, "value", maya_plug=node.translate.translateX
        ),
        minimum=-100,
        maximum=100,
    ),
    FloatRangeSliderSpinBox,
)
assert_type(
    FloatRangeSliderSpinBox(
        MayaFloat3PlugBinding(node.translate).view_model.x,
        minimum=-100,
        maximum=100,
    ),
    FloatRangeSliderSpinBox,
)
assert_type(
    maya_plug.show("pCube1").widget.translate_x_editor, FloatRangeSliderSpinBox
)
assert_type(
    maya_view.show("pCube1").widget.linked_translate_x_editor,
    FloatRangeSliderSpinBox,
)
assert_type(minimal.show().widget.editor, FloatRangeSliderSpinBox)
