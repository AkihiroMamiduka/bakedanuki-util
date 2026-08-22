# coding: utf-8
from pathlib import Path

import pytest
from PySide6 import QtCore, QtWidgets

from bd_util.ui import SettingsPath, UiStateManager, qt
from bd_util.ui import ui_state as ui_state_module


class _FailingStateAdapter(ui_state_module._UiStateAdapter):
    """状態収集中に失敗するtest用adapter。"""

    state_type = "failing"

    def __init__(self, widget: QtWidgets.QWidget) -> None:
        """生存判定に使用するWidgetを保持する。"""
        self.widget = widget

    @property
    def state_object(self) -> QtCore.QObject:
        """状態を所有するtest用Widgetを返す。"""
        return self.widget

    def save_state(self) -> None:
        """状態収集失敗を再現する。"""
        raise RuntimeError("test state collection failed")

    def restore_state(
        self,
        settings: QtCore.QSettings,
        state_key: str,
    ) -> bool:
        """testでは使用しない復元処理を定義する。"""
        return False


def _create_manager(
    settings_file: Path,
    settings_path: str = "sample_tool/windows/main",
) -> UiStateManager:
    """test用INIファイルを使用するUiStateManagerを生成する。"""
    # 各testで独立した物理ファイルを利用するQSettingsを作成する。
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    return UiStateManager(settings, SettingsPath(settings_path))


def test_save_and_restore_registered_widget_state(
    qt_application,
    tmp_path,
) -> None:
    # 保存元となるSplitterとTabWidgetを構築する。
    splitter = QtWidgets.QSplitter()
    splitter.addWidget(QtWidgets.QLabel("Left"))
    splitter.addWidget(QtWidgets.QLabel("Right"))
    splitter.resize(500, 200)
    splitter.setSizes([140, 360])

    tabs = QtWidgets.QTabWidget()
    tabs.addTab(QtWidgets.QWidget(), "First")
    tabs.addTab(QtWidgets.QWidget(), "Second")
    tabs.setCurrentIndex(1)

    # 2種類のWidgetを明示登録して現在の状態を保存する。
    settings_file = tmp_path / "ui.ini"
    first_manager = _create_manager(settings_file)
    first_manager.register_splitter("main_splitter", splitter)
    first_manager.register_tab_widget("main_tabs", tabs)
    assert first_manager.save()

    # 保存後に各Widgetの状態を異なる値へ変更する。
    saved_splitter_state = splitter.saveState()
    splitter.setSizes([400, 100])
    tabs.setCurrentIndex(0)

    # 新しいmanagerから登録済みの2種類をまとめて復元する。
    restored_manager = _create_manager(settings_file)
    restored_manager.register_splitter("main_splitter", splitter)
    restored_manager.register_tab_widget("main_tabs", tabs)
    restored_keys = restored_manager.restore()

    # Qt標準stateと選択indexが保存時の状態へ戻ることを確認する。
    assert restored_keys == frozenset({"main_splitter", "main_tabs"})
    assert splitter.saveState() == saved_splitter_state
    assert tabs.currentIndex() == 1

    # testで生成したtop level Widgetを削除する。
    splitter.deleteLater()
    tabs.deleteLater()
    qt_application.processEvents()


