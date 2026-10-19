# coding: utf-8
"""Paste中の削除履歴、同名再作成、復旧と一時監視の終了を検証する。"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterator
from dataclasses import dataclass, field
from typing import Literal, cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaFloatPlugsBinding,
    MayaFloatValueEdit,
    MayaNodeValueSnapshot,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
    apply_plugs_values,
    resolve_float_plug,
    shared_plugs_lifetime,
)
from bd_util.ui import EnumDefinition
from bd_util.maya import _identity
from bd_util.maya.ui.callback import dispose_owned_callbacks

_Kind = Literal["number", "enum"]
_Phase = Literal["pending", "applied", "noop"]
_ENUM = EnumDefinition.from_mapping({0: "First", 1: "Second", 2: "Third"})


@pytest.fixture(params=[False, True], autouse=True)
def sharing(request: pytest.FixtureRequest) -> Iterator[None]:
    """既存の削除・復旧契約を、独立監視と共有監視の両方で実行する。"""
    if request.param:
        with shared_plugs_lifetime():
            yield
    else:
        yield


@pytest.mark.parametrize("collision", [False, True])
def test_shared_lifetime_releases_only_its_own_subscription(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
    collision: bool,
) -> None:
    """一方を破棄しても残る行を監視し、最後の購読で全IDを解除する。"""
    driver, victim, _marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 1.0)
    if collision:
        monkeypatch.setattr(_identity, "_object_hash", lambda _node: 0)
    with shared_plugs_lifetime():
        first = MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
        second = MayaFloatPlugsBinding(
            [resolve_float_plug(node, "value") for node in (driver, victim)],
            monitor=False,
            monitor_lifetime=True,
        )
    assert len(callback_log.registered) == 4
    first.dispose()
    first.dispose()
    assert not callback_log.removed
    assert second.set_value(7.0)
    assert cmds.getAttr(driver + ".value") == 7.0
    second.dispose()
    callback_log.assert_closed()
    first.deleteLater()
    second.deleteLater()


def test_shared_lifetime_removes_unsubscribed_nodes_and_accepts_new_bindings(
    scene: tuple[str, str, str], callback_log: _CallbackLog
) -> None:
    """空になったnodeだけを解除し、生成範囲内では購読を再開できる。"""
    driver, victim, _marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 1.0)
    with shared_plugs_lifetime():
        first = MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
        second = MayaFloatPlugsBinding(
            [resolve_float_plug(victim, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
        first.dispose()
        assert len(callback_log.removed) == 2
        assert second.set_value(2.0)
        second.dispose()
        callback_log.assert_closed()
        third = MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
    assert third.set_value(3.0)
    third.dispose()
    callback_log.assert_closed()
    for binding in (first, second, third):
        binding.deleteLater()


def test_nested_lifetime_scopes_remain_independent(
    scene: tuple[str, str, str], callback_log: _CallbackLog
) -> None:
    """入れ子の生成範囲を分離し、内側の終了後は外側の共有へ戻る。"""
    driver, _victim, _marker = scene
    _add_value(driver, "number", 1.0)
    plugs = [resolve_float_plug(driver, "value")]
    with shared_plugs_lifetime():
        first = MayaFloatPlugsBinding(
            plugs, monitor=False, monitor_lifetime=True
        )
        with shared_plugs_lifetime():
            inner = MayaFloatPlugsBinding(
                plugs, monitor=False, monitor_lifetime=True
            )
        last = MayaFloatPlugsBinding(
            plugs, monitor=False, monitor_lifetime=True
        )
    assert len(callback_log.registered) == 4
    first.dispose()
    inner.dispose()
    assert [
        identifier
        for identifier in callback_log.removed
        if identifier in callback_log.registered
    ] == list(reversed(callback_log.registered[2:]))
    assert last.set_value(9.0)
    last.dispose()
    callback_log.assert_closed()
    for binding in (first, inner, last):
        binding.deleteLater()


def test_partial_lifetime_registration_failure_keeps_other_subscribers(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """追加nodeの監視登録に失敗しても、先行Bindingの購読を解除しない。"""
    driver, victim, _marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 1.0)
    source = om.MNodeMessage

    class FailureApi:
        """node削除前の監視登録だけを失敗させるAPI境界。"""

        def __getattr__(self, name: str) -> object:
            """他の登録と定数は記録付きの元APIへ渡す。"""
            if name == "addNodePreRemovalCallback":
                return self.fail
            return getattr(source, name)

        def fail(self, *_args: object, **_kwargs: object) -> int:
            """一つ目のcallbackを登録した後で例外を送出する。"""
            raise RuntimeError("監視登録の失敗")

    with shared_plugs_lifetime():
        first = MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
        with monkeypatch.context() as patch:
            patch.setattr(om, "MNodeMessage", FailureApi())
            with pytest.raises(RuntimeError, match="監視登録の失敗"):
                MayaFloatPlugsBinding(
                    [resolve_float_plug(victim, "value")],
                    monitor=False,
                    monitor_lifetime=True,
                )
        assert len(callback_log.registered) == 3
        assert len(callback_log.removed) == 1
    assert first.set_value(9.0)
    first.dispose()
    first.deleteLater()
    callback_log.assert_closed()


def test_shared_lifetime_uses_new_generation_after_node_undo(
    scene: tuple[str, str, str], callback_log: _CallbackLog
) -> None:
    """nodeをUndoで戻しても旧対象を復活させず、新Bindingだけを使える。"""
    driver, _victim, _marker = scene
    _add_value(driver, "number", 1.0)
    with shared_plugs_lifetime():
        old = MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
        cmds.delete(driver)
        cmds.undo()
        fresh = MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=True,
        )
    try:
        assert not old.store.is_available
        assert fresh.set_value(5.0)
        old.dispose()
        assert fresh.set_value(6.0)
        assert cmds.getAttr(driver + ".value") == 6.0
    finally:
        old.dispose()
        fresh.dispose()
        old.deleteLater()
        fresh.deleteLater()
    callback_log.assert_closed()


@pytest.mark.parametrize("batch", [False, True])
@pytest.mark.parametrize("phase", ["pending", "applied", "noop"])
@pytest.mark.parametrize("remove_node", [False, True])
def test_binding_lifetime_never_retargets_removed_identity(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
    batch: bool,
    phase: _Phase,
    remove_node: bool,
) -> None:
    """直接入力と一括入力で削除済み対象を拒否し、同名の新実体へ復旧しない。"""
    driver, victim, marker = scene
    _add_value(driver, "number", 1.0)
    _add_value(victim, "number", 7.0 if phase == "noop" else 1.0)
    nodes = (victim, driver) if phase == "applied" else (driver, victim)
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "value") for node in nodes],
        monitor=False,
        monitor_lifetime=True,
    )
    fired = _replace_during_write(
        monkeypatch,
        driver + ".value",
        victim + ".value",
        remove_node=remove_node,
    )
    cmds.flushUndo()
    try:
        expected = ExceptionGroup if phase == "applied" else RuntimeError
        with pytest.raises(expected):
            if batch:
                apply_plugs_values([MayaFloatValueEdit(binding, 7.0)])
            else:
                binding.set_value(7.0)
        assert fired
        assert cmds.getAttr(driver + ".value") == 1.0
        assert cmds.getAttr(victim + ".value") == 99.0
    finally:
        binding.dispose()
        binding.deleteLater()
    callback_log.assert_closed()
    _assert_undo_chunk_closed(marker)
    assert cmds.getAttr(victim + ".value") == 99.0


@pytest.mark.parametrize("batch", [False, True])
@pytest.mark.parametrize("monitor", [False, True])
@pytest.mark.parametrize("external", [False, True])
def test_binding_dispose_keeps_removal_monitor_until_restore_finishes(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
    batch: bool,
    monitor: bool,
    external: bool,
) -> None:
    """書込み中のdispose後も削除を記録し、復旧終了まで監視を解除しない。"""
    driver, victim, marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 1.0)
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "value") for node in (victim, driver)],
        monitor=monitor,
        monitor_lifetime=True,
    )
    original = cast(Callable[..., None], cmds.setAttr)
    fired: list[bool] = []

    def write(name: str, *args: object, **kwargs: object) -> None:
        """最後の入力でBindingを終了し、適用済み属性を新実体へ置き換える。"""
        original(name, *args, **kwargs)
        if fired or name != driver + ".value":
            return
        fired.append(True)
        if external and monitor:
            dispose_owned_callbacks(binding.store)
        else:
            binding.dispose()
        assert (
            len(set(callback_log.registered) - set(callback_log.removed)) >= 4
        )
        cmds.deleteAttr(victim + ".value")
        _add_value(victim, "number", 99.0)

    monkeypatch.setattr(cmds, "setAttr", write)
    cmds.flushUndo()
    try:
        with pytest.raises(ExceptionGroup):
            if batch:
                apply_plugs_values([MayaFloatValueEdit(binding, 7.0)])
            else:
                binding.set_value(7.0)
        assert fired
        assert cmds.getAttr(driver + ".value") == 1.0
        assert cmds.getAttr(victim + ".value") == 99.0
        callback_log.assert_closed()
    finally:
        binding.dispose()
        binding.deleteLater()
    callback_log.assert_closed()
    _assert_undo_chunk_closed(marker)


def test_lifetime_final_check_includes_an_entirely_unchanged_binding(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """全対象同値の別Bindingも終了検証に含め、変更した行を復旧する。"""
    driver, victim, marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 7.0)
    _add_value(driver, "number", 1.0, "trigger")
    unchanged = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "value") for node in (driver, victim)],
        monitor=False,
        monitor_lifetime=True,
    )
    changed = MayaFloatPlugsBinding(
        [resolve_float_plug(driver, "trigger")],
        monitor=False,
        monitor_lifetime=True,
    )
    fired = _replace_during_write(
        monkeypatch, driver + ".trigger", victim + ".value"
    )
    cmds.flushUndo()
    try:
        with pytest.raises(RuntimeError):
            apply_plugs_values(
                [
                    MayaFloatValueEdit(unchanged, 7.0),
                    MayaFloatValueEdit(changed, 9.0),
                ]
            )
        assert fired
        assert cmds.getAttr(driver + ".trigger") == 1.0
        assert cmds.getAttr(victim + ".value") == 99.0
    finally:
        for binding in (unchanged, changed):
            binding.dispose()
            binding.deleteLater()
    callback_log.assert_closed()
    _assert_undo_chunk_closed(marker)


@pytest.mark.parametrize(
    "monitor, lifetime, count",
    [
        (False, False, 0),
        (False, True, 4),
        (True, False, 4),
        (True, True, 8),
    ],
)
def test_lifetime_flag_reuses_full_monitor_and_default_stays_unwatched(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monitor: bool,
    lifetime: bool,
    count: int,
) -> None:
    """既定の監視なしを保ち、削除履歴の監視は表示監視から独立して保持する。"""
    driver, victim, _marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 1.0)
    plugs = [resolve_float_plug(node, "value") for node in (driver, victim)]
    binding = (
        MayaFloatPlugsBinding(plugs, monitor=False)
        if not monitor and not lifetime
        else MayaFloatPlugsBinding(
            plugs, monitor=monitor, monitor_lifetime=lifetime
        )
    )
    try:
        assert len(callback_log.registered) == count
        assert apply_plugs_values([MayaFloatValueEdit(binding, 7.0)])
        assert [
            cmds.getAttr(node + ".value") for node in (driver, victim)
        ] == [7.0, 7.0]
    finally:
        binding.dispose()
        binding.deleteLater()
    if count:
        callback_log.assert_closed()
    else:
        assert not callback_log.registered


@pytest.mark.parametrize("invalid", [0, 1, None, "true"])
def test_lifetime_monitor_requires_actual_bool_before_registration(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    invalid: object,
) -> None:
    """動的呼出しの非bool値を拒否し、削除監視を残さない。"""
    driver, _victim, _marker = scene
    _add_value(driver, "number", 1.0)
    with pytest.raises(TypeError, match="monitor_lifetime"):
        MayaFloatPlugsBinding(
            [resolve_float_plug(driver, "value")],
            monitor=False,
            monitor_lifetime=cast(bool, invalid),
        )
    assert not callback_log.registered


@dataclass
class _CallbackLog:
    """実際にMayaへ登録・解除したcallback IDを保持する。"""

    registered: list[int] = field(default_factory=list[int])
    removed: list[int] = field(default_factory=list[int])

    def assert_closed(self) -> None:
        """MayaがIDを再利用しても、登録回数と解除回数が一致するか確認する。"""
        assert self.registered
        counts = Counter(self.removed)
        assert all(
            counts[identifier] == number
            for identifier, number in Counter(self.registered).items()
        )


class _MessageApi:
    """変更できないMaya API型へ委譲し、監視の入出力だけを記録する。"""

    def __init__(self, source: object, log: _CallbackLog) -> None:
        """元のAPI型と記録先を保持する。"""
        self.source = source
        self.log = log

    def __getattr__(self, name: str) -> object:
        """対象外のAPI・定数は元の型からそのまま取得する。"""
        original = getattr(self.source, name)
        if name in (
            "addAttributeChangedCallback",
            "addNodePreRemovalCallback",
        ):
            add = cast(Callable[..., int], original)

            def register(*args: object, **kwargs: object) -> int:
                """実際に作成したcallback IDだけを記録する。"""
                identifier = int(add(*args, **kwargs))
                self.log.registered.append(identifier)
                return identifier

            return register
        if name == "removeCallback":
            remove = cast(Callable[[int], None], original)

            def unregister(identifier: int) -> None:
                """Maya側ですでに解除されている場合も解除要求を記録する。"""
                self.log.removed.append(int(identifier))
                remove(identifier)

            return unregister
        return original


@pytest.fixture
def callback_log(monkeypatch: pytest.MonkeyPatch) -> _CallbackLog:
    """公開APIの一時監視を実装名に依存せず追跡する。"""
    log = _CallbackLog()
    monkeypatch.setattr(om, "MNodeMessage", _MessageApi(om.MNodeMessage, log))
    monkeypatch.setattr(om, "MMessage", _MessageApi(om.MMessage, log))
    return log


@pytest.fixture
def scene(new_scene: None) -> Iterator[tuple[str, str, str]]:
    """独立した書込み元・削除対象・Undo確認用ノードを用意する。"""
    del new_scene
    old_undo = bool(cmds.undoInfo(query=True, state=True))
    cmds.undoInfo(state=True)
    driver, victim, marker = tuple(
        cmds.createNode("network", name=name)
        for name in (
            "pasteLifetimeDriver",
            "pasteLifetimeVictim",
            "pasteMarker",
        )
    )
    cmds.addAttr(marker, longName="checkpoint", attributeType="long")
    yield driver, victim, marker
    cmds.undoInfo(state=old_undo)


def _add_value(
    node: str, kind: _Kind, value: float | int, path: str = "value"
) -> None:
    """同じ型とenum定義で新しい属性を作り、初期値を設定する。"""
    if kind == "enum":
        cmds.addAttr(
            node,
            longName=path,
            attributeType="enum",
            enumName="First:Second:Third",
            keyable=True,
        )
    else:
        cmds.addAttr(node, longName=path, attributeType="double", keyable=True)
    cast(Callable[[str, float | int], None], cmds.setAttr)(
        f"{node}.{path}", value
    )


def _transfer(*values: MayaScalarValueSnapshot) -> MayaScalarValueTransfer:
    """OS clipboardを使わず、公開APIへ渡す値snapshotを作る。"""
    return MayaScalarValueTransfer((MayaNodeValueSnapshot(tuple(values)),))


def _replace_during_write(
    monkeypatch: pytest.MonkeyPatch,
    trigger: str,
    victim: str,
    *,
    kind: _Kind = "number",
    remove_node: bool = False,
) -> list[bool]:
    """指定書込み直後に対象を削除し、同名の新実体へ別の値を設定する。"""
    original = cast(Callable[..., None], cmds.setAttr)
    fired: list[bool] = []

    def write(name: str, *args: object, **kwargs: object) -> None:
        """実書込み後に一度だけ削除・同名再作成を発生させる。"""
        original(name, *args, **kwargs)
        if fired or name != trigger:
            return
        fired.append(True)
        node, path = victim.rsplit(".", 1)
        if remove_node:
            cmds.delete(node)
            cmds.createNode("network", name=node)
        else:
            cmds.deleteAttr(victim)
        _add_value(node, kind, 2 if kind == "enum" else 99.0, path)

    monkeypatch.setattr(cmds, "setAttr", write)
    return fired


def _assert_undo_chunk_closed(marker: str) -> None:
    """失敗後の独立操作だけをUndoし、Pasteのchunkが閉じたことを確かめる。"""
    cast(Callable[[str, int], None], cmds.setAttr)(marker + ".checkpoint", 1)
    cmds.undo()
    assert cmds.getAttr(marker + ".checkpoint") == 0


@pytest.mark.parametrize("phase", ["pending", "applied", "noop"])
@pytest.mark.parametrize("remove_node", [False, True])
def test_recreated_target_is_never_written_or_restored_by_old_identity(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
    phase: _Phase,
    remove_node: bool,
) -> None:
    """未適用・適用済み・同値対象の削除を検出し、新実体へ適用も復旧もしない。"""
    driver, victim, marker = scene
    _add_value(driver, "number", 1.0)
    _add_value(victim, "number", 7.0 if phase == "noop" else 1.0)
    nodes = (driver, victim) if phase == "pending" else (victim, driver)
    transfer = _transfer(MayaScalarValueSnapshot("value", "number", 7.0))
    fired = _replace_during_write(
        monkeypatch,
        driver + ".value",
        victim + ".value",
        remove_node=remove_node,
    )
    cmds.flushUndo()
    if phase == "applied":
        with pytest.raises(ExceptionGroup) as error:
            apply_scalar_value_transfer(
                nodes, transfer, enum_validation="operation"
            )
        assert len(error.value.exceptions) >= 2
    else:
        with pytest.raises(RuntimeError):
            apply_scalar_value_transfer(
                nodes, transfer, enum_validation="operation"
            )
    assert fired
    assert cmds.getAttr(driver + ".value") == 1.0
    assert cmds.getAttr(victim + ".value") == 99.0
    callback_log.assert_closed()
    _assert_undo_chunk_closed(marker)
    assert cmds.getAttr(driver + ".value") == 1.0
    assert cmds.getAttr(victim + ".value") == 99.0


def test_deleted_row_without_any_value_change_is_checked_at_completion(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """全対象同値で書込み計画に載らない行も、別行の適用中の削除を検出する。"""
    driver, victim, marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 7.0)
        _add_value(node, "number", 1.0, "trigger")
    transfer = _transfer(
        MayaScalarValueSnapshot("value", "number", 7.0),
        MayaScalarValueSnapshot("trigger", "number", 9.0),
    )
    fired = _replace_during_write(
        monkeypatch, driver + ".trigger", victim + ".value"
    )
    cmds.flushUndo()
    with pytest.raises(RuntimeError):
        apply_scalar_value_transfer(
            (driver, victim), transfer, enum_validation="operation"
        )
    assert fired
    assert cmds.getAttr(driver + ".value") == 7.0
    assert cmds.getAttr(victim + ".value") == 99.0
    assert [cmds.getAttr(node + ".trigger") for node in (driver, victim)] == [
        1,
        1,
    ]
    callback_log.assert_closed()
    _assert_undo_chunk_closed(marker)
    assert cmds.getAttr(victim + ".value") == 99.0


@pytest.mark.parametrize("policy", ["per_write", "operation"])
def test_same_enum_definition_does_not_hide_attribute_recreation(
    scene: tuple[str, str, str],
    callback_log: _CallbackLog,
    monkeypatch: pytest.MonkeyPatch,
    policy: Literal["per_write", "operation"],
) -> None:
    """新enumの選択肢が同じでも、旧属性を対象にした入力は継続しない。"""
    driver, victim, marker = scene
    for node in (driver, victim):
        _add_value(node, "enum", 0)
    transfer = _transfer(MayaScalarValueSnapshot("value", "enum", 1, _ENUM))
    fired = _replace_during_write(
        monkeypatch, driver + ".value", victim + ".value", kind="enum"
    )
    cmds.flushUndo()
    with pytest.raises(RuntimeError):
        apply_scalar_value_transfer(
            (driver, victim), transfer, enum_validation=policy
        )
    assert fired
    assert cmds.getAttr(driver + ".value") == 0
    assert cmds.getAttr(victim + ".value") == 2
    callback_log.assert_closed()
    _assert_undo_chunk_closed(marker)
    assert cmds.getAttr(victim + ".value") == 2


def test_successful_paste_removes_lifetime_callbacks_before_undo(
    scene: tuple[str, str, str], callback_log: _CallbackLog
) -> None:
    """正常終了時も監視を残さず、全値を一回のUndo/Redoで復元する。"""
    driver, victim, _marker = scene
    for node in (driver, victim):
        _add_value(node, "number", 1.0)
    transfer = _transfer(MayaScalarValueSnapshot("value", "number", 7.0))
    cmds.flushUndo()
    result = apply_scalar_value_transfer(
        (driver, victim), transfer, enum_validation="operation"
    )
    assert result.changed and result.eligible_count == 2
    assert result.excluded == ()
    callback_log.assert_closed()
    assert [cmds.getAttr(node + ".value") for node in (driver, victim)] == [
        7,
        7,
    ]
    cmds.undo()
    assert [cmds.getAttr(node + ".value") for node in (driver, victim)] == [
        1,
        1,
    ]
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    assert [cmds.getAttr(node + ".value") for node in (driver, victim)] == [
        7,
        7,
    ]
