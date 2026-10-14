# coding: utf-8
from typing import assert_type

from bd_util._sample.maya.ui.int_sample import maya_plug
from bd_util.maya.ui import (
    MayaIntPlug,
    MayaIntPlugBinding,
    MayaIntPlugsBinding,
    MayaPlugTargetState,
    resolve_int_plug,
)
from bd_util.ui import IntPresentation, IntSpinBox, IntValueStore, qt

plug = resolve_int_plug("node", "value")
assert_type(plug, MayaIntPlug)
single = MayaIntPlugBinding(plug)
assert_type(single, MayaIntPlugBinding)
assert_type(single.value, int)
assert_type(single.store.presentation, IntPresentation)
assert_type(single.set_value(2), bool)
assert_type(single.refresh(), bool)
assert_type(IntSpinBox(single).value(), int)
multiple = MayaIntPlugsBinding((plug, plug))
assert_type(multiple, MayaIntPlugsBinding)
assert_type(multiple.value, int)
assert_type(multiple.is_mixed, bool)
assert_type(multiple.target_count, int)
assert_type(multiple.writable_count, int)
assert_type(multiple.target_states, tuple[MayaPlugTargetState, ...])
assert_type(multiple.apply_representative_value(), bool)
assert_type(multiple.state_changed, qt.QtCore.SignalInstance)
assert_type(multiple.edit_failed, qt.QtCore.SignalInstance)


def accept_store(value: IntValueStore) -> None:
    """Maya整数Storeが汎用Store契約へ代入可能なことを確認する。"""
    assert_type(value.read(), int)


accept_store(single.store)
window = maya_plug.show_demo()
assert_type(window, maya_plug.MayaIntWindow)
assert_type(window.widget.byte_spin_box, IntSpinBox)
assert_type(maya_plug.dispose(), None)