def test_save_preserves_deleted_widget_state_and_updates_live_widget(
    qt_application,
    tmp_path,
) -> None:
    # SplitterとTabを同じmanagerへ登録する。
    splitter = QtWidgets.QSplitter()
    splitter.addWidget(QtWidgets.QLabel("Left"))
    splitter.addWidget(QtWidgets.QLabel("Right"))
    splitter.resize(500, 200)
    splitter.show()
    qt_application.processEvents()

    tabs = QtWidgets.QTabWidget()
    tabs.addTab(QtWidgets.QWidget(), "First")
    tabs.addTab(QtWidgets.QWidget(), "Second")

    settings_file = tmp_path / "ui.ini"
    manager = _create_manager(settings_file)
    manager.register_splitter("main_splitter", splitter)
    manager.register_tab_widget("main_tabs", tabs)

    # 登録後のSplitter移動をsignal経由でmemoryへ退避する。
    splitter.moveSplitter(180, 1)
    saved_splitter_state = splitter.saveState()
    tabs.setCurrentIndex(1)

    # 永続化前にSplitterを破棄し、Tabだけを別の状態へ変更する。
    splitter.deleteLater()
    QtCore.QCoreApplication.sendPostedEvents(
        None,
        QtCore.QEvent.Type.DeferredDelete,
    )
    qt_application.processEvents()
    assert not qt.isValid(splitter)
    tabs.setCurrentIndex(0)

    # 破棄前に退避したSplitter状態と、生存中のTab状態をまとめて保存する。
    assert manager.save()

    restored_splitter = QtWidgets.QSplitter()
    restored_splitter.addWidget(QtWidgets.QLabel("Left"))
    restored_splitter.addWidget(QtWidgets.QLabel("Right"))
    restored_tabs = QtWidgets.QTabWidget()
    restored_tabs.addTab(QtWidgets.QWidget(), "First")
    restored_tabs.addTab(QtWidgets.QWidget(), "Second")
    restored_tabs.setCurrentIndex(1)

    restored_manager = _create_manager(settings_file)
    restored_manager.register_splitter("main_splitter", restored_splitter)
    restored_manager.register_tab_widget("main_tabs", restored_tabs)
    assert restored_manager.restore() == frozenset(
        {"main_splitter", "main_tabs"}
    )
    assert restored_splitter.saveState() == saved_splitter_state
    assert restored_tabs.currentIndex() == 0

    # testで生成した残りのtop level Widgetを削除する。
    tabs.deleteLater()
    restored_splitter.deleteLater()
    restored_tabs.deleteLater()
    qt_application.processEvents()


def test_save_does_not_modify_settings_when_state_collection_fails(
    qt_application,
    tmp_path,
) -> None:
    # 保存済み状態を持つTabと、状態収集に失敗するWidgetを用意する。
    tabs = QtWidgets.QTabWidget()
    tabs.addTab(QtWidgets.QWidget(), "First")
    tabs.addTab(QtWidgets.QWidget(), "Second")
    tabs.setCurrentIndex(1)
    failing_widget = QtWidgets.QWidget()

    settings_file = tmp_path / "ui.ini"
    manager = _create_manager(settings_file)
    manager.register_tab_widget("main_tabs", tabs)
    assert manager.save()

    # Tabの変更後に後続adapterが失敗する保存処理を実行する。
    tabs.setCurrentIndex(0)
    manager._adapters["failing"] = _FailingStateAdapter(failing_widget)
    with pytest.raises(RuntimeError, match="state collection failed"):
        manager.save()

    # 収集完了前にはQSettingsを更新せず、以前のTab状態を復元できることを確認する。
    restored_tabs = QtWidgets.QTabWidget()
    restored_tabs.addTab(QtWidgets.QWidget(), "First")
    restored_tabs.addTab(QtWidgets.QWidget(), "Second")
    restored_tabs.setCurrentIndex(0)
    restored_manager = _create_manager(settings_file)
    restored_manager.register_tab_widget("main_tabs", restored_tabs)
    assert restored_manager.restore() == frozenset({"main_tabs"})
    assert restored_tabs.currentIndex() == 1

    # testで生成したWidgetを削除する。
    tabs.deleteLater()
    failing_widget.deleteLater()
    restored_tabs.deleteLater()
    qt_application.processEvents()


