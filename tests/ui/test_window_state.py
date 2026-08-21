# coding: utf-8
from pathlib import Path

from PySide6 import QtCore, QtWidgets

from bd_util.ui import (
    SettingsPath,
    WindowStateStore,
    WindowStateTracker,
    ensure_window_on_screen,
)
from bd_util.ui import window_state


class _Screen:
    """available geometryだけを持つtest用screen。"""

    def __init__(self, available_geometry: QtCore.QRect) -> None:
        """固定のavailable geometryを保持する。"""
        self._available_geometry = available_geometry

    def availableGeometry(self) -> QtCore.QRect:
        """test用の利用可能領域を返す。"""
        return QtCore.QRect(self._available_geometry)


def _replace_screens(
    monkeypatch,
    *available_geometries: QtCore.QRect,
) -> None:
    """Window配置処理が参照するscreenをtest用実装へ置き換える。"""
    # 実際のモニター構成に依存しない固定screenを生成する。
    screens = tuple(_Screen(geometry) for geometry in available_geometries)
    monkeypatch.setattr(window_state, "_get_screens", lambda: screens)
    monkeypatch.setattr(
        window_state,
        "_get_primary_screen",
        lambda: None if not screens else screens[0],
    )


def _create_store(settings_file: Path) -> WindowStateStore:
    """test用INIファイルを使用するWindowStateStoreを生成する。"""
    # NativeFormatに依存しないQSettingsを一時directoryへ作成する。
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    return WindowStateStore(
        settings,
        SettingsPath("test_tool/windows/main"),
    )


def test_store_restores_dialog_geometry(qt_application, tmp_path) -> None:
    # 保存元dialogへ位置とサイズを設定する。
    store = _create_store(tmp_path / "ui.ini")
    source = QtWidgets.QDialog()
    source.setGeometry(120, 140, 420, 260)
    expected_geometry = source.geometry()

    # geometryをINIファイルへ保存する。
    assert store.save(source)

    # 異なる初期geometryを持つdialogへ保存値を復元する。
    restored = QtWidgets.QDialog()
    restored.setGeometry(10, 20, 100, 80)
    assert store.restore(restored)

    # 位置とサイズが保存元と一致することを確認する。
    assert restored.geometry() == expected_geometry

    # testで生成したwidgetを削除する。
    source.deleteLater()
    restored.deleteLater()
    qt_application.processEvents()


def test_store_checks_screen_after_geometry_restore(
    qt_application,
    monkeypatch,
    tmp_path,
) -> None:
    # 復元可能なgeometryと補正対象Windowの記録先を用意する。
    store = _create_store(tmp_path / "ui.ini")
    source = QtWidgets.QDialog()
    source.setGeometry(120, 140, 420, 260)
    assert store.save(source)
    checked_windows: list[QtWidgets.QWidget] = []

    def record_window(window: QtWidgets.QWidget) -> bool:
        """screen確認対象のWindowを記録する。"""
        checked_windows.append(window)
        return False

    monkeypatch.setattr(
        window_state,
        "ensure_window_on_screen",
        record_window,
    )

    # restoreGeometry成功後に現在のscreen構成を必ず確認する。
    restored = QtWidgets.QDialog()
    assert store.restore(restored)
    assert checked_windows == [restored]

    # testで生成したWindowを削除する。
    source.deleteLater()
    restored.deleteLater()
    qt_application.processEvents()


def test_ensure_window_on_screen_keeps_accessible_geometry(
    qt_application,
    monkeypatch,
) -> None:
    # タイトル領域を十分に表示できる仮想screenとWindowを用意する。
    _replace_screens(monkeypatch, QtCore.QRect(0, 0, 1000, 700))
    window = QtWidgets.QDialog()
    window.setGeometry(930, 100, 400, 300)
    expected_geometry = window.geometry()

    # タイトルの必要幅が見えているWindowは意図した配置を維持する。
    assert not ensure_window_on_screen(window)
    assert window.geometry() == expected_geometry

    # testで生成したWindowを削除する。
    window.deleteLater()
    qt_application.processEvents()


def test_ensure_window_on_screen_centers_offscreen_window(
    qt_application,
    monkeypatch,
) -> None:
    # 現在のscreenから完全に外れたWindowを再現する。
    _replace_screens(monkeypatch, QtCore.QRect(0, 0, 1000, 700))
    window = QtWidgets.QDialog()
    window.setGeometry(2200, 1200, 400, 300)

    # primary screenの中央へ元のサイズを維持して配置する。
    assert ensure_window_on_screen(window)
    assert window.geometry() == QtCore.QRect(300, 200, 400, 300)

    # testで生成したWindowを削除する。
    window.deleteLater()
    qt_application.processEvents()


def test_ensure_window_on_screen_fits_oversized_window(
    qt_application,
    monkeypatch,
) -> None:
    # 切断済みの大型screenにあったWindowを小さいscreenへ戻す。
    _replace_screens(monkeypatch, QtCore.QRect(0, 0, 1000, 700))
    window = QtWidgets.QDialog()
    window.setGeometry(2200, 1200, 1400, 900)

    # available geometryを超える幅と高さを縮めて全体を表示する。
    assert ensure_window_on_screen(window)
    assert window.geometry() == QtCore.QRect(0, 0, 1000, 700)

    # testで生成したWindowを削除する。
    window.deleteLater()
    qt_application.processEvents()


