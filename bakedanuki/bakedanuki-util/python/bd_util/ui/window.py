# coding: utf-8
from collections.abc import Callable
from functools import partial
from typing import Generic, TypeVar

from PySide6 import QtCore, QtWidgets

WindowT = TypeVar("WindowT", bound=QtWidgets.QWidget)


class WindowController(Generic[WindowT]):
    """factoryから生成した1つのwindowを管理する。"""

    def __init__(self, factory: Callable[[], WindowT]) -> None:
        """factoryを受け取りcontrollerを初期化する。"""
        # windowの生成処理と現在の管理状態を保持する。
        self._factory = factory
        self._window: WindowT | None = None
        self._window_token: object | None = None

    @property
    def window(self) -> WindowT | None:
        """現在管理しているwindowを返す。"""
        # windowが未生成または破棄済みの場合はNoneを返す。
        return self._window

    def show(self) -> WindowT:
        """必要に応じてwindowを生成し、表示して前面へ移動する。"""
        # 管理対象がない場合だけwindowを生成して破棄通知を登録する。
        window = self._window
        if window is None:
            window = self._factory()
            token = object()
            self._window = window
            self._window_token = token
            window.destroyed.connect(partial(self._on_window_destroyed, token))

        # 最小化されている場合は、他の表示状態を保ったまま解除する。
        state = window.windowState()
        if state & QtCore.Qt.WindowState.WindowMinimized:
            window.setWindowState(
                state & ~QtCore.Qt.WindowState.WindowMinimized
            )

        # windowを表示してユーザーが操作できる状態へ移動する。
        window.show()
        window.raise_()
        window.activateWindow()
        return window

    def close(self) -> None:
        """instanceを保持したまま現在のwindowを閉じる。"""
        # 再表示に備えて参照を残し、Qtのclose処理だけを呼び出す。
        window = self._window
        if window is not None:
            window.close()

    def dispose(self) -> None:
        """現在のwindowを閉じ、Qt event loopへ削除を予約する。"""
        # 管理対象がない場合はQtの処理を呼び出さず終了する。
        window = self._window
        if window is None:
            return

        # 遅れて届く破棄通知が次のwindowへ影響しないよう先に参照を外す。
        self._window = None
        self._window_token = None
        window.close()
        window.deleteLater()

    def _on_window_destroyed(
        self,
        token: object,
        _object: QtCore.QObject | None = None,
    ) -> None:
        """管理対象windowの破棄通知を処理する。"""
        # 現在管理中のwindowから届いた通知だけを状態へ反映する。
        if token is self._window_token:
            self._window = None
            self._window_token = None
