# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, Self, cast

from maya.api import OpenMaya as om

from ...ui import UiStateManager, qt

if TYPE_CHECKING:
    from .dock.window import MayaDockableWindow


class _QTimerType(Protocol):
    """PySide stub境界で使用するQTimer classの必要最小API。"""

    @staticmethod
    def singleShot(
        milliseconds: int,
        callback: Callable[[], None],
    ) -> None:
        """指定時間後にcallbackを一度だけ呼び出す。"""
        raise NotImplementedError


class _WindowLifecycleFilter(qt.QtCore.QObject):
    """通常Windowの表示とcloseをtrackerへ通知するevent filter。"""

    def __init__(
        self,
        window: qt.QtWidgets.QWidget,
        on_shown: Callable[[], None],
        on_closed: Callable[[], None],
    ) -> None:
        """監視対象Windowとlifecycle callbackを受け取って初期化する。"""
        # trackerが所有する独立QObjectとしてWindowへevent filterを登録する。
        super().__init__()
        self._window: qt.QtWidgets.QWidget | None = window
        self._on_shown: Callable[[], None] | None = on_shown
        self._on_closed: Callable[[], None] | None = on_closed
        window.installEventFilter(self)

    def dispose(self) -> None:
        """Windowからevent filterを解除してcallback参照を破棄する。"""
        # 手動解除後に同じWindowからlifecycle通知を受けないよう接続を外す。
        window = self._window
        self._window = None
        self._on_shown = None
        self._on_closed = None
        if window is None:
            return
        try:
            window.removeEventFilter(self)
        except RuntimeError:
            # C++側で既に破棄されたWindowは解除済みとして扱う。
            pass

    def eventFilter(
        self,
        watched: qt.QtCore.QObject,
        event: qt.QtCore.QEvent,
    ) -> bool:
        """通常WindowのShowとClose eventをcallbackへ変換する。"""
        # 監視対象Windowへ届いたlifecycle eventだけをtrackerへ通知する。
        if watched is self._window:
            if event.type() == qt.QtCore.QEvent.Type.Show:
                on_shown = self._on_shown
                if on_shown is not None:
                    on_shown()
            elif event.type() == qt.QtCore.QEvent.Type.Close:
                on_closed = self._on_closed
                if on_closed is not None:
                    on_closed()

        # Window標準のevent処理は止めず、未処理としてQtへ返す。
        return False


def _add_maya_exiting_callback(callback: Callable[..., None]) -> int:
    """Maya終了直前に呼ばれるcallbackを登録する。"""
    # Qt Widgetが破棄される前に保存できるMaya固有の通知を使用する。
    return int(
        om.MSceneMessage.addCallback(
            om.MSceneMessage.kMayaExiting,
            callback,
        )
    )


def _remove_callback(callback_id: int) -> None:
    """登録済みMaya callbackを解除する。"""
    # toolの完全破棄やmodule reload後に古いcallbackを残さない。
    om.MMessage.removeCallback(callback_id)


def _restore_later(callback: Callable[[], None]) -> None:
    """次のQt event loopでUI state復元処理を呼び出す。"""
    # Window表示またはworkspaceControl接続後のlayout計算を待つ。
    timer_type = cast(_QTimerType, qt.QtCore.QTimer)
    timer_type.singleShot(0, callback)


