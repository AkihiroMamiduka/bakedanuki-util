# coding: utf-8
"""Undo途中の再読取りをまとめ、削除履歴と通常通知を維持する。"""

from collections.abc import Callable, Iterator
from typing import Literal, cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaChannelStateBinding,
    MayaFloatPlugsBinding,
    resolve_float_plug,
)
from bd_util.ui import qt

BindingKind = Literal["values", "states"]
Binding = MayaFloatPlugsBinding | MayaChannelStateBinding


def _events() -> None:
    """予約した同期とQtの破棄を処理する。"""
    for _ in range(3):
        qt.QApplication.processEvents()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


@pytest.fixture
def scene(new_scene: None) -> Iterator[tuple[str, qt.QObject]]:
    """Undo履歴を初期化した独立nodeと所有者を用意する。"""
    del new_scene
    node = cmds.createNode("transform")
    owner = qt.QObject()
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    yield node, owner
    if qt.isValid(owner):
        owner.deleteLater()
    _events()


def _binding(node: str, owner: qt.QObject, kind: BindingKind) -> Binding:
    """値または状態の表示を同じscalar属性へ接続する。"""
    plug = resolve_float_plug(node, "weight")
    if kind == "values":
        return MayaFloatPlugsBinding([plug], parent=owner)
    return MayaChannelStateBinding([plug], parent=owner)


def _subject(binding: Binding) -> object:
    """再読取りを管理する内部オブジェクトを取得する。"""
    return (
        binding.store
        if isinstance(binding, MayaFloatPlugsBinding)
        else binding
    )


def _record_reads(
    binding: Binding, monkeypatch: pytest.MonkeyPatch
) -> list[bool]:
    """実読取りがUndoの途中で起きたかも含めて記録する。"""
    subject = _subject(binding)
    original = cast(Callable[[], object], getattr(subject, "_read_state"))
    reads: list[bool] = []

    def read_state() -> object:
        """元の読取りを維持して呼出し時点の復元状態を記録する。"""
        reads.append(om.MGlobal.isUndoing() or om.MGlobal.isRedoing())
        return original()

    monkeypatch.setattr(subject, "_read_state", read_state)
    return reads


def _change(node: str, kind: BindingKind, index: int) -> None:
    """値またはlock状態を各回に差分が出るよう変更する。"""
    if kind == "values":
        cmds.setAttr(node + ".weight", float(index))
    else:
        cmds.setAttr(node + ".weight", lock=bool(index % 2))


def _assert_display(binding: Binding, expected: float | bool) -> None:
    """公開された確定値またはlock表示を確認する。"""
    if isinstance(binding, MayaFloatPlugsBinding):
        assert binding.value == expected
    else:
        assert binding.state.locked == expected


