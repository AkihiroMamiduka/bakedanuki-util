# coding: utf-8
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import FloatBinding, FloatSlider, FloatViewModel, qt
from bd_util.ui.binding import FloatSlider as BindingSlider
from bd_util.ui.binding.float import FloatSlider as PackageSlider
from bd_util.ui.binding.float.view import FloatSlider as ViewSlider
from bd_util.maya.ui import MayaFloatBinding, MayaFloatPlugBinding
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData

owner = qt.QWidget()
node = Nodes().existing.transform("pCube1")
data = TransformFloatData()
binding = FloatBinding.from_attribute(data, "translate_x")
slider = FloatSlider(binding, owner, minimum=-100, maximum=100)
assert_type(slider.view_model, FloatViewModel)
assert_type(slider.floatRange(), tuple[float, float])
assert_type(slider.effectiveFloatRange(), tuple[float, float] | None)
assert_type(slider.setFloatRange(-10, 10), None)
assert_type(slider.value(), int)
assert_type(slider.view_model.is_editing, bool)
assert_type(slider.view_model.begin_edit(owner), bool)
assert_type(slider.view_model.end_edit(owner), None)
assert_type(slider.view_model.edit_started, qt.QtCore.SignalInstance)
assert_type(slider.view_model.edit_finished, qt.QtCore.SignalInstance)
assert_type(BindingSlider(binding, minimum=0, maximum=1), FloatSlider)
assert_type(
    PackageSlider(binding.view_model, minimum=0, maximum=1), FloatSlider
)
assert_type(ViewSlider(FloatViewModel(), minimum=0, maximum=1), FloatSlider)
assert_type(
    FloatSlider(
        MayaFloatPlugBinding(node.translate.translateX),
        minimum=-100,
        maximum=100,
    ),
    FloatSlider,
)
assert_type(
    FloatSlider(
        MayaFloatBinding.from_attribute(
            data, "translate_x", maya_plug=node.translate.translateX
        ),
        minimum=-100,
        maximum=100,
    ),
    FloatSlider,
)
assert_type(maya_plug.show("pCube1").widget.translate_x_slider, FloatSlider)
assert_type(
    maya_view.show("pCube1").widget.linked_translate_x_slider, FloatSlider
)
assert_type(minimal.show().widget.slider, FloatSlider)
