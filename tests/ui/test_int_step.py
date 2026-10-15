# coding: utf-8
"""整数Stepの操作、正本からの独立性と保存形式を検証する。"""

import json
from dataclasses import dataclass

import pytest

from bd_util.ui import (
    IntBinding,
    IntStepSpinBox,
    IntValueStepSpinBox,
    IntStepProfile,
    IntStepSetting,
    SettingsPath,
    UiStateManager,
    qt,
)


@dataclass
class Data:
    """Step操作では変更しない整数正本。"""

    value: int = 5


@pytest.mark.parametrize(
    "initial,steps,expected",
    [
        (1, 1, 10),
        (10, 2, 1000),
        (100, -1, 10),
        (1, -1, 1),
        (15, -1, 1),
        (150, -1, 15),
        (3, 1, 30),
        (30, -2, 1),
        (1000000000, 1, 1000000000),
        (2147483647, -1, 214748364),
        (1, 2147483647, 1),
        (2147483647, -2147483648, 1),
    ],
)
def test_multiplicative_integer_arithmetic(
    qt_application, initial, steps, expected
):
    """整数演算の10倍・除算、下限1と上限超過時の無変更を固定する。"""
    spin = IntStepSpinBox(value=initial, step_mode="multiplicative")
    spin.stepBy(steps)
    assert spin.value() == expected
    assert type(spin.value()) is int
    flags = qt.QtWidgets.QAbstractSpinBox.StepEnabledFlag
    assert bool(spin.stepEnabled() & flags.StepUpEnabled) == (
        expected <= 214748364
    )
    assert bool(spin.stepEnabled() & flags.StepDownEnabled) == (expected > 1)
    spin.deleteLater()


def test_additive_input_commit_and_readonly(qt_application):
    """加算方式、未確定文字の確定と入力停止を確認する。"""
    spin = IntStepSpinBox(value=15, step_increment=5)
    spin.stepDown()
    assert spin.value() == 10
    spin.lineEdit().setText("25")
    spin.stepUp()
    assert spin.value() == 30
    spin.setReadOnly(True)
    spin.stepDown()
    assert spin.value() == 30
    spin.deleteLater()


@pytest.mark.parametrize("invalid", [0, -1, 1.5, 2.0, True, "10", 2147483648])
def test_invalid_step_rejected_at_public_boundaries(qt_application, invalid):
    """入力欄と保存用設定の公開境界で不正値を暗黙変換しない。"""
    with pytest.raises((TypeError, ValueError)):
        IntStepSpinBox(value=invalid)
    with pytest.raises((TypeError, ValueError)):
        IntStepSetting("key", invalid)
    spin = IntStepSpinBox()
    with pytest.raises((TypeError, ValueError)):
        spin.setValue(invalid)
    with pytest.raises((TypeError, ValueError)):
        spin.setSingleStep(invalid)
    assert spin.value() == 1
    spin.deleteLater()


def test_composite_settings_are_local_and_keep_readonly_step_editable(
    qt_application,
):
    """Step変更は正本や共有Viewへ伝播せず、終了後は両欄を停止する。"""
    data = Data()
    binding = IntBinding.from_attribute(data, "value")
    first = IntValueStepSpinBox(binding, step_mode="multiplicative")
    second = IntValueStepSpinBox(binding, single_step=3)
    changes = []
    first.settingsChanged.connect(lambda: changes.append(first.singleStep()))
    first.step_spin_box.stepUp()
    assert changes == [10]
    assert first.spin_box.singleStep() == 10
    assert second.singleStep() == 3
    assert data.value == 5
    first.setSingleStep(10)
    assert changes == [10]
    first.spin_box.stepUp()
    assert data.value == second.spin_box.value() == 15
    first.deleteLater()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    assert not binding.is_disposed
    binding.dispose()
    assert not second.step_spin_box.isEnabled()
    assert not second.spin_box.isEnabled()
    second.deleteLater()


def test_readonly_store_allows_step_and_returns_enter_locally(qt_application):
    """readonly正本でもStepを編集でき、Enterは親へ届かない。"""

    class ReadOnly:
        """読み取り専用のPython属性。"""

        @property
        def value(self):
            """固定の整数を返す。"""
            return 5

    binding = IntBinding.from_attribute(ReadOnly(), "value")
    editor = IntValueStepSpinBox(binding, step_mode="multiplicative")
    assert not editor.spin_box.isEnabled()
    assert editor.step_spin_box.isEnabled()
    editor.step_spin_box.lineEdit().setText("15")
    for key in (qt.Qt.Key.Key_Return, qt.Qt.Key.Key_Enter):
        event = qt.QtGui.QKeyEvent(
            qt.QEvent.Type.KeyPress, key, qt.Qt.KeyboardModifier.NoModifier
        )
        qt.QApplication.sendEvent(editor.step_spin_box, event)
        assert event.isAccepted()
    assert editor.singleStep() == 15
    assert binding.value == 5
    binding.dispose()
    editor.deleteLater()


