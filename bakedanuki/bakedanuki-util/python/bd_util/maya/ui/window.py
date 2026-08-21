# coding: utf-8
from collections.abc import Callable
from typing import TypeVar

from ...logger import get_logger
from ...ui import SettingsPath, WindowController, WindowStateTracker, qt
from .callback import dispose_owned_callbacks
from .main_window import get_main_window
from .settings import create_window_state_store

WindowT = TypeVar("WindowT", bound=qt.QtWidgets.QWidget)
logger = get_logger(__name__)


class MayaWindowController(WindowController[WindowT]):
    """Maya main windowをfactoryへ渡して1つのwindowを管理する。"""

    def __init__(
        self,
        factory: Callable[[qt.QtWidgets.QWidget | None], WindowT],
        *,
        settings_path: str | SettingsPath | None = None,
    ) -> None:
        """Maya main windowを受け取るfactoryで初期化する。"""
        # window生成時までMaya main windowとsettingsの取得を遅延する。
        self._maya_factory = factory
        self._settings_path = (
            None
            if settings_path is None
            else SettingsPath.from_value(settings_path)
        )
        self._state_tracker: WindowStateTracker | None = None
        super().__init__(self._create_window)

    @property
    def settings_path(self) -> SettingsPath | None:
        """window stateの保存先を返す。"""
        # 永続化が無効な場合はNoneを返す。
        return self._settings_path

    def _create_window(self) -> WindowT:
        """現在のMaya main windowを親としてwindowを生成する。"""
        # 生成のたびに最新のMaya main windowをfactoryへ渡す。
        window = self._maya_factory(get_main_window())

        # settings pathが指定されたwindowだけstateの復元と保存を有効にする。
        if self._settings_path is not None:
            try:
                store = create_window_state_store(self._settings_path)
            except (OSError, RuntimeError) as error:
                logger.warning(
                    "UI settingsを初期化できませんでした: %s",
                    error,
                )
            else:
                self._state_tracker = WindowStateTracker(window, store)

        return window

    def dispose(self) -> None:
        """Maya callbackを解除して現在のwindowを完全破棄する。"""
        # DeferredDeleteを待たず、Windowが所有するcallbackを先に解除する。
        window = self.window
        if window is not None and qt.isValid(window):
            dispose_owned_callbacks(window)
        super().dispose()