def test_ensure_window_on_screen_uses_largest_overlap(
    qt_application,
    monkeypatch,
) -> None:
    # タイトルだけが上へ外れ、右screenと大きく重なるWindowを用意する。
    _replace_screens(
        monkeypatch,
        QtCore.QRect(0, 0, 1000, 700),
        QtCore.QRect(1000, 0, 1000, 700),
    )
    window = QtWidgets.QDialog()
    window.setGeometry(1200, -100, 400, 500)

    # 現在のWindowと最も広く重なる右screenの中央へ配置する。
    assert ensure_window_on_screen(window)
    assert window.geometry() == QtCore.QRect(1300, 100, 400, 500)

    # testで生成したWindowを削除する。
    window.deleteLater()
    qt_application.processEvents()


def test_tracker_saves_geometry_on_close(qt_application, tmp_path) -> None:
    # trackerを取り付けたdialogを表示してgeometryを変更する。
    settings_file = tmp_path / "ui.ini"
    store = _create_store(settings_file)
    window = QtWidgets.QDialog()
    tracker = WindowStateTracker(window, store)
    window.show()
    window.setGeometry(80, 90, 360, 240)

    # title barやcontrollerと同じclose eventを発生させる。
    window.close()
    qt_application.processEvents()

    # 新しいdialogへclose時点のgeometryが復元されることを確認する。
    restored = QtWidgets.QDialog()
    restored_tracker = WindowStateTracker(restored, store)
    assert restored_tracker.restore_succeeded
    assert restored.geometry() == window.geometry()

    # trackerをtest終了まで保持し、生成したwidgetを削除する。
    assert tracker.parent() is window
    window.deleteLater()
    restored.deleteLater()
    qt_application.processEvents()


def test_store_restores_main_window_state(qt_application, tmp_path) -> None:
    # 保存元QMainWindowのdockを左側へ配置する。
    store = _create_store(tmp_path / "ui.ini")
    source = QtWidgets.QMainWindow()
    source_dock = QtWidgets.QDockWidget("Source", source)
    source_dock.setObjectName("testDock")
    source.addDockWidget(
        QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
        source_dock,
    )
    assert store.save(source)

    # 復元先では同じobjectNameのdockを異なる場所へ配置する。
    restored = QtWidgets.QMainWindow()
    restored_dock = QtWidgets.QDockWidget("Restored", restored)
    restored_dock.setObjectName("testDock")
    restored.addDockWidget(
        QtCore.Qt.DockWidgetArea.RightDockWidgetArea,
        restored_dock,
    )

    # geometryと分離されたwindow stateによってdock位置を復元する。
    assert store.restore(restored)
    assert (
        restored.dockWidgetArea(restored_dock)
        == QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
    )

    # testで生成したwidgetを削除する。
    source.deleteLater()
    restored.deleteLater()
    qt_application.processEvents()


def test_store_removes_invalid_geometry(qt_application, tmp_path) -> None:
    # 復元に失敗するgeometryをwindow groupへ書き込む。
    settings_file = tmp_path / "ui.ini"
    settings_path = SettingsPath("test_tool/windows/main")
    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    settings.beginGroup(settings_path.group_path)
    settings.setValue("schema_version", WindowStateStore.SCHEMA_VERSION)
    settings.setValue("geometry", QtCore.QByteArray(b"invalid"))
    settings.endGroup()
    settings.sync()

    # 壊れたgeometryを適用せず初期状態を維持する。
    store = WindowStateStore(settings, settings_path)
    window = QtWidgets.QDialog()
    initial_geometry = window.geometry()
    assert not store.restore(window)
    assert window.geometry() == initial_geometry

    # 次回起動時に再試行しないよう壊れた値が削除されたことを確認する。
    settings.beginGroup(settings_path.group_path)
    assert not settings.contains("geometry")
    settings.endGroup()

    # testで生成したwidgetを削除する。
    window.deleteLater()
    qt_application.processEvents()


def test_store_clear_preserves_unmanaged_values(
    qt_application,
    tmp_path,
) -> None:
    # window groupへ管理対象外の将来設定を追加する。
    settings_file = tmp_path / "ui.ini"
    store = _create_store(settings_file)
    window = QtWidgets.QDialog()
    assert store.save(window)

    settings = QtCore.QSettings(
        str(settings_file),
        QtCore.QSettings.Format.IniFormat,
    )
    settings.beginGroup(store.settings_path.group_path)
    settings.setValue("selected_tab", 2)
    settings.endGroup()
    settings.sync()

    # stateをclearしても他の設定値が残ることを確認する。
    assert store.clear()
    settings.beginGroup(store.settings_path.group_path)
    assert not settings.contains("geometry")
    assert not settings.contains("window_state")
    assert settings.value("selected_tab", -1, int) == 2
    settings.endGroup()

    # testで生成したwidgetを削除する。
    window.deleteLater()
    qt_application.processEvents()
