# coding: utf-8
from collections.abc import Callable

from maya.api import OpenMaya as om

from ...ui import qt


def _add_maya_exiting_callback(callback: Callable[..., None]) -> int:
    """Maya終了直前に呼ばれるcallbackを登録する。"""
    # Qt objectの破棄通知だけに依存せずMaya終了時にも解除できるようにする。
    return int(
        om.MSceneMessage.addCallback(
            om.MSceneMessage.kMayaExiting,
            callback,
        )
    )


def _remove_callback(callback_id: int) -> None:
    """登録済みMaya callbackを解除する。"""
    # API種別に依存しないMMessageの共通解除処理を使用する。
    om.MMessage.removeCallback(callback_id)


def _validate_callback_id(value: object) -> int:
    """値をMaya callback IDとして検証して返す。"""
    # boolを含む整数以外を拒否し、実行時にもregistryの型を維持する。
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(
            "callback_idにはMaya callback IDの整数を指定してください"
        )
    return value


class MayaCallbackRegistry(qt.QtCore.QObject):
    """Qt ownerと同じ寿命でMaya callback IDを管理する。"""

    def __init__(
        self,
        owner: qt.QtCore.QObject,
        *,
        on_maya_exiting: Callable[[], object] | None = None,
    ) -> None:
        """ownerと任意のMaya終了処理を受け取って初期化する。"""
        # QObjectの親子関係とdestroyed通知の両方でregistryの寿命をownerへ揃える。
        super().__init__(owner)
        self._owner: qt.QtCore.QObject | None = owner
        self._callback_ids: list[int] = []
        self._on_maya_exiting_callback = on_maya_exiting
        self._is_disposed = False
        self._maya_exiting_callback_id: int | None = None
        owner.destroyed.connect(self._on_owner_destroyed)

        # Maya終了時は利用側の処理後に全callbackを解除する。
        try:
            self._maya_exiting_callback_id = _add_maya_exiting_callback(
                self._on_maya_exiting
            )
        except Exception:
            self.dispose()
            raise

    @property
    def callback_ids(self) -> tuple[int, ...]:
        """現在管理している利用側callback IDを返す。"""
        # 内部のMaya終了callbackを除き、登録順のimmutableな値を公開する。
        return tuple(getattr(self, "_callback_ids", ()))

    @property
    def is_disposed(self) -> bool:
        """registryが解除済みか返す。"""
        return getattr(self, "_is_disposed", True)

    def register(self, callback_id: int) -> int:
        """Maya callback IDを管理対象へ追加して同じIDを返す。"""
        # Maya APIから返された整数IDだけを受け付ける。
        callback_id = _validate_callback_id(callback_id)
        if self._is_disposed:
            raise RuntimeError("破棄済みMayaCallbackRegistryへ登録できません")
        if callback_id in self._callback_ids:
            raise ValueError(
                f"callback IDは既に登録されています: {callback_id}"
            )

        self._callback_ids.append(callback_id)
        return callback_id

    def remove(self, callback_id: int) -> bool:
        """指定callbackを解除し、管理対象だったか返す。"""
        # 未登録IDはMayaへ渡さず何もしない。
        callback_id = _validate_callback_id(callback_id)
        if callback_id not in self._callback_ids:
            return False
        self._callback_ids.remove(callback_id)
        self._remove_safely(callback_id)
        return True

    def dispose(
        self,
        _object: qt.QtCore.QObject | None = None,
    ) -> None:
        """管理中のMaya callbackをすべて解除する。"""
        # 再入と二重解除を防ぐため、Maya APIを呼ぶ前に破棄済みへ変更する。
        if getattr(self, "_is_disposed", True):
            return
        self._is_disposed = True
        owner = self._owner
        callback_ids = tuple(reversed(self._callback_ids))
        maya_exiting_callback_id = self._maya_exiting_callback_id
        self._owner = None
        self._callback_ids.clear()
        self._maya_exiting_callback_id = None
        self._on_maya_exiting_callback = None

        # 手動dispose後にownerの遅いdestroyed通知から再度呼ばれないようにする。
        if owner is not None:
            try:
                owner.destroyed.disconnect(self._on_owner_destroyed)
            except (RuntimeError, TypeError):
                pass

        # 利用側callbackを登録と逆順に解除し、最後に終了callbackを解除する。
        for callback_id in callback_ids:
            self._remove_safely(callback_id)
        if maya_exiting_callback_id is not None:
            self._remove_safely(maya_exiting_callback_id)

    def _remove_safely(self, callback_id: int) -> None:
        """Maya側で解除済みのcallbackを許容して解除する。"""
        try:
            _remove_callback(callback_id)
        except RuntimeError:
            # Maya終了処理や外部処理で解除済みの場合も管理上は解除完了とする。
            pass

    def _on_maya_exiting(self, *_args: object) -> None:
        """利用側の終了処理後にregistryを破棄する。"""
        callback = self._on_maya_exiting_callback
        try:
            if callback is not None:
                callback()
        finally:
            self.dispose()

    @qt.Slot()
    def _on_owner_destroyed(self) -> None:
        """ownerの外部破棄時にregistryを破棄する。"""
        self.dispose()


def dispose_owned_callbacks(owner: qt.QtCore.QObject) -> int:
    """owner直下のMaya callback registryをすべて破棄する。"""
    disposed_count = 0

    # controllerの完全破棄時はDeferredDeleteを待たずcallbackを解除する。
    for child in tuple(owner.children()):
        if not isinstance(child, MayaCallbackRegistry) or child.is_disposed:
            continue
        child.dispose()
        disposed_count += 1
    return disposed_count
