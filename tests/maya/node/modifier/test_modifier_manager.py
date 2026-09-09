# coding: utf-8
from __future__ import annotations

from functools import partial

import pytest

pytestmark = pytest.mark.maya


def test_do_it_dg_undo_redo(modifier_manager, maya_cmds):
    manager = modifier_manager
    first_dg_mod = manager.dg_mod

    m_obj = manager.dg_mod.createNode("plusMinusAverage")
    manager.dg_mod.renameNode(m_obj, "manager_dg")

    assert not maya_cmds.objExists("manager_dg")

    manager.do_it_dg()

    assert maya_cmds.objExists("manager_dg")
    assert manager.dg_mod is not first_dg_mod
    assert manager.can_undo
    assert not manager.can_redo

    manager.undo_it()

    assert not maya_cmds.objExists("manager_dg")
    assert not manager.can_undo
    assert manager.can_redo

    manager.redo_it()

    assert maya_cmds.objExists("manager_dg")
    assert manager.can_undo
    assert not manager.can_redo


def test_do_it_dag_undo_redo(modifier_manager, maya_cmds):
    manager = modifier_manager
    first_dag_mod = manager.dag_mod

    m_obj = manager.dag_mod.createNode("transform")
    manager.dag_mod.renameNode(m_obj, "manager_dag")
    manager.do_it_dag()

    assert maya_cmds.objExists("manager_dag")
    assert manager.dag_mod is not first_dag_mod

    manager.undo_it()

    assert not maya_cmds.objExists("manager_dag")

    manager.redo_it()

    assert maya_cmds.objExists("manager_dag")


def test_mixed_dag_and_dg_history_is_one_command(
    modifier_manager,
    maya_cmds,
):
    manager = modifier_manager

    m_obj = manager.dag_mod.createNode("transform")
    manager.dag_mod.renameNode(m_obj, "manager_mixed")
    manager.do_it_dag()

    manager.dg_mod.renameNode(m_obj, "manager_mixed_renamed")
    manager.do_it_dg()

    assert not maya_cmds.objExists("manager_mixed")
    assert maya_cmds.objExists("manager_mixed_renamed")

    manager.undo_it()

    assert not maya_cmds.objExists("manager_mixed")
    assert not maya_cmds.objExists("manager_mixed_renamed")

    manager.redo_it()

    assert not maya_cmds.objExists("manager_mixed")
    assert maya_cmds.objExists("manager_mixed_renamed")


def test_redo_without_undo_raises(modifier_manager):
    manager = modifier_manager

    with pytest.raises(RuntimeError):
        manager.redo_it()

    m_obj = manager.dg_mod.createNode("plusMinusAverage")
    manager.dg_mod.renameNode(m_obj, "manager_redo_without_undo")
    manager.do_it_dg()

    with pytest.raises(RuntimeError):
        manager.redo_it()


def test_new_do_after_undo_discards_redo_stack(
    modifier_manager,
    maya_cmds,
):
    manager = modifier_manager

    first_obj = manager.dg_mod.createNode("plusMinusAverage")
    manager.dg_mod.renameNode(first_obj, "manager_first")
    manager.do_it_dg()

    manager.undo_it()

    assert not maya_cmds.objExists("manager_first")
    assert manager.can_redo

    second_obj = manager.dg_mod.createNode("plusMinusAverage")
    manager.dg_mod.renameNode(second_obj, "manager_second")
    manager.do_it_dg()

    assert not manager.can_redo
    assert not maya_cmds.objExists("manager_first")
    assert maya_cmds.objExists("manager_second")

    with pytest.raises(RuntimeError):
        manager.redo_it()


def test_clear_resets_current_modifiers_and_history(
    modifier_manager,
    maya_cmds,
):
    manager = modifier_manager
    first_dg_mod = manager.dg_mod
    first_dag_mod = manager.dag_mod

    m_obj = manager.dg_mod.createNode("plusMinusAverage")
    manager.dg_mod.renameNode(m_obj, "manager_clear")
    manager.do_it_dg()

    assert maya_cmds.objExists("manager_clear")

    manager.clear()

    assert manager.dg_mod is not first_dg_mod
    assert manager.dag_mod is not first_dag_mod
    assert not manager.can_undo
    assert not manager.can_redo

    with pytest.raises(RuntimeError):
        manager.undo_it()


def test_rollback_undoes_history_and_discards_pending_state(
    modifier_manager,
    maya_cmds,
):
    manager = modifier_manager

    executed_obj = manager.dg_mod.createNode("plusMinusAverage")
    manager.dg_mod.renameNode(executed_obj, "manager_rollback_executed")
    manager.do_it_dg()

    pending_obj = manager.dag_mod.createNode("transform")
    manager.dag_mod.renameNode(pending_obj, "manager_rollback_pending")

    manager.rollback()

    assert not maya_cmds.objExists("manager_rollback_executed")
    assert not maya_cmds.objExists("manager_rollback_pending")
    assert not manager.can_undo
    assert not manager.can_redo

    manager.do_it_dag()
    assert not maya_cmds.objExists("manager_rollback_pending")