def test_restore_only_changes_registered_widgets(
    qt_application,
    tmp_path,
) -> None:
    # 2つのTabWidgetのうち最初のWidgetだけを保存対象として登録する。
    first_tabs = QtWidgets.QTabWidget()
    second_tabs = QtWidgets.QTabWidget()
    for tabs in (first_tabs, second_tabs):
        tabs.addTab(QtWidgets.QWidget(), "First")
        tabs.addTab(QtWidgets.QWidget(), "Second")
        tabs.setCurrentIndex(1)

    manager = _create_manager(tmp_path / "ui.ini")
    manager.register_tab_widget("registered_tabs", first_tabs)
    assert manager.save()

    # 保存後に両方のWidgetを同じ状態へ変更する。
    first_tabs.setCurrentIndex(0)
    second_tabs.setCurrentIndex(0)
    assert manager.restore() == frozenset({"registered_tabs"})

    # 登録したWidgetだけが復元され、未登録Widgetは変更されないことを確認する。
    assert first_tabs.currentIndex() == 1
    assert second_tabs.currentIndex() == 0

    # testで生成したWidgetを削除する。
    first_tabs.deleteLater()
    second_tabs.deleteLater()
    qt_application.processEvents()


def test_separate_managers_preserve_each_others_state(
    qt_application,
    tmp_path,
) -> None:
    # 同じsettings pathを共有する2つのcomponent相当のWidgetを作成する。
    first_tabs = QtWidgets.QTabWidget()
    second_tabs = QtWidgets.QTabWidget()
    for tabs in (first_tabs, second_tabs):
        tabs.addTab(QtWidgets.QWidget(), "First")
        tabs.addTab(QtWidgets.QWidget(), "Second")
        tabs.setCurrentIndex(1)

    # 別managerから異なるkeyを順番に保存する。
    settings_file = tmp_path / "ui.ini"
    first_manager = _create_manager(settings_file)
    first_manager.register_tab_widget("first_tabs", first_tabs)
    assert first_manager.save()

    second_manager = _create_manager(settings_file)
    second_manager.register_tab_widget("second_tabs", second_tabs)
    assert second_manager.save()

    # 両方を変更してから1つのmanagerへまとめて登録する。
    first_tabs.setCurrentIndex(0)
    second_tabs.setCurrentIndex(0)
    restored_manager = _create_manager(settings_file)
    restored_manager.register_tab_widget("first_tabs", first_tabs)
    restored_manager.register_tab_widget("second_tabs", second_tabs)

    # 後から保存したmanagerが先のstateを削除していないことを確認する。
    assert restored_manager.restore() == frozenset(
        {"first_tabs", "second_tabs"}
    )
    assert first_tabs.currentIndex() == 1
    assert second_tabs.currentIndex() == 1

    # testで生成したWidgetを削除する。
    first_tabs.deleteLater()
    second_tabs.deleteLater()
    qt_application.processEvents()


def test_restore_removes_invalid_widget_state(
    qt_application,
    tmp_path,
) -> None:
    # 2タブ構成でindex 1を保存する。
    tabs = QtWidgets.QTabWidget()
    tabs.addTab(QtWidgets.QWidget(), "First")
    tabs.addTab(QtWidgets.QWidget(), "Second")
    tabs.setCurrentIndex(1)
    settings_file = tmp_path / "ui.ini"
    manager = _create_manager(settings_file)
    manager.register_tab_widget("main_tabs", tabs)
    assert manager.save()

    # タブ数を減らして保存済みindexを無効にする。
    tabs.removeTab(1)
    assert manager.restore() == frozenset()

    # 復元できなかったWidget単位の状態が削除されることを確認する。
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    assert not settings.contains(
        "windows/main/ui_state/widgets/main_tabs/state"
    )

    # testで生成したWidgetを削除する。
    tabs.deleteLater()
    qt_application.processEvents()


