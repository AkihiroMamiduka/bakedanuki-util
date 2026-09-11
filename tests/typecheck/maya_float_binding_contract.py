# coding: utf-8
from typing import assert_type

from bd_util import Nodes
from bd_util.maya.ui import MayaFloatBinding, MayaFloatPlugView
from bd_util.ui import (
    FloatBinding,
    FloatPresentation,
    FloatSpinBox,
    FloatValueStore,
    PythonFloatAttributeStore,
)
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData
from bd_util._sample.maya.ui.float_sample import maya_view

node = Nodes().existing.transform("pCube1")
data = TransformFloatData()
binding = MayaFloatBinding.from_attribute(
    data, "translate_x", maya_plug=node.translate.translateX
)
assert_type(
    binding, MayaFloatBinding[PythonFloatAttributeStore[TransformFloatData]]
)
assert_type(binding.store.instance, TransformFloatData)
assert_type(binding.store.instance.translate_x, float)
assert_type(binding.maya_view, MayaFloatPlugView | None)
assert_type(binding.set_value(1), bool)
assert_type(binding.refresh(), bool)
assert_type(FloatSpinBox(binding).value(), float)
if binding.maya_view is not None:
    assert_type(binding.maya_view.sync_from_view_model(), bool)
    assert_type(binding.maya_view.is_synchronized, bool)
    assert_type(binding.maya_view.last_sync_error, Exception | None)


def accept_binding(value: FloatBinding[FloatValueStore]) -> None:
    """Qt Viewが受け取る汎用Bindingとの互換性を確認する。"""
    assert_type(value.value, float)


def present(value: FloatPresentation) -> FloatPresentation:
    """表示変換の拡張点の引数と戻り値を確認する。"""
    return value


binding.view_model.set_presentation_adapter(present)
accept_binding(binding)
window = maya_view.show("pCube1", data)
assert_type(
    window.widget.translate_x_binding.store.instance, TransformFloatData
)
assert_type(window.widget.linked_translate_x, FloatSpinBox)
assert_type(maya_view.dispose(), None)
