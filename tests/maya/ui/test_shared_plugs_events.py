# coding: utf-8
"""属性群の固定通知共有と、購読ごとの寿命・失敗・再入を検証する。"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterator
from contextvars import Context, ContextVar
import gc
import importlib
from types import SimpleNamespace
from typing import cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaCallbackRegistry,
    MayaChannelStateBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
    resolve_enum_plug,
    resolve_float_plug,
    shared_plugs_events,
)
from bd_util.maya.ui import callback as callback_module
from bd_util.maya.ui.binding import (
    _plugs_events as events_module,  # pyright: ignore[reportPrivateUsage]
)
from bd_util.maya.ui.binding._plugs_store import (
    _PlugsCallbackRegistry as PlugsCallbackRegistry,  # pyright: ignore[reportPrivateUsage]
)
from bd_util.ui import qt


def _flush() -> None:
    """各Storeの遅延同期とQObjectの破棄を完了する。"""
    for _ in range(3):
        qt.QtCore.QCoreApplication.processEvents()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None, qt.QEvent.Type.DeferredDelete
        )


class _EventLog:
    """実Maya通知を維持し、共通イベントの登録数と解放を記録する。"""

    def __init__(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Maya APIの境界だけを包み、登録済み通知を直接配信可能にする。"""
        self.registered: list[str] = []
        self.active: dict[int, tuple[str, Callable[..., None], object]] = {}
        self.exiting: set[int] = set()
        self.fail_event: str | None = None
        self._add_event = cast(
            Callable[..., int], om.MEventMessage.addEventCallback
        )
        self._add_condition = cast(
            Callable[..., int], om.MConditionMessage.addConditionCallback
        )
        self._add_exiting = cast(
            Callable[[Callable[..., None]], int],
            getattr(callback_module, "_add_maya_exiting_callback"),
        )
        self._remove = om.MMessage.removeCallback
        monkeypatch.setattr(
            om,
            "MEventMessage",
            SimpleNamespace(addEventCallback=self.add_event),
        )
        monkeypatch.setattr(
            om,
            "MConditionMessage",
            SimpleNamespace(addConditionCallback=self.add_condition),
        )
        monkeypatch.setattr(
            callback_module, "_add_maya_exiting_callback", self.add_exiting
        )
        monkeypatch.setattr(
            om, "MMessage", SimpleNamespace(removeCallback=self.remove)
        )

    def add_event(
        self, name: str, callback: Callable[..., None], data: object = None
    ) -> int:
        """実イベントを登録し、指定した通知だけの失敗も再現する。"""
        if name == self.fail_event:
            raise RuntimeError("共通通知の登録失敗")
        identifier = int(self._add_event(name, callback, data))
        self.registered.append(name)
        self.active[identifier] = (name, callback, data)
        return identifier

    def add_condition(
        self, name: str, callback: Callable[..., None], data: object = None
    ) -> int:
        """conditionも同じ記録へ加え、Auto Key通知の重複を検出する。"""
        if name == self.fail_event:
            raise RuntimeError("共通通知の登録失敗")
        identifier = int(self._add_condition(name, callback, data))
        self.registered.append(name)
        self.active[identifier] = (name, callback, data)
        return identifier

    def add_exiting(self, callback: Callable[..., None]) -> int:
        """空scopeや最後の購読終了後に、終了監視も残らないことを記録する。"""
        identifier = self._add_exiting(callback)
        self.exiting.add(identifier)
        return identifier

    def remove(self, identifier: int) -> None:
        """Maya側の解除を維持し、有効なIDの集合から即座に外す。"""
        self._remove(identifier)
        self.active.pop(identifier, None)
        self.exiting.discard(identifier)

    def emit(self, name: str) -> None:
        """Maya境界で例外を握られず、共有配信の例外と再入を検査する。"""
        for event, callback, data in tuple(self.active.values()):
            if event != name:
                continue
            if name == "autoKeyframeState":
                callback(True, data)
            else:
                callback(data)


