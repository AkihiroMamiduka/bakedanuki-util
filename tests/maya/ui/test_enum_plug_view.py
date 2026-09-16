# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaEnumBinding,
    MayaEnumPlugView,
    resolve_enum_plug,
)
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import EnumBinding, EnumDefinition, qt

DEFINITION = EnumDefinition.from_mapping({0: "Off", 5: "Preview", 10: "Final"})


@dataclass
class Data:
    mode: int = 5


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def plug(new_scene):
    node = cmds.createNode("network")
    cmds.addAttr(
        node,
        longName="mode",
        attributeType="enum",
        enumName="Off=0:Preview=5:Final=10",
    )
    yield resolve_enum_plug(node, "mode")
    flush()


def make_binding(data, plug):
    return MayaEnumBinding.from_attribute(
        data, "mode", definition=DEFINITION, maya_plug=plug
    )


def test_initial_python_value_bidirectional_input_and_history(plug):
    data = Data()
    binding = make_binding(data, plug)
    view = binding.maya_view
    try:
        assert plug.get() == data.mode == binding.value == 5
        assert view.is_synchronized
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        binding.set_value(10)
        assert plug.get() == 10
        cmds.undo()
        flush()
        assert data.mode == binding.value == 5
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert data.mode == 10
        cmds.setAttr(plug.plug.name(), 0)
        assert data.mode == 10
        flush()
        assert data.mode == binding.value == 0
        data.mode = 5
        binding.refresh()
        assert plug.get() == 5
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("confirmation", ["command", "refresh"])
def test_python_confirmation_wins_over_queued_maya_input(plug, confirmation):
    data = Data()
    binding = make_binding(data, plug)
    try:
        cmds.setAttr(plug.plug.name(), 10)
        if confirmation == "command":
            binding.set_value(5)
        else:
            binding.refresh()
        flush()
        assert data.mode == binding.value == plug.get() == 5
    finally:
        binding.dispose()
        flush()


def test_schema_mismatch_preserves_python_and_recovers_after_restore(plug):
    data = Data()
    binding = make_binding(data, plug)
    view = binding.maya_view
    try:
        cmds.addAttr(
            plug.plug.name(), edit=True, enumName="Off=0:Other=5:Final=10"
        )
        flush()
        assert not view.is_synchronized
        assert isinstance(view.last_sync_error, ValueError)
        binding.set_value(10)
        assert data.mode == 10
        assert plug.get() == 5
        assert (
            cmds.addAttr(plug.plug.name(), query=True, enumName=True)
            == "Off:Other=5:Final=10"
        )
        cmds.addAttr(
            plug.plug.name(), edit=True, enumName="Off=0:Preview=5:Final=10"
        )
        flush()
        assert plug.get() == data.mode == 10
        assert view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_initial_schema_mismatch_releases_callbacks_and_view_slot(plug):
    binding = EnumBinding.from_attribute(Data(), "mode", definition=DEFINITION)
    try:
        cmds.addAttr(plug.plug.name(), edit=True, enumName="A:B")
        with pytest.raises(ValueError):
            MayaEnumPlugView(binding.view_model, plug, binding)
        for registry in binding.findChildren(MayaCallbackRegistry):
            assert registry.callback_ids == ()
        cmds.addAttr(
            plug.plug.name(), edit=True, enumName="Off=0:Preview=5:Final=10"
        )
        view = MayaEnumPlugView(binding.view_model, plug, binding)
        assert view.is_synchronized
        with pytest.raises(RuntimeError):
            MayaEnumPlugView(binding.view_model, plug, binding)
        view.dispose()
    finally:
        binding.dispose()
        flush()


def test_lock_and_connections_preserve_python_and_resume_sync(plug):
    data = Data()
    binding = make_binding(data, plug)
    view = binding.maya_view
    try:
        cmds.setAttr(plug.plug.name(), lock=True)
        binding.set_value(10)
        assert data.mode == 10
        assert plug.get() == 5
        assert not view.is_synchronized
        cmds.setAttr(plug.plug.name(), lock=False)
        flush()
        assert view.is_synchronized
        assert plug.get() == 10
        source = cmds.createNode("network")
        cmds.addAttr(
            source,
            longName="mode",
            attributeType="enum",
            enumName="Off=0:Preview=5:Final=10",
        )
        cmds.connectAttr(source + ".mode", plug.plug.name())
        cmds.disconnectAttr(source + ".mode", plug.plug.name())
        flush()
        assert data.mode == plug.get() == 10
    finally:
        binding.dispose()
        flush()


def test_invalid_maya_input_rejected_and_setter_normalization_preserves_redo(
    plug,
):
    class Model:
        _mode = 0

        @property
        def mode(self):
            return self._mode

        @mode.setter
        def mode(self, value):
            self._mode = 5 if value == 10 else value

    data = Model()
    binding = make_binding(data, plug)
    view = binding.maya_view
    try:
        cmds.setAttr(plug.plug.name(), 1)
        flush()
        assert data.mode == plug.get() == 0
        assert isinstance(view.last_sync_error, ValueError)
        binding.refresh()
        cmds.flushUndo()
        cmds.setAttr(plug.plug.name(), 10)
        flush()
        assert data.mode == plug.get() == 5
        cmds.undo()
        flush()
        assert plug.get() == 10
        assert data.mode == 5
        assert not view.is_synchronized
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert data.mode == plug.get() == 5
        assert view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_python_readonly_and_maya_deletion(plug):
    @dataclass(frozen=True)
    class ReadOnly:
        mode: int = 5

    binding = make_binding(ReadOnly(), plug)
    view = binding.maya_view
    try:
        cmds.setAttr(plug.plug.name(), 10)
        flush()
        assert binding.value == 5
        assert not view.is_synchronized
        view.sync_from_view_model()
        assert plug.get() == 5
    finally:
        binding.dispose()
        flush()
    binding = make_binding(Data(), plug)
    try:
        cmds.delete(plug.node.cmd_access_name)
        assert binding.maya_view.is_disposed
        assert binding.set_value(10)
        assert binding.value == 10
    finally:
        binding.dispose()
        flush()
