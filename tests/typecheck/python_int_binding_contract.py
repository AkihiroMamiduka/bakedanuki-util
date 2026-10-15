# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util._sample.maya.ui.int_sample import minimal
from bd_util._sample.maya.ui.int_sample.data import IntSampleData
from bd_util.ui import (
    IntBinding,
    IntLabel,
    IntPresentation,
    IntSpinBox,
    IntValueStore,
    IntViewModel,
    PythonIntAttributeStore,
    qt,
)


@dataclass
class Data:
    """型契約のテスト用正本。"""

    value: int = 0


data = Data()
presentation = IntPresentation(minimum=-10, maximum=10)
store = PythonIntAttributeStore(data, "value", presentation=presentation)
assert_type(store, PythonIntAttributeStore[Data])
assert_type(store.instance, Data)
assert_type(store.instance.value, int)
assert_type(store.presentation, IntPresentation)
assert_type(store.read(), int)
assert_type(store.write(1), int)
binding = IntBinding.from_attribute(data, "value", presentation=presentation)
assert_type(binding, IntBinding[PythonIntAttributeStore[Data]])
assert_type(binding.store.instance, Data)
assert_type(binding.value, int)
assert_type(binding.set_value(1), bool)
assert_type(binding.refresh(), bool)
assert_type(binding.changed, qt.QtCore.SignalInstance)
assert_type(IntBinding(store), IntBinding[PythonIntAttributeStore[Data]])
assert_type(IntSpinBox(binding).value(), int)
spin = IntSpinBox(binding, select_all_on_mouse_focus=True)
assert_type(spin.select_all_on_mouse_focus(), bool)
assert_type(spin.set_select_all_on_mouse_focus(False), None)
assert_type(IntLabel(binding).view_model, IntViewModel)


def accept_store(value: IntValueStore) -> None:
    """具象Storeが汎用Storeへ代入可能であることを確認する。"""
    assert_type(value.presentation, IntPresentation)


def accept_binding(value: IntBinding[IntValueStore]) -> None:
    """Viewが受け取る共通Binding型を確認する。"""
    assert_type(value.value, int)


accept_store(store)
accept_binding(binding)
window = minimal.show()
assert_type(window, minimal.MinimalIntWindow)
assert_type(window.widget.signed_binding.store.instance, IntSampleData)
assert_type(window.widget.spin_box, IntSpinBox)
assert_type(window.widget.value_label, IntLabel)
assert_type(minimal.dispose(), None)
