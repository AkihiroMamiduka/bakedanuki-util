# coding: utf-8
"""汎用Step profileとUiStateManager連携を検証する。"""

from __future__ import annotations

import json
from pathlib import Path
from sys import float_info

import pytest

from bd_util.ui import (
    FloatStepProfile,
    FloatStepSetting,
    SettingsPath,
    UiStateManager,
    qt,
)


def _manager(settings_file: Path) -> UiStateManager:
    """一時INIを使うpreferences用managerを作成する。"""
    settings = qt.QSettings(str(settings_file), qt.QSettings.Format.IniFormat)
    return UiStateManager(settings, SettingsPath("sample/preferences/main"))


def _state_key(key: str = "attribute_steps") -> str:
    """登録したprofileのQSettings上の状態pathを返す。"""
    return f"preferences/main/ui_state/widgets/{key}/state"


def _write_payload(
    manager: UiStateManager, payload: object, key: str = "attribute_steps"
) -> None:
    """adapterの内部JSONを不正値の検証用に差し替える。"""
    settings = qt.QSettings(manager.file_name, qt.QSettings.Format.IniFormat)
    settings.setValue(
        _state_key(key),
        qt.QByteArray(json.dumps(payload).encode("utf-8")),
    )
    settings.sync()


@pytest.mark.parametrize("step", (1e-323, 0.12345678901234567, float_info.max))
def test_profile_updates_atomically_and_keeps_precision(
    qt_application: qt.QApplication, step: float
) -> None:
    """複数項目の置換を一度だけ通知し、丸め前のStepを保持する。"""
    profile = FloatStepProfile()
    changes: list[tuple[FloatStepSetting, ...]] = []
    profile.changed.connect(lambda: changes.append(profile.entries))
    entries = (
        FloatStepSetting("translate.translateX", "distance", step),
        FloatStepSetting("rotate.rotateY", "angle", 15),
    )
    assert profile.replace_entries(entries)
    assert changes == [profile.entries]
    assert profile.single_step("translate.translateX", "distance") == step
    assert not profile.replace_entries(reversed(entries))
    assert len(changes) == 1
    assert profile.remove("rotate.rotateY", "angle")
    assert not profile.remove("rotate.rotateY", "angle")
    assert profile.clear()
    assert not profile.clear()
    profile.deleteLater()
    qt_application.processEvents()


@pytest.mark.parametrize(
    ("factory", "error"),
    (
        (lambda: FloatStepSetting("", "number", 1), ValueError),
        (lambda: FloatStepSetting("weight", "cm", 1), ValueError),
        (lambda: FloatStepSetting("weight", "number", 0), ValueError),
        (
            lambda: FloatStepSetting("weight", "number", float("inf")),
            ValueError,
        ),
        (lambda: FloatStepSetting(1, "number", 1), TypeError),
        (lambda: FloatStepSetting("weight", "number", True), TypeError),
    ),
)
def test_setting_rejects_invalid_identity_and_step(factory, error) -> None:
    """曖昧な識別子・単位種別とQtで扱えないStepを拒否する。"""
    with pytest.raises(error):
        factory()


def test_manager_roundtrip_and_empty_profile_removes_state(
    qt_application: qt.QApplication, tmp_path: Path
) -> None:
    """version付きprofileを復元し、全削除後は保存項目自体を除去する。"""
    settings_file = tmp_path / "ui.ini"
    source = FloatStepProfile()
    first = _manager(settings_file)
    first.register_float_step_profile("attribute_steps", source)
    source.replace_entries(
        (
            FloatStepSetting("rotate.rotateZ", "angle", 7.5),
            FloatStepSetting("translate.translateX", "distance", 0.01),
            FloatStepSetting("weight", "number", 2.5),
        )
    )
    assert first.save_cached()

    restored = FloatStepProfile()
    second = _manager(settings_file)
    second.register_float_step_profile("attribute_steps", restored)
    assert second.restore() == frozenset({"attribute_steps"})
    assert restored.entries == source.entries
    assert restored.clear()
    assert second.save_cached()
    settings = qt.QSettings(str(settings_file), qt.QSettings.Format.IniFormat)
    assert not settings.contains(_state_key())
    source.deleteLater()
    restored.deleteLater()
    qt_application.processEvents()


