# coding: utf-8
from typing import ClassVar, Protocol

from .settings_path import SettingsPath
from . import qt

_MINIMUM_ACCESSIBLE_TITLE_WIDTH = 64
_MINIMUM_ACCESSIBLE_TITLE_HEIGHT = 32


class _ScreenLike(Protocol):
    """Window配置補正で使用するscreenの必要最小API。"""

    def availableGeometry(self) -> qt.QtCore.QRect:
        """利用可能なscreen領域を返す。"""
        raise NotImplementedError


def _get_screens() -> tuple[_ScreenLike, ...]:
    """現在のQt applicationで利用可能なscreenを返す。"""
    # QApplication未生成の環境では画面補正を行わない。
    application = qt.QtGui.QGuiApplication.instance()
    if not isinstance(application, qt.QtGui.QGuiApplication):
        return ()
    return tuple(application.screens())


def _get_primary_screen() -> _ScreenLike | None:
    """現在のQt applicationのprimary screenを返す。"""
    # applicationまたはprimary screenがないbatch環境ではNoneを返す。
    application = qt.QtGui.QGuiApplication.instance()
    if not isinstance(application, qt.QtGui.QGuiApplication):
        return None
    return application.primaryScreen()


def _intersection_area(
    first: qt.QtCore.QRect,
    second: qt.QtCore.QRect,
) -> int:
    """2つの矩形が重なる面積を返す。"""
    # QRectの空矩形を0としてscreen選択用の比較値へ変換する。
    intersection = first.intersected(second)
    return max(0, intersection.width()) * max(0, intersection.height())


def _has_accessible_title(
    frame_geometry: qt.QtCore.QRect,
    screens: tuple[_ScreenLike, ...],
) -> bool:
    """Windowのタイトル領域がいずれかのscreenで操作可能か返す。"""
    # 小さいWindowでは実寸を上限とし、左上のタイトル領域を判定する。
    accessible_width = min(
        _MINIMUM_ACCESSIBLE_TITLE_WIDTH,
        max(1, frame_geometry.width()),
    )
    accessible_height = min(
        _MINIMUM_ACCESSIBLE_TITLE_HEIGHT,
        max(1, frame_geometry.height()),
    )
    title_geometry = qt.QtCore.QRect(
        frame_geometry.x(),
        frame_geometry.y(),
        max(1, frame_geometry.width()),
        accessible_height,
    )

    # 1つのscreen内で操作に必要な幅と高さが見えている場合は補正しない。
    for screen in screens:
        visible_title = title_geometry.intersected(screen.availableGeometry())
        if (
            visible_title.width() >= accessible_width
            and visible_title.height() >= accessible_height
        ):
            return True
    return False


def _select_target_screen(
    window: qt.QtWidgets.QWidget,
    frame_geometry: qt.QtCore.QRect,
    screens: tuple[_ScreenLike, ...],
) -> _ScreenLike:
    """画面外Windowの補正先screenを選択する。"""
    # 現在のWindowと最も広く重なるscreenを優先する。
    screen_areas = tuple(
        (
            _intersection_area(
                frame_geometry,
                screen.availableGeometry(),
            ),
            screen,
        )
        for screen in screens
    )
    largest_area, overlapping_screen = max(
        screen_areas,
        key=lambda item: item[0],
    )
    if largest_area > 0:
        return overlapping_screen

    # 完全な画面外では親Window、割り当て済み画面、primaryの順に選ぶ。
    parent = window.parent()
    candidate_screens = (
        parent.screen() if isinstance(parent, qt.QtWidgets.QWidget) else None,
        window.screen(),
        _get_primary_screen(),
    )
    for candidate in candidate_screens:
        if candidate is not None and candidate in screens:
            return candidate
    return screens[0]


def ensure_window_on_screen(window: qt.QtWidgets.QWidget) -> bool:
    """Windowのタイトル領域を現在のscreenへ収め、補正したか返す。"""
    # screenを取得できないbatch環境と既に操作可能なWindowは変更しない。
    screens = _get_screens()
    frame_geometry = window.frameGeometry()
    if not screens or _has_accessible_title(frame_geometry, screens):
        return False

    # 補正先のavailable geometryへ収まるサイズを求める。
    target_screen = _select_target_screen(window, frame_geometry, screens)
    available_geometry = target_screen.availableGeometry()
    if available_geometry.isEmpty():
        return False

    current_geometry = window.geometry()
    corrected_width = min(
        max(1, current_geometry.width()),
        available_geometry.width(),
    )
    corrected_height = min(
        max(1, current_geometry.height()),
        available_geometry.height(),
    )

    # 元のサイズを可能な限り維持し、選択したscreenの中央へ配置する。
    corrected_geometry = qt.QtCore.QRect(
        available_geometry.x()
        + (available_geometry.width() - corrected_width) // 2,
        available_geometry.y()
        + (available_geometry.height() - corrected_height) // 2,
        corrected_width,
        corrected_height,
    )
    window.setGeometry(corrected_geometry)
    return window.geometry() != current_geometry


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
            else:
                # モニター構成変更後もタイトル領域を操作可能な画面へ収める。
                ensure_window_on_screen(window)

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
