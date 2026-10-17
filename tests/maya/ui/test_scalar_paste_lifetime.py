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
    MayaNodeValueSnapshot,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
)
from bd_util.ui import EnumDefinition

_Kind = Literal["number", "enum"]
_Phase = Literal["pending", "applied", "noop"]
_ENUM = EnumDefinition.from_mapping({0: "First", 1: "Second", 2: "Third"})


@dataclass
class _CallbackLog:
    """実際にMayaへ登録・解除したcallback IDを保持する。"""

    registered: list[int] = field(default_factory=list[int])
    removed: list[int] = field(default_factory=list[int])

    def assert_closed(self) -> None:
        """登録した監視がすべて一度ずつ解除されたことを確認する。"""
        assert self.registered
        counts = Counter(self.removed)
        assert all(counts[identifier] == 1 for identifier in self.registered)


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
