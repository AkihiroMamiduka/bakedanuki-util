# coding: utf-8
from pathlib import Path

from maya import cmds

from ...ui import SettingsPath, UiStateManager, WindowStateStore, qt


def get_ui_settings_root() -> Path:
    """Mayaのuser preferences内にあるtool用設定の基点を返す。

    Raises:
        RuntimeError: Mayaが初期化されていない場合。
    """
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
    """指定したtoolの`ui.ini`のパスを返す。

    Args:
        settings_path: `tool名/group名`形式の保存先。

    Returns:
        tool単位で共有するINIファイルのパス。
    """
    # groupごとに別ファイルを作らず、tool名で保存先をまとめる。
    resolved_path = SettingsPath.from_value(settings_path)
    return get_ui_settings_root() / resolved_path.tool_name / "ui.ini"


def create_window_state_store(
    settings_path: str | SettingsPath,
) -> WindowStateStore:
    """指定したgroupのWindow状態を保存するStoreを作る。

    Args:
        settings_path: `tool名/group名`形式の保存先。

    Returns:
        Mayaのuser preferences内のINIファイルを使うStore。
    """
    # tool単位の共通QSettingsを使ってwindow geometryの保存先を作成する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings = _create_ui_settings(resolved_path)
    return WindowStateStore(settings, resolved_path)


def create_ui_state_manager(
    settings_path: str | SettingsPath,
) -> UiStateManager:
    """指定したgroupのWidget状態を保存するManagerを作る。

    Args:
        settings_path: `tool名/group名`形式の保存先。

    Returns:
        Mayaのuser preferences内のINIファイルを使うManager。
    """
    # tool単位の共通QSettingsを使ってWidget内部状態の保存先を作成する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings = _create_ui_settings(resolved_path)
    return UiStateManager(settings, resolved_path)


def _create_ui_settings(
    settings_path: SettingsPath,
) -> qt.QtCore.QSettings:
    """settings pathに対応するMaya用QSettingsを生成する。"""
    # QSettingsの作成前にtool単位の保存先を用意する。
    settings_file = get_ui_settings_file(settings_path)
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    # NativeFormatを避け、物理ファイルへ保存するQSettingsを生成する。
    return qt.QtCore.QSettings(
        str(settings_file),
        qt.QtCore.QSettings.Format.IniFormat,
    )
