# coding: utf-8
"""再利用するViewの入力元ごとに、Qt通知の接続と有効な世代を保持する。"""

from __future__ import annotations

from collections.abc import Callable
from functools import partial
from types import MethodType
from typing import Protocol, cast
from weakref import WeakMethod, ref

from .. import qt


class _Signal(Protocol):
    """PySideの版ごとのsignal型を内部の接続境界へ閉じ込める。"""

    def connect(
        self,
        slot: Callable[..., None],
        connection_type: qt.Qt.ConnectionType,
    ) -> qt.QtCore.QMetaObject.Connection:
        """指定した接続方式で通知先を登録する。"""
        raise NotImplementedError


class _QueuedDelivery(qt.QObject):
    """所有Viewと同じ寿命のQt受信先で、MetaCallを一回だけ予約する。"""

    requested = qt.Signal(object)

    def __init__(self, owner: qt.QObject) -> None:
        """送信元とは独立したQObjectへ、遅延通知の接続を一度だけ登録する。"""
        super().__init__(owner)
        cast(_Signal, self.requested).connect(
            self._deliver, qt.Qt.ConnectionType.QueuedConnection
        )

    @qt.Slot(object)
    def _deliver(self, callback: object) -> None:
        """送信元から独立したQObject受信先で、世代確認付き通知を実行する。"""
        cast(Callable[[], None], callback)()


class ViewSourceConnections:
    """切替前に予約された通知を無効にし、所有Viewの破棄時も全接続を解除する。"""

    def __init__(self, owner: qt.QObject) -> None:
        """入力元とは独立したViewの寿命と、最初の接続世代を記録する。"""
        self._owner = ref(owner)
        self._generation = 0
        self._connections: list[qt.QtCore.QMetaObject.Connection] = []
        self._queued_delivery = _QueuedDelivery(owner)
        owner.destroyed.connect(self.clear)

    @property
    def generation(self) -> int:
        """終了通知への再入で新しい接続へ切り替わったか判定する世代を返す。"""
        return self._generation

    def connect(
        self,
        signal: object,
        slot: Callable[..., None],
        *,
        queued: bool = False,
        discard_args: bool = False,
    ) -> None:
        """現在世代とViewの生存を確認してから、通知を転送する。"""
        generation = self._generation
        weak_slot = WeakMethod(slot) if isinstance(slot, MethodType) else None
        receiver = getattr(slot, "__self__", None)
        method_name = getattr(slot, "__name__", "")
        weak_builtin = (
            ref(receiver)
            if weak_slot is None
            and isinstance(receiver, qt.QObject)
            and isinstance(method_name, str)
            and method_name
            else None
        )
        strong_slot = (
            slot if weak_slot is None and weak_builtin is None else None
        )

        def dispatch(*args: object) -> None:
            """切替前のqueued通知を無視し、生存中のViewだけへ通知する。"""
            owner = self._owner()
            if (
                generation != self._generation
                or owner is None
                or not qt.isValid(owner)
            ):
                return
            if weak_slot is not None:
                callback = weak_slot()
            elif weak_builtin is not None:
                target = weak_builtin()
                callback = (
                    None
                    if target is None or not qt.isValid(target)
                    else cast(
                        Callable[..., None], getattr(target, method_name)
                    )
                )
            else:
                callback = strong_slot
            if callback is None:
                return
            if discard_args:
                callback()
            else:
                callback(*args)

        def enqueue(*args: object) -> None:
            """Viewと同じ寿命の受信先へ、1回のMetaCallで通知を渡す。"""
            payload = () if discard_args else args
            if qt.isValid(self._queued_delivery):
                self._queued_delivery.requested.emit(
                    partial(dispatch, *payload)
                )

        self._connections.append(
            cast(_Signal, signal).connect(
                enqueue if queued else dispatch,
                qt.Qt.ConnectionType.AutoConnection,
            )
        )

    def clear(self, *_args: object) -> None:
        """予約済み通知を先に失効させ、現在世代の接続だけを解除する。"""
        self._generation += 1
        connections, self._connections = self._connections, []
        disconnect = cast(
            Callable[[qt.QtCore.QMetaObject.Connection], bool],
            getattr(qt.QObject, "disconnect"),
        )
        for connection in connections:
            try:
                disconnect(connection)
            except (RuntimeError, TypeError):
                pass
