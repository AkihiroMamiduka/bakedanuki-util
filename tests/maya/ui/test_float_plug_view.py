# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    MayaFloatPlugView,
    resolve_float_plug,
)
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import FloatBinding, FloatPresentation, FloatViewModel, qt


def test_readonly_python_rejects_maya_input_and_allows_explicit_redraw(node):
    @dataclass(frozen=True)
    class ReadOnly:
        value: float = 2

    data = ReadOnly()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.scale.scaleX
    )
    try:
        assert not binding.view_model.set_value_command.can_execute
        cmds.setAttr(f"{node.cmd_access_name}.sx", 3)
        flush()
        assert data.value == binding.value == 2
        assert not binding.maya_view.is_synchronized
        assert binding.maya_view.sync_from_view_model()
        assert node.scale.scaleX.get() == 2
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_unreadable_python_after_setter_preserves_error_until_repaired(node):
    class Model:
        broken = False
        error = RuntimeError("getter failed")

        @property
        def value(self):
            if self.broken:
                raise self.error
            return 2.0

        @value.setter
        def value(self, value):
            self.broken = True

    data = Model()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.scale.scaleX
    )
    try:
        cmds.setAttr(f"{node.cmd_access_name}.sx", 3)
        flush()
        assert binding.maya_view.last_sync_error is data.error
        assert binding.value == 2
        assert not binding.view_model.set_value_command.can_execute
        data.broken = False
        binding.refresh()
        assert binding.view_model.set_value_command.can_execute
        assert binding.maya_view.is_synchronized
        assert node.scale.scaleX.get() == 2
    finally:
        binding.dispose()
        flush()


def test_registry_disposal_releases_unit_callbacks_and_restores_presentation(
    node,
):
    data = Data(2)
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.translate.translateX
    )
    registry = binding.findChildren(MayaCallbackRegistry)[0]
    try:
        assert len(registry.callback_ids) == 4
        registry.dispose()
        assert registry.callback_ids == ()
        assert binding.maya_view.is_disposed
        assert binding.view_model.presentation == binding.store.presentation
        assert binding.set_value(3)
        assert node.translate.translateX.get() == 2
        cmds.currentUnit(linear="m")
        assert binding.view_model.presentation.suffix == ""
    finally:
        binding.dispose()
        flush()


@dataclass
class Data:
    value: float = 0.0


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def node(new_scene):
    linear = cmds.currentUnit(q=True, linear=True)
    angle = cmds.currentUnit(q=True, angle=True)
    cmds.currentUnit(linear="cm", angle="deg")
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield node
    cmds.currentUnit(linear=linear, angle=angle)
    flush()


