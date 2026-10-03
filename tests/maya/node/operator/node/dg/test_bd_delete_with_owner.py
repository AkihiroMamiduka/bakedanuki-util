# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest
import bd_util as bdu

pytestmark = pytest.mark.maya


def _load_plugin(maya_cmds) -> None:
    default_path = (
        Path(__file__).resolve().parents[6]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / "maya2025"
        / "bdUtilNodes.mll"
    )
    plugin_path = Path(
        os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
    )
    if not plugin_path.is_file():
        pytest.skip("bdUtilNodes.mll is not built")
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)


def _create_setup(maya_cmds):
    owner = maya_cmds.createNode("transform", name="deleteOwner")
    child = maya_cmds.createNode("transform", name="deleteChild", parent=owner)
    guard = maya_cmds.createNode("bdDeleteWithOwner", name="deleteGuard")
    target = maya_cmds.createNode("multiplyDivide", name="deleteTarget")
    maya_cmds.connectAttr(f"{owner}.message", f"{guard}.owner")
    maya_cmds.connectAttr(f"{target}.message", f"{guard}.deleteTarget[0]")
    maya_cmds.connectAttr(f"{owner}.scale", f"{target}.input1")
    maya_cmds.connectAttr(f"{target}.output", f"{child}.scale")
    return owner, child, guard, target


def test_owner_delete_cascades_and_undo_redo_restores_connections(
    maya_cmds, maya_om, new_scene
):
    _load_plugin(maya_cmds)
    owner, child, guard, target = _create_setup(maya_cmds)

    assert maya_cmds.attributeQuery("deleteTarget", node=guard, multi=True)
    selection = maya_om.MSelectionList()
    selection.add(guard)
    assert maya_om.MFnDependencyNode(
        selection.getDependNode(0)
    ).typeId.id() == (0x0014271E)

    maya_cmds.delete(owner)
    assert not any(
        maya_cmds.objExists(node) for node in (owner, child, guard, target)
    )

    maya_cmds.undo()
    assert all(
        maya_cmds.objExists(node) for node in (owner, child, guard, target)
    )
    assert maya_cmds.isConnected(f"{owner}.message", f"{guard}.owner")
    assert maya_cmds.isConnected(
        f"{target}.message", f"{guard}.deleteTarget[0]"
    )
    assert maya_cmds.isConnected(f"{owner}.scale", f"{target}.input1")
    assert maya_cmds.isConnected(f"{target}.output", f"{child}.scale")

    maya_cmds.redo()
    assert not any(
        maya_cmds.objExists(node) for node in (owner, child, guard, target)
    )


def test_guard_direct_delete_removes_only_registered_target(
    maya_cmds, new_scene
):
    _load_plugin(maya_cmds)
    owner, child, guard, target = _create_setup(maya_cmds)
    unrelated = maya_cmds.createNode("multiplyDivide", name="unrelatedNode")

    maya_cmds.delete(guard)
    assert maya_cmds.objExists(owner)
    assert maya_cmds.objExists(child)
    assert not maya_cmds.objExists(guard)
    assert not maya_cmds.objExists(target)
    assert maya_cmds.objExists(unrelated)

    maya_cmds.undo()
    assert maya_cmds.objExists(guard)
    assert maya_cmds.objExists(target)
    assert maya_cmds.isConnected(
        f"{target}.message", f"{guard}.deleteTarget[0]"
    )

    maya_cmds.delete(owner)
    assert not maya_cmds.objExists(guard)
    assert not maya_cmds.objExists(target)


def test_disconnect_and_target_delete_do_not_cascade(maya_cmds, new_scene):
    _load_plugin(maya_cmds)
    owner, _, guard, target = _create_setup(maya_cmds)

    maya_cmds.disconnectAttr(f"{target}.message", f"{guard}.deleteTarget[0]")
    assert all(maya_cmds.objExists(node) for node in (owner, guard, target))

    maya_cmds.delete(target)
    assert maya_cmds.objExists(owner)
    assert maya_cmds.objExists(guard)


def test_two_sparse_targets_are_deleted_once(maya_cmds, new_scene):
    _load_plugin(maya_cmds)
    owner, _, guard, target = _create_setup(maya_cmds)
    other = maya_cmds.createNode("multiplyDivide", name="otherTarget")
    maya_cmds.connectAttr(f"{other}.message", f"{guard}.deleteTarget[3]")

    maya_cmds.delete(owner)
    assert not any(
        maya_cmds.objExists(node) for node in (guard, target, other)
    )
    maya_cmds.undo()
    assert all(maya_cmds.objExists(node) for node in (guard, target, other))
    assert maya_cmds.isConnected(
        f"{other}.message", f"{guard}.deleteTarget[3]"
    )


