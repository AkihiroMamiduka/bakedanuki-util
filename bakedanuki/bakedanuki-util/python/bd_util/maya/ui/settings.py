# coding: utf-8
from pathlib import Path

from maya import cmds
from PySide6 import QtCore

from ...ui import SettingsPath, WindowStateStore


def get_ui_settings_root() -> Path:
    """Maya user preferences内のUI settings rootを返す。"""
    # Maya versionごとのuser preferences directoryを取得する。
    try:
        user_pref_dir = cmds.internalVar(userPrefDir=True)
    except AttributeError as error:
        raise RuntimeError("Mayaが初期化されていません") from error

    # bakedanukiのtool settingsをまとめるdirectoryを構成する。
    return Path(user_pref_dir) / "bakedanuki" / "tools"


def get_ui_settings_file(
    settings_path: str | SettingsPath,
) -> Path:
    """settings pathに対応するtoolのINIファイルを返す。"""
    # 先頭segmentをtool directoryとして安全なpathへ変換する。
    resolved_path = SettingsPath.from_value(settings_path)
    return get_ui_settings_root() / resolved_path.tool_name / "ui.ini"


def create_window_state_store(
    settings_path: str | SettingsPath,
) -> WindowStateStore:
    """Maya用INIファイルを使うWindowStateStoreを生成する。"""
    # tool directoryを作成してINIファイルの保存先を準備する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings_file = get_ui_settings_file(resolved_path)
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    # NativeFormatを避け、物理ファイルへ保存するQSettingsを生成する。
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    return WindowStateStore(settings, resolved_path)