def manager(file_name):
    """独立したINIを使う保存Managerを作る。"""
    return UiStateManager(
        qt.QSettings(str(file_name), qt.QSettings.Format.IniFormat),
        SettingsPath("int_step/preferences/main"),
    )


def test_profile_atomic_replace_and_persistence(qt_application, tmp_path):
    """型付き項目を一括更新し、整数のまま保存・復元・削除する。"""
    profile = IntStepProfile()
    observed = []
    profile.changed.connect(lambda: observed.append(profile.entries))
    assert profile.set_single_step("long:count", 15)
    assert not profile.set_single_step("long:count", 15)
    with pytest.raises(TypeError):
        profile.replace_entries([IntStepSetting("byte:count", 10), object()])
    assert profile.entries == (IntStepSetting("long:count", 15),)
    assert len(observed) == 1
    first = manager(tmp_path / "ui.ini")
    first.register_int_step_profile("steps", profile)
    first.save_cached()
    restored = IntStepProfile()
    second = manager(tmp_path / "ui.ini")
    second.register_int_step_profile("steps", restored)
    assert second.restore() == frozenset({"steps"})
    assert restored.single_step("long:count") == 15
    assert type(restored.single_step("long:count")) is int
    assert restored.remove("long:count")
    assert not restored.clear()
    second.save_cached()
    settings = qt.QSettings(
        str(tmp_path / "ui.ini"), qt.QSettings.Format.IniFormat
    )
    assert not settings.contains(
        "preferences/main/ui_state/widgets/steps/state"
    )
    profile.deleteLater()
    restored.deleteLater()


@pytest.mark.parametrize(
    "payload",
    [
        {
            "version": 1,
            "entries": [
                {"key": "ok", "single_step": 15},
                {"key": "small", "single_step": 0.5},
                {"key": "bool", "single_step": True},
                {"key": "float", "single_step": 2.0},
                {"key": "", "single_step": 1},
                {"key": "big", "single_step": 2**31},
            ],
        },
        {"version": True, "entries": []},
        {"version": 2, "entries": []},
        {"version": 1, "entries": {}},
        [],
    ],
)
def test_restore_filters_invalid_data_without_touching_other_settings(
    qt_application, tmp_path, payload
):
    """不正な項目と形式を検証し、同居する設定の復元を維持する。"""
    file_name = tmp_path / "ui.ini"
    profile = IntStepProfile()
    profile.set_single_step("old", 9)
    action = qt.QAction("Option")
    action.setCheckable(True)
    action.setChecked(True)
    source = manager(file_name)
    source.register_int_step_profile("steps", profile)
    source.register_checkable_action("option", action)
    source.save_cached()
    settings = qt.QSettings(str(file_name), qt.QSettings.Format.IniFormat)
    settings.setValue(
        "preferences/main/ui_state/widgets/steps/state",
        qt.QByteArray(json.dumps(payload).encode("utf-8")),
    )
    settings.sync()
    action.setChecked(False)
    restored = source.restore()
    assert action.isChecked()
    assert "option" in restored
    assert profile.entries == (
        (IntStepSetting("ok", 15),)
        if isinstance(payload, dict)
        and type(payload.get("version")) is int
        and payload.get("version") == 1
        and isinstance(payload.get("entries"), list)
        else (IntStepSetting("old", 9),)
    )
    profile.deleteLater()
    action.deleteLater()


def test_sample_modes_save_reset_and_reopen_without_scene_changes(
    qt_application, maya_standalone, tmp_path, monkeypatch
):
    """操作サンプルの二方式、独立保存・リセット・再表示を確認する。"""
    from maya import cmds
    from bd_util.maya.ui import settings as maya_settings
    from bd_util._sample.maya.ui.int_sample import step

    monkeypatch.setattr(
        maya_settings, "get_ui_settings_root", lambda: tmp_path
    )
    step.dispose()
    before = cmds.ls(long=True)
    window = step.show()
    qt.QApplication.processEvents()
    try:
        assert step.show() is window
        widget = window.widget
        for editor in (
            widget.multiplicative_editor,
            widget.additive_editor,
        ):
            assert editor.rect().contains(editor.step_spin_box.geometry())
            assert not editor.step_spin_box.visibleRegion().isEmpty()
        initial = widget.binding.value
        widget.multiplicative_editor.step_spin_box.setValue(15)
        widget.additive_editor.step_spin_box.setValue(5)
        assert widget.binding.value == initial
        window.close()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()
        reopened = step.show()
        qt.QApplication.processEvents()
        assert reopened.widget.multiplicative_editor.singleStep() == 15
        assert reopened.widget.additive_editor.singleStep() == 5
        reopened.widget.multiplicative_editor.step_spin_box.stepDown()
        assert reopened.widget.multiplicative_editor.singleStep() == 1
        assert reopened.widget.additive_editor.singleStep() == 5
        reopened.widget.reset_button.click()
        assert reopened.widget.additive_editor.singleStep() == 1
        assert reopened.profile.entries == ()
        assert cmds.ls(long=True) == before
    finally:
        step.dispose()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()