@pytest.mark.parametrize(
    "attribute,value",
    [("tx", 123.456789123), ("rx", 450.123456789), ("sx", -2.123456789)],
)
def test_python_initial_commands_maya_input_undo_and_redo(
    node, attribute, value
):
    data = Data(value)
    plug = resolve_float_plug(node.cmd_access_name, attribute)
    binding = MayaFloatBinding.from_attribute(data, "value", maya_plug=plug)
    view = binding.maya_view
    try:
        assert data.value == value
        assert view.is_synchronized
        assert plug.get() == pytest.approx(value, rel=1e-14)
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert binding.set_value(20.125)
        assert data.value == 20.125
        assert plug.get() == pytest.approx(20.125)
        cmds.undo()
        flush()
        assert data.value == pytest.approx(value, rel=1e-14)
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert data.value == pytest.approx(20.125)
        assert cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.setAttr(f"{node.cmd_access_name}.{attribute}", 7.25)
        assert data.value == pytest.approx(20.125)
        assert not view.is_synchronized
        flush()
        assert binding.value == data.value == pytest.approx(7.25)
        assert view.is_synchronized
        assert view.last_sync_error is None
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "attribute,value,scale,suffix",
    [
        ("tx", 100.123456789, 0.01, " m"),
        ("rx", 90.123456789, 0.017453292519943295, " rad"),
    ],
)
def test_units_preserve_python_precision_pending_input_and_model_limits(
    node, attribute, value, scale, suffix
):
    data = Data(value)
    plug = resolve_float_plug(node.cmd_access_name, attribute)
    presentation = FloatPresentation(
        scale=2, suffix=" custom", minimum=-500, maximum=500
    )
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=plug, presentation=presentation
    )
    events = []
    binding.changed.connect(events.append)
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        cmds.currentUnit(linear="m", angle="rad")
        flush()
        assert data.value == value
        assert events == []
        assert binding.view_model.presentation == FloatPresentation(
            scale, suffix, -500, 500
        )
        assert binding.store.presentation == presentation
        assert not binding.set_value(value)
        assert data.value == value
        assert binding.maya_view.is_synchronized
        # unit event自身の履歴を除いた状態で、同値再同期が履歴を作らないことを確認する。
        cmds.flushUndo()
        assert not binding.refresh()
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        cmds.setAttr(f"{node.cmd_access_name}.{attribute}", 10 * scale)
        cmds.currentUnit(linear="cm", angle="deg")
        flush()
        assert data.value == pytest.approx(10)
        binding.maya_view.dispose()
        assert binding.view_model.presentation == presentation
        assert binding.set_value(200)
        assert plug.get() == pytest.approx(10)
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("confirmation", ["command", "refresh"])
def test_later_same_python_confirmation_wins_pending_maya_input(
    node, confirmation
):
    data = Data(1)
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.translate.translateX
    )
    try:
        cmds.setAttr(f"{node.cmd_access_name}.tx", 20)
        if confirmation == "command":
            assert not binding.set_value(1)
        else:
            assert not binding.refresh()
        flush()
        assert (
            binding.value == data.value == node.translate.translateX.get() == 1
        )
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "mode", ["round", "reject", "before", "after", "invalid"]
)
def test_maya_input_uses_setter_result_and_contains_original_failure(
    node, mode
):
    class Model:
        _value = 1.0
        writes = 0
        error = RuntimeError("setter failed")

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self.writes += 1
            if mode == "before":
                raise self.error
            if mode == "reject":
                return
            self._value = round(value, 1)
            if mode == "invalid":
                self._value = float("nan")
            if mode == "after":
                raise self.error

    data = Model()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.scale.scaleX
    )
    errors = []
    binding.maya_view.sync_failed.connect(errors.append)
    try:
        cmds.setAttr(f"{node.cmd_access_name}.sx", 3.14159)
        flush()
        assert data.writes == 1
        expected = 3.1 if mode in ("round", "after") else 1
        assert binding.value == expected
        if mode != "invalid":
            assert node.scale.scaleX.get() == expected
        if mode in ("before", "after"):
            assert binding.maya_view.last_sync_error is data.error
            assert errors[-1] is data.error
            assert binding.view_model.set_value_command.can_execute
        elif mode == "invalid":
            assert not binding.view_model.set_value_command.can_execute
            assert not binding.maya_view.is_synchronized
            data._value = 8
            assert binding.refresh()
            assert node.scale.scaleX.get() == 8
            assert binding.maya_view.is_synchronized
        else:
            assert not errors
            assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("parent", [False, True])
def test_lock_and_connection_keep_python_editable_and_resume(node, parent):
    data = Data(1)
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.translate.translateX
    )
    path = f"{node.cmd_access_name}.{'translate' if parent else 'translateX'}"
    try:
        cmds.setAttr(path, lock=True)
        flush()
        assert binding.set_value(5)
        assert data.value == 5
        assert node.translate.translateX.get() == 1
        assert binding.view_model.set_value_command.can_execute
        assert not binding.maya_view.is_synchronized
        cmds.setAttr(path, lock=False)
        flush()
        assert node.translate.translateX.get() == 5
        assert binding.maya_view.is_synchronized
        source = cmds.createNode("transform")
        source_path = f"{source}.{'translate' if parent else 'translateX'}"
        cmds.setAttr(f"{source}.tx", 20)
        cmds.connectAttr(source_path, path)
        flush()
        assert data.value == 5
        assert binding.set_value(7)
        assert node.translate.translateX.get() == 20
        cmds.disconnectAttr(source_path, path)
        flush()
        assert data.value == node.translate.translateX.get() == 7
        # 1tick内の接続・切断でも、一時的な評価値をPythonへ入力しない。
        cmds.connectAttr(source_path, path)
        cmds.disconnectAttr(source_path, path)
        flush()
        assert data.value == node.translate.translateX.get() == 7
    finally:
        binding.dispose()
        flush()