@pytest.mark.parametrize("kind", ["dg", "dag"])
@pytest.mark.parametrize("existing_key", [False, True])
def test_failed_modifier_restores_partial_edits_and_preserves_history(
    modifier_manager,
    maya_cmds,
    maya_om,
    kind,
    existing_key,
):
    manager = modifier_manager
    node_name = maya_cmds.createNode("transform", name="failure_target")
    if existing_key:
        maya_cmds.setKeyframe(f"{node_name}.translateX", time=1, value=2)

    previous_obj = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous_obj, "previous_success")
    manager.do_it_dg()

    modifier = getattr(manager, f"{kind}_mod")
    selection = maya_om.MSelectionList()
    selection.add(f"{node_name}.translateY")
    modifier.newPlugValueDouble(selection.getPlug(0), 12.0)
    modifier.pythonCommandToExecute(
        partial(
            maya_cmds.setKeyframe, f"{node_name}.translateX", time=1, value=7
        )
    )
    modifier.pythonCommandToExecute(
        partial(maya_cmds.setKeyframe, "missing_node.translateX", time=1)
    )
    other_kind = "dag" if kind == "dg" else "dg"
    other_modifier = getattr(manager, f"{other_kind}_mod")
    pending_obj = other_modifier.createNode(
        "transform" if other_kind == "dag" else "network"
    )
    other_modifier.renameNode(pending_obj, "discarded_pending")

    with pytest.raises(RuntimeError):
        getattr(manager, f"do_it_{kind}")()

    assert maya_cmds.getAttr(f"{node_name}.translateY") == 0.0
    assert maya_cmds.keyframe(
        f"{node_name}.translateX", query=True, valueChange=True
    ) == ([2.0] if existing_key else None)
    assert maya_cmds.objExists("previous_success")
    assert manager.can_undo
    assert not manager.can_redo

    manager.do_it_dg()
    manager.do_it_dag()
    assert not maya_cmds.objExists("discarded_pending")
    manager.undo_it()
    assert not maya_cmds.objExists("previous_success")
    manager.redo_it()
    assert maya_cmds.objExists("previous_success")
    assert maya_cmds.keyframe(
        f"{node_name}.translateX", query=True, valueChange=True
    ) == ([2.0] if existing_key else None)


def test_failed_redo_restores_partial_edits_and_discards_redo(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    manager = modifier_manager
    node_name = maya_cmds.createNode("transform", name="redo_failure_target")
    previous_obj = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous_obj, "redo_previous_success")
    manager.do_it_dg()

    class FailingRedoModifier(maya_om.MDGModifier):
        fail_on_redo = False

        def doIt(self):
            super().doIt()
            if self.fail_on_redo:
                raise RuntimeError("intentional redo failure")

    modifier = FailingRedoModifier()
    manager._dg_mod = modifier
    modifier.pythonCommandToExecute(
        partial(
            maya_cmds.setKeyframe, f"{node_name}.translateX", time=1, value=7
        )
    )
    manager.do_it_dg()
    manager.undo_it()
    modifier.fail_on_redo = True

    with pytest.raises(RuntimeError, match="intentional redo failure"):
        manager.redo_it()

    assert maya_cmds.objExists("redo_previous_success")
    assert not maya_cmds.keyframe(
        f"{node_name}.translateX", query=True, keyframeCount=True
    )
    assert manager.can_undo
    assert not manager.can_redo
    manager.rollback()
    assert not maya_cmds.objExists("redo_previous_success")


def test_new_execution_failure_discards_previous_redo_history(
    modifier_manager,
    maya_cmds,
):
    manager = modifier_manager
    previous_obj = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous_obj, "discarded_redo")
    manager.do_it_dg()
    manager.undo_it()
    assert manager.can_redo

    manager.dg_mod.pythonCommandToExecute(
        partial(maya_cmds.setKeyframe, "missing_node.translateX", time=1)
    )
    with pytest.raises(RuntimeError):
        manager.do_it_dg()

    assert not manager.can_undo
    assert not manager.can_redo
    with pytest.raises(RuntimeError, match="No undone modifier history"):
        manager.redo_it()
    assert not maya_cmds.objExists("discarded_redo")


def test_failed_modifier_preserves_original_error_when_recovery_fails(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    manager = modifier_manager
    previous_obj = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous_obj, "recovery_previous_success")
    manager.do_it_dg()
    original_error = RuntimeError("original execution failure")

    class FailingModifier(maya_om.MDGModifier):
        def doIt(self):
            raise original_error

        def undoIt(self):
            raise RuntimeError("intentional recovery failure")

    manager._dg_mod = FailingModifier()
    with pytest.raises(
        RuntimeError, match="original execution failure"
    ) as caught:
        manager.do_it_dg()

    assert caught.value is original_error
    assert any(
        "intentional recovery failure" in note
        for note in caught.value.__notes__
    )
    assert manager.can_undo
    assert not manager.can_redo
    manager.do_it_dg()
    manager.rollback()
    assert not maya_cmds.objExists("recovery_previous_success")
