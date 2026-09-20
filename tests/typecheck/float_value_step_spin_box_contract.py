# coding: utf-8
"""値とstepの複合Viewの入力元と部品の型を固定する。"""

from typing import assert_type

from bd_util.maya.ui import MayaFloatPlugsBinding, resolve_float_plug
from bd_util.ui import (
    FloatSpinBox,
    FloatStepMode,
    FloatStepSpinBox,
    FloatValueStepSpinBox,
    FloatViewModel,
    qt,
)

binding = MayaFloatPlugsBinding([resolve_float_plug("node", "translateX")])
editor = FloatValueStepSpinBox(
    binding,
    step_mode="multiplicative",
    value_wheel_requires_focus=True,
    step_wheel_requires_focus=False,
    value_width=90,
    step_width=68,
)
assert_type(editor.view_model, FloatViewModel)
assert_type(editor.spin_box, FloatSpinBox)
assert_type(editor.step_spin_box, FloatStepSpinBox)
assert_type(editor.step_spin_box.stepMode(), FloatStepMode)
assert_type(editor.spin_box.wheel_requires_focus(), bool)
assert_type(editor.spin_box.set_wheel_requires_focus(False), None)
assert_type(editor.step_spin_box.wheel_requires_focus(), bool)
assert_type(editor.step_spin_box.set_wheel_requires_focus(True), None)
assert_type(editor.singleStep(), float)
assert_type(editor.setSingleStep(15), None)
assert_type(editor.settingsChanged, qt.QtCore.SignalInstance)
assert_type(FloatSpinBox(binding, wheel_requires_focus=True), FloatSpinBox)
assert_type(FloatStepSpinBox(wheel_requires_focus=False), FloatStepSpinBox)
assert_type(FloatValueStepSpinBox(binding.view_model), FloatValueStepSpinBox)
