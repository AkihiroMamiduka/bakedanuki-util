# coding: utf-8
from typing import assert_type
from bd_util._sample.maya.ui.int_sample import step

from bd_util.ui import (
    IntBinding,
    IntStepMode,
    IntStepProfile,
    IntStepSetting,
    IntStepSpinBox,
    IntValueStepSpinBox,
    IntViewModel,
    SettingsPath,
    UiStateManager,
    qt,
)


class Data:
    """型契約用の整数正本。"""

    count: int = 3


binding = IntBinding.from_attribute(Data(), "count")
editor = IntValueStepSpinBox(
    binding, single_step=15, step_mode="multiplicative"
)
assert_type(editor.spin_box.value(), int)
assert_type(editor.step_spin_box, IntStepSpinBox)
assert_type(editor.singleStep(), int)
assert_type(editor.setSingleStep(100), None)
assert_type(editor.view_model, IntViewModel)
assert_type(editor.settingsChanged, qt.QtCore.SignalInstance)
assert_type(editor.step_spin_box.stepMode(), IntStepMode)
profile = IntStepProfile()
assert_type(profile.entries, tuple[IntStepSetting, ...])
assert_type(profile.single_step("count"), int | None)
assert_type(profile.set_single_step("count", 15), bool)
assert_type(profile.replace_entries((IntStepSetting("count", 15),)), bool)
manager = UiStateManager(qt.QSettings(), SettingsPath("sample/preferences"))
assert_type(manager.register_int_step_profile("steps", profile), None)
window = step.show()
assert_type(window, step.IntStepWindow)
assert_type(window.widget.multiplicative_editor, IntValueStepSpinBox)
assert_type(window.profile, IntStepProfile)
assert_type(step.dispose(), None)
