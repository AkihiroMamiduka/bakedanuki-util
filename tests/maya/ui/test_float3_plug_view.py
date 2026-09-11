# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import (
    MayaFloat3Binding,
    MayaFloat3PlugBinding,
    MayaFloat3PlugView,
    MayaFloatPlugView,
    resolve_float3_plug,
)
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import Float3Binding, Float3ViewModel, FloatPresentation, qt


class Data:
    def __init__(self, value=(1.23456789123, 2.3456789123, 3.456789123)):
        self._value = value
        self.writes = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.writes.append(value)
        self._value = value


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def node(new_scene):
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    cmds.currentUnit(linear="cm", angle="deg")
    yield Nodes().existing.transform(cmds.createNode("transform"))
    cmds.currentUnit(linear=units[0], angle=units[1])
    flush()


@pytest.mark.parametrize("attribute", ["translate", "rotate", "scale"])
def test_initial_bulk_command_parent_input_and_single_undo(node, attribute):
    data = Data()
    initial = data.value
    plug = resolve_float3_plug(node.cmd_access_name, attribute)
    binding = MayaFloat3Binding.from_attribute(data, "value", maya_plug=plug)
    events = []
    binding.changed.connect(events.append)
    path = f"{node.cmd_access_name}.{attribute}"
    try:
        assert data.value == binding.value == initial
        assert data.writes == []
        assert cmds.getAttr(path)[0] == pytest.approx(initial)
        assert binding.maya_view.is_synchronized
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert binding.set_value((10, 20, 30))
        assert data.writes == [(10, 20, 30)]
        assert events == [(10, 20, 30)]
        cmds.undo()
        flush()
        assert data.value == pytest.approx(initial)
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert data.value == pytest.approx((10, 20, 30))
        assert binding.maya_view.is_synchronized
        data.writes.clear()
        events.clear()
        cmds.setAttr(path, 5, 6, 7, type="double3")
        assert data.writes == []
        flush()
        assert data.writes == [pytest.approx((5, 6, 7))]
        assert events == [pytest.approx((5, 6, 7))]
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("input_from", ["maya", "python"])
def test_axis_input_preserves_latest_other_axes_and_ignores_their_bounds(
    node, input_from
):
    data = Data((1, 2, 3))
    binding = MayaFloat3Binding.from_attribute(
        data,
        "value",
        maya_plug=node.translate,
        presentation=FloatPresentation(minimum=-10, maximum=10),
    )
    try:
        data._value = (1, 123.456789123456, -987.654321987654)
        if input_from == "maya":
            cmds.setAttr(f"{node.cmd_access_name}.tx", 4)
            flush()
        else:
            binding.view_model.x.set_value_command.execute(4)
        assert data.value == (4, 123.456789123456, -987.654321987654)
        assert data.writes == [data.value]
        assert binding.value == data.value
        assert tuple(node.translate.get()) == data.value
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("confirmation", ["axis", "bulk", "refresh"])
def test_later_same_value_python_confirmation_wins_queued_maya_edit(
    node, confirmation
):
    data = Data((1, 2, 3))
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.translate
    )
    try:
        cmds.setAttr(
            f"{node.cmd_access_name}.translate", 4, 5, 6, type="double3"
        )
        if confirmation == "axis":
            assert not binding.view_model.x.set_value_command.execute(1)
        elif confirmation == "bulk":
            assert not binding.set_value((1, 2, 3))
        else:
            assert not binding.refresh()
        flush()
        assert (
            data.value
            == binding.value
            == tuple(node.translate.get())
            == (1, 2, 3)
        )
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("parent", [False, True])
@pytest.mark.parametrize("restriction", ["lock", "connection"])
def test_pending_bulk_never_partially_writes_and_resumes(
    node, parent, restriction
):
    data = Data((1, 2, 3))
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.translate
    )
    path = f"{node.cmd_access_name}.{'translate' if parent else 'ty'}"
    source = cmds.createNode("transform")
    source_path = f"{source}.{'translate' if parent else 'ty'}"
    cmds.setAttr(f"{source}.translate", 20, 30, 40, type="double3")
    try:
        if restriction == "lock":
            cmds.setAttr(path, lock=True)
        else:
            cmds.connectAttr(source_path, path)
        flush()
        before = tuple(node.translate.get())
        assert data.value == (1, 2, 3)
        assert binding.set_value((4, 5, 6))
        assert tuple(node.translate.get()) == before
        assert all(
            vm.set_value_command.can_execute
            for vm in (
                binding.view_model.x,
                binding.view_model.y,
                binding.view_model.z,
            )
        )
        assert not binding.maya_view.is_synchronized
        if restriction == "lock":
            cmds.setAttr(path, lock=False)
        else:
            cmds.disconnectAttr(source_path, path)
        flush()
        assert tuple(node.translate.get()) == data.value == (4, 5, 6)
        assert binding.maya_view.is_synchronized
        if restriction == "connection":
            cmds.connectAttr(source_path, path)
            cmds.disconnectAttr(source_path, path)
            flush()
            assert tuple(node.translate.get()) == data.value == (4, 5, 6)
    finally:
        binding.dispose()
        flush()


