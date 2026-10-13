# coding: utf-8
"""実Mayaのノード名を正本とするBindingの対象と寿命を確認する。"""

from pathlib import Path

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaNodeNameBinding, MayaNodeNameStore
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import StringBinding, StringViewModel, qt


def _flush() -> None:
    """Maya callbackから予約されたQt処理と遅延破棄を実行する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


def test_initial_binding_reads_without_rename_and_dispose_releases_callbacks(
    new_scene,
):
    """初期読取りはUndoを増やさず、終了時に監視を残さない。"""
    node = Nodes().existing(cmds.createNode("transform", name="boundNode"))
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaNodeNameBinding(node)
    try:
        assert isinstance(binding, StringBinding)
        assert isinstance(binding.store, MayaNodeNameStore)
        assert binding.store.node_operator is node
        assert binding.store.parent() is binding
        assert binding.view_model.store is binding.store
        assert binding.value == binding.store.read() == "boundNode"
        assert binding.store.is_available
        assert binding.store.is_writable
        assert binding.view_model.set_value_command.can_execute
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        assert len(om.MMessage.nodeCallbacks(node.m_obj)) > len(callbacks)
        registries = binding.findChildren(MayaCallbackRegistry)
        binding.dispose()
        assert binding.store.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
        assert all(not registry.callback_ids for registry in registries)
    finally:
        binding.dispose()
        _flush()


def test_store_attachment_is_explicit(new_scene):
    """Store単体はViewModelを勝手に接続せず、既存のString契約を守る。"""
    node = Nodes().existing(cmds.createNode("network", name="nameSource"))
    owner = qt.QObject()
    model = StringViewModel("detached", owner)
    store = MayaNodeNameStore(model, node, owner)
    try:
        assert model.store is None
        assert model.value.value == "detached"
        model.attach_store(store)
        assert model.value.value == "nameSource"
        assert store.write("renamedSource") == "renamedSource"
        _flush()
        assert model.value.value == "renamedSource"
    finally:
        store.dispose()
        model.dispose()
        owner.deleteLater()
        _flush()


def test_collision_external_rename_and_undo_redo_use_actual_name(new_scene):
    """衝突後の確定名と外部改名を追跡し、改名一回を一回Undoにする。"""
    cmds.createNode("transform", name="occupied")
    target = cmds.createNode("transform", name="target")
    binding = MayaNodeNameBinding(Nodes().existing(target))
    values = []
    binding.changed.connect(values.append)
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert binding.set_value("occupied")
        _flush()
        assert binding.value == "occupied1"
        assert cmds.objExists("|occupied1")
        assert values == ["occupied1"]
        assert not binding.set_value("occupied1")
        cmds.undo()
        _flush()
        assert binding.value == "target"
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        _flush()
        assert binding.value == "occupied1"
        cmds.rename("|occupied1", "externalName")
        _flush()
        assert binding.value == "externalName"
        assert values == ["occupied1", "target", "occupied1", "externalName"]
    finally:
        binding.dispose()
        _flush()


def test_binding_keeps_original_node_despite_selection_and_duplicate_dag_name(
    new_scene,
):
    """選択変更や同名の別DAGノードへ編集先を切り替えない。"""
    left = cmds.createNode("transform", name="left")
    right = cmds.createNode("transform", name="right")
    target = cmds.createNode("transform", name="child", parent=left)
    target_node = Nodes().existing(target)
    other = cmds.createNode("transform", name="child", parent=right)
    binding = MayaNodeNameBinding(target_node)
    try:
        cmds.select(other, replace=True)
        selected = cmds.ls(selection=True, long=True)
        assert binding.set_value("renamed")
        assert cmds.objExists("|left|renamed")
        assert cmds.objExists("|right|child")
        assert cmds.ls(selection=True, long=True) == selected
        assert binding.value == "renamed"
    finally:
        binding.dispose()
        _flush()


def test_parent_rename_does_not_stale_the_target_before_callback_flush(
    new_scene,
):
    """親の改名直後も同じ子実体の現在のパスへ書き込む。"""
    parent = cmds.createNode("transform", name="parentBefore")
    child = cmds.createNode("transform", name="childBefore", parent=parent)
    binding = MayaNodeNameBinding(Nodes().existing(child))
    try:
        cmds.rename(parent, "parentAfter")
        assert binding.set_value("childAfter")
        assert cmds.objExists("|parentAfter|childAfter")
        assert binding.value == "childAfter"
    finally:
        binding.dispose()
        _flush()


def test_namespace_is_preserved_with_relative_names_and_duplicate_dag_paths(
    new_scene,
):
    """relativeNames中も絶対namespaceと対象DAGを取り違えない。"""
    cmds.namespace(add="character")
    cmds.namespace(add="elsewhere")
    left = cmds.createNode("transform", name="character:left")
    right = cmds.createNode("transform", name="character:right")
    target = cmds.createNode("transform", name="character:child", parent=left)
    node = Nodes().existing(target)
    other = cmds.createNode("transform", name="character:child", parent=right)
    other_node = Nodes().existing(other)
    binding = MayaNodeNameBinding(node)
    try:
        cmds.namespace(set=":character")
        cmds.namespace(relativeNames=True)
        assert not binding.refresh()
        assert binding.value == "character:child"
        assert binding.set_value("localRename")
        assert binding.value == "character:localRename"
        assert om.MFnDependencyNode(node.m_obj).absoluteName() == (
            ":character:localRename"
        )
        assert om.MFnDependencyNode(other_node.m_obj).absoluteName() == (
            ":character:child"
        )

        # 現在namespaceが異なっても、同じ完全namespaceの入力を受理する
        cmds.namespace(set=":elsewhere")
        assert binding.set_value("character:qualifiedRename")
        assert binding.value == "character:qualifiedRename"
        assert binding.set_value(":character:absoluteRename")
        assert binding.value == "character:absoluteRename"
        assert cmds.namespace(query=True, relativeNames=True)
        assert (
            cmds.namespaceInfo(currentNamespace=True, absoluteName=True)
            == ":elsewhere"
        )
    finally:
        cmds.namespace(relativeNames=False)
        cmds.namespace(set=":")
        binding.dispose()
        _flush()


@pytest.mark.parametrize("requested", ["other:newName", ":other:newName"])
def test_namespace_move_is_rejected_without_changing_node(
    new_scene, requested
):
    """別namespaceへの移動要求は改名として実行しない。"""
    cmds.namespace(add="source")
    cmds.namespace(add="other")
    node = cmds.createNode("network", name="source:target")
    binding = MayaNodeNameBinding(Nodes().existing(node))
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        with pytest.raises(ValueError):
            binding.set_value(requested)
        assert binding.value == "source:target"
        assert cmds.objExists(":source:target")
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
        _flush()


def test_namespace_rename_is_observed_by_explicit_refresh(new_scene):
    """namespace自身の改名はrefreshで読み直し、次の入力も新namespaceへ送る。"""
    cmds.namespace(add="before")
    node = cmds.createNode("network", name="before:target")
    binding = MayaNodeNameBinding(Nodes().existing(node))
    try:
        cmds.namespace(rename=("before", "after"))
        binding.refresh()
        assert binding.value == "after:target"
        assert binding.set_value("renamed")
        assert cmds.objExists(":after:renamed")
    finally:
        binding.dispose()
        _flush()


@pytest.mark.parametrize("rename_shapes", [True, False])
def test_shape_rename_option_and_undo_follow_maya(new_scene, rename_shapes):
    """transformに同名prefixで付くshapeの改名方針をMayaへ渡す。"""
    transform = cmds.createNode("transform", name="shapeBefore")
    shape = cmds.createNode("mesh", name="shapeBeforeShape", parent=transform)
    shape_node = Nodes().existing(shape)
    binding = MayaNodeNameBinding(
        Nodes().existing(transform), rename_shapes=rename_shapes
    )
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert binding.set_value("shapeAfter")
        expected = "shapeAfterShape" if rename_shapes else "shapeBeforeShape"
        assert om.MFnDependencyNode(shape_node.m_obj).name() == expected
        cmds.undo()
        _flush()
        assert binding.value == "shapeBefore"
        assert (
            om.MFnDependencyNode(shape_node.m_obj).name() == "shapeBeforeShape"
        )
    finally:
        binding.dispose()
        _flush()


@pytest.mark.parametrize("lock_flag", ["lock", "lockName"])
def test_node_and_name_lock_are_read_only_until_refresh(new_scene, lock_flag):
    """node lockとname lockを再取得し、読取りを保って改名を禁止する。"""
    node = cmds.createNode("transform", name="lockedTarget")
    binding = MayaNodeNameBinding(Nodes().existing(node))
    try:
        if lock_flag == "lockName":
            cmds.lockNode(node, lock=False, lockName=True)
        else:
            cmds.lockNode(node, lock=True)
        binding.refresh()
        assert binding.value == "lockedTarget"
        assert binding.store.is_available
        assert not binding.store.is_writable
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value("forbidden")
        with pytest.raises(RuntimeError):
            binding.store.write("forbidden")
        cmds.lockNode(node, lock=False, lockName=False)
        binding.refresh()
        assert binding.view_model.set_value_command.can_execute
        assert binding.set_value("unlockedTarget")
    finally:
        binding.dispose()
        _flush()


def test_referenced_node_is_read_only(new_scene, tmp_path: Path):
    """参照ノードは表示できるが名前変更を許可しない。"""
    node = cmds.createNode("transform", name="referencedTarget")
    cmds.select(node, replace=True)
    source = str(tmp_path / "node_name_reference.ma")
    cmds.file(source, force=True, type="mayaAscii", exportSelected=True)
    cmds.file(new=True, force=True)
    cmds.file(source, reference=True, namespace="reference")
    binding = MayaNodeNameBinding(
        Nodes().existing(":reference:referencedTarget")
    )
    try:
        assert binding.value == "reference:referencedTarget"
        assert binding.store.is_available
        assert not binding.store.is_writable
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value("forbidden")
    finally:
        binding.dispose()
        _flush()


@pytest.mark.parametrize(
    "requested", ["", "node\x00name", "|node", "parent|child"]
)
def test_invalid_name_is_rejected_without_undo(new_scene, requested):
    """空文字、NUL、DAGパスを名前入力として実行しない。"""
    node = cmds.createNode("network", name="validName")
    binding = MayaNodeNameBinding(Nodes().existing(node))
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        with pytest.raises(ValueError):
            binding.set_value(requested)
        assert binding.value == "validName"
        assert cmds.objExists(node)
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
        _flush()


@pytest.mark.parametrize("restore", ["undo", "recreate"])
def test_deletion_permanently_stops_binding_before_restore(new_scene, restore):
    """削除直後のUndoや同名再生成で終了済みStoreを再接続しない。"""
    node = cmds.createNode("transform", name="deletedTarget")
    binding = MayaNodeNameBinding(Nodes().existing(node))
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        cmds.delete(node)
        if restore == "undo":
            cmds.undo()
        else:
            cmds.createNode("transform", name="deletedTarget")
        _flush()
        assert cmds.objExists("|deletedTarget")
        assert binding.store.is_disposed
        assert not binding.store.is_available
        assert not binding.store.is_writable
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value("forbidden")
        assert not binding.refresh()
        assert not cmds.objExists("|forbidden")
    finally:
        binding.dispose()
        _flush()


def test_parent_destruction_releases_callbacks_and_stops_pending_updates(
    new_scene,
):
    """Qt所有者の破棄が未処理の名前通知とMaya監視を終了する。"""
    node = Nodes().existing(cmds.createNode("network", name="ownedName"))
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QObject()
    binding = MayaNodeNameBinding(node, parent=owner)
    model = binding.view_model
    cmds.rename("ownedName", "pendingName")
    owner.deleteLater()
    _flush()
    assert binding.is_disposed
    assert binding.store.is_disposed
    assert model.is_disposed
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
    binding.dispose()


def test_store_destruction_releases_callbacks_while_owner_survives(new_scene):
    """StoreだけのQt破棄でも監視とCommandを終了し、所有者へ残さない。"""
    node = Nodes().existing(cmds.createNode("network", name="storeLifetime"))
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QObject()
    model = StringViewModel(parent=owner)
    store = MayaNodeNameStore(model, node, owner)
    model.attach_store(store)
    try:
        assert model.set_value_command.can_execute
        store.deleteLater()
        _flush()
        # DeferredDeleteから発生するqueuedの破棄通知まで進める
        _flush()
        assert qt.isValid(owner)
        assert not qt.isValid(store)
        assert store.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
        assert not model.set_value_command.can_execute
        assert not model.set_value_command.execute("forbidden")
        assert cmds.objExists("storeLifetime")
    finally:
        model.dispose()
        owner.deleteLater()
        _flush()
