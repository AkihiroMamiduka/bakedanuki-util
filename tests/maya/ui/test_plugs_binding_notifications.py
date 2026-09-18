# coding: utf-8
"""複数属性Bindingの通知対象の絞り込みと依存先の同期を検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.ui import qt


def flush():
    """dirtyの遅延同期と破棄を次のQtイベントまで処理する。"""
    for _ in range(3):
        qt.QtCore.QCoreApplication.processEvents()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None, qt.QEvent.Type.DeferredDelete
        )


def add_value(node, kind, name="watched"):
    """比較用の独立scalar属性を追加する。"""
    options = {"enumName": "Off:Preview:Final"} if kind == "enum" else {}
    cmds.addAttr(
        node,
        longName=name,
        attributeType="double" if kind == "float" else kind,
        **options,
    )


def bind(nodes, owner, kind, attribute="watched"):
    """同じ属性pathを型別の複数Bindingへ接続する。"""
    factory, resolver = {
        "float": (MayaFloatPlugsBinding, resolve_float_plug),
        "bool": (MayaBoolPlugsBinding, resolve_bool_plug),
        "enum": (MayaEnumPlugsBinding, resolve_enum_plug),
    }[kind]
    return factory([resolver(node, attribute) for node in nodes], parent=owner)


@pytest.fixture
def scene(new_scene):
    """独立したnode群とBindingの所有者を用意する。"""
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    yield nodes, owner
    owner.deleteLater()
    flush()


@pytest.mark.parametrize("kind", ["float", "bool", "enum"])
def test_unrelated_dirty_does_not_read_or_refresh_binding(
    scene, monkeypatch, kind
):
    """別属性の変更では正本の読取りもViewModelの同期も実行しない。"""
    nodes, owner = scene
    for node in nodes:
        add_value(node, kind)
    binding = bind(nodes, owner, kind)
    flush()
    refreshed = []
    original = binding.store.refresh

    def record_refresh():
        """値が同じ場合の無駄な読取りも数える。"""
        refreshed.append(True)
        return original()

    monkeypatch.setattr(binding.store, "refresh", record_refresh)
    for node in nodes:
        cmds.setAttr(node + ".tx", 4)
    flush()
    assert not refreshed
    assert not binding.is_mixed
    assert binding.value == 0


@pytest.mark.parametrize(
    "kind,value", [("float", 3.5), ("bool", True), ("enum", 2)]
)
@pytest.mark.parametrize("target_index", [0, 2])
def test_connected_target_dirty_updates_value_and_mixed_without_echo(
    scene, kind, value, target_index
):
    """上流からのdirtyで代表値と後続の混在を同期し、他の対象へ転送しない。"""
    nodes, owner = scene
    source = cmds.createNode("transform")
    for node in (*nodes, source):
        add_value(node, kind)
    cmds.connectAttr(source + ".watched", nodes[target_index] + ".watched")
    binding = bind(nodes, owner, kind)
    flush()
    cmds.flushUndo()
    cmds.setAttr(source + ".watched", value)
    flush()
    assert binding.value == (value if target_index == 0 else 0)
    assert binding.is_mixed
    assert binding.writable_count == 2
    assert all(
        cmds.getAttr(node + ".watched") == 0
        for index, node in enumerate(nodes)
        if index != target_index
    )
    cmds.undo()
    flush()
    assert binding.value == 0
    assert not binding.is_mixed
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.is_mixed


def test_compound_parent_changes_all_watched_children_on_same_node(scene):
    """一nodeの複数対象をまとめても親への値入力とlockを全ての子へ反映する。"""
    nodes, owner = scene
    binding = MayaFloatPlugsBinding(
        [
            resolve_float_plug(node, axis)
            for node in nodes[:2]
            for axis in ("tx", "ty")
        ],
        parent=owner,
    )
    cmds.setAttr(nodes[0] + ".translate", 2, 3, 4, type="double3")
    flush()
    assert binding.value == 2
    assert binding.is_mixed
    cmds.setAttr(nodes[1] + ".translate", lock=True)
    flush()
    assert binding.writable_count == 2
    assert not binding.target_states[2].is_writable
    assert not binding.target_states[3].is_writable
    cmds.setAttr(nodes[1] + ".translate", lock=False)
    assert binding.set_value(6)
    assert all(
        cmds.getAttr(node + "." + axis) == 6
        for node in nodes[:2]
        for axis in ("tx", "ty")
    )


def test_compound_connection_propagates_computed_output_dirty(scene):
    """親compoundで接続した計算出力の変更を子scalarの表示へ反映する。"""
    nodes, owner = scene
    multiply = cmds.createNode("multiplyDivide")
    cmds.setAttr(multiply + ".input2", 2, 3, 4, type="double3")
    cmds.connectAttr(nodes[0] + ".translate", multiply + ".input1")
    cmds.connectAttr(multiply + ".output", nodes[1] + ".translate")
    binding = bind(nodes[1:], owner, "float", "tx")
    cmds.setAttr(nodes[0] + ".translate", 5, 6, 7, type="double3")
    flush()
    assert binding.value == 10
    assert binding.is_mixed
    assert not binding.view_model.set_value_command.can_execute
    cmds.disconnectAttr(multiply + ".output", nodes[1] + ".translate")
    flush()
    assert binding.view_model.set_value_command.can_execute


def test_animation_time_dirty_updates_bound_scalar(scene):
    """時間変更によるアニメーション評価もdirty経由で値表示へ同期する。"""
    nodes, owner = scene
    initial_time = cmds.currentTime(query=True)
    cmds.setKeyframe(nodes[0], attribute="tx", time=1, value=2)
    cmds.setKeyframe(nodes[0], attribute="tx", time=10, value=8)
    cmds.currentTime(1)
    binding = bind(nodes, owner, "float", "tx")
    try:
        assert binding.value == 2
        for frame, expected in ((10, 8), (1, 2), (10, 8)):
            cmds.currentTime(frame)
            flush()
            assert binding.value == expected
        assert not binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        cmds.currentTime(initial_time)


def test_delete_multiple_targets_on_one_node_does_not_retarget_after_undo(
    scene,
):
    """node単位の削除通知で所属対象を全て無効化し、削除Undoでも再接続しない。"""
    nodes, owner = scene
    binding = MayaFloatPlugsBinding(
        [
            resolve_float_plug(nodes[0], "tx"),
            resolve_float_plug(nodes[0], "ty"),
            resolve_float_plug(nodes[1], "tx"),
        ],
        parent=owner,
    )
    cmds.delete(nodes[0])
    flush()
    assert [state.is_available for state in binding.target_states] == [
        False,
        False,
        True,
    ]
    cmds.undo()
    flush()
    assert [state.is_available for state in binding.target_states] == [
        False,
        False,
        True,
    ]


def test_dispose_with_pending_dirty_never_reads_destroyed_targets(
    scene, monkeypatch
):
    """dirty予約後の終了で、遅延処理から正本を再読取りしない。"""
    nodes, owner = scene
    cmds.connectAttr(nodes[0] + ".tx", nodes[1] + ".tx")
    binding = bind(nodes[1:], owner, "float", "tx")
    read = []
    original = binding.store._read_state

    def record_read():
        """終了後の正本アクセスだけを検出する。"""
        read.append(True)
        return original()

    monkeypatch.setattr(binding.store, "_read_state", record_read)
    cmds.setAttr(nodes[0] + ".tx", 4)
    binding.dispose()
    read.clear()
    cmds.delete(nodes)
    flush()
    assert not read
