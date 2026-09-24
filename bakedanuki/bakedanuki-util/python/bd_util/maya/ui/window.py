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
    """Maya main windowを親にして通常Windowを管理する。"""

    def __init__(
        self,
        factory: Callable[[qt.QtWidgets.QWidget | None], WindowT],
        *,
        settings_path: str | SettingsPath | None = None,
        retain: bool = False,
    ) -> None:
        """生成方法とWindow状態の保存先を設定する。

        Args:
            factory: Maya main windowを受け取りWindowを作る関数。
            settings_path: geometryの保存先。`None`なら自動保存しない。
            retain: `True`ならclose後も同じWindowを再利用する。
        """
        # Maya main windowと設定ファイルは、Windowの生成時に取得する。
        self._maya_factory = factory
        self._settings_path = (
            None
            if settings_path is None
            else SettingsPath.from_value(settings_path)
        )
        self._state_tracker: WindowStateTracker | None = None
        super().__init__(self._create_window, retain=retain)

    @property
    def settings_path(self) -> SettingsPath | None:
        """Window状態の保存先を返す。自動保存しない場合は`None`。"""
        return self._settings_path

    def _create_window(self) -> WindowT:
        """現在のMaya main windowを親としてwindowを生成する。"""
        # Maya側のWindowが再生成されても最新の親を渡す。
        window = self._maya_factory(get_main_window())

        # 設定ファイルの利用に失敗してもWindowの表示自体は継続する。
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
        """Maya callbackを直ちに解除してWindowを完全破棄する。"""
        # DeferredDeleteを待たず、Windowが所有するcallbackを先に解除する。
        window = self.window
        if window is not None and qt.isValid(window):
            dispose_owned_callbacks(window)
        super().dispose()
