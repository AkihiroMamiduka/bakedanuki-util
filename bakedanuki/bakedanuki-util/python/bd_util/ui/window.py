# coding: utf-8
from collections.abc import Callable
from functools import partial
from typing import Generic, TypeVar

from . import qt

WindowT = TypeVar("WindowT", bound=qt.QtWidgets.QWidget)


class WindowController(Generic[WindowT]):
    """factoryから生成した1つのWindowを表示・破棄する。"""

    def __init__(
        self,
        factory: Callable[[], WindowT],
        *,
        retain: bool = False,
    ) -> None:
        """Windowの生成方法とclose時の保持方針を設定する。

        Args:
            factory: Windowを生成する引数なしの関数。初回表示時に呼ぶ。
            retain: `True`ならclose後も同じWindowを再利用する。
        """
        self._factory = factory
        self._retain = retain
        self._window: WindowT | None = None
        self._window_token: object | None = None

    @property
    def window(self) -> WindowT | None:
        """管理中のWindowを返す。未生成・破棄済みなら`None`。"""
        return self._window

    @property
    def retain(self) -> bool:
        """close時にwindow instanceを保持するか返す。"""
        return self._retain

    def show(self) -> WindowT:
        """Windowを生成または再表示して前面へ移動する。

        Returns:
            表示したWindow。同じWindowが生存中なら再利用する。
        """
        window = self._window
        if window is None:
            window = self._factory()
            token = object()
            self._window = window
            self._window_token = token

            # Qt側のclose操作もcontrollerの保持方針に合わせる。
            window.setAttribute(
                qt.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose,
                not self._retain,
            )
            window.destroyed.connect(partial(self._on_window_destroyed, token))

        # 最小化だけを解除し、最大化などの表示状態は維持する。
        state = window.windowState()
        if state & qt.QtCore.Qt.WindowState.WindowMinimized:
            window.setWindowState(
                state & ~qt.QtCore.Qt.WindowState.WindowMinimized
            )

        window.show()
        window.raise_()
        window.activateWindow()
        return window

    def close(self) -> None:
        """Windowを閉じる。`retain=False`なら完全破棄する。"""
        window = self._window
        if window is None:
            return

        if not self._retain:
            self.dispose()
            return

        window.close()

    def dispose(self) -> None:
        """Windowを閉じて参照を外し、Qtへ削除を予約する。"""
        window = self._window
        if window is None:
            return

        # 破棄通知が遅れても次に生成したWindowを消さないよう、先に参照を外す。
        self._window = None
        self._window_token = None
        window.close()
        window.deleteLater()

    def _on_window_destroyed(
        self,
        token: object,
        _object: qt.QtCore.QObject | None = None,
    ) -> None:
        """管理対象windowの破棄通知を処理する。"""
        # 古いWindowの破棄通知は新しいWindowの状態へ反映しない。
        if token is self._window_token:
            self._window = None
            self._window_token = None