def test_restore_ignores_unsupported_schema(
    qt_application,
    tmp_path,
) -> None:
    # 復元されると判別できる選択タブを保存する。
    tabs = QtWidgets.QTabWidget()
    tabs.addTab(QtWidgets.QWidget(), "First")
    tabs.addTab(QtWidgets.QWidget(), "Second")
    tabs.setCurrentIndex(1)
    settings_file = tmp_path / "ui.ini"
    manager = _create_manager(settings_file)
    manager.register_tab_widget("main_tabs", tabs)
    assert manager.save()

    # INI内のschema versionを未対応の値へ変更する。
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    settings.setValue("windows/main/ui_state/schema_version", 999)
    settings.sync()
    tabs.setCurrentIndex(0)

    # 未対応schemaはWidgetへ適用されず現在値を維持することを確認する。
    assert manager.restore() == frozenset()
    assert tabs.currentIndex() == 0

    # testで生成したWidgetを削除する。
    tabs.deleteLater()
    qt_application.processEvents()


def test_clear_preserves_other_settings(tmp_path) -> None:
    # manager所有外のgeometryと任意設定を同じgroupへ用意する。
    settings_file = tmp_path / "ui.ini"
    manager = _create_manager(settings_file)
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    settings.setValue("windows/main/geometry", QtCore.QByteArray(b"geometry"))
    settings.setValue("windows/main/tool_option", True)
    settings.setValue("windows/main/ui_state/schema_version", 1)
    settings.sync()

    # UiStateManager専用groupだけを削除する。
    assert manager.clear()
    assert settings.value("windows/main/tool_option", False, bool)
    assert settings.contains("windows/main/geometry")
    assert not settings.contains("windows/main/ui_state/schema_version")


def test_registered_keys_keep_registration_order(
    qt_application,
    tmp_path,
) -> None:
    # 複数種類のWidgetを安定したkeyで順番に登録する。
    manager = _create_manager(tmp_path / "ui.ini")
    splitter = QtWidgets.QSplitter()
    tabs = QtWidgets.QTabWidget()
    manager.register_splitter("main_splitter", splitter)
    manager.register_tab_widget("main_tabs", tabs)

    # 登録状態が呼び出し順のimmutableなtupleで公開されることを確認する。
    assert manager.registered_keys == ("main_splitter", "main_tabs")

    # testで生成したWidgetを削除する。
    splitter.deleteLater()
    tabs.deleteLater()
    qt_application.processEvents()


@pytest.mark.parametrize("key", ["", "main/tabs", "main tabs", "1tabs"])
def test_register_rejects_invalid_key(
    qt_application,
    tmp_path,
    key: str,
) -> None:
    # QSettingsのgroup構造を壊す不安定なkeyを拒否する。
    manager = _create_manager(tmp_path / "ui.ini")
    tabs = QtWidgets.QTabWidget()
    with pytest.raises(ValueError):
        manager.register_tab_widget(key, tabs)

    # testで生成したWidgetを削除する。
    tabs.deleteLater()
    qt_application.processEvents()


def test_register_rejects_non_string_key(
    qt_application,
    tmp_path,
) -> None:
    # 静的型検査を迂回した文字列以外のkeyを用意する。
    manager = _create_manager(tmp_path / "ui.ini")
    tabs = QtWidgets.QTabWidget()

    # QSettingsへ変換する前に明確なTypeErrorを送出することを確認する。
    with pytest.raises(TypeError):
        manager.register_tab_widget(
            123,  # pyright: ignore[reportArgumentType]
            tabs,
        )

    # testで生成したWidgetを削除する。
    tabs.deleteLater()
    qt_application.processEvents()


def test_register_rejects_duplicate_key(
    qt_application,
    tmp_path,
) -> None:
    # 異なるWidgetへ同じstate keyを割り当てる操作を用意する。
    manager = _create_manager(tmp_path / "ui.ini")
    first_tabs = QtWidgets.QTabWidget()
    second_tabs = QtWidgets.QTabWidget()
    manager.register_tab_widget("main_tabs", first_tabs)

    # 保存対象が曖昧になる重複登録を拒否することを確認する。
    with pytest.raises(ValueError):
        manager.register_tab_widget("main_tabs", second_tabs)

    # testで生成したWidgetを削除する。
    first_tabs.deleteLater()
    second_tabs.deleteLater()
    qt_application.processEvents()
