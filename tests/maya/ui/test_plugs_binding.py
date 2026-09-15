# coding: utf-8
"""複数属性の明示編集、読取り専用状態、Undoと失敗復旧を検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import resolve_bool_plug, resolve_float_plug
from bd_util.maya.ui.binding.plugs_binding import (
    MayaBoolPlugsBinding,
    MayaFloatPlugsBinding,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import qt


def flush():
    """遅延同期とQObjectの破棄を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def scene(new_scene):
    """独立した三つの属性とcallback ownerを用意する。"""
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    undo_enabled = cmds.undoInfo(q=True, state=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    yield nodes, owner
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo_enabled)


def float_binding(nodes, owner, attribute="tx"):
    """指定した全nodeの同名属性を入力へ接続する。"""
    return MayaFloatPlugsBinding(
        [resolve_float_plug(node, attribute) for node in nodes], parent=owner
    )


def bool_binding(nodes, owner):
    """標準visibility属性を一括入力へ接続する。"""
    return MayaBoolPlugsBinding(
        [resolve_bool_plug(node, "visibility") for node in nodes], parent=owner
    )


@pytest.mark.parametrize("kind", ["float", "bool"])
def test_initial_refresh_external_change_never_write(scene, kind):
    """初期表示と外部変更の追従では他対象を変更しない。"""
    nodes, owner = scene
    attribute = "tx" if kind == "float" else "visibility"
    cmds.setAttr(f"{nodes[1]}.{attribute}", 1 if kind == "float" else False)
    cmds.flushUndo()
    binding = (
        float_binding(nodes, owner)
        if kind == "float"
        else bool_binding(nodes, owner)
    )
    try:
        assert binding.is_mixed
        assert binding.target_count == binding.writable_count == 3
        binding.refresh()
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        cmds.setAttr(
            f"{nodes[0]}.{attribute}", 2 if kind == "float" else False
        )
        flush()
        assert cmds.getAttr(f"{nodes[2]}.{attribute}") == (
            0 if kind == "float" else True
        )
        cmds.undo()
        flush()
        assert binding.value == (0 if kind == "float" else True)
        assert binding.is_mixed
    finally:
        binding.dispose()


@pytest.mark.parametrize("kind", ["float", "bool"])
def test_representative_same_value_applies_other_targets_once(scene, kind):
    """代表と同値の入力も混在を揃え、全対象を一回でUndoできる。"""
    nodes, owner = scene
    attribute = "tx" if kind == "float" else "visibility"
    initial = 4.0 if kind == "float" else False
    cmds.setAttr(f"{nodes[1]}.{attribute}", initial)
    binding = (
        float_binding(nodes, owner)
        if kind == "float"
        else bool_binding(nodes, owner)
    )
    try:
        notifications = []
        binding.state_changed.connect(
            lambda: notifications.append(binding.is_mixed)
        )
        cmds.flushUndo()
        assert binding.apply_representative_value()
        assert not binding.is_mixed
        assert notifications[-1] is False
        cmds.undo()
        flush()
        assert cmds.getAttr(f"{nodes[1]}.{attribute}") == initial
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        cmds.redo()
        flush()
        assert not binding.is_mixed
        cmds.flushUndo()
        assert not binding.set_value(binding.value)
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    finally:
        binding.dispose()


def test_secondary_read_only_skipped_and_representative_disables(scene):
    """後続のlockと接続は除外し、代表lockでは全体を停止する。"""
    nodes, owner = scene
    cmds.setAttr(f"{nodes[1]}.tx", lock=True)
    binding = float_binding(nodes, owner)
    try:
        assert binding.writable_count == 2
        assert binding.target_states[1].reason == "ロックされています"
        assert binding.set_value(3)
        assert [cmds.getAttr(f"{node}.tx") for node in nodes] == [3, 0, 3]
        cmds.setAttr(f"{nodes[0]}.translate", lock=True)
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value(5)
        cmds.setAttr(f"{nodes[0]}.translate", lock=False)
        assert binding.view_model.set_value_command.can_execute
        cmds.connectAttr(f"{nodes[1]}.ty", f"{nodes[2]}.tx")
        assert binding.writable_count == 1
        assert "入力接続" in binding.target_states[2].reason
    finally:
        binding.dispose()


def test_units_hard_limits_and_complete_preflight(scene):
    """代表の表示範囲を保ち、後続の制限違反を変更前に拒否する。"""
    nodes, owner = scene
    for index, node in enumerate(nodes):
        cmds.addAttr(
            node,
            ln="limited",
            at="doubleLinear",
            minValue=-10,
            maxValue=10 - index * 3,
        )
    binding = float_binding(nodes, owner, "limited")
    try:
        messages = []
        binding.edit_failed.connect(messages.append)
        assert binding.view_model.presentation.maximum == 10
        cmds.currentUnit(linear="m")
        flush()
        assert binding.view_model.presentation.scale == pytest.approx(0.01)
        cmds.flushUndo()
        with pytest.raises(ValueError, match="上限"):
            binding.set_value(5)
        assert messages and "上限" in messages[-1]
        assert f"{nodes[2]}.limited" in messages[-1]
        assert [cmds.getAttr(f"{node}.limited") for node in nodes] == [0, 0, 0]
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        assert binding.set_value(2)
        assert [
            cmds.getAttr(f"{node}.limited") for node in nodes
        ] == pytest.approx([0.02] * 3)
    finally:
        binding.dispose()


