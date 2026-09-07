from typing import assert_type

from bd_util import Nodes
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
from bd_util._sample.maya.ui.bool_sample import maya_plug
from bd_util.maya.ui import (
    MayaBoolPlugBinding,
    MayaBoolPlugStore,
    resolve_bool_plug,
)
from bd_util.ui import (
    BoolBinding,
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolViewModel,
    qt,
)

node = Nodes().existing.transform("sampleTransform")
binding = MayaBoolPlugBinding(node.visibility)
named_binding = MayaBoolPlugBinding(
    resolve_bool_plug("sampleTransform", "visibility")
)
assert_type(named_binding, MayaBoolPlugBinding)
assert_type(binding.store, MayaBoolPlugStore)
assert_type(binding.store.plug_operator, BoolPlugOperator)
assert_type(binding.value, bool)
assert_type(binding.view_model, BoolViewModel)
assert_type(binding.changed, qt.QtCore.SignalInstance)
binding.changed.connect(print)
assert_type(binding.set_value(False), bool)
assert_type(binding.refresh(), bool)
assert_type(BoolCheckBox(binding).view_model, BoolViewModel)
assert_type(BoolComboBox(binding).view_model, BoolViewModel)
assert_type(BoolPushButton(binding).view_model, BoolViewModel)
assert_type(BoolRadioButtonGroup(binding).view_model, BoolViewModel)
assert_type(BoolStatusLabel(binding).view_model, BoolViewModel)


def accept_binding(source: BoolBinding[MayaBoolPlugStore]) -> None:
    assert_type(source.store, MayaBoolPlugStore)


accept_binding(binding)
widget = maya_plug.MayaPlugBoolWidget(node.visibility)
assert_type(widget.binding, MayaBoolPlugBinding)
assert_type(widget.check_box, BoolCheckBox)
assert_type(widget.status_label, BoolStatusLabel)
assert_type(maya_plug.show("sampleTransform"), maya_plug.MayaPlugBoolWindow)
assert_type(maya_plug.dispose(), None)
