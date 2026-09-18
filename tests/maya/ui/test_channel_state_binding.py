# coding: utf-8
"""表示状態の生フラグ、標準Undo、独立した編集可否と失敗復旧を検証する。"""

from collections.abc import Callable, Iterator
from typing import cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    ChannelDisplayState,
    MayaChannelStateBinding,
    resolve_float_plug,
)
from bd_util.ui import qt


def _events() -> None:
    """予約した同期とQObjectの破棄を処理する。"""
    qt.QApplication.processEvents()
    qt.QApplication.processEvents()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


def _raw(name: str) -> tuple[bool, bool, bool]:
    """見かけの表示状態ではなくOpenMayaの生フラグを取得する。"""
    plug = resolve_float_plug(name, "weight").plug
    return bool(plug.isKeyable), bool(plug.isChannelBox), bool(plug.isLocked)


@pytest.fixture
def scene(new_scene: None) -> Iterator[tuple[list[str], qt.QObject]]:
    """独立したscalar属性と、Bindingを所有するQObjectを用意する。"""
    del new_scene
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    for node in nodes:
        cmds.addAttr(
            node, longName="weight", attributeType="double", keyable=True
        )
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    yield nodes, owner
    if qt.isValid(owner):
        owner.deleteLater()
    _events()


def _binding(nodes: list[str], owner: qt.QObject) -> MayaChannelStateBinding:
    """全ノードの同名属性を状態編集へ接続する。"""
    return MayaChannelStateBinding(
        [resolve_float_plug(node, "weight") for node in nodes], parent=owner
    )


@pytest.mark.parametrize(
    "before", [(False, False), (False, True), (True, False)]
)
@pytest.mark.parametrize("display", ["keyable", "channel_box", "hidden"])
def test_all_raw_flags_round_trip_undo_redo(
    scene: tuple[list[str], qt.QObject],
    before: tuple[bool, bool],
    display: ChannelDisplayState,
) -> None:
    """三状態間の全遷移が、Undoで元の生フラグへ戻る。"""
    nodes, owner = scene
    for node in nodes:
        plug = resolve_float_plug(node, "weight").plug
        plug.isChannelBox = before[1]
        plug.isKeyable = before[0]
        assert _raw(node)[:2] == before
    binding = _binding(nodes, owner)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    expected = (display == "keyable", display == "channel_box", False)
    changed = binding.set_display_state(display)
    assert [_raw(n) for n in nodes] == [expected] * 3
    if not changed:
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        return
    cmds.undo()
    _events()
    assert [_raw(n) for n in nodes] == [(*before, False)] * 3
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    _events()
    assert [_raw(n) for n in nodes] == [expected] * 3


