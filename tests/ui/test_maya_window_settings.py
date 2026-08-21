# coding: utf-8
from pathlib import Path

from PySide6 import QtCore, QtWidgets

from bd_util.maya.ui import (
    MayaUiStateTracker,
    MayaWindowController,
    create_ui_state_manager,
    reset_and_show_ui_layout,
)
from bd_util.maya.ui import settings as maya_ui_settings
from bd_util.maya.ui import callback as maya_callback
from bd_util.maya.ui import ui_state as maya_ui_state
from bd_util.maya.ui import window as maya_window
from bd_util.ui import SettingsPath

_STATEFUL_SETTINGS_PATH = "tool_name/windows/stateful"


class _StatefulWindow(QtWidgets.QDialog):
    """通常WindowのWidget状態連携を確認するtest用dialog。"""

    def __init__(
        self,
        parent: QtWidgets.QWidget | None = None,
    ) -> None:
        """選択タブとlifecycle trackerを持つdialogを生成する。"""
        # 通常Windowとして表示できるTab Widgetを構築する。
        super().__init__(parent)
        self.main_tabs = QtWidgets.QTabWidget()
        self.main_tabs.addTab(QtWidgets.QWidget(), "First")
        self.main_tabs.addTab(QtWidgets.QWidget(), "Second")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.main_tabs)

        # 実際のMaya用QSettingsと通常Window trackerを接続する。
        self.ui_state = create_ui_state_manager(_STATEFUL_SETTINGS_PATH)
        self.ui_state.register_tab_widget("main_tabs", self.main_tabs)
        self.ui_state_tracker = MayaUiStateTracker.for_window(
            self.ui_state,
            self,
        )


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


def _replace_maya_callbacks(monkeypatch) -> None:
    """Maya callback操作をtest用の固定処理へ置き換える。"""
    # Qt lifecycleだけを検証し、Maya終了callbackの実登録を避ける。
    monkeypatch.setattr(
        maya_callback,
        "_add_maya_exiting_callback",
        lambda _callback: 42,
    )
    monkeypatch.setattr(
        maya_callback,
        "_remove_callback",
        lambda _callback_id: None,
    )


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


def test_maya_controller_disposes_owned_callbacks_immediately(
    qt_application,
    monkeypatch,
) -> None:
    # controllerがcallback解除へ渡したWindowを記録する。
    disposed_owners: list[QtWidgets.QWidget] = []
    monkeypatch.setattr(
        maya_window,
        "dispose_owned_callbacks",
        lambda owner: disposed_owners.append(owner),
    )
    controller = MayaWindowController(QtWidgets.QDialog)
    window = controller.show()

    # DeferredDeleteより前に現在のWindowがcallback解除対象になる。
    controller.dispose()
    assert disposed_owners == [window]
    _process_deferred_deletes(qt_application)


def test_normal_window_tracker_restores_widget_state_after_dispose(
    qt_application,
    monkeypatch,
    tmp_path,
) -> None:
    # Maya settingsと終了callbackをtest用実装へ切り替える。
    monkeypatch.setattr(
        maya_ui_settings,
        "get_ui_settings_root",
        lambda: tmp_path,
    )
    _replace_maya_callbacks(monkeypatch)
    controller = MayaWindowController(
        _StatefulWindow,
        settings_path=_STATEFUL_SETTINGS_PATH,
    )

    # 最初のWindowで変更した選択タブをclose時に保存して完全破棄する。
    first = controller.show()
    qt_application.processEvents()
    first.main_tabs.setCurrentIndex(1)
    controller.dispose()
    _process_deferred_deletes(qt_application)

    # 新しいWindowのShow後に保存済み選択タブが一度だけ復元される。
    second = controller.show()
    qt_application.processEvents()
    assert second is not first
    assert second.main_tabs.currentIndex() == 1

    # testで生成したWindowを完全破棄する。
    controller.dispose()
    _process_deferred_deletes(qt_application)


def test_normal_window_reset_does_not_restore_state_on_delayed_destroy(
    qt_application,
    monkeypatch,
    tmp_path,
) -> None:
    # Maya settingsと終了callbackをtest用実装へ切り替える。
    monkeypatch.setattr(
        maya_ui_settings,
        "get_ui_settings_root",
        lambda: tmp_path,
    )
    _replace_maya_callbacks(monkeypatch)
    controller = MayaWindowController(
        _StatefulWindow,
        settings_path=_STATEFUL_SETTINGS_PATH,
    )

    # 変更済み状態を持つWindowをリセットして直ちに再表示する。
    first = controller.show()
    qt_application.processEvents()
    first.main_tabs.setCurrentIndex(1)
    second = reset_and_show_ui_layout(
        controller,
        _STATEFUL_SETTINGS_PATH,
    )
    _process_deferred_deletes(qt_application)

    # 古いWindowの遅延破棄後も保存値が復活せず初期タブを維持する。
    assert second is not first
    assert second.main_tabs.currentIndex() == 0

    # testで生成したWindowを完全破棄する。
    controller.dispose()
    _process_deferred_deletes(qt_application)
