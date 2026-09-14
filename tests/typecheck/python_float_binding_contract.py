# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util._sample.maya.ui.float_sample import minimal
from bd_util._sample.maya.ui.float_sample.data import WeightData
from bd_util.ui import (
    FloatBinding,
    FloatPresentation,
    FloatSpinBox,
    FloatValueStore,
    PythonFloatAttributeStore,
    qt,
)


@dataclass
class Data:
    weight: float = 0.5


data = Data()
presentation = FloatPresentation(scale=100, suffix=" %", minimum=0, maximum=1)
store = PythonFloatAttributeStore(data, "weight", presentation=presentation)
assert_type(store, PythonFloatAttributeStore[Data])
assert_type(store.instance, Data)
assert_type(store.instance.weight, float)
assert_type(store.attribute_name, str)
assert_type(store.presentation, FloatPresentation)
assert_type(store.is_available, bool)
assert_type(store.is_writable, bool)
assert_type(store.read(), float)
assert_type(store.write(0.25), float)

binding = FloatBinding.from_attribute(
    data, "weight", presentation=presentation
)
assert_type(binding, FloatBinding[PythonFloatAttributeStore[Data]])
assert_type(binding.store.instance, Data)
assert_type(binding.store.instance.weight, float)
assert_type(binding.value, float)
assert_type(binding.set_value(0.75), bool)
assert_type(binding.refresh(), bool)
assert_type(binding.changed, qt.QtCore.SignalInstance)
assert_type(FloatBinding(store), FloatBinding[PythonFloatAttributeStore[Data]])
assert_type(FloatSpinBox(binding).value(), float)


def accept_store(value: FloatValueStore) -> None:
    """汎用Storeの契約へ代入できることを確認する。"""
    assert_type(value.presentation, FloatPresentation)


def accept_binding(value: FloatBinding[FloatValueStore]) -> None:
    """Viewが受け取る汎用Bindingの型へ代入できることを確認する。"""
    assert_type(value.value, float)


accept_store(store)
accept_binding(binding)
window = minimal.show()
assert_type(window, minimal.MinimalFloatWindow)
assert_type(window.widget.binding.store.instance, WeightData)
assert_type(window.widget.binding.store.instance.weight, float)
assert_type(window.widget.spin_box, FloatSpinBox)
assert_type(window.widget.linked_spin_box, FloatSpinBox)
assert_type(minimal.dispose(), None)
