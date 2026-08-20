# coding: utf-8
from typing import ClassVar

from .settings_path import SettingsPath
from . import qt


class WindowStateStore:
    """QSettingsへwindowのgeometryとstateを保存する。"""

    SCHEMA_VERSION: ClassVar[int] = 1
    WINDOW_STATE_VERSION: ClassVar[int] = 1
    _SCHEMA_VERSION_KEY: ClassVar[str] = "schema_version"
    _GEOMETRY_KEY: ClassVar[str] = "geometry"
    _WINDOW_STATE_KEY: ClassVar[str] = "window_state"

    def __init__(
        self,
        settings: qt.QtCore.QSettings,
        settings_path: SettingsPath,
    ) -> None:
        """保存先QSettingsとsettings pathを受け取って初期化する。"""
        # QSettings instanceとtool内の保存groupを保持する。
        self._settings = settings
        self._settings_path = settings_path

    @property
    def settings_path(self) -> SettingsPath:
        """window stateの保存先を表すsettings pathを返す。"""
        # 初期化時に検証済みのSettingsPathをそのまま公開する。
        return self._settings_path

    @property
    def file_name(self) -> str:
        """QSettingsが使用するファイル名を返す。"""
        # 実際にQSettingsが解決した保存先を取得する。
        return self._settings.fileName()

    def save(self, window: qt.QtWidgets.QWidget) -> bool:
        """windowのgeometryと対応するstateを保存する。"""
        # window単位のgroupへschema versionとgeometryを保存する。
        self._settings.beginGroup(self._settings_path.group_path)
        try:
            self._settings.setValue(
                self._SCHEMA_VERSION_KEY,
                self.SCHEMA_VERSION,
            )
            self._settings.setValue(
                self._GEOMETRY_KEY,
                window.saveGeometry(),
            )

            # QMainWindowの場合だけdockやtoolbarのstateも保存する。
            if isinstance(window, qt.QtWidgets.QMainWindow):
                self._settings.setValue(
                    self._WINDOW_STATE_KEY,
                    window.saveState(self.WINDOW_STATE_VERSION),
                )
            else:
                self._settings.remove(self._WINDOW_STATE_KEY)
        finally:
            self._settings.endGroup()

        # Maya終了前にも反映されるよう変更内容を即座に同期する。
        self._settings.sync()
        return self._settings.status() == qt.QtCore.QSettings.Status.NoError

    def restore(self, window: qt.QtWidgets.QWidget) -> bool:
        """保存済みのgeometryと対応するstateをwindowへ復元する。"""
        # window単位のgroupから保存値をまとめて読み取る。
        self._settings.beginGroup(self._settings_path.group_path)
        try:
            schema_version = self._settings.value(
                self._SCHEMA_VERSION_KEY,
                self.SCHEMA_VERSION,
                int,
            )
            geometry = self._settings.value(
                self._GEOMETRY_KEY,
                qt.QtCore.QByteArray(),
                qt.QtCore.QByteArray,
            )
            window_state = self._settings.value(
                self._WINDOW_STATE_KEY,
                qt.QtCore.QByteArray(),
                qt.QtCore.QByteArray,
            )
        finally:
            self._settings.endGroup()

        # 未対応schemaの値はwindowへ適用せず初期状態を維持する。
        if schema_version != self.SCHEMA_VERSION:
            return False

        # 有効なgeometryがある場合だけwindowへ復元する。
        geometry_restored = False
        if (
            isinstance(geometry, qt.QtCore.QByteArray)
            and not geometry.isEmpty()
        ):
            geometry_restored = window.restoreGeometry(geometry)
            if not geometry_restored:
                self._remove_value(self._GEOMETRY_KEY)

        # QMainWindowにはgeometryと分離してdockやtoolbarも復元する。
        if (
            isinstance(window, qt.QtWidgets.QMainWindow)
            and isinstance(window_state, qt.QtCore.QByteArray)
            and not window_state.isEmpty()
            and not window.restoreState(
                window_state,
                self.WINDOW_STATE_VERSION,
            )
        ):
            self._remove_value(self._WINDOW_STATE_KEY)

        return geometry_restored

    def clear(self) -> bool:
        """管理対象windowのgeometryとstateを削除する。"""
        # 将来追加される他の設定を残し、管理対象keyだけを削除する。
        self._settings.beginGroup(self._settings_path.group_path)
        try:
            self._settings.remove(self._SCHEMA_VERSION_KEY)
            self._settings.remove(self._GEOMETRY_KEY)
            self._settings.remove(self._WINDOW_STATE_KEY)
        finally:
            self._settings.endGroup()

        # 削除結果をファイルへ反映して成否を返す。
        self._settings.sync()
        return self._settings.status() == qt.QtCore.QSettings.Status.NoError

    def _remove_value(self, key: str) -> None:
        """復元できなかった1つの保存値を削除する。"""
        # 壊れた値を次回起動時に繰り返し読み込まないよう削除する。
        self._settings.beginGroup(self._settings_path.group_path)
        try:
            self._settings.remove(key)
        finally:
            self._settings.endGroup()
        self._settings.sync()


class WindowStateTracker(qt.QtCore.QObject):
    """windowの生成とcloseに合わせてstateを復元・保存する。"""

    def __init__(
        self,
        window: qt.QtWidgets.QWidget,
        store: WindowStateStore,
    ) -> None:
        """監視対象windowと保存処理を受け取って初期化する。"""
        # trackerをwindowのchildにして同じlifecycleで管理する。
        super().__init__(window)
        self._window = window
        self._store = store

        # close eventを監視し、最初の表示前に保存済みstateを復元する。
        window.installEventFilter(self)
        self._restore_succeeded = store.restore(window)

    @property
    def restore_succeeded(self) -> bool:
        """geometryの復元に成功したか返す。"""
        # 初期化時に実行したrestoreの結果を公開する。
        return self._restore_succeeded

    def save(self) -> bool:
        """現在のwindow stateを保存する。"""
        # 明示保存でもclose eventと同じstoreを使用する。
        return self._store.save(self._window)

    def eventFilter(
        self,
        watched: qt.QtCore.QObject,
        event: qt.QtCore.QEvent,
    ) -> bool:
        """監視対象windowのclose eventでstateを保存する。"""
        # タイトルバーやcontroller経由のcloseを同じ経路で処理する。
        if (
            watched is self._window
            and event.type() == qt.QtCore.QEvent.Type.Close
        ):
            self.save()

        # 保存対象以外のeventはQt標準の処理へ渡す。
        return super().eventFilter(watched, event)
