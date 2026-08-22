# coding: utf-8
from pathlib import Path

import pytest

from bd_util.maya.ui import (
    MayaWindowController,
    reset_and_show_ui_layout,
    reset_ui_layout,
)
from bd_util.maya.ui import layout as maya_ui_layout
from bd_util.maya.ui import settings as maya_ui_settings
from bd_util.ui import qt

_SETTINGS_PATH = "sample_tool/windows/main"


def _write_saved_layout(settings: qt.QtCore.QSettings) -> None:
    """controller破棄時に保存されるUI配置をtest用INIへ書き込む。"""
    # Window geometry、QMainWindow state、Widget内部状態をまとめて再現する。
    settings.setValue(
        "windows/main/geometry",
        qt.QtCore.QByteArray(b"geometry"),
    )
    settings.setValue(
        "windows/main/window_state",
        qt.QtCore.QByteArray(b"window-state"),
    )
    settings.setValue("windows/main/schema_version", 1)
    settings.setValue("windows/main/ui_state/schema_version", 1)
    settings.setValue(
        "windows/main/ui_state/widgets/main_tabs/type",
        "tab_widget",
    )
    settings.setValue(
        "windows/main/ui_state/widgets/main_tabs/state",
        1,
    )
    settings.sync()


class _NormalController:
    """通常Windowのdispose時保存を再現するtest用controller。"""

    def __init__(self, settings: qt.QtCore.QSettings) -> None:
        """保存先とdispose回数を保持して初期化する。"""
        self._settings = settings
        self.dispose_count = 0
        self.show_count = 0
        self.layout_present_when_shown: bool | None = None
        self.shown_window = object()

    def dispose(self) -> None:
        """close eventによる最終保存を再現する。"""
        self.dispose_count += 1
        _write_saved_layout(self._settings)

    def show(self) -> object:
        """再表示時点の保存状態を記録してtest用Windowを返す。"""
        # 別QSettings instanceによるclear結果を読み直してから状態を記録する。
        self._settings.sync()
        self.show_count += 1
        self.layout_present_when_shown = self._settings.contains(
            "windows/main/geometry"
        ) or self._settings.contains("windows/main/ui_state/schema_version")
        return self.shown_window


class _DockController(_NormalController):
    """dockable Windowのworkspace state resetを再現するcontroller。"""

    def __init__(self, settings: qt.QtCore.QSettings) -> None:
        """通常controllerの状態にworkspace reset回数を追加する。"""
        super().__init__(settings)
        self.workspace_reset_count = 0

    def reset_workspace_state(self) -> None:
        """dock完全破棄時の最終保存とworkspace state削除を再現する。"""
        self.workspace_reset_count += 1
        _write_saved_layout(self._settings)


@pytest.fixture
def layout_settings(
    monkeypatch,
    tmp_path: Path,
) -> qt.QtCore.QSettings:
    """tool設定を一時directoryへ保存するQSettingsを返す。"""
    # Maya user preferencesの代わりにtestごとの一時directoryを使用する。
    monkeypatch.setattr(
        maya_ui_settings,
        "get_ui_settings_root",
        lambda: tmp_path,
    )
    settings_file = maya_ui_settings.get_ui_settings_file(_SETTINGS_PATH)
    settings_file.parent.mkdir(parents=True, exist_ok=True)
    return qt.QtCore.QSettings(
        str(settings_file),
        qt.QtCore.QSettings.Format.IniFormat,
    )


def test_reset_dock_layout_clears_state_saved_during_dispose(
    layout_settings: qt.QtCore.QSettings,
) -> None:
    # reset対象外のtool固有設定とdock controllerを用意する。
    layout_settings.setValue("windows/main/tool_option", True)
    layout_settings.sync()
    controller = _DockController(layout_settings)

    # workspace state reset後にINI上のWindowとWidget状態を削除する。
    assert reset_ui_layout(controller, _SETTINGS_PATH)
    layout_settings.sync()

    # dock専用resetを使い、dispose時に再保存された配置だけを削除する。
    assert controller.workspace_reset_count == 1
    assert controller.dispose_count == 0
    assert not layout_settings.contains("windows/main/geometry")
    assert not layout_settings.contains("windows/main/window_state")
    assert not layout_settings.contains("windows/main/schema_version")
    assert not layout_settings.contains("windows/main/ui_state/schema_version")
    assert layout_settings.value("windows/main/tool_option", False, bool)


