# coding: utf-8
"""共通配布ルートのアンインストール処理を確認する。"""

from __future__ import annotations

import json
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Callable, cast

import maya
import pytest

_UNINSTALLER_PATH = (
    Path(__file__).resolve().parents[3] / "bakedanuki" / "uninstaller.py"
)
_UNINSTALLER_SPEC = spec_from_file_location(
    "bakedanuki_uninstaller_test", _UNINSTALLER_PATH
)
if _UNINSTALLER_SPEC is None or _UNINSTALLER_SPEC.loader is None:
    raise RuntimeError(f"uninstaller.pyを読み込めません: {_UNINSTALLER_PATH}")
uninstaller = module_from_spec(_UNINSTALLER_SPEC)
_UNINSTALLER_SPEC.loader.exec_module(uninstaller)


class FakeUninstallerCmds:
    """Mayaのversion、設定先、確認ダイアログを代替する。"""

    def __init__(self, app_dir: Path) -> None:
        """仮のユーザー設定先を保持する。"""
        self.app_dir = app_dir
        self.messages: list[str] = []
        self.confirm_next = True
        self.before_confirm: Callable[[], None] | None = None

    def about(self, *, version: bool) -> str:
        """使用中のMayaバージョンを返す。"""
        assert version
        return "2025"

    def internalVar(self, *, userAppDir: bool) -> str:
        """仮のMayaアプリケーションディレクトリを返す。"""
        assert userAppDir
        return str(self.app_dir)

    def confirmDialog(self, **kwargs: object) -> str:
        """確認内容を記録し、指定した選択を返す。"""
        self.messages.append(cast(str, kwargs["message"]))
        if "Cancel" in cast(list[str], kwargs["button"]):
            if self.before_confirm is not None:
                self.before_confirm()
            return "OK" if self.confirm_next else "Cancel"
        return "OK"


