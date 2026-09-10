# coding: utf-8
from typing import assert_type

from bd_util._sample.maya.ui.float3_sample import minimal
from bd_util._sample.maya.ui.float3_sample.data import OffsetData
from bd_util.ui import (
    Float3,
    Float3Binding,
    Float3SpinBox,
    Float3ValueStore,
    FloatPresentation,
    FloatValueStore,
    FloatViewModel,
    PythonFloat3AttributeStore,
    qt,
)

data = OffsetData()
store = PythonFloat3AttributeStore(
    data, "offset", presentation=FloatPresentation(suffix=" cm")
)
assert_type(store, PythonFloat3AttributeStore[OffsetData])
assert_type(store.instance, OffsetData)
assert_type(store.instance.offset, tuple[float, float, float])
assert_type(store.read(), Float3)
assert_type(store.write((1, 2, 3)), Float3)
assert_type(store.attribute_name, str)
assert_type(
    store.presentations,
    tuple[FloatPresentation, FloatPresentation, FloatPresentation],
)
assert_type(
    store.components, tuple[FloatValueStore, FloatValueStore, FloatValueStore]
)
assert_type(store.components[0].write(5), float)

binding = Float3Binding.from_attribute(data, "offset")
assert_type(binding, Float3Binding[PythonFloat3AttributeStore[OffsetData]])
assert_type(binding.store.instance.offset, Float3)
assert_type(binding.set_value([1, 2, 3]), bool)
assert_type(binding.refresh(), bool)
assert_type(binding.changed, qt.QtCore.SignalInstance)
assert_type(binding.view_model.x, FloatViewModel)
assert_type(
    Float3Binding(store), Float3Binding[PythonFloat3AttributeStore[OffsetData]]
)
assert_type(Float3SpinBox(binding).x_spin_box.value(), float)


def accept_store(value: Float3ValueStore) -> None:
    """汎用Storeの契約との互換性を確認する。"""
    assert_type(value.read(), Float3)


def accept_binding(value: Float3Binding[Float3ValueStore]) -> None:
    """共有Viewが受け取るBindingの型との互換性を確認する。"""
    assert_type(value.value, Float3)


accept_store(store)
accept_binding(binding)
per_axis = Float3Binding.from_attribute(
    data,
    "offset",
    presentation=(
        FloatPresentation(),
        FloatPresentation(),
        FloatPresentation(),
    ),
)
assert_type(per_axis.store, PythonFloat3AttributeStore[OffsetData])
window = minimal.show()
assert_type(window, minimal.MinimalFloat3Window)
assert_type(window.widget.binding.store.instance, OffsetData)
assert_type(window.widget.linked_spin_box, Float3SpinBox)
assert_type(minimal.dispose(), None)
