# coding: utf-8
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import (
    FloatBinding,
    FloatLabel,
    FloatPresentation,
    FloatViewModel,
    qt,
)
from bd_util.ui.binding import FloatLabel as BindingFloatLabel
from bd_util.ui.binding.float import FloatLabel as PackageFloatLabel
from bd_util.ui.binding.float.view import FloatLabel as ViewFloatLabel
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    MayaFloat3PlugBinding,
)
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData

node = Nodes().existing.transform("pCube1")
data = TransformFloatData()
binding = FloatBinding.from_attribute(
    data, "translate_x", presentation=FloatPresentation(suffix=" cm")
)
label = FloatLabel(binding, decimals=3)
assert_type(label, FloatLabel)
assert_type(label.view_model, FloatViewModel)
assert_type(label.text(), str)
assert_type(label.selectedText(), str)
assert_type(label.decimals(), int)
assert_type(label.setDecimals(6), None)
assert_type(label.view_model.disposed, qt.QtCore.SignalInstance)
assert_type(BindingFloatLabel(binding), FloatLabel)
assert_type(PackageFloatLabel(binding.view_model), FloatLabel)
assert_type(ViewFloatLabel(FloatViewModel(1)), FloatLabel)
assert_type(
    FloatLabel(MayaFloatPlugBinding(node.translate.translateX)), FloatLabel
)
assert_type(
    FloatLabel(
        MayaFloatBinding.from_attribute(
            data, "translate_x", maya_plug=node.translate.translateX
        )
    ),
    FloatLabel,
)
assert_type(
    FloatLabel(MayaFloat3PlugBinding(node.translate).view_model.x), FloatLabel
)
assert_type(maya_plug.show("pCube1").widget.translate_x_label, FloatLabel)
assert_type(
    maya_view.show("pCube1").widget.linked_translate_x_label, FloatLabel
)
assert_type(minimal.show().widget.value_label, FloatLabel)
