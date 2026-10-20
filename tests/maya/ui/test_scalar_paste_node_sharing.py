# coding: utf-8
"""値Pasteのnode共有を構築中に限定し、拒否・Undo・例外後の解放を検証する。"""

from contextlib import contextmanager

import pytest
from maya import cmds

from bd_util.maya.node.inspection import inspect_scalar_attributes
from bd_util.maya.ui import (
    MayaScalarValueTransfer,
    capture_scalar_node_values,
)
from bd_util.maya.ui.binding import scalar_value_transfer as transfer_module


@pytest.fixture
def scene(new_scene):
    """二つの数値属性を持つコピー元と、二つの貼り付け先を用意する。"""
    nodes = tuple(cmds.createNode("network") for _ in range(3))
    for node in nodes:
        cmds.addAttr(node, ln="alpha", at="double")
        cmds.addAttr(node, ln="beta", at="double")
    cmds.setAttr(nodes[0] + ".alpha", 5.0)
    cmds.setAttr(nodes[0] + ".beta", 9.0)
    cmds.undoInfo(state=True)
    return nodes


def _transfer(source, paths):
    """指定属性を入力順のsnapshotへ変換する。"""
    lookup = {a.path: a for a in inspect_scalar_attributes(source)}
    return MayaScalarValueTransfer(
        (capture_scalar_node_values(source, tuple(lookup[p] for p in paths)),)
    )


def _apply(targets, transfer, paths, route):
    """コピー済みpath数ではなく、展開後のPaste属性数で各公開入口を比較する。"""
    if route == "all":
        return transfer_module.apply_scalar_value_transfer(targets, transfer)
    if route == "paths":
        return transfer_module.apply_scalar_value_transfer_to_paths(
            targets, paths, transfer
        )
    return transfer_module.apply_scalar_value_to_paths(
        targets, paths, transfer
    )


def _observe_preparation(monkeypatch, fail_path=None):
    """実際のStore生成とtransactionを保ち、共有の開始・終了だけを記録する。"""
    original_scope = transfer_module.shared_scalar_plug_nodes
    original_create = transfer_module._create_paste_store
    original_apply = transfer_module.apply_edit_requests
    active = False
    events = []
    stores = []
    failed = False

    @contextmanager
    def scope():
        """共有範囲を通常どおり閉じ、例外でも終了を記録する。"""
        nonlocal active
        with original_scope():
            active = True
            events.append("enter")
            try:
                yield
            finally:
                active = False
                events.append("leave")

    def create(node_name, snapshot, **options):
        """同じnodeを参照する実Storeと、生成中の共有状態を保持する。"""
        nonlocal failed
        store = original_create(node_name, snapshot, **options)
        stores.append((node_name, snapshot.path, store, active))
        if not failed and snapshot.path == fail_path:
            failed = True
            raise RuntimeError("構築中断")
        return store

    def apply(*args, **options):
        """全件事前検証へ入る前に、共有範囲が終了したことを要求する。"""
        assert not active
        events.append("apply")
        return original_apply(*args, **options)

    monkeypatch.setattr(transfer_module, "shared_scalar_plug_nodes", scope)
    monkeypatch.setattr(transfer_module, "_create_paste_store", create)
    monkeypatch.setattr(transfer_module, "apply_edit_requests", apply)
    return stores, events


@pytest.mark.parametrize("route", ["all", "paths", "single"])
@pytest.mark.parametrize("attribute_count", [1, 2])
def test_paste_shares_nodes_only_for_multiple_effective_paths(
    scene, monkeypatch, route, attribute_count
):
    """全Paste入口で複数属性だけを共有し、除外・一回UndoRedoと次操作の独立を保つ。"""
    source, first, second = scene
    paths = ("alpha", "beta")[:attribute_count]
    copied_paths = ("alpha", "beta") if route == "paths" else paths
    if route == "single":
        copied_paths = ("alpha",)
    transfer = _transfer(source, copied_paths)
    cmds.setAttr(first + ".alpha", lock=True)
    stores, events = _observe_preparation(monkeypatch)
    cmds.flushUndo()

    result = _apply((first, second), transfer, paths, route)

    assert result.changed and result.eligible_count == 2 * attribute_count - 1
    assert len(result.excluded) == 1 and "ロック" in result.excluded[0]
    shared = attribute_count > 1
    assert events == (["enter", "leave", "apply"] if shared else ["apply"])
    assert len(stores) == 2 * attribute_count
    assert all(active == shared for _, _, _, active in stores)
    by_node = {
        name: [store.target.node for n, _, store, _ in stores if n == name]
        for name in (first, second)
    }
    assert by_node[first][0] is not by_node[second][0]
    if shared:
        assert all(nodes[0] is nodes[1] for nodes in by_node.values())
    wanted_beta = (5.0 if route == "single" else 9.0) if shared else 0.0
    expected = ((0.0, wanted_beta), (5.0, wanted_beta))

    def values():
        """対象外属性も含めて全値を照合する。"""
        return tuple(
            tuple(
                cmds.getAttr(node + "." + path) for path in ("alpha", "beta")
            )
            for node in (first, second)
        )

    assert values() == expected
    cmds.undo()
    assert values() == ((0.0, 0.0),) * 2
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    cmds.redo()
    assert values() == expected
    assert cmds.undoInfo(q=True, redoQueueEmpty=True)
    stores.clear()
    assert not _apply((first, second), transfer, paths, route).changed
    for name, _, store, _ in stores:
        assert store.target.node is not by_node[name][0]


def test_paste_closes_shared_nodes_when_preparation_fails(scene, monkeypatch):
    """構築途中の例外では値を書かず共有を閉じ、次のPasteを独立して実行する。"""
    source, first, second = scene
    transfer = _transfer(source, ("alpha", "beta"))
    stores, events = _observe_preparation(monkeypatch, fail_path="beta")
    cmds.flushUndo()

    with pytest.raises(RuntimeError, match="構築中断"):
        transfer_module.apply_scalar_value_transfer((first, second), transfer)

    assert events == ["enter", "leave"]
    assert all(active for _, _, _, active in stores)
    assert all(
        cmds.getAttr(node + "." + path) == 0
        for node in (first, second)
        for path in ("alpha", "beta")
    )
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    previous = {name: store.target.node for name, _, store, _ in stores}
    stores.clear()
    assert transfer_module.apply_scalar_value_transfer(
        (first, second), transfer
    ).changed
    assert events[-3:] == ["enter", "leave", "apply"]
    assert all(
        store.target.node is not previous[name] for name, _, store, _ in stores
    )