def test_unaffected_locked_axis_allows_single_axis_write(node):
    data = Data((1, 2, 3))
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.translate
    )
    try:
        cmds.setAttr(f"{node.cmd_access_name}.ty", lock=True)
        flush()
        assert not binding.maya_view.is_writable
        assert binding.view_model.x.set_value_command.execute(4)
        assert tuple(node.translate.get()) == (4, 2, 3)
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "mode",
    [
        "round",
        "reject",
        "same_axis",
        "before",
        "after",
        "invalid",
        "unreadable",
    ],
)
@pytest.mark.parametrize("bulk", [False, True])
def test_setter_runs_once_and_all_corrected_axes_are_synchronized(
    node, mode, bulk
):
    class Model(Data):
        error = RuntimeError("setter or getter failed")
        broken = False

        @property
        def value(self):
            if self.broken:
                raise self.error
            return self._value

        @value.setter
        def value(self, value):
            self.writes.append(value)
            if mode == "before":
                raise self.error
            if mode == "reject":
                return
            self._value = (round(value[0], 1), 8, 9)
            if mode == "same_axis":
                self._value = (1, 8, 9)
            elif mode == "invalid":
                self._value = (1, float("nan"), 3)
            elif mode == "unreadable":
                self.broken = True
            elif mode == "after":
                raise self.error

    data = Model((1, 2, 3))
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.scale
    )
    try:
        if bulk:
            cmds.setAttr(
                f"{node.cmd_access_name}.scale", 3.14159, 5, 6, type="double3"
            )
        else:
            cmds.setAttr(f"{node.cmd_access_name}.sx", 3.14159)
        flush()
        assert len(data.writes) == 1
        if mode in ("invalid", "unreadable"):
            assert not binding.view_model.x.set_value_command.can_execute
            assert not binding.maya_view.is_synchronized
            if mode == "unreadable":
                assert binding.maya_view.last_sync_error is data.error
            data.broken = False
            data._value = (7, 8, 9)
            binding.refresh()
            assert tuple(node.scale.get()) == (7, 8, 9)
        else:
            assert binding.value == data.value == tuple(node.scale.get())
            if mode in ("before", "after"):
                assert binding.maya_view.last_sync_error is data.error
            else:
                assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_history_setter_correction_preserves_redo_and_defers_mismatch(node):
    class Rounded(Data):
        @Data.value.setter
        def value(self, value):
            self._value = tuple(round(item, 1) for item in value)

    data = Rounded((1, 2, 3))
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.scale
    )
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        cmds.setAttr(
            f"{node.cmd_access_name}.scale",
            3.14159,
            4.14159,
            5.14159,
            type="double3",
        )
        flush()
        assert data.value == tuple(node.scale.get()) == (3.1, 4.1, 5.1)
        cmds.undo()
        flush()
        assert tuple(node.scale.get()) == (3.14159, 4.14159, 5.14159)
        assert data.value == (3.1, 4.1, 5.1)
        assert not binding.maya_view.is_synchronized
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.undo()
        flush()
        assert data.value == tuple(node.scale.get()) == (1, 2, 3)
        cmds.redo()
        flush()
        assert data.value == (3.1, 4.1, 5.1)
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
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
def test_units_and_repeated_refresh_preserve_python_precision_without_echo(
    node, linear, angle
):
    cmds.currentUnit(linear=linear, angle=angle)
    presentation = FloatPresentation(
        scale=2, suffix=" custom", minimum=-1e14, maximum=1e14
    )
    for plug in (node.translate, node.rotate):
        data = Data()
        binding = MayaFloat3Binding.from_attribute(
            data, "value", maya_plug=plug, presentation=presentation
        )
        try:
            for values in (
                (123.456789123456, -3.141592653589793, 1e-12),
                (1e12, -1e12, 0),
            ):
                binding.set_value(values)
                assert binding.maya_view.is_synchronized
                assert data.value == values
                cmds.flushUndo()
                assert not binding.refresh()
                flush()
                assert data.value == values
                assert cmds.undoInfo(q=True, undoQueueEmpty=True)
            binding.maya_view.dispose()
            assert binding.view_model.x.presentation == presentation
        finally:
            binding.dispose()
            flush()


