# coding: utf-8
from pathlib import Path

from PySide6 import QtCore, QtWidgets

from bd_util.maya.ui import MayaWindowController, create_ui_state_manager
from bd_util.maya.ui import settings as maya_ui_settings
from bd_util.ui import SettingsPath


def _process_deferred_deletes(
    application: QtWidgets.QApplication,
) -> None:
    """Qt event loopへ予約された削除処理を実行する。"""
    # DeferredDelete eventを送信してから残りのeventを処理する。
    QtCore.QCoreApplication.sendPostedEvents(
        None,
        QtCore.QEvent.Type.DeferredDelete,
    )
    application.processEvents()


def test_settings_file_uses_tool_directory(monkeypatch, tmp_path) -> None:
    # Maya user preferencesの代わりに一時directoryを使用する。
    monkeypatch.setattr(
        maya_ui_settings,
        "get_ui_settings_root",
        lambda: tmp_path,
    )
    settings_path = SettingsPath("tool_name/widget_a/func_a/my_window")

    # 先頭segmentだけが物理tool directoryになることを確認する。
    settings_file = maya_ui_settings.get_ui_settings_file(settings_path)
    assert settings_file == tmp_path / "tool_name" / "ui.ini"

    # store生成時にtool directoryとINI保存先が準備されることを確認する。
    store = maya_ui_settings.create_window_state_store(settings_path)
    assert Path(store.file_name) == settings_file
    assert settings_file.parent.is_dir()
    assert store.settings_path.group_path == "widget_a/func_a/my_window"

    # UI内部状態も同じtool単位のINIファイルとgroupを共有する。
    manager = create_ui_state_manager(settings_path)
    assert Path(manager.file_name) == settings_file
    assert manager.settings_path == settings_path


def test_maya_controller_restores_saved_geometry(
    qt_application,
    monkeypatch,
    tmp_path,
) -> None:
    # Maya settingsの保存先を一時directoryへ切り替える。
    monkeypatch.setattr(
        maya_ui_settings,
        "get_ui_settings_root",
        lambda: tmp_path,
    )
    settings_path = "tool_name/windows/main"

    # 最初のcontrollerからwindow geometryを保存する。
    first_controller = MayaWindowController(
        QtWidgets.QDialog,
        settings_path=settings_path,
    )
    first = first_controller.show()
    first.setGeometry(130, 150, 410, 270)
    first_controller.close()
    qt_application.processEvents()

    # 別controllerが同じsettings pathからgeometryを復元する。
    second_controller = MayaWindowController(
        QtWidgets.QDialog,
        settings_path=settings_path,
    )
    second = second_controller.show()
    assert second.geometry() == first.geometry()
    assert second_controller.settings_path == SettingsPath(settings_path)

    # testで生成したwindowを削除する。
    first_controller.dispose()
    second_controller.dispose()
    _process_deferred_deletes(qt_application)


def test_maya_controller_can_disable_settings(
    qt_application,
    monkeypatch,
    tmp_path,
) -> None:
    # settings rootを監視できる一時directoryへ切り替える。
    monkeypatch.setattr(
        maya_ui_settings,
        "get_ui_settings_root",
        lambda: tmp_path,
    )

    # settings pathを省略したcontrollerでwindowを表示する。
    controller = MayaWindowController(QtWidgets.QDialog)
    controller.show()

    # 永続化が無効で設定ファイルも作成されないことを確認する。
    assert controller.settings_path is None
    assert not tuple(tmp_path.iterdir())

    # testで生成したwindowを削除する。
    controller.dispose()
    _process_deferred_deletes(qt_application)
