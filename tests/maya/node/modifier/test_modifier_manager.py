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


def _anim_curve_fn(maya_om, node_name):
    from maya.api import OpenMayaAnim as oma

    selection = maya_om.MSelectionList()
    selection.add(node_name)
    return oma.MFnAnimCurve(selection.getDependNode(0))


def test_animation_changes_keep_dg_dag_order_and_do_not_reapply_callbacks(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    from maya.api import OpenMayaAnim as oma

    manager = modifier_manager
    target = manager.dag_mod.createNode("transform")
    manager.dag_mod.renameNode(target, "animation_history_target")
    manager.do_it_dag()
    target_fn = maya_om.MFnDependencyNode(target)
    curve = manager.dg_mod.createNode("animCurveTL")
    manager.dg_mod.renameNode(curve, "animation_history_curve")
    curve_fn = maya_om.MFnDependencyNode(curve)
    manager.dg_mod.connect(
        curve_fn.findPlug("output", False),
        target_fn.findPlug("translateX", False),
    )
    calls = []

    def add_key(change):
        assert maya_cmds.objExists("animation_history_curve")
        fn = oma.MFnAnimCurve(curve)
        assert fn.numKeys == 0
        fn.addKey(maya_om.MTime(1, maya_om.MTime.uiUnit()), 3, change=change)
        calls.append("add")

    manager.queue_anim_curve_change(add_key)
    manager.dg_mod.renameNode(curve, "animation_history_renamed")

    def change_key(change):
        assert maya_cmds.objExists("animation_history_renamed")
        fn = oma.MFnAnimCurve(curve)
        assert fn.value(0) == 3
        fn.setValue(0, 7, change=change)
        calls.append("change")

    manager.queue_anim_curve_change(change_key)
    manager.dg_mod.renameNode(curve, "animation_history_final")

    assert calls == []
    assert not maya_cmds.objExists("animation_history_curve")
    manager.do_it_dg()
    manager.dag_mod.renameNode(target, "animation_history_final_target")
    manager.do_it_dag()

    for _ in range(2):
        assert calls == ["add", "change"]
        assert maya_cmds.objExists("animation_history_final")
        assert (
            maya_cmds.getAttr(
                "animation_history_final_target.translateX", time=1
            )
            == 7
        )
        manager.undo_it()
        assert not maya_cmds.objExists("animation_history_final")
        assert not maya_cmds.objExists("animation_history_final_target")
        assert not manager.can_undo
        assert manager.can_redo
        manager.redo_it()
        assert manager.can_undo
        assert not manager.can_redo


@pytest.mark.parametrize("failure_kind", ["animation", "dg"])
def test_failed_mixed_flush_restores_existing_keys_and_all_its_dg_steps(
    modifier_manager,
    maya_cmds,
    maya_om,
    failure_kind,
):
    manager = modifier_manager
    curve_name = maya_cmds.createNode("animCurveTU", name="failure_curve")
    maya_cmds.setKeyframe(curve_name, time=1, value=2)
    fn = _anim_curve_fn(maya_om, curve_name)
    previous = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous, "animation_previous_success")
    manager.do_it_dg()
    current = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(current, "animation_failed_flush")
    calls = []

    def first_change(change):
        fn.setValue(0, 7, change=change)
        calls.append("first")

    manager.queue_anim_curve_change(first_change)
    manager.dg_mod.renameNode(fn.object(), "renamed_failure_curve")

    def failing_change(change):
        assert fn.value(0) == 7
        fn.setValue(0, 9, change=change)
        calls.append("second")
        if failure_kind == "animation":
            raise RuntimeError("intentional animation callback failure")

    manager.queue_anim_curve_change(failing_change)
    if failure_kind == "dg":
        manager.dg_mod.pythonCommandToExecute(
            partial(maya_cmds.setKeyframe, "missing_node.translateX", time=1)
        )
    pending = manager.dag_mod.createNode("transform")
    manager.dag_mod.renameNode(pending, "animation_discarded_pending")

    with pytest.raises(RuntimeError):
        manager.do_it_dg()

    assert calls == ["first", "second"]
    assert fn.value(0) == 2
    assert maya_cmds.objExists(curve_name)
    assert not maya_cmds.objExists("renamed_failure_curve")
    assert not maya_cmds.objExists("animation_failed_flush")
    assert maya_cmds.objExists("animation_previous_success")
    assert manager.can_undo
    assert not manager.can_redo
    manager.do_it_dg()
    manager.do_it_dag()
    assert calls == ["first", "second"]
    assert not maya_cmds.objExists("animation_discarded_pending")
    manager.undo_it()
    assert fn.value(0) == 2
    assert not maya_cmds.objExists("animation_previous_success")
    manager.redo_it()
    assert fn.value(0) == 2
    assert maya_cmds.objExists("animation_previous_success")


