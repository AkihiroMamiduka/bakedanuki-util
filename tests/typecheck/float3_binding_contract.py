from typing import assert_type

from bd_util import Nodes
from bd_util._sample.maya.ui.float3_sample import maya_plug as sample
from bd_util.maya.node.operator.attr.define.node_attr.transform import (
    TranslatePlugOperator,
)
from bd_util.maya.ui import (
    MayaFloat3Plug,
    MayaFloat3PlugBinding,
    MayaFloat3PlugStore,
    resolve_float3_plug,
)
from bd_util.maya.value import Double3, DoubleAngle3, DoubleLinear3
from bd_util.ui import (
    Float3,
    Float3Binding,
    Float3SpinBox,
    Float3Value,
    Float3ValueStore,
    Float3ViewModel,
    FloatSpinBox,
    FloatViewModel,
    SetFloat3Command,
    qt,
)

node = Nodes().existing.transform("sampleTransform")
binding = MayaFloat3PlugBinding(node.translate)
assert_type(binding, MayaFloat3PlugBinding[TranslatePlugOperator])
assert_type(binding.store, MayaFloat3PlugStore[TranslatePlugOperator])
assert_type(binding.store.plug_operator, TranslatePlugOperator)
assert_type(binding.store.plug_operator.translateX.get(), float)
assert_type(binding.value, Float3)
assert_type(binding.changed, qt.QtCore.SignalInstance)
assert_type(binding.view_model, Float3ViewModel)
assert_type(binding.view_model.value, Float3Value)
assert_type(binding.view_model.x, FloatViewModel)
assert_type(binding.view_model.y.value.value, float)
assert_type(binding.view_model.z.set_value_command.execute(1), bool)
assert_type(binding.view_model.set_value_command, SetFloat3Command)
assert_type(binding.set_value((1, 2, 3)), bool)
assert_type(binding.set_value(DoubleLinear3(1, 2, 3)), bool)
assert_type(
    MayaFloat3PlugBinding(node.rotate).set_value(DoubleAngle3(1, 2, 3)), bool
)
assert_type(
    MayaFloat3PlugBinding(node.scale).set_value(Double3(1, 2, 3)), bool
)
assert_type(binding.refresh(), bool)
assert_type(
    resolve_float3_plug("sampleTransform", "translate"), MayaFloat3Plug
)


def accept_binding(value: Float3Binding[Float3ValueStore]) -> None:
    assert_type(value.store, Float3ValueStore)


accept_binding(binding)
view = Float3SpinBox(binding)
assert_type(view.x_spin_box, FloatSpinBox)
assert_type(view.view_model, Float3ViewModel)
assert_type(view.x(), int)
assert_type(FloatSpinBox(binding.view_model.x), FloatSpinBox)
window = sample.show("sampleTransform")
assert_type(window, sample.TransformFloat3Window)
assert_type(window.widget.translate, Float3SpinBox)
assert_type(
    window.widget.rotate_binding, MayaFloat3PlugBinding[MayaFloat3Plug]
)
assert_type(sample.dispose(), None)
