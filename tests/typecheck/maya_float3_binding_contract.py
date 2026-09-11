# coding: utf-8
from typing import assert_type

from bd_util import Nodes
from bd_util.maya.node.operator.attr.define.node_attr.transform import (
    TranslatePlugOperator,
)
from bd_util.maya.ui import (
    MayaFloat3Binding,
    MayaFloat3Plug,
    MayaFloat3PlugView,
)
from bd_util.ui import (
    Float3,
    Float3Binding,
    Float3ValueStore,
    Float3SpinBox,
    PythonFloat3AttributeStore,
    qt,
)
from bd_util._sample.maya.ui.float3_sample.data import TransformFloat3Data
from bd_util._sample.maya.ui.float3_sample import maya_view

node = Nodes().existing.transform("pCube1")
data = TransformFloat3Data()
binding = MayaFloat3Binding.from_attribute(
    data, "translate", maya_plug=node.translate
)
assert_type(
    binding, MayaFloat3Binding[PythonFloat3AttributeStore[TransformFloat3Data]]
)
assert_type(binding.store.instance, TransformFloat3Data)
assert_type(binding.store.instance.translate, Float3)
assert_type(binding.maya_view, MayaFloat3PlugView[MayaFloat3Plug] | None)
assert_type(binding.set_value((1, 2, 3)), bool)
assert_type(binding.refresh(), bool)
assert_type(Float3SpinBox(binding).x_spin_box.value(), float)
if binding.maya_view is not None:
    assert_type(binding.maya_view.sync_from_view_model(), bool)
    assert_type(binding.maya_view.is_synchronized, bool)
    assert_type(binding.maya_view.last_sync_error, Exception | None)


def accept_binding(value: Float3Binding[Float3ValueStore]) -> None:
    """Qt Viewが受け取る汎用Bindingとの互換性を確認する。"""
    assert_type(value.value, Float3)


accept_binding(binding)
window = maya_view.show("pCube1", data)
assert_type(
    window.widget.translate_binding.store.instance, TransformFloat3Data
)
assert_type(window.widget.linked_translate, Float3SpinBox)
assert_type(maya_view.dispose(), None)

# 直接Viewを構築する場合も、親plugから子属性の補完を辿れる。
source = Float3Binding.from_attribute(data, "translate")
view = MayaFloat3PlugView(source.view_model, node.translate, qt.QObject())
assert_type(view.plug_operator, TranslatePlugOperator)
view.plug_operator.translateX.get()