@pytest.mark.parametrize("kind", ["values", "states"])
def test_chunk_undo_redo_reads_final_state_once_without_writing(
    scene: tuple[str, qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    kind: BindingKind,
) -> None:
    """連続変更の途中値は読まず、UndoとRedoの最終表示だけを一度読む。"""
    node, owner = scene
    cmds.addAttr(node, longName="weight", attributeType="double", keyable=True)
    binding = _binding(node, owner, kind)
    _events()
    cmds.flushUndo()
    cmds.undoInfo(openChunk=True)
    try:
        for index in range(1, 32):
            _change(node, kind, index)
    finally:
        cmds.undoInfo(closeChunk=True)
    _events()
    reads = _record_reads(binding, monkeypatch)
    writes: list[object] = []

    def record_write(*args: object, **_kwargs: object) -> None:
        """表示同期からMayaへ値を書き戻していないことを記録する。"""
        writes.append(args)

    monkeypatch.setattr(cmds, "setAttr", record_write)

    cmds.undo()
    assert not reads
    _events()
    assert reads == [False]
    _assert_display(binding, 0.0 if kind == "values" else False)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert not cmds.undoInfo(query=True, redoQueueEmpty=True)

    reads.clear()
    cmds.redo()
    assert not reads
    _events()
    assert reads == [False]
    _assert_display(binding, 31.0 if kind == "values" else True)
    assert not writes


@pytest.mark.parametrize("kind", ["values", "states"])
def test_normal_attribute_change_still_updates_immediately(
    scene: tuple[str, qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    kind: BindingKind,
) -> None:
    """通常の外部変更は次のevent loopを待たず表示へ反映する。"""
    node, owner = scene
    cmds.addAttr(node, longName="weight", attributeType="double", keyable=True)
    binding = _binding(node, owner, kind)
    _events()
    reads = _record_reads(binding, monkeypatch)
    _change(node, kind, 1)
    assert reads
    assert not any(reads)
    _assert_display(binding, 1.0 if kind == "values" else True)


@pytest.mark.parametrize("kind", ["values", "states"])
def test_reentrant_event_loop_during_undo_does_not_read_intermediate_state(
    scene: tuple[str, qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    kind: BindingKind,
) -> None:
    """Undo callbackからQtへ再入しても中間値を読まず最後に同期する。"""
    node, owner = scene
    cmds.addAttr(node, longName="weight", attributeType="double", keyable=True)
    binding = _binding(node, owner, kind)
    _events()
    cmds.flushUndo()
    cmds.undoInfo(openChunk=True)
    try:
        for index in range(1, 8):
            _change(node, kind, index)
    finally:
        cmds.undoInfo(closeChunk=True)
    _events()
    reads = _record_reads(binding, monkeypatch)
    reentered: list[bool] = []

    def process_during_undo(
        _message: int, _plug: om.MPlug, _other: om.MPlug, _data: object
    ) -> None:
        """復元中の属性通知からイベントループを一度処理する。"""
        if om.MGlobal.isUndoing():
            reentered.append(True)
            qt.QApplication.processEvents()

    callback = om.MNodeMessage.addAttributeChangedCallback(
        resolve_float_plug(node, "weight").plug.node(), process_during_undo
    )
    try:
        cmds.undo()
    finally:
        om.MMessage.removeCallback(callback)
    assert reentered
    assert not reads
    _events()
    assert reads == [False]
    _assert_display(binding, 0.0 if kind == "values" else False)


@pytest.mark.parametrize("kind", ["values", "states"])
@pytest.mark.parametrize("deletion", ["attribute", "node"])
def test_undo_deletion_invalidates_targets_before_deferred_read(
    scene: tuple[str, qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    kind: BindingKind,
    deletion: str,
) -> None:
    """削除を先に記録し、Undoで復活しても古い対象へ再接続しない。"""
    node, owner = scene
    cmds.addAttr(node, longName="weight", attributeType="double", keyable=True)
    binding = _binding(node, owner, kind)
    _events()
    if deletion == "node":
        # node削除のUndoは復活前から保持していた削除履歴を維持する
        cmds.delete(node)
        _events()
    reads = _record_reads(binding, monkeypatch)

    cmds.undo()
    targets = getattr(_subject(binding), "_targets")
    assert targets[0].removed
    assert not reads
    _events()
    assert reads == [False]
    cmds.redo()
    _events()
    assert targets[0].removed
    if isinstance(binding, MayaFloatPlugsBinding):
        assert not binding.store.is_available
    else:
        assert not binding.state.targets[0].is_available


@pytest.mark.parametrize("kind", ["values", "states"])
@pytest.mark.parametrize("dispose_owner", [False, True])
def test_disposal_cancels_pending_undo_read(
    scene: tuple[str, qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    kind: BindingKind,
    dispose_owner: bool,
) -> None:
    """Undo後の遅延同期前に終了しても対象を読み直さない。"""
    node, owner = scene
    cmds.addAttr(node, longName="weight", attributeType="double", keyable=True)
    binding = _binding(node, owner, kind)
    _events()
    _change(node, kind, 1)
    _events()
    reads = _record_reads(binding, monkeypatch)
    cmds.undo()
    if dispose_owner:
        owner.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    else:
        binding.dispose()
    _events()
    assert not reads