def test_float32_projection_and_maya_limits_are_sync_constraints(node):
    path = node.cmd_access_name
    cmds.addAttr(path, longName="weights", attributeType="float3")
    for axis in "XYZ":
        cmds.addAttr(
            path,
            longName=f"weight{axis}",
            attributeType="float",
            parent="weights",
            minValue=-10,
            maxValue=10,
        )
    data = Data()
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=resolve_float3_plug(path, "weights")
    )
    try:
        initial = data.value
        assert tuple(cmds.getAttr(f"{path}.weights")[0]) != initial
        assert binding.maya_view.is_synchronized
        cmds.flushUndo()
        binding.refresh()
        binding.set_value(tuple(value + 1e-15 for value in initial))
        flush()
        assert data.value != initial
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        before = cmds.getAttr(f"{path}.weights")
        for value in (20, 1e40):
            assert binding.set_value((5, value, 6))
            assert cmds.getAttr(f"{path}.weights") == before
            assert isinstance(binding.maya_view.last_sync_error, ValueError)
            assert binding.view_model.y.set_value_command.can_execute
        binding.set_value((4, 5, 6))
        assert binding.maya_view.is_synchronized
    finally:
        binding.dispose()
        flush()


def test_view_reservation_cleanup_and_replacement(node):
    binding = Float3Binding.from_attribute(Data(), "value")
    owner = qt.QObject()
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    try:
        scalar = MayaFloatPlugView(
            binding.view_model.x, node.translate.translateX, owner
        )
        with pytest.raises(RuntimeError, match="複数"):
            MayaFloat3PlugView(binding.view_model, node.translate, owner)
        scalar.dispose()
        view = MayaFloat3PlugView(binding.view_model, node.translate, owner)
        with pytest.raises(RuntimeError, match="複数"):
            MayaFloatPlugView(
                binding.view_model.x, node.translate.translateX, owner
            )
        with pytest.raises(RuntimeError, match="複数"):
            MayaFloat3PlugView(binding.view_model, node.translate, owner)
        view.dispose()
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        replacement = MayaFloat3PlugView(
            binding.view_model, node.translate, owner
        )
        registries = replacement.findChildren(MayaCallbackRegistry)
        assert [len(registry.callback_ids) for registry in registries] == [
            4,
            4,
            4,
        ]
        registries[0].dispose()
        assert replacement.is_disposed
        assert all(not registry.callback_ids for registry in registries)
        assert binding.set_value((4, 5, 6))
        third = MayaFloat3PlugView(binding.view_model, node.translate, owner)
        cmds.delete(node.cmd_access_name)
        assert third.is_disposed
        assert binding.set_value((7, 8, 9))
    finally:
        owner.deleteLater()
        binding.dispose()
        flush()


def test_readonly_python_and_optional_maya_view(node):
    @dataclass(frozen=True)
    class ReadOnly:
        value: tuple = (1, 2, 3)

    data = ReadOnly()
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.translate
    )
    try:
        cmds.setAttr(
            f"{node.cmd_access_name}.translate", 4, 5, 6, type="double3"
        )
        flush()
        assert data.value == (1, 2, 3)
        assert not binding.maya_view.is_synchronized
        assert binding.maya_view.sync_from_view_model()
        assert tuple(node.translate.get()) == (1, 2, 3)
        optional = MayaFloat3Binding.from_attribute(Data(), "value")
        assert optional.maya_view is None
        assert optional.set_value((4, 5, 6))
        optional.dispose()
    finally:
        binding.dispose()
        flush()


def test_view_rejects_missing_or_maya_source_store(node):
    owner = qt.QObject()
    vm = Float3ViewModel()
    with pytest.raises(RuntimeError, match="Storeを接続"):
        MayaFloat3PlugView(vm, node.translate, owner)
    binding = MayaFloat3PlugBinding(node.translate)
    try:
        with pytest.raises(RuntimeError, match="Python側を正本"):
            MayaFloat3PlugView(binding.view_model, node.translate, owner)
    finally:
        binding.dispose()
        vm.deleteLater()
        owner.deleteLater()
        flush()