def test_float32_projection_never_rounds_python_or_creates_echo_undo(node):
    cmds.addAttr(
        node.cmd_access_name, longName="weight", attributeType="float"
    )
    data = Data(0.123456789012345)
    plug = resolve_float_plug(node.cmd_access_name, "weight")
    binding = MayaFloatBinding.from_attribute(data, "value", maya_plug=plug)
    try:
        assert data.value == 0.123456789012345
        assert plug.get() != data.value
        assert binding.maya_view.is_synchronized
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert not binding.refresh()
        flush()
        assert data.value == 0.123456789012345
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        assert binding.set_value(0.123456789012346)
        assert data.value == 0.123456789012346
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        assert binding.set_value(0.75)
        cmds.undo()
        flush()
        assert data.value == plug.get()
        cmds.redo()
        flush()
        assert data.value == 0.75
        assert binding.set_value(1e40)
        assert data.value == 1e40
        assert plug.get() == 0.75
        assert isinstance(binding.maya_view.last_sync_error, ValueError)
        assert binding.view_model.set_value_command.can_execute
        assert binding.set_value(0.5)
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_maya_hard_limits_are_sync_constraints_not_python_constraints(node):
    cmds.addAttr(
        node.cmd_access_name,
        longName="weight",
        attributeType="double",
        minValue=0,
        maxValue=1,
    )
    data = Data(0.5)
    binding = MayaFloatBinding.from_attribute(
        data,
        "value",
        maya_plug=resolve_float_plug(node.cmd_access_name, "weight"),
    )
    try:
        assert binding.view_model.presentation.minimum is None
        assert binding.set_value(2)
        assert data.value == 2
        assert cmds.getAttr(f"{node.cmd_access_name}.weight") == 0.5
        assert not binding.maya_view.is_synchronized
        assert binding.view_model.set_value_command.can_execute
        assert binding.set_value(0.25)
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_failed_initial_sync_single_view_and_callback_cleanup(node):
    binding = FloatBinding.from_attribute(Data(2), "value")
    owner = qt.QObject()
    plug = node.translate.translateX
    cmds.setAttr(f"{node.cmd_access_name}.tx", lock=True)
    try:
        with pytest.raises(RuntimeError, match="書き込めません"):
            MayaFloatPlugView(binding.view_model, plug, owner)
        flush()
        assert all(
            registry.is_disposed
            for registry in owner.findChildren(MayaCallbackRegistry)
        )
        assert binding.view_model.presentation == binding.store.presentation
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=False)
        view = MayaFloatPlugView(binding.view_model, plug, owner)
        with pytest.raises(RuntimeError, match="複数"):
            MayaFloatPlugView(binding.view_model, plug, owner)
        cmds.setAttr(f"{node.cmd_access_name}.tx", 3)
        view.dispose()
        flush()
        assert binding.value == 2
        assert binding.set_value(4)
        assert plug.get() == 3
        replacement = MayaFloatPlugView(binding.view_model, plug, owner)
        cmds.delete(node.cmd_access_name)
        assert replacement.is_disposed
        assert binding.set_value(5)
    finally:
        owner.deleteLater()
        binding.dispose()
        flush()


def test_view_requires_python_store_and_can_be_omitted(node):
    owner = qt.QObject()
    vm = FloatViewModel()
    with pytest.raises(RuntimeError, match="Storeを接続"):
        MayaFloatPlugView(vm, node.scale.scaleX, owner)
    maya_binding = MayaFloatPlugBinding(node.scale.scaleX)
    try:
        with pytest.raises(RuntimeError, match="Python側を正本"):
            MayaFloatPlugView(
                maya_binding.view_model, node.scale.scaleX, owner
            )
        binding = MayaFloatBinding.from_attribute(Data(2), "value")
        assert binding.maya_view is None
        assert binding.set_value(3)
        assert node.scale.scaleX.get() == 1
        binding.dispose()
    finally:
        maya_binding.dispose()
        vm.deleteLater()
        owner.deleteLater()
        flush()


@pytest.mark.parametrize(
    "linear,angle",
    [
        ("mm", "deg"),
        ("m", "rad"),
        ("km", "deg"),
        ("in", "rad"),
        ("ft", "deg"),
        ("yd", "rad"),
        ("mi", "deg"),
    ],
)
def test_unit_roundtrips_match_storage_without_tolerance_or_echo(
    node, linear, angle
):
    cmds.currentUnit(linear=linear, angle=angle)
    for plug in (node.translate.translateX, node.rotate.rotateX):
        data = Data(1.2345678912345)
        binding = MayaFloatBinding.from_attribute(
            data, "value", maya_plug=plug
        )
        try:
            for value in (
                123.456789123456,
                -3.141592653589793,
                1e-12,
                1e12,
                0,
            ):
                binding.set_value(value)
                assert binding.maya_view.is_synchronized
                assert data.value == value
                cmds.undoInfo(state=True)
                cmds.flushUndo()
                binding.refresh()
                flush()
                assert data.value == value
                assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        finally:
            binding.dispose()
            flush()


def test_undo_of_setter_correction_preserves_redo_instead_of_rewriting_history(
    node,
):
    class Model:
        _value = 1.0

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = round(value, 1)

    data = Model()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.scale.scaleX
    )
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        cmds.setAttr(f"{node.cmd_access_name}.sx", 3.14159)
        flush()
        assert data.value == node.scale.scaleX.get() == 3.1
        # 補正setAttrをUndoした値がsetterで再度補正されても、履歴を上書きしない。
        cmds.undo()
        flush()
        assert node.scale.scaleX.get() == 3.14159
        assert data.value == 3.1
        assert not binding.maya_view.is_synchronized
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.undo()
        flush()
        assert node.scale.scaleX.get() == data.value == 1
        cmds.redo()
        flush()
        assert node.scale.scaleX.get() == 3.14159
        assert data.value == 3.1
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert node.scale.scaleX.get() == data.value == 3.1
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()