@pytest.fixture
def event_log(monkeypatch: pytest.MonkeyPatch) -> _EventLog:
    """各testに独立したMaya通知の記録境界を用意する。"""
    return _EventLog(monkeypatch)


@pytest.fixture
def scene(new_scene: None) -> Iterator[tuple[str, qt.QObject]]:
    """削除可能な属性を持つnodeと、BindingのQt ownerを用意する。"""
    del new_scene
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="amount", attributeType="double", keyable=True)
    cmds.addAttr(
        node,
        longName="choice",
        attributeType="enum",
        enumName="First:Second",
        keyable=True,
    )
    owner = qt.QObject()
    try:
        yield node, owner
    finally:
        if qt.isValid(owner):
            owner.deleteLater()
        _flush()


def _binding(
    node: str,
    owner: qt.QObject,
    attribute: str = "tx",
    *,
    connected: bool = False,
    monitor: bool = True,
) -> MayaFloatPlugsBinding:
    """一つの属性へ接続し、共有有無以外の既存Binding規則を保つ。"""
    return MayaFloatPlugsBinding(
        [resolve_float_plug(node, attribute)],
        parent=owner,
        edit_connected=connected,
        monitor=monitor,
    )


def _registry_callback_count(owner: qt.QObject) -> int:
    """Qt bindingの動的な型境界で、Storeの従来監視数を取得する。"""
    return len(_registry(owner).callback_ids)


def _registry(owner: qt.QObject) -> PlugsCallbackRegistry:
    """所有するStoreのRegistryを、共有購読を管理する具体型で取得する。"""
    find_registries = cast(
        Callable[[type[MayaCallbackRegistry]], list[MayaCallbackRegistry]],
        getattr(owner, "findChildren"),
    )
    return cast(
        PlugsCallbackRegistry, find_registries(MayaCallbackRegistry)[0]
    )


