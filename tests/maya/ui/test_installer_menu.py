# coding: utf-8
"""共通installerからbdメニュー表示を再有効化する動作を確認する。"""

from __future__ import annotations

import json
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import cast

import maya
import pytest

from bd_util.maya.ui import is_menu_auto_install_enabled
from bd_util.maya.ui import menu as menu_module

_INSTALLER_PATH = (
    Path(__file__).resolve().parents[3] / "bakedanuki" / "installer.py"
)
_INSTALLER_SPEC = spec_from_file_location(
    "bakedanuki_installer_test", _INSTALLER_PATH
)
if _INSTALLER_SPEC is None or _INSTALLER_SPEC.loader is None:
    raise RuntimeError(f"installer.pyを読み込めません: {_INSTALLER_PATH}")
installer = module_from_spec(_INSTALLER_SPEC)
_INSTALLER_SPEC.loader.exec_module(installer)


class FakeInstallerCmds:
    """installerが使うMaya commandと確認ダイアログを代替する。"""

    def __init__(self, prefs_dir: Path) -> None:
        """設定と表示履歴を空の状態で用意する。"""
        self.option_vars: dict[str, int] = {}
        self.prefs_dir = prefs_dir
        self.messages: list[str] = []
        self.confirm_next = True

    def internalVar(self, **kwargs: object) -> str:
        """一時ディレクトリをMayaのユーザー設定先として返す。"""
        assert kwargs == {"userPrefDir": True}
        return str(self.prefs_dir)

    def optionVar(self, **kwargs: object) -> object:
        """現在のMayaバージョン用設定の照会と保存を模倣する。"""
        if "exists" in kwargs:
            return kwargs["exists"] in self.option_vars
        if "query" in kwargs:
            return self.option_vars[cast(str, kwargs["query"])]
        raise AssertionError("旧optionVarへ書き込んではいけません")

    def about(self, *, batch: bool) -> bool:
        """UIを持たないMayaの状態を返す。"""
        return True

    def savePrefs(self, **kwargs: object) -> None:
        """installerがMayaの一般設定を保存しないことを確認する。"""
        raise AssertionError("savePrefsを呼んではいけません")

    def confirmDialog(self, **kwargs: object) -> str:
        """確認と完了ダイアログの文面を保持する。"""
        self.messages.append(cast(str, kwargs["message"]))
        if "Cancel" in cast(list[str], kwargs["button"]):
            return "OK" if self.confirm_next else "Cancel"
        return "OK"


@pytest.fixture
def installer_env(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> tuple[FakeInstallerCmds, Path, Path]:
    """Maya.envとModule pathを一時ディレクトリへ分離する。"""
    fake = FakeInstallerCmds(tmp_path / "prefs")
    env_path = tmp_path / "Maya.env"
    modules_dir = tmp_path / "bakedanuki" / "modules"
    monkeypatch.setattr(maya, "cmds", fake)
    monkeypatch.setattr(menu_module, "cmds", fake)
    monkeypatch.setattr(installer, "_maya_env_path", lambda _cmds: env_path)
    monkeypatch.setattr(installer, "_target_modules_dir", lambda: modules_dir)
    return fake, env_path, modules_dir


def test_redrop_enables_menu_without_rewriting_registered_module_path(
    installer_env: tuple[FakeInstallerCmds, Path, Path],
) -> None:
    """既登録の再D&DでOFF設定だけをONへ戻す。"""
    fake, env_path, modules_dir = installer_env
    content = f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n"
    env_path.write_text(content, encoding="utf-8")
    fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] = 0
    assert not is_menu_auto_install_enabled()

    installer.install()

    assert env_path.read_text(encoding="utf-8") == content
    assert fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] == 0
    assert is_menu_auto_install_enabled()
    assert json.loads(
        (fake.prefs_dir / "bakedanuki" / "menu.json").read_text(
            encoding="utf-8"
        )
    ) == {"show_menu_on_startup": True}
    assert any("再び有効にしますか" in message for message in fake.messages)
    assert any("Maya を再起動" in message for message in fake.messages)


def test_redrop_cancel_keeps_menu_disabled(
    installer_env: tuple[FakeInstallerCmds, Path, Path],
) -> None:
    """再有効化をキャンセルしたときは設定を変更しない。"""
    fake, env_path, modules_dir = installer_env
    content = f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n"
    env_path.write_text(content, encoding="utf-8")
    fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] = 0
    fake.confirm_next = False

    installer.install()

    assert env_path.read_text(encoding="utf-8") == content
    assert fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] == 0
    assert not (fake.prefs_dir / "bakedanuki" / "menu.json").exists()


def test_new_install_reenables_disabled_menu(
    installer_env: tuple[FakeInstallerCmds, Path, Path],
) -> None:
    """Module pathを追加するときはOFF設定も確認後にONへ戻す。"""
    fake, env_path, modules_dir = installer_env
    fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] = 0

    installer.install()

    assert modules_dir.as_posix() in env_path.read_text(encoding="utf-8")
    assert fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] == 0
    assert json.loads(
        (fake.prefs_dir / "bakedanuki" / "menu.json").read_text(
            encoding="utf-8"
        )
    ) == {"show_menu_on_startup": True}
    assert any("起動時表示も有効" in message for message in fake.messages)


def test_installer_can_enable_before_util_is_loaded(
    installer_env: tuple[FakeInstallerCmds, Path, Path],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """初回導入で基盤が未読込でもMaya設定を直接更新する。"""
    fake, _, _ = installer_env
    fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] = 0
    monkeypatch.delitem(sys.modules, "bd_util.maya.ui")

    installer.install()

    assert fake.option_vars[installer.MENU_AUTO_INSTALL_OPTION_VAR] == 0
    assert json.loads(
        (fake.prefs_dir / "bakedanuki" / "menu.json").read_text(
            encoding="utf-8"
        )
    ) == {"show_menu_on_startup": True}


def test_redrop_migrates_legacy_json_key(
    installer_env: tuple[FakeInstallerCmds, Path, Path],
) -> None:
    """再D&Dで旧JSONキーのOFFを新しいキーのONへ更新する。"""
    fake, env_path, modules_dir = installer_env
    env_path.write_text(
        f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n", encoding="utf-8"
    )
    setting_path = fake.prefs_dir / "bakedanuki" / "menu.json"
    setting_path.parent.mkdir(parents=True)
    setting_path.write_text('{"auto_install": false}\n', encoding="utf-8")
    assert not is_menu_auto_install_enabled()

    installer.install()

    assert is_menu_auto_install_enabled()
    assert json.loads(setting_path.read_text(encoding="utf-8")) == {
        "show_menu_on_startup": True
    }