def test_drag_all_targets_one_undo_and_dispose_closes_chunk(scene):
    """複数対象の連続編集を一つのUndoにまとめ、終了時にも閉じる。"""
    nodes, owner = scene
    binding = float_binding(nodes, owner)
    try:
        cmds.flushUndo()
        assert binding.view_model.begin_edit(owner)
        for value in (1, 2, 3):
            assert binding.set_value(value)
            assert [cmds.getAttr(f"{node}.tx") for node in nodes] == [
                value
            ] * 3
        binding.view_model.end_edit(owner)
        cmds.undo()
        flush()
        assert [cmds.getAttr(f"{node}.tx") for node in nodes] == [0] * 3
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        cmds.redo()
        assert [cmds.getAttr(f"{node}.tx") for node in nodes] == [3] * 3
        assert binding.view_model.begin_edit(owner)
        binding.set_value(4)
    finally:
        binding.dispose()
    assert FloatEditUndo._active is None
    cmds.setAttr(f"{nodes[0]}.ty", 9)
    cmds.undo()
    assert cmds.getAttr(f"{nodes[0]}.tx") == 4


@pytest.mark.parametrize("during_drag", [False, True])
def test_partial_write_failure_restores_only_current_input(
    scene, monkeypatch, during_drag
):
    """途中失敗は今回の入力を復旧し、前のドラッグ位置を保持する。"""
    nodes, owner = scene
    binding = float_binding(nodes, owner)
    original_set_attr = cmds.setAttr
    failed = False

    def failing_set_attr(path, value):
        """二つ目の書込み後に一回だけ失敗する。"""
        nonlocal failed
        original_set_attr(path, value)
        if (
            path.split(".")[0].rsplit("|", 1)[-1] == nodes[1]
            and value == 6
            and not failed
        ):
            failed = True
            raise RuntimeError("write failed")

    try:
        if during_drag:
            binding.view_model.begin_edit(owner)
        binding.set_value(2)
        monkeypatch.setattr(cmds, "setAttr", failing_set_attr)
        with pytest.raises(RuntimeError, match="write failed"):
            binding.set_value(6)
        assert [cmds.getAttr(f"{node}.tx") for node in nodes] == [2] * 3
        assert binding.value == 2
        assert not binding.is_mixed
        assert FloatEditUndo._active is None
    finally:
        binding.dispose()


def test_removal_does_not_retarget_and_dispose_releases_callbacks(scene):
    """削除をUndoしても再接続せず、明示終了で全監視を解除する。"""
    nodes, owner = scene
    binding = float_binding(nodes, owner)
    registries = binding.findChildren(MayaCallbackRegistry)
    assert registries and any(registry.callback_ids for registry in registries)
    cmds.delete(nodes[1])
    flush()
    assert not binding.target_states[1].is_available
    cmds.undo()
    flush()
    assert not binding.target_states[1].is_available
    assert binding.set_value(4)
    assert cmds.getAttr(f"{nodes[1]}.tx") == 0
    cmds.delete(nodes[0])
    flush()
    assert not binding.view_model.set_value_command.can_execute
    binding.dispose()
    assert all(registry.is_disposed for registry in registries)


def test_float32_noop_and_incompatible_kind_rejection(scene):
    """格納値で無変更を判断し、異なる単位や重複対象を拒否する。"""
    nodes, owner = scene
    for node in nodes:
        cmds.addAttr(node, ln="value", at="float")
    binding = float_binding(nodes, owner, "value")
    try:
        assert binding.set_value(0.1)
        cmds.flushUndo()
        assert not binding.set_value(0.1)
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
    with pytest.raises(TypeError, match="単位"):
        MayaFloatPlugsBinding(
            [
                resolve_float_plug(nodes[0], "tx"),
                resolve_float_plug(nodes[1], "rx"),
            ]
        )
    with pytest.raises(ValueError, match="同じ属性"):
        MayaFloatPlugsBinding([resolve_float_plug(nodes[0], "tx")] * 2)


def test_constructor_failure_releases_registered_callbacks(scene, monkeypatch):
    """監視登録途中の失敗でも生成済みのcallbackを解放する。"""
    nodes, owner = scene
    original_register = MayaCallbackRegistry.register
    registries = []

    def failing_register(registry, callback_id):
        """登録済みcallbackを残さず途中失敗を発生させる。"""
        registries.append(registry)
        result = original_register(registry, callback_id)
        if len(registries) == 2:
            raise RuntimeError("registration failed")
        return result

    monkeypatch.setattr(MayaCallbackRegistry, "register", failing_register)
    with pytest.raises(RuntimeError, match="registration failed"):
        float_binding(nodes, owner)
    assert registries and all(registry.is_disposed for registry in registries)


def test_non_unique_leaf_writes_only_canonical_target(scene):
    """同名leafが最上位とcompound配下にあっても意図した実体だけを変更する。"""
    _, owner = scene
    nodes = [cmds.createNode("hierarchyTestNode4") for _ in range(2)]
    paths = (".envelope", "kitA.envelope", "kitB.envelope")
    plugs = [
        [resolve_float_plug(node, path) for path in paths] for node in nodes
    ]
    for index, path in enumerate(paths):
        binding = float_binding(nodes, owner, path)
        try:
            before = [[plug.plug.asDouble() for plug in row] for row in plugs]
            value = 0.125 * (index + 1)
            assert binding.set_value(value)
            for row, original in zip(plugs, before):
                expected = list(original)
                expected[index] = value
                assert [plug.plug.asDouble() for plug in row] == expected
        finally:
            binding.dispose()