@pytest.mark.parametrize("discard", ["clear", "rollback"])
def test_discard_removes_pending_animation_and_split_dg_buffers(
    modifier_manager,
    maya_cmds,
    discard,
):
    manager = modifier_manager
    calls = []
    first = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(first, "discard_animation_first")
    manager.queue_anim_curve_change(lambda change: calls.append(change))
    second = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(second, "discard_animation_second")

    assert not manager.can_undo
    assert not manager.can_redo
    getattr(manager, discard)()
    assert not manager.can_undo
    assert not manager.can_redo
    manager.do_it_dg()
    assert calls == []
    assert not maya_cmds.objExists("discard_animation_first")
    assert not maya_cmds.objExists("discard_animation_second")


def test_rollback_restores_animation_history_and_discards_later_callback(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    manager = modifier_manager
    curve = maya_cmds.createNode("animCurveTU")
    maya_cmds.setKeyframe(curve, time=1, value=2)
    fn = _anim_curve_fn(maya_om, curve)
    manager.queue_anim_curve_change(
        lambda change: fn.setValue(0, 7, change=change)
    )
    manager.do_it_dg()
    assert fn.value(0) == 7
    calls = []
    manager.queue_anim_curve_change(lambda change: calls.append(change))

    manager.rollback()

    assert fn.value(0) == 2
    assert not manager.can_undo
    assert not manager.can_redo
    manager.do_it_dg()
    assert calls == []
    assert fn.value(0) == 2


def test_new_animation_execution_discards_old_redo_history(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    manager = modifier_manager
    curve = maya_cmds.createNode("animCurveTU")
    maya_cmds.setKeyframe(curve, time=1, value=2)
    fn = _anim_curve_fn(maya_om, curve)
    manager.queue_anim_curve_change(
        lambda change: fn.setValue(0, 7, change=change)
    )
    manager.do_it_dg()
    manager.undo_it()
    assert fn.value(0) == 2
    assert manager.can_redo
    manager.queue_anim_curve_change(
        lambda change: fn.setValue(0, 9, change=change)
    )
    manager.do_it_dg()
    assert fn.value(0) == 9
    assert manager.can_undo
    assert not manager.can_redo
    manager.undo_it()
    assert fn.value(0) == 2
    manager.redo_it()
    assert fn.value(0) == 9


def test_failed_animation_redo_restores_its_flush_and_preserves_prior_flush(
    modifier_manager,
    maya_cmds,
    maya_om,
    monkeypatch,
):
    from maya.api import OpenMayaAnim as oma

    manager = modifier_manager
    curve = maya_cmds.createNode("animCurveTU", name="animation_redo_curve")
    maya_cmds.setKeyframe(curve, time=1, value=2)
    fn = _anim_curve_fn(maya_om, curve)

    class FailingRedoChange(oma.MAnimCurveChange):
        fail_on_redo = False

        def redoIt(self):
            super().redoIt()
            if self.fail_on_redo:
                raise RuntimeError("intentional animation redo failure")

    monkeypatch.setattr(oma, "MAnimCurveChange", FailingRedoChange)
    previous = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous, "animation_redo_previous")
    manager.do_it_dg()
    current = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(current, "animation_redo_current")
    caches = []

    def change_key(change):
        fn.setValue(0, 7, change=change)
        caches.append(change)

    manager.queue_anim_curve_change(change_key)
    manager.dg_mod.renameNode(fn.object(), "animation_redo_renamed")
    manager.do_it_dg()
    manager.undo_it()
    caches[0].fail_on_redo = True

    with pytest.raises(
        RuntimeError, match="intentional animation redo failure"
    ):
        manager.redo_it()

    assert len(caches) == 1
    assert fn.value(0) == 2
    assert maya_cmds.objExists(curve)
    assert maya_cmds.objExists("animation_redo_previous")
    assert not maya_cmds.objExists("animation_redo_current")
    assert not maya_cmds.objExists("animation_redo_renamed")
    assert manager.can_undo
    assert not manager.can_redo
    manager.rollback()
    assert not maya_cmds.objExists("animation_redo_previous")
    assert fn.value(0) == 2


def test_deferred_dg_prepares_after_prior_edits_and_redo_does_not_prepare_again(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    manager = modifier_manager
    curve = maya_cmds.createNode("animCurveTU", name="prepare_curve")
    maya_cmds.setKeyframe(curve, time=1, value=2)
    fn = _anim_curve_fn(maya_om, curve)
    target = maya_cmds.createNode("transform", name="prepare_target")
    selection = maya_om.MSelectionList()
    selection.add(f"{target}.translateY")
    plug = selection.getPlug(0)
    calls = []
    manager.dg_mod.renameNode(fn.object(), "prepare_curve_renamed")
    manager.queue_anim_curve_change(
        lambda change: fn.setValue(0, 7, change=change)
    )

    def prepare(modifier):
        assert maya_cmds.objExists("prepare_curve_renamed")
        assert fn.value(0) == 7
        assert plug.asDouble() == 0
        modifier.newPlugValueDouble(plug, fn.value(0))
        assert plug.asDouble() == 0
        calls.append("prepare")

    manager.queue_dg_modifier(prepare)

    def edit_after_prepared_modifier(change):
        assert plug.asDouble() == 7
        fn.setValue(0, 9, change=change)
        calls.append("animation")

    manager.queue_anim_curve_change(edit_after_prepared_modifier)
    manager.dg_mod.renameNode(fn.object(), "prepare_curve_final")
    assert fn.value(0) == 2
    assert calls == []
    assert maya_cmds.objExists(curve)
    assert plug.asDouble() == 0
    manager.do_it_dg()

    for _ in range(2):
        assert calls == ["prepare", "animation"]
        assert fn.value(0) == 9
        assert plug.asDouble() == 7
        assert maya_cmds.objExists("prepare_curve_final")
        manager.undo_it()
        assert fn.value(0) == 2
        assert plug.asDouble() == 0
        assert maya_cmds.objExists(curve)
        manager.redo_it()


@pytest.mark.parametrize("failure_stage", ["prepare", "execute"])
def test_deferred_dg_failure_restores_mixed_flush_and_discards_queued_values(
    modifier_manager,
    maya_cmds,
    maya_om,
    failure_stage,
):
    manager = modifier_manager
    curve = maya_cmds.createNode("animCurveTU", name="prepare_failure_curve")
    maya_cmds.setKeyframe(curve, time=1, value=2)
    fn = _anim_curve_fn(maya_om, curve)
    target = maya_cmds.createNode("transform", name="prepare_failure_target")
    selection = maya_om.MSelectionList()
    selection.add(f"{target}.translateY")
    plug = selection.getPlug(0)
    previous = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(previous, "prepare_failure_previous")
    manager.do_it_dg()
    current = manager.dg_mod.createNode("network")
    manager.dg_mod.renameNode(current, "prepare_failure_current")
    manager.dg_mod.newPlugValueDouble(plug, 3)
    manager.queue_anim_curve_change(
        lambda change: fn.setValue(0, 7, change=change)
    )
    calls = []

    def prepare(modifier):
        assert fn.value(0) == 7
        assert plug.asDouble() == 3
        modifier.newPlugValueDouble(plug, 99)
        calls.append("prepare")
        if failure_stage == "prepare":
            raise RuntimeError("intentional DG preparation failure")
        modifier.pythonCommandToExecute(
            partial(maya_cmds.setKeyframe, "missing_node.translateX", time=1)
        )

    manager.queue_dg_modifier(prepare)
    manager.dg_mod.renameNode(fn.object(), "discarded_prepare_rename")
    with pytest.raises(RuntimeError):
        manager.do_it_dg()

    assert calls == ["prepare"]
    assert fn.value(0) == 2
    assert plug.asDouble() == 0
    assert maya_cmds.objExists(curve)
    assert not maya_cmds.objExists("discarded_prepare_rename")
    assert not maya_cmds.objExists("prepare_failure_current")
    assert maya_cmds.objExists("prepare_failure_previous")
    assert manager.can_undo
    assert not manager.can_redo
    manager.do_it_dg()
    assert calls == ["prepare"]
    assert fn.value(0) == 2
    assert plug.asDouble() == 0
    manager.undo_it()
    assert not maya_cmds.objExists("prepare_failure_previous")
    manager.redo_it()
    assert calls == ["prepare"]
    assert maya_cmds.objExists("prepare_failure_previous")
    assert fn.value(0) == 2
    assert plug.asDouble() == 0
