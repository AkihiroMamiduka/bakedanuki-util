# coding: utf-8
"""複数属性Bindingの公開値と既存Viewへの受け渡し型を固定する。"""

from typing import assert_type

from bd_util.maya.ui.binding.plugs_binding import (
    MayaBoolPlugsBinding,
    MayaFloatPlugsBinding,
)
from bd_util.maya.ui.binding.plugs_state import MayaPlugTargetState
from bd_util.maya.ui import resolve_bool_plug, resolve_float_plug
from bd_util.ui import (
    BoolComboBox,
    BoolViewModel,
    FloatSpinBox,
    FloatSliderSpinBox,
    FloatViewModel,
    qt,
)

bool_binding = MayaBoolPlugsBinding([resolve_bool_plug("node", "visibility")])
float_binding = MayaFloatPlugsBinding(
    [resolve_float_plug("node", "translateX")]
)
assert_type(bool_binding.value, bool)
assert_type(float_binding.value, float)
assert_type(bool_binding.view_model, BoolViewModel)
assert_type(float_binding.view_model, FloatViewModel)
assert_type(bool_binding.apply_representative_value(), bool)
assert_type(float_binding.set_value(1), bool)
assert_type(bool_binding.target_states, tuple[MayaPlugTargetState, ...])
assert_type(float_binding.target_states[0].reason, str | None)
assert_type(float_binding.is_mixed, bool)
assert_type(bool_binding.target_count, int)
assert_type(float_binding.writable_count, int)
assert_type(bool_binding.state_changed, qt.QtCore.SignalInstance)
assert_type(float_binding.edit_failed, qt.QtCore.SignalInstance)
assert_type(BoolComboBox(bool_binding), BoolComboBox)
assert_type(FloatSpinBox(float_binding), FloatSpinBox)
assert_type(
    FloatSliderSpinBox(float_binding, minimum=0, maximum=1), FloatSliderSpinBox
)
