# coding: utf-8
"""値通知を同期せず、入力対象の削除履歴と復旧前の生存だけを確認する。"""

from __future__ import annotations

from collections.abc import Callable, Generator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import Protocol, cast

from maya.api import OpenMaya as om

from ....ui import qt
from ..._identity import ObjectIdentityIndex
from ..callback import MayaCallbackRegistry


class LifetimeTarget(Protocol):
    """値型に依存せず、属性と祖先の削除履歴を保持する対象。"""

    plug: om.MPlug
    watched: list[om.MPlug]
    removed: bool


class _Write(Protocol):
    """値の検証・適用・復旧だけを共有する書込み契約。"""

    def validate(self) -> None:
        """書込み条件を検証する。"""
        raise NotImplementedError

    def apply(self) -> None:
        """差分を適用する。"""
        raise NotImplementedError

    def restore(self) -> None:
        """適用前の状態へ復旧する。"""
        raise NotImplementedError


@dataclass
class _NodeLifetime:
    """同じnode世代の購読対象と、解除するcallbackを保持する。"""

    identity: int
    targets: dict[int, list[LifetimeTarget]] = field(
        default_factory=dict[int, list[LifetimeTarget]]
    )
    callback_ids: list[int] = field(default_factory=list[int])
    retired: bool = False


class _LifetimePool:
    """一緒に作成したBindingの間だけ、nodeの削除通知を共有する。"""

    def __init__(self) -> None:
        """書込み中のBinding破棄から独立した共有ownerを用意する。"""
        self._owner = qt.QObject()
        self._registry = MayaCallbackRegistry(self._owner)
        self._indices = ObjectIdentityIndex()
        self._nodes: dict[int, _NodeLifetime] = {}
        self._leases = 0
        self._accepting = True

    def acquire(self) -> None:
        """生成範囲が開いている間だけ、新しい購読を受け付ける。"""
        if not self._accepting or self._registry.is_disposed:
            raise RuntimeError("終了した削除監視へ登録できません")
        self._leases += 1

    def add(self, lease: int, target: LifetimeTarget) -> _NodeLifetime:
        """初期読取り前に登録し、削除済みnodeの旧世代を再利用しない。"""
        identity = self._indices.index(target.plug.node())
        observer = self._nodes.get(identity)
        if observer is None or observer.retired:
            observer = _NodeLifetime(identity)
            self._nodes[identity] = observer
            try:
                observer.callback_ids.append(
                    self._registry.register(
                        int(
                            om.MNodeMessage.addAttributeChangedCallback(
                                target.plug.node(),
                                self._on_attribute_changed,
                                observer,
                            )
                        )
                    )
                )
                observer.callback_ids.append(
                    self._registry.register(
                        int(
                            om.MNodeMessage.addNodePreRemovalCallback(
                                target.plug.node(),
                                self._on_node_removed,
                                observer,
                            )
                        )
                    )
                )
            except Exception:
                self._nodes.pop(identity, None)
                self._registry.remove_many(observer.callback_ids)
                raise
        observer.targets.setdefault(lease, []).append(target)
        return observer

    @staticmethod
    def _on_attribute_changed(
        message: int, plug: om.MPlug, _other: om.MPlug, data: object
    ) -> None:
        """通常の値通知は処理せず、対象または祖先の削除だけを記録する。"""
        if not message & om.MNodeMessage.kAttributeRemoved:
            return
        observer = cast(_NodeLifetime, data)
        for targets in observer.targets.values():
            for target in targets:
                if not target.removed and any(
                    plug == watched for watched in target.watched
                ):
                    target.removed = True

    @staticmethod
    def _on_node_removed(_node: om.MObject, data: object) -> None:
        """削除前の同じnodeに属する全対象を恒久的に無効化する。"""
        observer = cast(_NodeLifetime, data)
        observer.retired = True
        for targets in observer.targets.values():
            for target in targets:
                target.removed = True

    def release(
        self, lease: int, observers: tuple[_NodeLifetime, ...]
    ) -> None:
        """購読者自身の対象を外し、最後の購読が去った監視だけを解除する。"""
        self._leases -= 1
        if not self._leases:
            if self._accepting:
                self._registry.remove_many(self._registry.callback_ids)
                self._nodes.clear()
                self._indices = ObjectIdentityIndex()
            else:
                self._close()
            return
        callback_ids: list[int] = []
        for observer in observers:
            observer.targets.pop(lease, None)
            if not observer.targets:
                if self._nodes.get(observer.identity) is observer:
                    self._nodes.pop(observer.identity)
                callback_ids.extend(observer.callback_ids)
        self._registry.remove_many(callback_ids)

    def seal(self) -> None:
        """新規購読を終了し、生成されなかった範囲も即座に解放する。"""
        self._accepting = False
        if not self._leases:
            self._close()

    def _close(self) -> None:
        """全IDを一括解除し、対象の削除履歴は各Bindingへ残す。"""
        self._accepting = False
        try:
            self._registry.dispose()
        finally:
            self._nodes.clear()
            self._indices = ObjectIdentityIndex()
            if qt.isValid(self._owner):
                self._owner.deleteLater()


_CURRENT_POOL: ContextVar[_LifetimePool | None] = ContextVar(
    "plugs_lifetime_pool", default=None
)


@contextmanager
def shared_plugs_lifetime() -> Generator[None, None, None]:
    """範囲内で生成する複数Bindingの削除監視をnodeごとに共有する。

    `monitor_lifetime=True`のBindingだけが参加する。範囲を抜けても既存の
    購読は維持し、各Bindingの`dispose()`と書込み・復旧の終了後に解除する。
    入れ子の範囲は独立し、通常の値通知・検証・Undoは共有しない。
    """
    pool = _LifetimePool()
    token = _CURRENT_POOL.set(pool)
    try:
        yield
    finally:
        _CURRENT_POOL.reset(token)
        pool.seal()


class PlugLifetime:
    """Binding自身の購読を保持し、共有中も削除履歴を独立させる。"""

    def __init__(self) -> None:
        """明示された生成範囲内でだけpoolを共有する。"""
        current = _CURRENT_POOL.get()
        self._pool = current or _LifetimePool()
        self._pool.acquire()
        if current is None:
            self._pool.seal()
        self._observers: dict[int, _NodeLifetime] = {}
        self._closed = False

    def add(self, target: LifetimeTarget) -> None:
        """初期読取り前の対象を記録し、閉じた購読への追加を拒否する。"""
        if self._closed:
            raise RuntimeError("終了した削除監視へ登録できません")
        observer = self._pool.add(id(self), target)
        self._observers[id(observer)] = observer

    def close(self) -> None:
        """自分の購読だけを一度解除し、他のBindingの監視を維持する。"""
        if self._closed:
            return
        self._closed = True
        observers = tuple(self._observers.values())
        self._observers.clear()
        self._pool.release(id(self), observers)


@dataclass
class LifetimeWrite:
    """削除済みMPlugへ触れず、共通の差分適用・復旧を呼ぶ。"""

    original: _Write
    require_available: Callable[[], None]
    attempted: bool = False

    def validate(self) -> None:
        """生存確認後に従来の事前検証を実行する。"""
        self.require_available()
        self.original.validate()

    def apply(self) -> None:
        """書込みを実際に試みた対象だけを復旧対象へ含める。"""
        self.require_available()
        self.attempted = True
        self.original.apply()

    def restore(self) -> None:
        """未試行を除き、削除された対象への書き戻しを明示的に拒否する。"""
        if not self.attempted:
            return
        self.require_available()
        self.original.restore()
