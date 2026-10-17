# coding: utf-8
"""表示状態の生フラグ、標準Undo、独立した編集可否と失敗復旧を検証する。"""

from collections.abc import Callable, Iterator
from typing import Literal, cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya import _identity
from bd_util.maya.ui import (
    ChannelDisplayState,
    MayaCallbackRegistry,
    MayaChannelStateBinding,
    MayaEditSession,
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


def _callback_count(binding: MayaChannelStateBinding) -> int:
    """Bindingが直接所有するregistryの登録callback数を返す。"""
    return sum(
        len(child.callback_ids)
        for child in binding.children()
        if isinstance(child, MayaCallbackRegistry)
    )


def test_shared_session_groups_bindings_and_ignores_noop(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """別Bindingの変更を一回でUndo/Redoし、無変更では履歴を作らない。"""
    nodes, owner = scene
    first, second = _binding(nodes[:1], owner), _binding(nodes[1:], owner)
    session = MayaEditSession(owner)
    session.begin()
    assert not first.set_display_state("keyable", edit_session=session)
    session.finish()
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    session.begin()
    first.set_display_state("hidden", edit_session=session)
    _events()
    second.set_display_state("channel_box", edit_session=session)
    session.finish()
    cmds.undo()
    assert all(_raw(node) == (True, False, False) for node in nodes)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    assert _raw(nodes[0]) == (False, False, False)
    assert _raw(nodes[1]) == (False, True, False)


def test_session_finish_inside_write_closes_in_order(
    scene: tuple[list[str], qt.QObject], monkeypatch: pytest.MonkeyPatch
) -> None:
    """Maya書込みcallbackからの終了を内側chunkの後へ延期する。"""
    nodes, owner = scene
    binding = _binding(nodes, owner)
    session = MayaEditSession(owner)
    original = binding._write

    def interrupt(target, raw, operation):
        """書込み中の終了要求を発生させて通常の書込みを継続する。"""
        session.finish()
        original(target, raw, operation)

    monkeypatch.setattr(binding, "_write", interrupt)
    session.begin()
    binding.set_display_state("hidden", edit_session=session)
    assert not session.is_editing
    cmds.undo()
    assert all(_raw(node) == (True, False, False) for node in nodes)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize("locked", [True, False])
def test_shared_lock_session_groups_bindings_and_ignores_noop(
    scene: tuple[list[str], qt.QObject], locked: bool
) -> None:
    """複数Bindingのlock変更を一回でUndo/Redoし、同値要求は省く。"""
    nodes, owner = scene
    for node in nodes:
        cmds.setAttr(node + ".weight", lock=not locked)
    first, second = _binding(nodes[:1], owner), _binding(nodes[1:], owner)
    session = MayaEditSession(owner)
    cmds.flushUndo()
    session.begin()
    assert not first.set_locked(not locked, edit_session=session)
    session.finish()
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    session.begin()
    assert first.set_locked(locked, edit_session=session)
    assert second.set_locked(locked, edit_session=session)
    assert not second.set_locked(locked, edit_session=session)
    session.finish()
    assert all(_raw(node) == (True, False, locked) for node in nodes)
    cmds.undo()
    assert all(_raw(node) == (True, False, not locked) for node in nodes)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    assert all(_raw(node) == (True, False, locked) for node in nodes)


def test_session_preserves_disabled_undo_and_owner_disposal(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """Undo無効設定を保ち、QObjectの破棄時にも開いたchunkを閉じる。"""
    nodes, owner = scene
    binding = _binding(nodes, owner)
    session = MayaEditSession(owner)
    cmds.undoInfo(state=False)
    try:
        session.begin()
        binding.set_display_state("hidden", edit_session=session)
        session.finish()
        assert not cmds.undoInfo(query=True, state=True)
    finally:
        cmds.undoInfo(state=True)
    cmds.flushUndo()
    session.begin()
    binding.set_display_state("keyable", edit_session=session)
    owner.deleteLater()
    _events()
    cmds.undo()
    assert all(_raw(node) == (False, False, False) for node in nodes)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


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


@pytest.mark.parametrize("restricted_index", [0, 1])
@pytest.mark.parametrize("restriction", ["parent", "node"])
def test_shared_lock_session_preserves_restricted_targets(
    scene: tuple[list[str], qt.QObject],
    restricted_index: int,
    restriction: str,
) -> None:
    """代表対象なら行を拒否し、後続だけなら除外して親・nodeを維持する。"""
    nodes, owner = scene
    for node in nodes:
        cmds.setAttr(node + ".tx", lock=True)
    restricted = nodes[restricted_index]
    if restriction == "parent":
        cmds.setAttr(restricted + ".translate", lock=True)
    else:
        cmds.lockNode(restricted, lock=True)
    binding = MayaChannelStateBinding(
        [resolve_float_plug(node, "tx") for node in nodes], parent=owner
    )
    cmds.flushUndo()
    session = MayaEditSession(owner)
    session.begin()
    assert binding.set_locked(False, edit_session=session) == (
        restricted_index != 0
    )
    session.finish()
    assert cmds.getAttr(restricted + ".tx", lock=True)
    if restriction == "parent":
        assert cmds.getAttr(restricted + ".translate", lock=True)
    else:
        assert cmds.lockNode(restricted, query=True, lock=True) == [True]
    if restricted_index == 0:
        assert all(cmds.getAttr(node + ".tx", lock=True) for node in nodes)
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    else:
        assert not cmds.getAttr(nodes[0] + ".tx", lock=True)
        assert not cmds.getAttr(nodes[2] + ".tx", lock=True)
        cmds.undo()
        assert all(cmds.getAttr(node + ".tx", lock=True) for node in nodes)
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)


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


@pytest.mark.parametrize("operation", ["lock", "display"])
def test_many_targets_visit_only_the_notifying_node(
    scene: tuple[list[str], qt.QObject],
    operation: Literal["lock", "display"],
) -> None:
    """千対象の通知照合が線形回数に収まり、全件適用とUndo/Redoを維持する。"""
    _, owner = scene
    count = 1000
    nodes = [cmds.createNode("transform") for _ in range(count)]
    visited = 0

    class WatchedPlugs(tuple[om.MPlug, ...]):
        """通知照合が調べた対象と祖先の数を記録する。"""

        def __iter__(self) -> Iterator[om.MPlug]:
            """通常の列挙を維持し、通知照合だけを数える。"""
            nonlocal visited
            visited += len(self)
            return super().__iter__()

    class CountedBinding(MayaChannelStateBinding):
        """書込み処理を変えず、通知照合の列挙回数を記録する。"""

        def record_target_visits(self) -> None:
            """対象ごとの監視plug列挙に計数処理を付ける。"""
            for target in self._targets:
                target.watched = WatchedPlugs(target.watched)

    binding = CountedBinding(
        [resolve_float_plug(node, "tx") for node in nodes], parent=owner
    )
    binding.record_target_visits()
    assert _callback_count(binding) == count * 3 + 2
    cmds.flushUndo()
    if operation == "lock":
        assert binding.set_locked(True)
        assert all(target.locked for target in binding.state.targets)
    else:
        assert binding.set_display_state("hidden")
        assert all(
            target.display_state == "hidden"
            for target in binding.state.targets
        )
    assert 0 < visited <= count * 4

    # 多数ノードの一時Bindingと同様に破棄し、Mayaの履歴を直接照合する
    binding.dispose()
    assert _callback_count(binding) == 0
    cmds.undo()
    flag = "lock" if operation == "lock" else "keyable"
    expected = operation == "display"
    assert all(
        cmds.getAttr(node + ".tx", **{flag: True}) == expected
        for node in nodes
    )
    cmds.redo()
    assert all(
        cmds.getAttr(node + ".tx", **{flag: True}) != expected
        for node in nodes
    )


def test_hash_collisions_preserve_aliases_ancestors_and_node_identity(
    scene: tuple[list[str], qt.QObject], monkeypatch: pytest.MonkeyPatch
) -> None:
    """hash衝突時も実体を区別し、改名・祖先通知・削除履歴を保持する。"""
    nodes, owner = scene

    def colliding_hash(_node: om.MObject) -> int:
        """異なるnodeと属性を同じhash候補へ集める。"""
        return 1

    monkeypatch.setattr(_identity, "_object_hash", colliding_hash)
    binding = MayaChannelStateBinding(
        [resolve_float_plug(node, "tx") for node in nodes], parent=owner
    )
    assert _callback_count(binding) == len(nodes) * 3 + 2
    with pytest.raises(ValueError, match="同じ属性"):
        MayaChannelStateBinding(
            [
                resolve_float_plug(nodes[0], "tx"),
                resolve_float_plug(nodes[0], "translateX"),
            ],
            parent=owner,
        )

    nodes[1] = cmds.rename(nodes[1], "renamedChannelStateTarget")
    cmds.setAttr(nodes[1] + ".translate", lock=True)
    assert binding.state.targets[1].parent_locked
    assert not binding.state.targets[0].parent_locked
    assert not binding.state.targets[2].parent_locked
    assert "renamedChannelStateTarget" in binding.state.targets[1].plug_name
    cmds.setAttr(nodes[1] + ".translate", lock=False)
    assert not binding.state.targets[1].parent_locked
    cmds.delete(nodes[2])
    assert not binding.state.targets[2].is_available
    cmds.undo()
    assert not binding.state.targets[2].is_available
    _events()
    assert binding.state.targets[0].is_available
    assert binding.state.targets[1].is_available
    assert not binding.state.targets[2].is_available


@pytest.mark.parametrize("remove_node", [False, True])
def test_deletion_during_write_stays_removed_after_recreation(
    scene: tuple[list[str], qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    remove_node: bool,
) -> None:
    """書込み中の削除通知も記録し、同名再作成への適用を拒否して復旧する。"""
    nodes, owner = scene
    binding = _binding(nodes, owner)
    original = cast(Callable[..., None], cmds.setAttr)
    interrupted = False

    def remove_during_write(name: str, **flags: object) -> None:
        """先頭への適用後に末尾の実体を削除して同名属性を作る。"""
        nonlocal interrupted
        original(name, **flags)
        if interrupted or name.rsplit("|", 1)[-1] != nodes[0] + ".weight":
            return
        interrupted = True
        if remove_node:
            cmds.delete(nodes[-1])
            cmds.createNode("transform", name=nodes[-1])
        else:
            cmds.deleteAttr(nodes[-1] + ".weight")
        cmds.addAttr(
            nodes[-1], longName="weight", attributeType="double", keyable=True
        )

    monkeypatch.setattr(cmds, "setAttr", remove_during_write)
    with pytest.raises(RuntimeError, match="状態が変わりました"):
        binding.set_locked(True)
    assert interrupted
    assert not binding.state.targets[-1].is_available
    assert all(not _raw(node)[2] for node in nodes)
