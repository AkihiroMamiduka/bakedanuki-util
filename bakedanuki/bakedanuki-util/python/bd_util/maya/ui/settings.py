# coding: utf-8
from pathlib import Path

from maya import cmds

from ...ui import SettingsPath, UiStateManager, WindowStateStore, qt


def get_ui_settings_root() -> Path:
    """Maya の user preferences 内にある tool 用設定の基点を返す。

    Raises:
        RuntimeError: Mayaが初期化されていない場合。
    """
    # Maya version ごとの user preferences directory を取得する。
    try:
        user_pref_dir = cmds.internalVar(userPrefDir=True)
    except AttributeError as error:
        raise RuntimeError("Mayaが初期化されていません") from error

    # bakedanukiのtool settingsをまとめるdirectoryを構成する。
    return Path(user_pref_dir) / "bakedanuki" / "tools"


def get_ui_settings_file(
    settings_path: str | SettingsPath,
) -> Path:
    """指定した tool の `ui.ini` のパスを返す。

    Args:
        settings_path: `tool名/group名` 形式の保存先。

    Returns:
        tool 単位で共有する INI ファイルのパス。
    """
    # groupごとに別ファイルを作らず、tool名で保存先をまとめる。
    resolved_path = SettingsPath.from_value(settings_path)
    return get_ui_settings_root() / resolved_path.tool_name / "ui.ini"


def create_window_state_store(
    settings_path: str | SettingsPath,
) -> WindowStateStore:
    """指定した group の Window 状態を保存する `WindowStateStore` を作る。

    Args:
        settings_path: `tool名/group名` 形式の保存先。

    Returns:
        Maya の user preferences 内の INI ファイルを使う `WindowStateStore`。
    """
    # tool 単位の共通 `QSettings` を使って Window geometry の保存先を作成する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings = _create_ui_settings(resolved_path)
    return WindowStateStore(settings, resolved_path)


def create_ui_state_manager(
    settings_path: str | SettingsPath,
) -> UiStateManager:
    """指定した group の Widget 状態を保存する `UiStateManager` を作る。

    Args:
        settings_path: `tool名/group名` 形式の保存先。

    Returns:
        Maya の user preferences 内の INI ファイルを使う `UiStateManager`。
    """
    # tool 単位の共通 `QSettings` を使って Widget 内部状態の保存先を作成する。
    resolved_path = SettingsPath.from_value(settings_path)
    settings = _create_ui_settings(resolved_path)
    return UiStateManager(settings, resolved_path)


def _create_ui_settings(
    settings_path: SettingsPath,
) -> qt.QtCore.QSettings:
    """`settings_path` に対応する Maya 用 `QSettings` を生成する。"""
    # `QSettings` の作成前に tool 単位の保存先を用意する。
    settings_file = get_ui_settings_file(settings_path)
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    # `NativeFormat` を避け、物理ファイルへ保存する `QSettings` を生成する。
    return qt.QtCore.QSettings(
        str(settings_file),
        qt.QtCore.QSettings.Format.IniFormat,
    )