def test_restore_drops_invalid_entries_and_keeps_valid_entries(
    qt_application: qt.QApplication, tmp_path: Path
) -> None:
    """profile全体が読める場合は、不正な個別項目だけを除外する。"""
    settings_file = tmp_path / "ui.ini"
    source = FloatStepProfile()
    manager = _manager(settings_file)
    manager.register_float_step_profile("attribute_steps", source)
    source.set_single_step("old", "number", 9)
    assert manager.save_cached()
    _write_payload(
        manager,
        {
            "version": 1,
            "entries": [
                {
                    "key": "translate.translateX",
                    "unit_kind": "distance",
                    "single_step": 0.25,
                },
                {"key": "", "unit_kind": "number", "single_step": 1},
                {"key": "bad", "unit_kind": "cm", "single_step": 1},
                {"key": "bad", "unit_kind": "number", "single_step": 0},
                {
                    "key": "overflow",
                    "unit_kind": "number",
                    "single_step": 10**1000,
                },
                "bad",
            ],
        },
    )
    observed: list[tuple[FloatStepSetting, ...]] = []
    source.changed.connect(lambda: observed.append(source.entries))
    assert manager.restore() == frozenset({"attribute_steps"})
    assert source.entries == (
        FloatStepSetting("translate.translateX", "distance", 0.25),
    )
    assert observed == [source.entries]
    source.deleteLater()
    qt_application.processEvents()


@pytest.mark.parametrize(
    "raw",
    (
        qt.QByteArray(b"{"),
        qt.QByteArray(b"\xff"),
        "text",
        123,
    ),
)
def test_malformed_profile_removes_only_its_state(
    qt_application: qt.QApplication, tmp_path: Path, raw: object
) -> None:
    """JSONや保存値が壊れていても、同じmanagerのAction状態を復元する。"""
    settings_file = tmp_path / "ui.ini"
    source = FloatStepProfile()
    source.set_single_step("weight", "number", 2)
    action = qt.QAction("Option")
    action.setCheckable(True)
    action.setChecked(True)
    manager = _manager(settings_file)
    manager.register_float_step_profile("attribute_steps", source)
    manager.register_checkable_action("option", action)
    assert manager.save_cached()
    settings = qt.QSettings(str(settings_file), qt.QSettings.Format.IniFormat)
    settings.setValue(_state_key(), raw)
    settings.sync()

    restored = FloatStepProfile()
    restored_action = qt.QAction("Option")
    restored_action.setCheckable(True)
    probe = _manager(settings_file)
    probe.register_float_step_profile("attribute_steps", restored)
    probe.register_checkable_action("option", restored_action)
    assert probe.restore() == frozenset({"option"})
    assert not restored.entries
    assert restored_action.isChecked()
    assert not settings.contains(_state_key())
    source.deleteLater()
    restored.deleteLater()
    action.deleteLater()
    restored_action.deleteLater()
    qt_application.processEvents()


@pytest.mark.parametrize(
    "payload",
    (
        {"version": 2, "entries": []},
        {"version": True, "entries": []},
        {"version": 1, "entries": {}},
        [],
    ),
)
def test_invalid_profile_removes_only_its_state(
    qt_application: qt.QApplication, tmp_path: Path, payload: object
) -> None:
    """未知形式のprofileだけを破棄し、同じmanagerのAction状態は復元する。"""
    settings_file = tmp_path / "ui.ini"
    source = FloatStepProfile()
    source.set_single_step("weight", "number", 2)
    action = qt.QAction("Option")
    action.setCheckable(True)
    action.setChecked(True)
    manager = _manager(settings_file)
    manager.register_float_step_profile("attribute_steps", source)
    manager.register_checkable_action("option", action)
    assert manager.save_cached()
    _write_payload(manager, payload)

    restored = FloatStepProfile()
    restored_action = qt.QAction("Option")
    restored_action.setCheckable(True)
    probe = _manager(settings_file)
    probe.register_float_step_profile("attribute_steps", restored)
    probe.register_checkable_action("option", restored_action)
    assert probe.restore() == frozenset({"option"})
    assert not restored.entries
    assert restored_action.isChecked()
    settings = qt.QSettings(str(settings_file), qt.QSettings.Format.IniFormat)
    assert not settings.contains(_state_key())
    source.deleteLater()
    restored.deleteLater()
    action.deleteLater()
    restored_action.deleteLater()
    qt_application.processEvents()


def test_registration_rejects_wrong_or_destroyed_profile(
    qt_application: qt.QApplication, tmp_path: Path
) -> None:
    """型違い・破棄済み・重複keyを登録前に拒否する。"""
    manager = _manager(tmp_path / "ui.ini")
    with pytest.raises(TypeError, match="FloatStepProfile"):
        manager.register_float_step_profile(
            "attribute_steps",
            object(),  # pyright: ignore[reportArgumentType]
        )
    profile = FloatStepProfile()
    profile.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt_application.processEvents()
    with pytest.raises(RuntimeError, match="破棄"):
        manager.register_float_step_profile("attribute_steps", profile)
    assert manager.registered_keys == ()