def test_target_cannot_be_registered_twice(maya_cmds, new_scene):
    _load_plugin(maya_cmds)
    _, _, guard, target = _create_setup(maya_cmds)
    other_guard = maya_cmds.createNode("bdDeleteWithOwner", name="otherGuard")

    with pytest.raises(RuntimeError):
        maya_cmds.connectAttr(f"{target}.message", f"{guard}.deleteTarget[3]")
    with pytest.raises(RuntimeError):
        maya_cmds.connectAttr(
            f"{target}.message", f"{other_guard}.deleteTarget[0]"
        )


def test_dag_target_is_rejected(maya_cmds, new_scene):
    _load_plugin(maya_cmds)
    owner, child, guard, _ = _create_setup(maya_cmds)
    with pytest.raises(RuntimeError):
        maya_cmds.connectAttr(f"{child}.message", f"{guard}.deleteTarget[3]")
    assert maya_cmds.objExists(owner)


def test_locked_target_is_rejected_or_skipped(maya_cmds, new_scene):
    _load_plugin(maya_cmds)
    owner = maya_cmds.createNode("transform", name="lockedOwner")
    guard = maya_cmds.createNode("bdDeleteWithOwner", name="lockedGuard")
    target = maya_cmds.createNode("multiplyDivide", name="lockedTarget")
    maya_cmds.connectAttr(f"{owner}.message", f"{guard}.owner")

    maya_cmds.lockNode(target, lock=True)
    with pytest.raises(RuntimeError):
        maya_cmds.connectAttr(f"{target}.message", f"{guard}.deleteTarget[0]")
    maya_cmds.lockNode(target, lock=False)
    maya_cmds.connectAttr(f"{target}.message", f"{guard}.deleteTarget[0]")
    maya_cmds.lockNode(target, lock=True)

    maya_cmds.delete(owner)
    assert not maya_cmds.objExists(guard)
    assert maya_cmds.objExists(target)


@pytest.mark.parametrize("owner_first", [True, False])
def test_owner_cannot_be_its_own_target(maya_cmds, new_scene, owner_first):
    _load_plugin(maya_cmds)
    owner = maya_cmds.createNode("multiplyDivide", name="dgOwner")
    guard = maya_cmds.createNode("bdDeleteWithOwner", name="selfTargetGuard")
    first, second = (
        (f"{guard}.owner", f"{guard}.deleteTarget[0]")
        if owner_first
        else (f"{guard}.deleteTarget[0]", f"{guard}.owner")
    )
    maya_cmds.connectAttr(f"{owner}.message", first)
    with pytest.raises(RuntimeError):
        maya_cmds.connectAttr(f"{owner}.message", second)


def test_owner_can_be_reconnected(maya_cmds, new_scene):
    _load_plugin(maya_cmds)
    owner, _, guard, target = _create_setup(maya_cmds)
    maya_cmds.disconnectAttr(f"{owner}.message", f"{guard}.owner")
    maya_cmds.delete(owner)
    assert maya_cmds.objExists(guard)
    assert maya_cmds.objExists(target)

    replacement = maya_cmds.createNode("transform", name="replacementOwner")
    maya_cmds.connectAttr(f"{replacement}.message", f"{guard}.owner")
    maya_cmds.delete(replacement)
    assert not maya_cmds.objExists(guard)
    assert not maya_cmds.objExists(target)


def test_node_operator_exposes_message_connections(
    maya_cmds, modifier_manager, new_scene
):
    _load_plugin(maya_cmds)
    owner = maya_cmds.createNode("transform", name="operatorOwner")
    target = maya_cmds.createNode("multiplyDivide", name="operatorTarget")

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    owner_op = nodes.existing(owner)
    target_op = nodes.existing(target)
    guard = nodes.create.bdDeleteWithOwner(name="operatorGuard")
    owner_op.message.connect(guard.owner)
    target_op.message.connect(guard.deleteTarget[next])
    modifier_manager.do_it_dg()

    assert maya_cmds.isConnected(f"{owner}.message", "operatorGuard.owner")
    assert maya_cmds.isConnected(
        f"{target}.message", "operatorGuard.deleteTarget[0]"
    )


def test_scene_reload_restores_owner_delete_callback(
    maya_cmds, new_scene, tmp_path
):
    _load_plugin(maya_cmds)
    owner, _, guard, target = _create_setup(maya_cmds)
    scene_path = tmp_path / "bd_delete_with_owner.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    maya_cmds.delete(owner)
    assert not maya_cmds.objExists(guard)
    assert not maya_cmds.objExists(target)
