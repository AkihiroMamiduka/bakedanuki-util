# coding: utf-8
from pathlib import Path

from maya import cmds
from PySide6 import QtCore

from ...ui import SettingsPath, UiStateManager, WindowStateStore


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
    # tool単位の共通QSettingsを使ってwindow geometryの保存先を作成する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings = _create_ui_settings(resolved_path)
    return WindowStateStore(settings, resolved_path)


def create_ui_state_manager(
    settings_path: str | SettingsPath,
) -> UiStateManager:
    """Maya用INIファイルを使うUiStateManagerを生成する。"""
    # tool単位の共通QSettingsを使ってWidget内部状態の保存先を作成する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings = _create_ui_settings(resolved_path)
    return UiStateManager(settings, resolved_path)


def _create_ui_settings(
    settings_path: SettingsPath,
) -> QtCore.QSettings:
    """settings pathに対応するMaya用QSettingsを生成する。"""
    # tool directoryを作成してINIファイルの保存先を準備する。
    settings_file = get_ui_settings_file(settings_path)
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    # NativeFormatを避け、物理ファイルへ保存するQSettingsを生成する。
    return QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