def test_display_and_lock_are_independent_of_connection_and_value_lock(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """入力接続中や値ロック中も状態を操作し、値と接続を維持する。"""
    nodes, owner = scene
    cmds.connectAttr(nodes[0] + ".tx", nodes[1] + ".weight")
    cmds.setAttr(nodes[0] + ".weight", lock=True)
    binding = _binding(nodes, owner)
    assert binding.state.display_writable_count == 3
    assert binding.state.lock_writable_count == 3
    assert binding.state.lock_mixed
    binding.set_display_state("hidden")
    assert _raw(nodes[0]) == (False, False, True)
    binding.set_locked(False)
    assert [_raw(n) for n in nodes] == [(False, False, False)] * 3
    assert cmds.isConnected(nodes[0] + ".tx", nodes[1] + ".weight")


def test_external_flags_only_synchronize_and_noop_has_no_undo(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """外部のchannelBox単独変更を読み取り、同値操作では履歴を作らない。"""
    nodes, owner = scene
    binding = _binding(nodes, owner)
    assert not binding.set_locked(False)
    assert not binding.set_display_state("keyable")
    binding.refresh()
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.setAttr(nodes[1] + ".weight", keyable=False)
    cmds.setAttr(nodes[1] + ".weight", channelBox=True)
    _events()
    assert binding.state.display_mixed
    assert _raw(nodes[0]) == (True, False, False)
    assert binding.state.targets[1].display_state == "channel_box"


def test_partial_write_failure_restores_flags_and_reports_error(
    scene: tuple[list[str], qt.QObject], monkeypatch: pytest.MonkeyPatch
) -> None:
    """後続対象での書込み失敗時に先行対象の生フラグを復元する。"""
    nodes, owner = scene
    cmds.setAttr(nodes[0] + ".weight", keyable=False)
    cmds.setAttr(nodes[0] + ".weight", channelBox=True)
    before = [_raw(n) for n in nodes]
    binding = _binding(nodes, owner)
    errors: list[str] = []
    binding.edit_failed.connect(errors.append)
    original = cast(Callable[..., None], cmds.setAttr)
    failed = False

    def fail_once(name: str, **flags: object) -> None:
        """二つ目の対象への実書込みを一度だけ拒否する。"""
        nonlocal failed
        if name.rsplit("|", 1)[-1] == nodes[1] + ".weight" and not failed:
            failed = True
            raise RuntimeError("検証用の書込み失敗")
        original(name, **flags)

    monkeypatch.setattr(cmds, "setAttr", fail_once)
    with pytest.raises(RuntimeError, match="検証用"):
        binding.set_display_state("hidden")
    assert failed and errors
    assert [_raw(n) for n in nodes] == before
    assert binding.state.display_mixed


def test_removed_attribute_never_reconnects_and_dispose_stops_callbacks(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """属性削除後の同名再作成へ接続せず、終了後の入力を拒否する。"""
    nodes, owner = scene
    binding = _binding(nodes, owner)
    cmds.deleteAttr(nodes[1] + ".weight")
    cmds.addAttr(nodes[1], longName="weight", attributeType="double")
    _events()
    assert not binding.state.targets[1].is_available
    binding.set_locked(True)
    assert not _raw(nodes[1])[2]
    owner.deleteLater()
    _events()
    assert binding.is_disposed
    assert not binding.refresh()
    with pytest.raises(RuntimeError):
        binding.set_locked(False)


def test_parent_lock_is_reported_without_changing_parent(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """親由来の実効lockを理由付きで示し、表示変更だけを許可する。"""
    nodes, owner = scene
    cmds.setAttr(nodes[0] + ".translate", lock=True)
    binding = MayaChannelStateBinding(
        [resolve_float_plug(node, "tx") for node in nodes], parent=owner
    )
    assert binding.state.targets[0].parent_locked
    assert not binding.state.can_set_locked
    assert binding.state.can_set_display
    assert not binding.set_locked(False)
    assert binding.set_display_state("hidden")
    assert cmds.getAttr(nodes[0] + ".translate", lock=True)


def test_undo_disabled_setting_is_not_changed(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """Undo無効時も設定を勝手に有効化せず明示操作を適用する。"""
    nodes, owner = scene
    binding = _binding(nodes, owner)
    cmds.undoInfo(state=False)
    try:
        assert binding.set_locked(True)
        assert not cmds.undoInfo(query=True, state=True)
        assert [_raw(n)[2] for n in nodes] == [True] * 3
    finally:
        cmds.undoInfo(state=True)


@pytest.mark.parametrize("special_index", [0, 1])
def test_simultaneous_default_flags_disable_only_display_editing(
    scene: tuple[list[str], qt.QObject], special_index: int
) -> None:
    """標準Undoで戻せない両有効の定義は表示変更から除外し、lockは許可する。"""
    nodes, owner = scene
    node = nodes[special_index]
    cmds.deleteAttr(node + ".weight")
    definition = om.MFnNumericAttribute()
    attribute = definition.create(
        "weight", "weight", om.MFnNumericData.kDouble
    )
    definition.keyable = True
    definition.channelBox = True
    selection = om.MSelectionList()
    selection.add(node)
    om.MFnDependencyNode(selection.getDependNode(0)).addAttribute(attribute)
    assert _raw(node) == (True, True, False)
    binding = _binding(nodes, owner)
    assert not binding.state.targets[special_index].can_set_display
    assert binding.state.targets[special_index].can_set_locked
    assert binding.state.targets[special_index].display_reason
    cmds.flushUndo()
    assert binding.set_display_state("hidden") == (special_index != 0)
    assert _raw(node) == (True, True, False)
    if special_index != 0:
        cmds.undo()
        _events()
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert binding.set_locked(True)
    assert _raw(node) == (True, True, True)
    cmds.undo()
    _events()
    assert _raw(node) == (True, True, False)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