def test_common_notifications_share_once_and_release_per_binding(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """固定七通知を一度だけ登録し、一行の終了で他行の同期を止めない。"""
    node, owner = scene
    with shared_plugs_events():
        first = _binding(node, owner, connected=True)
        second = _binding(node, owner, "ty", connected=True)
    assert Counter(event_log.registered) == Counter(
        {
            "linearUnitChanged": 1,
            "angularUnitChanged": 1,
            "Undo": 1,
            "Redo": 1,
            "autoKeyframeState": 1,
            "animLayerRefresh": 1,
            "animLayerRebuild": 1,
        }
    )
    assert _registry_callback_count(first) == 3
    first.dispose()
    first.dispose()
    assert len(event_log.active) == 7
    assert second.set_value(3.0)
    cmds.undo()
    _flush()
    assert second.value == 0.0
    second.dispose()
    assert not event_log.active
    assert not event_log.exiting


@pytest.mark.parametrize(
    "ending", ("binding", "owner", "view_model", "view_model_delete", "store")
)
def test_all_existing_endings_close_shared_subscription(
    scene: tuple[str, qt.QObject], event_log: _EventLog, ending: str
) -> None:
    """既存の全終了経路で、他のQt遅延削除へ購読を持ち越さない。"""
    node, owner = scene
    with shared_plugs_events():
        binding = (
            MayaEnumPlugsBinding(
                [resolve_enum_plug(node, "choice")], parent=owner
            )
            if ending in ("view_model", "view_model_delete")
            else _binding(node, owner)
        )
    view_model = binding.view_model
    if ending == "binding":
        binding.dispose()
    elif ending == "owner":
        owner.deleteLater()
    elif ending == "view_model":
        view_model.dispose()
    elif ending == "view_model_delete":
        view_model.deleteLater()
    else:
        binding.store.dispose()
    if ending not in ("owner", "view_model_delete"):
        assert not event_log.active
    _flush()
    assert not event_log.active
    assert not event_log.exiting
    if qt.isValid(view_model):
        assert not view_model.set_value_command.can_execute


def test_registry_dispose_closes_only_its_subscription_and_disables_input(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """Registryの直接終了でもStoreへ再入し、別行の同期を残して自分を終了する。"""
    node, owner = scene
    with shared_plugs_events():
        first = _binding(node, owner)
        second = _binding(node, owner, "ty")
    view_model = first.view_model
    registry = _registry(first)
    registry.dispose()
    registry.dispose()
    assert registry.is_disposed and not registry.callback_ids
    assert first.store.is_disposed
    assert not view_model.set_value_command.can_execute
    assert len(event_log.active) == 4
    assert second.set_value(3.0)
    first.dispose()
    second.dispose()
    assert not event_log.active and not event_log.exiting


def test_owner_destruction_closes_subscriptions_while_python_references_remain(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """PythonのBinding参照を保持したままでも、Qt親の破棄で全購読を外す。"""
    node, owner = scene
    with shared_plugs_events():
        bindings = (_binding(node, owner), _binding(node, owner, "ty"))
    registries = tuple(_registry(binding) for binding in bindings)
    owner.deleteLater()
    _flush()
    assert all(not qt.isValid(binding) for binding in bindings)
    assert all(registry.is_disposed for registry in registries)
    assert all(not registry.callback_ids for registry in registries)
    assert not event_log.active and not event_log.exiting


def test_registry_rejects_subscription_after_dispose(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """終了済みRegistryへの受渡しは、追加した購読を閉じてから拒否する。"""
    _node, owner = scene
    registry = PlugsCallbackRegistry(owner)
    registry.dispose()
    receiver = _Receiver()
    with shared_plugs_events():
        subscription = events_module.subscribe_plugs_events(
            receiver.notify, connected=False
        )
        assert subscription is not None
        with pytest.raises(RuntimeError, match="終了したRegistry"):
            registry.set_shared_events(subscription)
        assert not event_log.active
    assert not event_log.exiting


def test_registry_dispose_does_not_reenter_from_subscription_close(
    scene: tuple[str, qt.QObject],
    event_log: _EventLog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """購読解除から再度Registryを終了しても、native解除と終了通知は一度にする。"""
    node, owner = scene
    with shared_plugs_events():
        binding = _binding(node, owner)
    registry = _registry(binding)
    subscription = cast(
        events_module.PlugsEventsSubscription,
        getattr(registry, "_shared_events"),
    )
    original = events_module.PlugsEventsSubscription.close
    calls: list[str] = []

    def close(item: events_module.PlugsEventsSubscription) -> None:
        """所有する購読の終了だけで再入を起こし、通常の解除も実行する。"""
        if item is subscription:
            calls.append("close")
            registry.dispose()
        original(item)

    def disposed() -> None:
        """一回だけ届くRegistryの終了通知を記録する。"""
        calls.append("disposed")

    monkeypatch.setattr(events_module.PlugsEventsSubscription, "close", close)
    registry.disposed.connect(disposed)
    registry.dispose()
    assert calls == ["close", "disposed"]
    assert binding.store.is_disposed
    assert not registry.callback_ids
    assert not event_log.active and not event_log.exiting
    binding.dispose()


@pytest.mark.parametrize("ending", ("registry", "binding"))
def test_subscription_close_failure_still_finishes_registry_and_open_undo(
    scene: tuple[str, qt.QObject],
    event_log: _EventLog,
    monkeypatch: pytest.MonkeyPatch,
    ending: str,
) -> None:
    """購読解除の例外でも、node監視・入力と既に開いた連続編集Undoを終了する。"""
    node, owner = scene
    with shared_plugs_events():
        binding = _binding(node, owner)
    view_model = binding.view_model
    registry = _registry(binding)
    subscription = cast(
        events_module.PlugsEventsSubscription,
        getattr(registry, "_shared_events"),
    )
    original = events_module.PlugsEventsSubscription.close

    def close(item: events_module.PlugsEventsSubscription) -> None:
        """実際の解除後に一つだけ例外を加え、他の解放を妨げないことを調べる。"""
        original(item)
        if item is subscription:
            raise RuntimeError("共有購読の終了失敗")

    monkeypatch.setattr(events_module.PlugsEventsSubscription, "close", close)
    cmds.flushUndo()
    view_model.begin_edit(owner)
    assert binding.set_value(2.0)
    try:
        with pytest.raises(RuntimeError, match="共有購読の終了失敗"):
            if ending == "registry":
                registry.dispose()
            else:
                binding.dispose()
        assert registry.is_disposed and not registry.callback_ids
        assert not view_model.is_editing
        assert not view_model.set_value_command.can_execute
        assert not event_log.active and not event_log.exiting
        cmds.undo()
        _flush()
        assert cmds.getAttr(node + ".tx") == 0.0
    finally:
        binding.dispose()


def test_registry_constructor_failure_has_initialized_subscription_state(
    scene: tuple[str, qt.QObject],
    event_log: _EventLog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """基底constructorの失敗によるvirtual disposeも、未初期化の購読へ触れない。"""
    _node, owner = scene

    def fail(_callback: Callable[..., None]) -> int:
        """Maya終了監視の登録だけを失敗させ、constructor中の終了を起こす。"""
        raise RuntimeError("Maya終了監視の登録失敗")

    monkeypatch.setattr(callback_module, "_add_maya_exiting_callback", fail)
    with pytest.raises(RuntimeError, match="Maya終了監視の登録失敗"):
        PlugsCallbackRegistry(owner)
    assert not event_log.active and not event_log.exiting


def test_empty_nested_and_unmonitored_scopes_are_independent(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """空範囲と入れ子を解放し、監視なしBindingは共通通知へ参加させない。"""
    node, owner = scene
    with shared_plugs_events():
        pass
    assert not event_log.active and not event_log.exiting
    with shared_plugs_events():
        unmonitored = _binding(node, owner, monitor=False)
    assert not event_log.active and not event_log.exiting
    unmonitored.dispose()
    with shared_plugs_events():
        outer = _binding(node, owner)
        with shared_plugs_events():
            inner = _binding(node, owner, "ty")
        assert len(event_log.active) == 8
        inner.dispose()
        assert len(event_log.active) == 4
    assert outer.set_value(5.0)
    outer.dispose()
    assert not event_log.active and not event_log.exiting


def test_scope_can_resubscribe_before_exit_and_does_not_change_default(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """生成範囲内の再登録を許し、範囲外は従来の七callbackを維持する。"""
    node, owner = scene
    with shared_plugs_events():
        first = _binding(node, owner)
        first.dispose()
        assert not event_log.active
        second = _binding(node, owner, "ty")
    assert len(event_log.active) == 4
    second.dispose()
    ordinary = _binding(node, owner)
    assert _registry_callback_count(ordinary) == 7
    ordinary.dispose()
    assert not event_log.active and not event_log.exiting


def test_channel_state_binding_keeps_its_own_notifications(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """値Bindingだけを共有し、状態BindingのUndo・Redo監視は変更しない。"""
    node, owner = scene
    with shared_plugs_events():
        value = _binding(node, owner)
        state = MayaChannelStateBinding(
            [resolve_float_plug(node, "tx")], parent=owner
        )
    assert Counter(event_log.registered)["Undo"] == 2
    assert Counter(event_log.registered)["Redo"] == 2
    value.dispose()
    assert len(event_log.active) == 2
    state.dispose()
    assert not event_log.active and not event_log.exiting


def test_dispose_stops_shared_notifications_during_lifetime_restore(
    scene: tuple[str, qt.QObject],
    event_log: _EventLog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """復旧用node監視が残る書込み中でも、終了した行への共通通知は即外す。"""
    node, owner = scene
    with shared_plugs_events():
        binding = MayaFloatPlugsBinding(
            [resolve_float_plug(node, "amount")],
            parent=owner,
            monitor_lifetime=True,
        )
    original = cast(Callable[..., None], cmds.setAttr)
    disposed_during_write = False

    def write(name: str, *args: object, **kwargs: object) -> None:
        """適用後の終了で共通購読を外し、復旧に必要なnode監視だけを残す。"""
        nonlocal disposed_during_write
        original(name, *args, **kwargs)
        if disposed_during_write or not name.endswith(".amount"):
            return
        disposed_during_write = True
        binding.dispose()
        assert not event_log.active
        assert _registry_callback_count(binding) > 0

    monkeypatch.setattr(cmds, "setAttr", write)
    try:
        with pytest.raises(RuntimeError):
            binding.set_value(3.0)
        assert disposed_during_write
        assert cmds.getAttr(node + ".amount") == 0.0
        assert not event_log.active and not event_log.exiting
    finally:
        binding.dispose()


@pytest.mark.parametrize("event", ("Undo", "autoKeyframeState"))
def test_partial_registration_failure_keeps_existing_subscribers(
    scene: tuple[str, qt.QObject], event_log: _EventLog, event: str
) -> None:
    """途中登録の失敗では、その行だけを外して既存の共有購読を維持する。"""
    node, owner = scene
    with shared_plugs_events():
        first = None if event == "Undo" else _binding(node, owner)
        event_log.fail_event = event
        with pytest.raises(RuntimeError, match="登録失敗"):
            _binding(node, owner, "ty", connected=True)
        event_log.fail_event = None
        assert len(event_log.active) == (0 if first is None else 4)
    if first is not None:
        assert first.set_value(2.0)
        first.dispose()
    assert not event_log.active and not event_log.exiting


def test_shared_notifications_preserve_units_and_immediate_node_changes(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """共通通知だけをまとめ、単位・lock・外部値・削除の既存同期を維持する。"""
    node, owner = scene
    original_unit = cast(str, cmds.currentUnit(query=True, linear=True))
    cmds.currentUnit(linear="cm")
    with shared_plugs_events():
        binding = _binding(node, owner)
        dynamic = _binding(node, owner, "amount")
    try:
        cast(Callable[..., None], cmds.setAttr)(node + ".tx", 4.0)
        assert binding.value == 4.0
        cmds.setAttr(node + ".tx", lock=True)
        assert not binding.view_model.set_value_command.can_execute
        cmds.setAttr(node + ".tx", lock=False)
        assert binding.view_model.set_value_command.can_execute
        cmds.currentUnit(linear="m")
        _flush()
        assert binding.view_model.presentation.to_display(100.0) == 1.0
        cmds.flushUndo()
        assert binding.set_value(8.0)
        cmds.undo()
        _flush()
        assert binding.value == 4.0
        cmds.redo()
        _flush()
        assert binding.value == 8.0
        cmds.deleteAttr(node + ".amount")
        assert not dynamic.store.is_available
        cmds.undo()
        _flush()
        assert not dynamic.store.is_available
    finally:
        binding.dispose()
        dynamic.dispose()
        cmds.currentUnit(linear=original_unit)
    assert not event_log.active and not event_log.exiting


class _Receiver:
    """配信時の解除・追加と例外を、Storeの内部同期へ依存せず再現する。"""

    def __init__(self, action: Callable[[], None] | None = None) -> None:
        """通知数と、一度だけ実行する任意の処理を保持する。"""
        self.calls = 0
        self.action = action

    def notify(self) -> None:
        """呼出し回数を記録し、指定された配信中の操作を実行する。"""
        self.calls += 1
        action, self.action = self.action, None
        if action is not None:
            action()


def test_dispatch_reports_one_failure_after_notifying_other_rows(
    event_log: _EventLog,
) -> None:
    """一つの購読例外を通知しつつ、後続行へ必要な同期を配信する。"""

    def fail() -> None:
        """最初の行だけが同期予約で失敗する状態を再現する。"""
        raise RuntimeError("一行の同期失敗")

    first, second = _Receiver(fail), _Receiver()
    with shared_plugs_events():
        a = events_module.subscribe_plugs_events(first.notify, connected=False)
        b = events_module.subscribe_plugs_events(
            second.notify, connected=False
        )
    assert a is not None and b is not None
    try:
        with pytest.raises(ExceptionGroup, match="共有Maya通知") as caught:
            event_log.emit("Undo")
        assert len(caught.value.exceptions) == 1
        assert first.calls == second.calls == 1
    finally:
        a.close()
        b.close()
    assert not event_log.active and not event_log.exiting


def test_dispatch_skips_removed_rows_and_waits_for_new_subscribers(
    event_log: _EventLog,
) -> None:
    """配信snapshotから解除済み行を除き、新しい購読は次の通知から呼ぶ。"""
    first, second, third = _Receiver(), _Receiver(), _Receiver()
    added: list[events_module.PlugsEventsSubscription] = []
    with shared_plugs_events():
        a = events_module.subscribe_plugs_events(first.notify, connected=False)
        b = events_module.subscribe_plugs_events(
            second.notify, connected=False
        )
        assert a is not None and b is not None

        def change_subscriptions() -> None:
            """配信途中に後続行を外し、新しい行を同じscopeへ追加する。"""
            assert b is not None
            b.close()
            subscription = events_module.subscribe_plugs_events(
                third.notify, connected=False
            )
            assert subscription is not None
            added.append(subscription)

        first.action = change_subscriptions
        event_log.emit("Undo")
        assert (first.calls, second.calls, third.calls) == (1, 0, 0)
        event_log.emit("Undo")
        assert (first.calls, second.calls, third.calls) == (2, 0, 1)
    a.close()
    b.close()
    for subscription in added:
        subscription.close()
    assert not event_log.active and not event_log.exiting


def test_dead_receiver_and_module_reload_leave_no_global_subscription(
    scene: tuple[str, qt.QObject], event_log: _EventLog
) -> None:
    """弱参照の消失とmodule更新の前後も、旧poolを孤立させず終了する。"""
    receiver = _Receiver()
    with shared_plugs_events():
        subscription = events_module.subscribe_plugs_events(
            receiver.notify, connected=False
        )
    assert subscription is not None
    del receiver
    gc.collect()
    assert not event_log.active and not event_log.exiting
    node, owner = scene
    with shared_plugs_events():
        binding = _binding(node, owner)
    importlib.reload(events_module)
    binding.dispose()
    assert not event_log.active and not event_log.exiting
    with shared_plugs_events():
        replacement = _binding(node, owner)
    replacement.dispose()
    assert not event_log.active and not event_log.exiting


def test_module_reload_inside_scope_releases_original_context_and_pool(
    event_log: _EventLog,
) -> None:
    """scope内reloadでも開始時のContextVarへ戻し、旧poolを確実に封鎖する。"""
    receiver = _Receiver()
    with shared_plugs_events():
        original_context = cast(
            ContextVar[object], getattr(events_module, "_CURRENT_POOL")
        )
        subscription = events_module.subscribe_plugs_events(
            receiver.notify, connected=False
        )
        assert subscription is not None
        importlib.reload(events_module)
        assert getattr(events_module, "_CURRENT_POOL") is not original_context
    assert original_context.get() is None
    assert len(event_log.active) == 4
    subscription.close()
    assert not event_log.active and not event_log.exiting


def test_context_reset_failure_still_releases_empty_scope(
    event_log: _EventLog,
) -> None:
    """異なるContextで終了してresetが失敗しても、空poolの終了監視を外す。"""
    scope = shared_plugs_events()
    Context().run(scope.__enter__)
    assert event_log.exiting
    with pytest.raises(ValueError, match="different Context"):
        scope.__exit__(None, None, None)
    assert not event_log.active and not event_log.exiting
