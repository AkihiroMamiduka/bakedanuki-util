# coding: utf-8
import pytest
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaBoolPlugBinding, MayaBoolPlugStore
from bd_util.maya.ui.binding import MayaBoolPlugBinding as ModuleBinding
from bd_util.ui import BoolBinding, qt


def _flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QtCore.QEvent.Type.DeferredDelete
    )


@pytest.mark.parametrize("value", [False, True])
@pytest.mark.parametrize("locked", [False, True])
def test_plug_binding_reads_initial_state_without_writing(
    new_scene, maya_cmds, value, locked
):
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    name = f"{node.cmd_access_name}.visibility"
    maya_cmds.setAttr(name, value)
    maya_cmds.setAttr(name, lock=locked)
    maya_cmds.undoInfo(state=True)
    maya_cmds.flushUndo()
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaBoolPlugBinding(node.visibility)
    try:
        assert ModuleBinding is MayaBoolPlugBinding
        assert isinstance(binding, BoolBinding)
        assert isinstance(binding.store, MayaBoolPlugStore)
        assert binding.store.parent() is binding
        assert binding.view_model.parent() is binding
        assert binding.view_model.store is binding.store
        assert binding.store.view_model is binding.view_model
        assert binding.store.plug_operator.plug == node.visibility.plug
        assert binding.value is value
        assert binding.view_model.set_value_command.can_execute is not locked
        assert maya_cmds.getAttr(name) is value
        assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
        assert len(om.MMessage.nodeCallbacks(node.m_obj)) > len(callbacks)
    finally:
        binding.dispose()
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
        _flush()


def test_plug_binding_commands_external_changes_and_undo_share_notifications(
    new_scene, maya_cmds
):
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    name = f"{node.cmd_access_name}.visibility"
    binding = MayaBoolPlugBinding(node.visibility)
    changes = []
    binding.changed.connect(changes.append)
    try:
        maya_cmds.undoInfo(state=True)
        maya_cmds.flushUndo()
        assert changes == []
        assert binding.set_value(False)
        assert not binding.set_value(False)
        _flush()
        assert changes == [False]
        maya_cmds.undo()
        _flush()
        assert binding.value
        assert changes == [False, True]
        maya_cmds.redo()
        _flush()
        assert not binding.value
        assert changes == [False, True, False]
        maya_cmds.setAttr(name, True)
        _flush()
        assert binding.value
        assert not binding.refresh()
        assert changes == [False, True, False, True]
    finally:
        binding.dispose()
        _flush()


def test_plug_binding_tracks_lock_and_input_connection(new_scene, maya_cmds):
    source = maya_cmds.createNode("transform")
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    name = f"{node.cmd_access_name}.visibility"
    binding = MayaBoolPlugBinding(node.visibility)
    try:
        maya_cmds.setAttr(name, lock=True)
        _flush()
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value(False)
        assert binding.value
        maya_cmds.setAttr(name, lock=False)
        _flush()
        assert binding.view_model.set_value_command.can_execute
        maya_cmds.connectAttr(f"{source}.visibility", name)
        _flush()
        assert not binding.view_model.set_value_command.can_execute
        maya_cmds.setAttr(f"{source}.visibility", False)
        maya_cmds.getAttr(name)
        _flush()
        assert not binding.value
        maya_cmds.disconnectAttr(f"{source}.visibility", name)
        _flush()
        assert binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        _flush()


@pytest.mark.parametrize("during_change", [False, True])
def test_plug_binding_dispose_stops_callbacks_immediately(
    new_scene, maya_cmds, during_change
):
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    name = f"{node.cmd_access_name}.visibility"
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaBoolPlugBinding(node.visibility)
    view_model = binding.view_model
    changes = []
    binding.changed.connect(changes.append)
    try:
        if during_change:
            binding.changed.connect(binding.dispose)
            assert binding.set_value(False)
        else:
            binding.dispose()
        assert binding.is_disposed
        assert binding.store.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
        assert not view_model.set_value_command.can_execute
        assert not view_model.set_value_command.execute(True)
        maya_cmds.setAttr(name, not during_change)
        _flush()
        assert changes == ([False] if during_change else [])
        assert maya_cmds.objExists(node.cmd_access_name)
        with pytest.raises(RuntimeError, match="終了しています"):
            binding.refresh()
    finally:
        binding.dispose()
        _flush()


def test_plug_binding_parent_destruction_releases_callbacks(
    new_scene, maya_cmds
):
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QObject()
    binding = MayaBoolPlugBinding(node.visibility, parent=owner)
    owner.deleteLater()
    _flush()
    assert binding.is_disposed
    assert binding.store.is_disposed
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
    binding.dispose()


def test_node_removal_disables_plug_binding(new_scene, maya_cmds):
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    binding = MayaBoolPlugBinding(node.visibility)
    try:
        maya_cmds.delete(node.cmd_access_name)
        _flush()
        assert not binding.store.is_available
        assert binding.store.is_disposed
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value(False)
        assert not binding.refresh()
    finally:
        binding.dispose()
        _flush()


@pytest.mark.parametrize("failure", ["argument", "callbacks", "read"])
def test_plug_binding_construction_failure_leaves_no_callbacks(
    new_scene, maya_cmds, monkeypatch, failure
):
    node = Nodes().existing.transform(maya_cmds.createNode("transform"))
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QObject()
    original_register = MayaBoolPlugStore._register_callbacks

    def fail_register(self):
        original_register(self)
        raise ValueError("register failed")

    def fail_read(self):
        raise ValueError("read failed")

    if failure == "callbacks":
        monkeypatch.setattr(
            MayaBoolPlugStore, "_register_callbacks", fail_register
        )
    elif failure == "read":
        monkeypatch.setattr(MayaBoolPlugStore, "read", fail_read)
    try:
        if failure == "argument":
            with pytest.raises(TypeError, match="plug"):
                MayaBoolPlugBinding(object(), parent=owner)
        else:
            with pytest.raises(ValueError, match="failed"):
                MayaBoolPlugBinding(node.visibility, parent=owner)
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
        _flush()
        assert not owner.children()
    finally:
        owner.deleteLater()
        _flush()