@pytest.fixture
def uninstall_env(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> tuple[FakeUninstallerCmds, Path, Path]:
    """Maya.envと解除対象を一時ディレクトリへ分離する。"""
    fake = FakeUninstallerCmds(tmp_path / "maya")
    env_path = fake.app_dir / "2025" / "Maya.env"
    modules_dir = tmp_path / "bakedanuki" / "modules"
    monkeypatch.delenv("MAYA_ENV_DIR", raising=False)
    monkeypatch.setattr(maya, "cmds", fake)
    monkeypatch.setattr(
        uninstaller, "_target_modules_dir", lambda: modules_dir
    )
    return fake, env_path, modules_dir


def test_uninstall_removes_only_own_path_and_preserves_file_format(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """共有rootの重複だけを解除し、別rootと設定を維持する。"""
    fake, env_path, modules_dir = uninstall_env
    env_path.parent.mkdir(parents=True)
    target = modules_dir.as_posix()
    other = "D:/develop/bakedanuki-tools/bakedanuki/modules"
    original = (
        "# 個人設定\r\n"
        f"MAYA_MODULE_PATH={target};D:/other/modules;"
        f"{target.upper().replace('/', chr(92))};{other};\r\n"
        "MY_SETTING=値\r\n"
    ).encode("utf-8-sig")
    env_path.write_bytes(original)
    menu_path = fake.app_dir / "2025" / "prefs" / "bakedanuki" / "menu.json"
    menu_path.parent.mkdir(parents=True)
    menu_path.write_text(json.dumps({"show_menu_on_startup": False}))

    uninstaller.uninstall()

    result = env_path.read_bytes()
    assert result.startswith(b"\xef\xbb\xbf")
    assert result.decode("utf-8-sig") == (
        "# 個人設定\r\n"
        f"MAYA_MODULE_PATH=D:/other/modules;{other};\r\n"
        "MY_SETTING=値\r\n"
    )
    backups = list(env_path.parent.glob("Maya.env.bakedanuki-*.bak"))
    assert len(backups) == 1
    assert backups[0].read_bytes() == original
    assert json.loads(menu_path.read_text()) == {"show_menu_on_startup": False}
    assert any("Maya 2025" in message for message in fake.messages)
    assert any("再起動" in message for message in fake.messages)


def test_uninstall_removes_empty_module_line_but_keeps_env_file(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """対象だけだった場合は変数行を消し、他の設定とファイルを残す。"""
    _, env_path, modules_dir = uninstall_env
    env_path.parent.mkdir(parents=True)
    env_path.write_text(
        f"MAYA_MODULE_PATH={modules_dir.as_posix()};\nOTHER=1\n"
    )

    uninstaller.uninstall()

    assert env_path.read_text() == "OTHER=1\n"


def test_cancel_and_missing_registration_leave_file_unchanged(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """キャンセルと未登録では設定やバックアップを作らない。"""
    fake, env_path, modules_dir = uninstall_env
    env_path.parent.mkdir(parents=True)
    original = f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n"
    env_path.write_text(original)
    fake.confirm_next = False

    uninstaller.uninstall()

    assert env_path.read_text() == original
    assert not list(env_path.parent.glob("*.bak"))
    env_path.write_text("MAYA_MODULE_PATH=D:/other/modules;\n")
    fake.messages.clear()

    uninstaller.uninstall()

    assert env_path.read_text() == "MAYA_MODULE_PATH=D:/other/modules;\n"
    assert len(fake.messages) == 1
    assert "解除対象はありません" in fake.messages[0]


def test_missing_maya_env_does_not_create_file(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """Maya.envがなければ案内だけを表示する。"""
    fake, env_path, _ = uninstall_env

    uninstaller.uninstall()

    assert not env_path.exists()
    assert "解除対象はありません" in fake.messages[0]


def test_uninstall_uses_custom_maya_env_directory(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """MAYA_ENV_DIRがあればそこにある設定だけを解除する。"""
    _, default_path, modules_dir = uninstall_env
    default_path.parent.mkdir(parents=True)
    original = f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n"
    default_path.write_text(original)
    custom_path = tmp_path / "custom" / "Maya.env"
    custom_path.parent.mkdir()
    custom_path.write_text(original)
    monkeypatch.setenv("MAYA_ENV_DIR", str(custom_path.parent))

    uninstaller.uninstall()

    assert custom_path.read_text() == ""
    assert default_path.read_text() == original


def test_uninstall_uses_app_dir_fallback(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """バージョン別Maya.envがなければ共通ファイルを解除する。"""
    fake, version_path, modules_dir = uninstall_env
    fallback_path = fake.app_dir / "Maya.env"
    fallback_path.parent.mkdir(parents=True)
    fallback_path.write_text(f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n")

    uninstaller.uninstall()

    assert fallback_path.read_text() == ""
    assert not version_path.exists()


def test_multiple_module_lines_stop_without_changes(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """曖昧な複数定義は推測して書き換えない。"""
    _, env_path, modules_dir = uninstall_env
    env_path.parent.mkdir(parents=True)
    original = (
        f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n"
        "MAYA_MODULE_PATH=D:/other/modules;\n"
    )
    env_path.write_text(original)

    with pytest.raises(ValueError, match="複数行"):
        uninstaller.uninstall()

    assert env_path.read_text() == original
    assert not list(env_path.parent.glob("*.bak"))


def test_concurrent_edit_is_not_overwritten(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """確認中にMaya.envが変わったら古い内容で上書きしない。"""
    fake, env_path, modules_dir = uninstall_env
    env_path.parent.mkdir(parents=True)
    env_path.write_text(f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n")
    external_edit = "MAYA_MODULE_PATH=D:/external/modules;\n"
    fake.before_confirm = lambda: env_path.write_text(external_edit)

    with pytest.raises(RuntimeError, match="確認後に Maya.env が変更"):
        uninstaller.uninstall()

    assert env_path.read_text() == external_edit
    assert not list(env_path.parent.glob("*.bak"))


def test_replace_failure_keeps_original_env(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """保存の置換に失敗しても元ファイルと退避内容を保つ。"""
    _, env_path, modules_dir = uninstall_env
    env_path.parent.mkdir(parents=True)
    original = f"MAYA_MODULE_PATH={modules_dir.as_posix()};\n".encode()
    env_path.write_bytes(original)

    def fail_replace(_source: object, _destination: object) -> None:
        """一時ファイルからの置換失敗を再現する。"""
        raise OSError("replace failed")

    monkeypatch.setattr(uninstaller.os, "replace", fail_replace)
    with pytest.raises(OSError, match="replace failed"):
        uninstaller.uninstall()

    assert env_path.read_bytes() == original
    backups = list(env_path.parent.glob("Maya.env.bakedanuki-*.bak"))
    assert len(backups) == 1
    assert backups[0].read_bytes() == original
    assert not list(env_path.parent.glob(".Maya.env-*.tmp"))


def test_invalid_utf8_with_bom_stops_before_edit(
    uninstall_env: tuple[FakeUninstallerCmds, Path, Path],
) -> None:
    """BOM付きUTF-8が壊れていれば別の文字コードとして扱わない。"""
    _, env_path, _ = uninstall_env
    env_path.parent.mkdir(parents=True)
    original = b"\xef\xbb\xbf\xff"
    env_path.write_bytes(original)

    with pytest.raises(UnicodeError, match="文字コード"):
        uninstaller.uninstall()

    assert env_path.read_bytes() == original
