from typing import assert_type

from bd_util import Nodes
from bd_util._sample.maya.ui.float_sample import maya_plug as sample
from bd_util.maya.ui import (
    MayaFloatPlug,
    MayaFloatPlugBinding,
    MayaFloatPlugStore,
    get_channel_box_precision,
    resolve_float_plug,
)
from bd_util.ui import (
    FloatBinding,
    FloatPresentation,
    FloatSpinBox,
    FloatValue,
    FloatValueStore,
    FloatViewModel,
    SetFloatCommand,
    qt,
)

node = Nodes().existing.transform("sampleTransform")
binding = MayaFloatPlugBinding(node.translate.translateX)
angle_binding = MayaFloatPlugBinding(node.rotate.rotateX)
scale_binding = MayaFloatPlugBinding(node.scale.scaleX)
assert_type(binding, MayaFloatPlugBinding)
assert_type(binding.store, MayaFloatPlugStore)
assert_type(binding.store.plug_operator, MayaFloatPlug)
assert_type(binding.value, float)
assert_type(binding.changed, qt.QtCore.SignalInstance)
assert_type(binding.view_model, FloatViewModel)
assert_type(binding.view_model.value, FloatValue)
assert_type(binding.view_model.set_value_command, SetFloatCommand)
assert_type(binding.view_model.presentation, FloatPresentation)
assert_type(binding.view_model.presentation.to_display(100), float)
assert_type(binding.set_value(1.25), bool)
assert_type(binding.refresh(), bool)
assert_type(resolve_float_plug("sampleTransform", "tx"), MayaFloatPlug)
assert_type(get_channel_box_precision(), int)
assert_type(FloatSpinBox(binding).view_model, FloatViewModel)
assert_type(FloatSpinBox(binding.view_model).value(), float)


def accept_binding(value: FloatBinding[FloatValueStore]) -> None:
    assert_type(value.store, FloatValueStore)


accept_binding(binding)
window = sample.show("sampleTransform")
assert_type(window, sample.TransformFloatWindow)
assert_type(window.widget.translate_x, FloatSpinBox)
assert_type(window.widget.rotate_x_binding, MayaFloatPlugBinding)
assert_type(sample.dispose(), None)