def test_reset_normal_layout_can_preserve_window_state(
    layout_settings: qt.QtCore.QSettings,
) -> None:
    # 通常Windowのdispose時にWindowとWidget状態が保存される状態を作る。
    controller = _NormalController(layout_settings)

    # Window geometryを残し、Widget内部状態だけを統合resetから削除する。
    assert reset_ui_layout(
        controller,
        _SETTINGS_PATH,
        clear_window_state=False,
    )
    layout_settings.sync()

    # 通常controllerはdisposeされ、指定どおりWindow stateだけが維持される。
    assert controller.dispose_count == 1
    assert layout_settings.contains("windows/main/geometry")
    assert layout_settings.contains("windows/main/window_state")
    assert not layout_settings.contains("windows/main/ui_state/schema_version")


def test_reset_normal_layout_can_preserve_widget_state(
    layout_settings: qt.QtCore.QSettings,
) -> None:
    # 通常Windowのdispose時にWindowとWidget状態が保存される状態を作る。
    controller = _NormalController(layout_settings)

    # Widget内部状態を残し、Window geometryだけを統合resetから削除する。
    assert reset_ui_layout(
        controller,
        _SETTINGS_PATH,
        clear_widget_state=False,
    )
    layout_settings.sync()

    # 指定どおりWindow stateだけが削除され、Widget状態は維持される。
    assert controller.dispose_count == 1
    assert not layout_settings.contains("windows/main/geometry")
    assert not layout_settings.contains("windows/main/window_state")
    assert layout_settings.contains("windows/main/ui_state/schema_version")


def test_reset_validates_settings_path_before_dispose(
    layout_settings: qt.QtCore.QSettings,
) -> None:
    # 無効なsettings pathと通常controllerを用意する。
    controller = _NormalController(layout_settings)

    # 保存先を解決できない場合はWindowを破棄せず明確なerrorを送出する。
    with pytest.raises(ValueError):
        reset_ui_layout(controller, "invalid_path")
    assert controller.dispose_count == 0


def test_reset_rejects_different_maya_window_settings_path() -> None:
    # factoryを呼ばずに保存先を持つ通常Maya controllerを構築する。
    controller = MayaWindowController(
        lambda _parent: qt.QWidget(),
        settings_path="sample_tool/windows/other",
    )

    # 別groupをclearしてcontrollerの保存値を残す誤操作を破棄前に拒否する。
    with pytest.raises(ValueError, match="保存先と一致"):
        reset_ui_layout(controller, _SETTINGS_PATH)
    assert controller.window is None


def test_reset_and_show_dock_layout_returns_new_window(
    layout_settings: qt.QtCore.QSettings,
) -> None:
    # workspace stateと再表示結果を記録できるdock controllerを用意する。
    controller = _DockController(layout_settings)

    # 完全reset後にcontrollerから初期状態のWindowを再表示する。
    window = reset_and_show_ui_layout(controller, _SETTINGS_PATH)

    # 保存配置を削除してからshowし、controllerの戻り値をそのまま公開する。
    assert controller.workspace_reset_count == 1
    assert controller.show_count == 1
    assert controller.layout_present_when_shown is False
    assert window is controller.shown_window


def test_reset_and_show_does_not_show_after_clear_failure(
    monkeypatch,
    layout_settings: qt.QtCore.QSettings,
) -> None:
    """QSettingsのclear失敗を再現する保存処理。"""

    class _FailingWindowStateStore:
        """clear失敗を返すtest用WindowStateStore。"""

        def clear(self) -> bool:
            """保存状態を変更せず失敗を返す。"""
            return False

    # Window stateだけがclearできない状態と通常controllerを用意する。
    monkeypatch.setattr(
        maya_ui_layout,
        "create_window_state_store",
        lambda _settings_path: _FailingWindowStateStore(),
    )
    controller = _NormalController(layout_settings)

    # reset失敗時は古い保存値を使うWindowを再表示せず明確なerrorにする。
    with pytest.raises(RuntimeError, match="再表示しません"):
        reset_and_show_ui_layout(
            controller,
            _SETTINGS_PATH,
            clear_widget_state=False,
        )
    assert controller.dispose_count == 1
    assert controller.show_count == 0
