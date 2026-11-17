# coding: utf-8
"""同時に構築する属性群の固定Maya通知だけを、明示範囲内で共有する。"""

from __future__ import annotations

from collections.abc import Callable, Generator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from weakref import WeakMethod

from maya.api import OpenMaya as om

from ....ui import qt
from ..callback import MayaCallbackRegistry

__all__ = ["shared_plugs_events"]

_VALUE_EVENTS = ("linearUnitChanged", "angularUnitChanged", "Undo", "Redo")
_CONNECTED_EVENTS = (
    "autoKeyframeState",
    "animLayerRefresh",
    "animLayerRebuild",
)


@dataclass
class _EventReceivers:
    """一つのMaya通知IDと、登録順を保つ有効な購読を持つ。"""

    callback_id: int
    subscriptions: dict[int, PlugsEventsSubscription] = field(
        default_factory=dict[int, "PlugsEventsSubscription"]
    )


class PlugsEventsSubscription:
    """共有受信の購読だけを所有し、旧Storeや別行の寿命を延ばさない。"""

    def __init__(
        self,
        pool: _EventsPool,
        callback: Callable[..., None],
        events: tuple[str, ...],
    ) -> None:
        """Storeのbound methodを弱参照で保持し、消失時も購読を解除する。"""
        self._pool: _EventsPool | None = pool
        self._events = events
        self._closed = False
        self._callback: WeakMethod[Callable[..., None]] | None = WeakMethod(
            callback, self._on_callback_lost
        )

    def notify(self) -> None:
        """既に解除された行を拒否し、既存の同期予約だけを呼び出す。"""
        if self._closed or self._callback is None:
            return
        callback = self._callback()
        if callback is None:
            self.close()
        else:
            callback()

    def close(self) -> None:
        """自分の購読を即座に外し、他行の通知は維持する。"""
        if self._closed:
            return
        self._closed = True
        pool, self._pool = self._pool, None
        self._callback = None
        if pool is not None:
            pool.release(self, self._events)

    def _on_callback_lost(self, _reference: object) -> None:
        """Storeが破棄された場合に、空の共有監視を残さない。"""
        self.close()


class _EventsPool:
    """構築範囲の外でも既存購読だけを維持する、固定通知の共有受信。"""

    def __init__(self) -> None:
        """各Storeとは独立したownerを用意し、Maya終了時にも解除する。"""
        self._owner = qt.QObject()
        self._registry = MayaCallbackRegistry(
            self._owner, on_maya_exiting=self._close
        )
        self._receivers: dict[str, _EventReceivers] = {}
        self._accepting = True
        self._closed = False

    def subscribe(
        self, callback: Callable[..., None], *, connected: bool
    ) -> PlugsEventsSubscription:
        """必要な固定通知へ参加し、途中失敗では追加した購読だけを解除する。"""
        if not self._accepting or self._closed:
            raise RuntimeError("終了した共通イベント監視へ登録できません")
        events = _VALUE_EVENTS + (_CONNECTED_EVENTS if connected else ())
        subscription = PlugsEventsSubscription(self, callback, events)
        try:
            for event in events:
                receivers = self._receivers.get(event)
                if receivers is None:
                    receivers = _EventReceivers(self._add_event(event))
                    self._receivers[event] = receivers
                receivers.subscriptions[id(subscription)] = subscription
        except Exception:
            subscription.close()
            raise
        return subscription

    def _add_event(self, event: str) -> int:
        """同じ通知を一度だけ登録し、ID管理へ失敗した場合も解除する。"""
        if event == "autoKeyframeState":
            callback_id = int(
                om.MConditionMessage.addConditionCallback(
                    event, self._on_condition, event
                )
            )
        else:
            callback_id = int(
                om.MEventMessage.addEventCallback(event, self._on_event, event)
            )
        try:
            return self._registry.register(callback_id)
        except Exception:
            om.MMessage.removeCallback(callback_id)
            raise

    def _on_event(self, event: object) -> None:
        """通知されたeventに属する購読へ、値を読まず配信する。"""
        if not isinstance(event, str):
            raise TypeError("共通イベントの識別子はstrでなければなりません")
        self._notify(event)

    def _on_condition(self, _state: bool, event: object) -> None:
        """Auto Keyのcondition通知も、既存Storeの同期予約へまとめる。"""
        self._on_event(event)

    def _notify(self, event: str) -> None:
        """配信中の解除と追加を区別し、一行の失敗後も残る行へ通知する。"""
        receivers = self._receivers.get(event)
        if self._closed or receivers is None:
            return
        failures: list[Exception] = []
        for identity, subscription in tuple(receivers.subscriptions.items()):
            if receivers.subscriptions.get(identity) is not subscription:
                continue
            try:
                subscription.notify()
            except Exception as error:
                failures.append(error)
        if failures:
            raise ExceptionGroup("共有Maya通知の配信に失敗しました", failures)

    def release(
        self, subscription: PlugsEventsSubscription, events: tuple[str, ...]
    ) -> None:
        """最後の購読が去った通知を外し、封鎖済みの空poolを即解放する。"""
        if self._closed:
            return
        for event in events:
            receivers = self._receivers.get(event)
            if receivers is None:
                continue
            receivers.subscriptions.pop(id(subscription), None)
            if not receivers.subscriptions:
                self._receivers.pop(event)
                self._registry.remove(receivers.callback_id)
        if not self._accepting and not self._receivers:
            self._close()

    def seal(self) -> None:
        """構築後の追加だけを禁止し、既存Bindingの購読は維持する。"""
        self._accepting = False
        if not self._receivers:
            self._close()

    def _close(self) -> None:
        """購読と全Maya通知を停止し、Qtの遅延削除を待たず解放する。"""
        if self._closed:
            return
        self._closed = True
        self._accepting = False
        subscriptions = {
            identity: subscription
            for receivers in self._receivers.values()
            for identity, subscription in receivers.subscriptions.items()
        }
        self._receivers.clear()
        try:
            for subscription in subscriptions.values():
                subscription.close()
        finally:
            self._registry.dispose()
            if qt.isValid(self._owner):
                self._owner.deleteLater()


_CURRENT_POOL: ContextVar[_EventsPool | None] = ContextVar(
    "plugs_events_pool", default=None
)


@contextmanager
def shared_plugs_events() -> Generator[None, None, None]:
    """範囲内で作る値Bindingの、固定Maya通知だけを共有する。

    `monitor=True`のscalar属性群Bindingが対象。単位変更・Undo・Redoと、
    接続編集用のAuto Key・Layer通知を各一度だけ受信する。属性・dirty・削除、
    動的な時刻・カーブ監視、書込み・検証・復旧は共有しない。
    範囲を抜けても購読は続き、各Bindingの`dispose()`で即解除する。
    入れ子の範囲は独立し、状態編集Bindingと範囲外の監視は変更しない。
    """
    pool = _EventsPool()
    current_pool = _CURRENT_POOL
    token = current_pool.set(pool)
    try:
        yield
    finally:
        try:
            current_pool.reset(token)
        finally:
            pool.seal()


def subscribe_plugs_events(
    callback: Callable[..., None], *, connected: bool
) -> PlugsEventsSubscription | None:
    """明示された構築範囲内だけで購読し、範囲外は従来の登録を使う。"""
    pool = _CURRENT_POOL.get()
    return (
        None if pool is None else pool.subscribe(callback, connected=connected)
    )
