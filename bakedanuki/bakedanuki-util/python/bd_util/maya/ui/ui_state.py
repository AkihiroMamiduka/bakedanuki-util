# coding: utf-8
from collections.abc import Callable

from maya.api import OpenMaya as om

from ...ui import UiStateManager, qt


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
    # workspaceControl接続後のlayout計算を待つため0ms timerへ登録する。
    qt.QtCore.QTimer.singleShot(0, callback)


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
        self._callback_id: int | None = None
        self._restore_requested = False
        owner.destroyed.connect(self.dispose)
        self._callback_id = _add_maya_exiting_callback(self._on_maya_exiting)

    @property
    def manager(self) -> UiStateManager:
        """監視対象のUiStateManagerを返す。"""
        return self._manager

    def restore(self) -> None:
        """dock接続後の次のevent loopでUI stateを一度だけ復元する。"""
        # 同じWindowの再表示で保存済み状態を繰り返し適用しない。
        if self._restore_requested or self._owner is None:
            return
        self._restore_requested = True

        # Mayaのlayout計算が完了してからWidget内部状態を反映する。
        _restore_later(self._restore_after_attach)

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
        callback_id = self._callback_id
        self._owner = None
        self._callback_id = None

        # 手動破棄後にownerの遅いdestroyed通知がPython終了処理へ入るのを防ぐ。
        if owner is not None:
            try:
                owner.destroyed.disconnect(self.dispose)
            except (RuntimeError, TypeError):
                pass

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

    def _restore_after_attach(self) -> None:
        """Mayaのlayout接続後に保存済みUI stateを復元する。"""
        # 待機中にownerが破棄された場合は復元処理を実行しない。
        if self._owner is None:
            return
        self._manager.restore()
