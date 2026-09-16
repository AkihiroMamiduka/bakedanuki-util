# coding: utf-8
import pytest
from maya import cmds

from bd_util import Nodes
from bd_util.maya.ui import (
    MayaEnumPlugsBinding,
    MayaEnumPlugView,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import EnumViewModel, qt

ENUM_NAME = "Negative=-2:Off=0:Preview=5:Final=10"


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def scene(new_scene):
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    for node, value in zip(nodes, (5, 0, -2)):
        cmds.addAttr(
            node,
            longName="mode",
            shortName="md",
            attributeType="enum",
            enumName=ENUM_NAME,
        )
        cmds.setAttr(node + ".mode", value)
    cmds.undoInfo(state=True)
    yield nodes, owner
    if qt.isValid(owner):
        owner.deleteLater()
    flush()


def group(nodes, owner, attribute="mode"):
    return MayaEnumPlugsBinding(
        [resolve_enum_plug(node, attribute) for node in nodes], parent=owner
    )


def values(nodes):
    return [cmds.getAttr(node + ".mode") for node in nodes]


def test_initial_refresh_and_external_changes_do_not_write(scene):
    nodes, owner = scene
    cmds.flushUndo()
    binding = group(nodes, owner)
    assert binding.value == 5
    assert binding.is_mixed
    assert binding.target_count == binding.writable_count == 3
    assert binding.definition.item_for_value(-2).name == "Negative"
    assert not binding.refresh()
    assert values(nodes) == [5, 0, -2]
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.setAttr(nodes[0] + ".mode", 10)
    flush()
    assert binding.value == 10
    assert values(nodes) == [10, 0, -2]
    cmds.undo()
    flush()
    assert binding.value == 5
    assert values(nodes) == [5, 0, -2]
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert values(nodes) == [10, 0, -2]


def test_same_representative_value_applies_once_and_notifies_state(scene):
    nodes, owner = scene
    binding = group(nodes, owner)
    changed = []
    states = []
    binding.changed.connect(changed.append)
    binding.state_changed.connect(lambda: states.append(binding.is_mixed))
    cmds.flushUndo()
    assert binding.apply_representative_value()
    assert values(nodes) == [5, 5, 5]
    assert changed == []
    assert states == [False]
    cmds.undo()
    flush()
    assert values(nodes) == [5, 0, -2]
    assert binding.is_mixed
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert values(nodes) == [5, 5, 5]
    cmds.flushUndo()
    assert not binding.set_value(5)
    assert not binding.refresh()
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize(
    "value,error",
    [
        (True, TypeError),
        (5.0, TypeError),
        ("5", TypeError),
        (1, ValueError),
        (2**80, ValueError),
    ],
)
def test_invalid_input_is_rejected_before_any_write(scene, value, error):
    nodes, owner = scene
    binding = group(nodes, owner)
    failures = []
    binding.edit_failed.connect(failures.append)
    cmds.flushUndo()
    with pytest.raises(error):
        binding.set_value(value)
    assert values(nodes) == [5, 0, -2]
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    if error is ValueError:
        assert failures


def test_unknown_values_are_preserved_and_undo_restores_them(scene):
    nodes, owner = scene
    cmds.setAttr(nodes[0] + ".mode", 1)
    binding = group(nodes, owner)
    assert binding.value == 1
    assert not binding.is_value_defined
    cmds.flushUndo()
    with pytest.raises(ValueError):
        binding.apply_representative_value()
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert binding.set_value(-2)
    assert values(nodes) == [-2, -2, -2]
    cmds.undo()
    flush()
    assert values(nodes) == [1, 0, -2]
    assert binding.value == 1


@pytest.mark.parametrize(
    "definition",
    [
        "Off=0:Different=5:Final=10:Negative=-2",
        "Negative=-2:Off=0:Preview=6:Final=10",
    ],
)
def test_constructor_rejects_mismatched_definitions_even_if_locked(
    scene, definition
):
    nodes, owner = scene
    cmds.addAttr(nodes[1] + ".mode", edit=True, enumName=definition)
    cmds.setAttr(nodes[1] + ".mode", lock=True)
    with pytest.raises(ValueError, match="enum定義"):
        group(nodes, owner)
    assert all(
        not registry.callback_ids
        for registry in owner.findChildren(MayaCallbackRegistry)
    )


def test_definition_mismatch_blocks_group_and_undo_recovers_without_echo(
    scene,
):
    nodes, owner = scene
    binding = group(nodes, owner)
    states = []
    changed = []
    binding.state_changed.connect(lambda: states.append(binding.target_states))
    binding.changed.connect(changed.append)
    cmds.addAttr(
        nodes[1] + ".mode",
        edit=True,
        enumName="Negative=-2:Off=0:Renamed=5:Final=10",
    )
    flush()
    assert not binding.view_model.set_value_command.can_execute
    assert binding.writable_count == 2
    assert binding.target_states[1].is_available
    assert "enum定義" in binding.target_states[1].reason
    assert not binding.set_value(10)
    assert values(nodes) == [5, 0, -2]
    count = len(states)
    binding.refresh()
    assert len(states) == count
    cmds.undo()
    flush()
    assert binding.view_model.set_value_command.can_execute
    assert binding.writable_count == 3
    assert changed == []
    assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
    cmds.redo()
    flush()
    assert not binding.view_model.set_value_command.can_execute
    for node in (nodes[0], nodes[2]):
        cmds.addAttr(
            node + ".mode",
            edit=True,
            enumName="Negative=-2:Off=0:Renamed=5:Final=10",
        )
    flush()
    assert binding.view_model.set_value_command.can_execute
    assert binding.definition.item_for_value(5).name == "Renamed"
    assert values(nodes) == [5, 0, -2]


def test_readonly_followers_skip_and_readonly_representative_blocks(scene):
    nodes, owner = scene
    binding = group(nodes, owner)
    cmds.setAttr(nodes[1] + ".mode", lock=True)
    assert binding.writable_count == 2
    assert binding.set_value(10)
    assert values(nodes) == [10, 0, 10]
    assert binding.is_mixed
    cmds.setAttr(nodes[0] + ".mode", lock=True)
    assert not binding.view_model.set_value_command.can_execute
    assert not binding.set_value(5)
    cmds.setAttr(nodes[0] + ".mode", lock=False)
    cmds.connectAttr(nodes[1] + ".mode", nodes[2] + ".mode")
    flush()
    assert binding.writable_count == 1
    assert "入力接続" in binding.target_states[2].reason
    cmds.setAttr(nodes[1] + ".mode", lock=False)
    cmds.setAttr(nodes[1] + ".mode", -2)
    flush()
    assert values(nodes) == [10, -2, -2]
    assert binding.is_mixed


@pytest.mark.parametrize("restore_fails", [False, True])
def test_partial_failure_restores_previous_values_and_reports_errors(
    scene, monkeypatch, restore_fails
):
    nodes, owner = scene
    cmds.setAttr(nodes[0] + ".mode", 1)
    binding = group(nodes, owner)
    real_set_attr = cmds.setAttr
    failed = False

    def set_attr(path, value):
        nonlocal failed
        if failed and restore_fails and value == 1:
            raise RuntimeError("restore failed")
        real_set_attr(path, value)
        if nodes[1] in path and value == 10 and not failed:
            failed = True
            raise RuntimeError("write failed")

    failures = []
    binding.edit_failed.connect(failures.append)
    monkeypatch.setattr(cmds, "setAttr", set_attr)
    with pytest.raises(ExceptionGroup if restore_fails else RuntimeError):
        binding.set_value(10)
    assert values(nodes) == ([10, 0, -2] if restore_fails else [1, 0, -2])
    assert binding.value == values(nodes)[0]
    assert failures
    monkeypatch.setattr(cmds, "setAttr", real_set_attr)
    cmds.setAttr(nodes[0] + ".rotateOrder", 2)
    cmds.undo()
    assert cmds.getAttr(nodes[0] + ".rotateOrder") == 0
    assert values(nodes) == ([10, 0, -2] if restore_fails else [1, 0, -2])


def test_definition_change_during_write_stops_and_restores_input(
    scene, monkeypatch
):
    nodes, owner = scene
    binding = group(nodes, owner)
    real_set_attr = cmds.setAttr
    changed = False

    def set_attr(path, value):
        nonlocal changed
        real_set_attr(path, value)
        if not changed and value == 10:
            changed = True
            cmds.addAttr(
                nodes[1] + ".mode",
                edit=True,
                enumName="Negative=-2:Off=0:Preview=5:Changed=10",
            )

    monkeypatch.setattr(cmds, "setAttr", set_attr)
    with pytest.raises(ValueError, match="enum定義"):
        binding.set_value(10)
    assert values(nodes) == [5, 0, -2]
    assert not binding.view_model.set_value_command.can_execute


def test_removed_targets_are_not_reconnected_after_undo(scene):
    nodes, owner = scene
    binding = group(nodes, owner)
    cmds.deleteAttr(nodes[1] + ".mode")
    flush()
    cmds.undo()
    flush()
    assert not binding.target_states[1].is_available
    binding.set_value(10)
    assert values(nodes) == [10, 0, 10]
    cmds.delete(nodes[0])
    flush()
    assert not binding.view_model.set_value_command.can_execute


@pytest.mark.parametrize(
    "ending", ["binding", "owner", "view_model", "view_model_delete", "store"]
)
def test_lifetime_releases_callbacks_and_disables_input(scene, ending):
    nodes, owner = scene
    binding = group(nodes, owner)
    vm = binding.view_model
    registries = binding.findChildren(MayaCallbackRegistry)
    assert len(registries) == 1
    assert len(registries[0].callback_ids) == 13
    if ending == "binding":
        binding.dispose()
    elif ending == "owner":
        owner.deleteLater()
    elif ending == "view_model":
        vm.dispose()
    elif ending == "view_model_delete":
        vm.deleteLater()
    else:
        binding.store.dispose()
    flush()
    assert all(not registry.callback_ids for registry in registries)
    if qt.isValid(vm):
        assert not vm.set_value_command.can_execute


def test_builtin_enums_share_one_nodes_callbacks_and_reject_bad_targets(scene):
    nodes, owner = scene
    node = Nodes().existing.transform(nodes[0])
    binding = MayaEnumPlugsBinding([node.rotateOrder], parent=owner)
    assert binding.set_value(node.rotateOrder.ZYX)
    assert binding.value == 5
    assert len(binding.findChildren(MayaCallbackRegistry)[0].callback_ids) == 7
    plug = resolve_enum_plug(nodes[0], "mode")
    for targets, error in (
        ([], ValueError),
        ([plug, plug], ValueError),
        ([resolve_float_plug(nodes[0], "tx")], TypeError),
    ):
        with pytest.raises(error):
            MayaEnumPlugsBinding(targets, parent=owner)
    vm = EnumViewModel()
    with pytest.raises(ValueError, match="構築時"):
        vm.attach_store(binding.store)
    vm.dispose()
    vm.deleteLater()
    with pytest.raises(RuntimeError, match="Python"):
        MayaEnumPlugView(
            binding.view_model,
            resolve_enum_plug(nodes[1], "rotateOrder"),
            owner,
        )


def test_registration_failure_releases_callbacks(scene, monkeypatch):
    nodes, owner = scene
    real_register = MayaCallbackRegistry.register
    registries = []

    def register(registry, callback_id):
        result = real_register(registry, callback_id)
        registries.append(registry)
        if len(registries) == 2:
            raise RuntimeError("registration failed")
        return result

    monkeypatch.setattr(MayaCallbackRegistry, "register", register)
    with pytest.raises(RuntimeError, match="registration failed"):
        group(nodes, owner)
    assert registries and all(
        not registry.callback_ids for registry in registries
    )


def test_compound_parent_lock_and_distinct_dag_paths(scene):
    nodes, owner = scene
    paths = []
    for parent in nodes[:2]:
        cmds.createNode("transform", name="same", parent=parent)
        path = "|" + parent + "|same"
        cmds.addAttr(
            path,
            longName="settings",
            attributeType="compound",
            numberOfChildren=1,
        )
        cmds.addAttr(
            path,
            longName="mode",
            attributeType="enum",
            enumName=ENUM_NAME,
            parent="settings",
        )
        paths.append(path)
    binding = group(paths, owner, "settings.mode")
    cmds.setAttr(paths[1] + ".settings", lock=True)
    assert binding.writable_count == 1
    assert binding.set_value(5)
    assert values(paths) == [5, 0]
    renamed = cmds.rename(paths[0], "renamed")
    assert binding.set_value(10)
    assert cmds.getAttr(renamed + ".mode") == 10


def test_reentrant_input_and_dispose_publish_latest_state(scene):
    nodes, owner = scene
    binding = group(nodes, owner)
    binding.changed.connect(
        lambda value: binding.set_value(0) if value == 10 else None
    )
    assert binding.set_value(10)
    assert values(nodes) == [0, 0, 0]
    assert binding.value == 0
    binding.state_changed.connect(binding.dispose)
    binding.set_value(5)
    assert values(nodes) == [5, 5, 5]
    assert binding.is_disposed