class MayaUiStateTracker:
    """MayaでのUI state復元・終了前保存とcallbackの寿命を管理する。"""

    def __init__(
        self,
        manager: UiStateManager,
        owner: qt.QtCore.QObject,
    ) -> None:
        """保存処理とcallbackの所有者を受け取って監視を開始する。"""
        # owner破棄時にcallbackを解除できるよう参照とIDを保持する。
        self._manager = manager
        self._owner: qt.QtCore.QObject | None = owner
        self._dockable_window: MayaDockableWindow | None = None
        self._window_lifecycle_filter: _WindowLifecycleFilter | None = None
        self._window_closed = False
        self._callback_id: int | None = None
        self._restore_requested = False
        owner.destroyed.connect(self._on_owner_destroyed)
        self._callback_id = _add_maya_exiting_callback(self._on_maya_exiting)

    @classmethod
    def for_window(
        cls,
        manager: UiStateManager,
        window: qt.QtWidgets.QWidget,
    ) -> Self:
        """通常Windowのlifecycleへ接続したtrackerを生成する。"""
        # Show後の復元とClose前の保存をQt event filterで自動化する。
        tracker = cls(manager, window)
        tracker._window_lifecycle_filter = _WindowLifecycleFilter(
            window,
            tracker._on_window_shown,
            tracker._on_window_closed,
        )
        return tracker

    @classmethod
    def for_dockable(
        cls,
        manager: UiStateManager,
        window: MayaDockableWindow,
    ) -> Self:
        """dockable Windowのlifecycleへ接続したtrackerを生成する。"""
        # trackerを生成してからdock固有signalへ保存・復元処理を接続する。
        tracker = cls(manager, window)
        tracker._dockable_window = window
        window.dock_attached.connect(tracker.restore)
        window.dock_closed.connect(tracker.save)
        window.dock_about_to_dispose.connect(tracker._on_dock_about_to_dispose)
        return tracker

    @property
    def manager(self) -> UiStateManager:
        """監視対象のUiStateManagerを返す。"""
        return self._manager

    def restore(self) -> None:
        """layout接続後の次のevent loopでUI stateを一度だけ復元する。"""
        # 同じWindowの再表示で保存済み状態を繰り返し適用しない。
        if self._restore_requested or self._owner is None:
            return
        self._restore_requested = True

        # Mayaのlayout計算が完了してからWidget内部状態を反映する。
        _restore_later(self._restore_after_layout)

    def save(self) -> bool:
        """破棄前に退避したUI stateを保存する。"""
        # 終了処理中のWidget状態で退避済み状態を上書きせずに永続化する。
        return self._manager.save_cached()

    def dispose(
        self,
        _object: qt.QtCore.QObject | None = None,
    ) -> None:
        """Maya終了callbackを解除する。"""
        # 二重解除を避け、解除処理中の再入でも安全な状態へ先に変更する。
        owner = self._owner
        dockable_window = self._dockable_window
        window_lifecycle_filter = self._window_lifecycle_filter
        callback_id = self._callback_id
        self._owner = None
        self._dockable_window = None
        self._window_lifecycle_filter = None
        self._callback_id = None

        # 手動破棄後にownerの遅いdestroyed通知がPython終了処理へ入るのを防ぐ。
        if owner is not None:
            try:
                owner.destroyed.disconnect(self._on_owner_destroyed)
            except (RuntimeError, TypeError):
                pass

        # dockable連携を解除し、破棄処理後のsignalから再保存されないようにする。
        if dockable_window is not None:
            try:
                dockable_window.dock_attached.disconnect(self.restore)
            except (RuntimeError, TypeError):
                pass
            try:
                dockable_window.dock_closed.disconnect(self.save)
            except (RuntimeError, TypeError):
                pass
            try:
                dockable_window.dock_about_to_dispose.disconnect(
                    self._on_dock_about_to_dispose
                )
            except (RuntimeError, TypeError):
                pass

        # 通常Windowのevent filterを外して手動破棄後の通知を止める。
        if window_lifecycle_filter is not None:
            window_lifecycle_filter.dispose()

        if callback_id is None:
            return
        try:
            _remove_callback(callback_id)
        except RuntimeError:
            # Maya終了処理で既に解除済みのcallbackは破棄完了として扱う。
            pass

    def _on_maya_exiting(self, *_args: object) -> None:
        """Widget破棄前のMaya終了通知で状態を保存する。"""
        # 保存に失敗した場合もcallback IDを残さないよう必ず解除する。
        try:
            self.save()
        finally:
            self.dispose()

    def _on_dock_about_to_dispose(self) -> None:
        """dockable Windowの完全破棄前に状態保存とcallback解除を行う。"""
        # module reload前にも退避済み状態を残し、古いMaya callbackを破棄する。
        try:
            self.save()
        finally:
            self.dispose()

    def _on_owner_destroyed(
        self,
        _object: qt.QtCore.QObject | None = None,
    ) -> None:
        """ownerが外部から破棄された場合の後始末を行う。"""
        # 通常close後の遅延破棄ではreset後に古い状態を再保存しない。
        try:
            if self._dockable_window is not None or (
                self._window_lifecycle_filter is not None
                and not self._window_closed
            ):
                self.save()
        finally:
            self.dispose()

    def _on_window_shown(self) -> None:
        """通常Windowの表示時に状態復元を予約する。"""
        # 再表示後の外部破棄を保存対象とし、復元自体は一度だけ予約する。
        self._window_closed = False
        self.restore()

    def _on_window_closed(self) -> None:
        """通常Windowのclose前に退避済み状態を保存する。"""
        # close済みと先に記録し、直後の遅延破棄による二重保存を防ぐ。
        self._window_closed = True
        self.save()

    def _restore_after_layout(self) -> None:
        """Mayaのlayout計算後に保存済みUI stateを復元する。"""
        # 待機中にownerが破棄された場合は復元処理を実行しない。
        if self._owner is None:
            return
        self._manager.restore()
