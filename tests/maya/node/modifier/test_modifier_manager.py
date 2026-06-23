# coding: utf-8
from __future__ import annotations

import pytest


pytestmark = pytest.mark.maya


@pytest.fixture
def modifier_manager(maya_cmds, maya_om, new_scene):
    from bd_util.maya.node.modifier import ModifierManager

    return ModifierManager()


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
