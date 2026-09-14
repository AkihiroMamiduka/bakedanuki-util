# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util import Nodes
from bd_util.ui import (
    Float3Binding,
    Float3Label,
    Float3ViewModel,
    FloatLabel,
    qt,
)
from bd_util.ui.binding import Float3Label as BindingLabel
from bd_util.ui.binding.float3 import Float3Label as PackageLabel
from bd_util.ui.binding.float3.view import Float3Label as ViewLabel
from bd_util.maya.ui import MayaFloat3Binding, MayaFloat3PlugBinding
from bd_util._sample.maya.ui.float3_sample import maya_plug, maya_view, minimal


@dataclass
class Data:
    value: tuple[float, float, float] = (1, 2, 3)


owner = qt.QWidget()
binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
view = Float3Label(binding, owner, decimals=3)
assert_type(view.view_model, Float3ViewModel)
assert_type(view.x_label, FloatLabel)
assert_type(view.y_label, FloatLabel)
assert_type(view.z_label, FloatLabel)
assert_type(view.x_label.text(), str)
assert_type(view.decimals(), int)
assert_type(view.setDecimals(6), None)
assert_type(BindingLabel(binding), Float3Label)
assert_type(PackageLabel(binding.view_model), Float3Label)
assert_type(ViewLabel(binding), Float3Label)
node = Nodes().existing.transform("pCube1")
assert_type(Float3Label(MayaFloat3PlugBinding(node.translate)), Float3Label)
assert_type(
    Float3Label(
        MayaFloat3Binding.from_attribute(
            Data(), "value", maya_plug=node.translate
        )
    ),
    Float3Label,
)
assert_type(maya_plug.show("pCube1").widget.translate_label, Float3Label)
assert_type(maya_plug.show("pCube1").widget.rotate_label, Float3Label)
assert_type(maya_plug.show("pCube1").widget.scale_label, Float3Label)
assert_type(
    maya_view.show("pCube1").widget.linked_translate_label, Float3Label
)
assert_type(minimal.show().widget.value_label, Float3Label)
assert_type(minimal.show().widget.linked_value_label, Float3Label)
