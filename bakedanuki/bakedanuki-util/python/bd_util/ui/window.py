# coding: utf-8
from collections.abc import Callable
from functools import partial
from typing import Generic, TypeVar

from . import qt

WindowT = TypeVar("WindowT", bound=qt.QtWidgets.QWidget)


class WindowController(Generic[WindowT]):
    """factoryから生成した1つのwindowを管理する。"""

    def __init__(
        self,
        factory: Callable[[], WindowT],
        *,
        retain: bool = False,
    ) -> None:
        """factoryとclose時のinstance保持設定で初期化する。"""
        # windowの生成処理、close policy、現在の管理状態を保持する。
        self._factory = factory
        self._retain = retain
        self._window: WindowT | None = None
        self._window_token: object | None = None

    @property
    def window(self) -> WindowT | None:
        """現在管理しているwindowを返す。"""
        # windowが未生成または破棄済みの場合はNoneを返す。
        return self._window

    @property
    def retain(self) -> bool:
        """close時にwindow instanceを保持するか返す。"""
        return self._retain

    def show(self) -> WindowT:
        """必要に応じてwindowを生成し、表示して前面へ移動する。"""
        # 管理対象がない場合だけwindowを生成して破棄通知を登録する。
        window = self._window
        if window is None:
            window = self._factory()
            token = object()
            self._window = window
            self._window_token = token

            # 既定ではタイトルバーのcloseでもWindowを完全破棄する。
            window.setAttribute(
                qt.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose,
                not self._retain,
            )
            window.destroyed.connect(partial(self._on_window_destroyed, token))

        # 最小化されている場合は、他の表示状態を保ったまま解除する。
        state = window.windowState()
        if state & qt.QtCore.Qt.WindowState.WindowMinimized:
            window.setWindowState(
                state & ~qt.QtCore.Qt.WindowState.WindowMinimized
            )

        # windowを表示してユーザーが操作できる状態へ移動する。
        window.show()
        window.raise_()
        window.activateWindow()
        return window

    def close(self) -> None:
        """close policyに従って現在のwindowを閉じる。"""
        window = self._window
        if window is None:
            return

        # 破棄policyでは参照と関連resourceを即座に解放する。
        if not self._retain:
            self.dispose()
            return

        # 保持policyでは同じinstanceを再表示できる状態で閉じる。
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
        _object: qt.QtCore.QObject | None = None,
    ) -> None:
        """管理対象windowの破棄通知を処理する。"""
        # 現在管理中のwindowから届いた通知だけを状態へ反映する。
        if token is self._window_token:
            self._window = None
            self._window_token = None
