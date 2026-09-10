# coding: utf-8
import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util._sample.maya.ui.float3_sample import maya_plug as sample
from bd_util.maya.ui import MayaFloat3PlugBinding
from bd_util.ui import (
    Float3Binding,
    Float3SpinBox,
    Float3ViewModel,
    FloatPresentation,
    FloatSpinBox,
    qt,
)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def press_enter(view):
    event = qt.QtGui.QKeyEvent(
        qt.QEvent.Type.KeyPress,
        qt.Qt.Key.Key_Return,
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(view, event)


class ComponentStore:
    def __init__(self, group, index):
        self.group, self.index = group, index
        self.is_available = True
        self.is_writable = True
        self.presentation = FloatPresentation()

    def read(self):
        return self.group.values[self.index]

    def write(self, value):
        values = list(self.group.values)
        values[self.index] = round(value, 2)
        self.group.values = tuple(values)
        return self.read()


class TripleStore:
    def __init__(self):
        self.values = (1.23456789, 2.3456789123, 3.4567891234)
        self.components = tuple(
            ComponentStore(self, index) for index in range(3)
        )
        self.write_count = 0

    @property
    def is_available(self):
        return all(store.is_available for store in self.components)

    @property
    def is_writable(self):
        return self.is_available and all(
            store.is_writable for store in self.components
        )

    def read(self):
        return self.values

    def write(self, value):
        self.write_count += 1
        self.values = tuple(round(component, 2) for component in value)
        return self.read()


def test_generic_store_shared_views_single_axis_and_bulk_actual_values(
    qt_application,
):
    store = TripleStore()
    binding = Float3Binding(store)
    first = Float3SpinBox(binding, decimals=3)
    second = Float3SpinBox(binding.view_model, decimals=6)
    axis_only = FloatSpinBox(binding.view_model.x, decimals=6)
    try:
        before = store.values
        for view in (first.x_spin_box, first.y_spin_box, first.z_spin_box):
            press_enter(view)
        assert store.values == before
        first.x_spin_box.setValue(10.123)
        assert binding.value == (10.12, before[1], before[2])
        assert second.x_spin_box.value() == 10.12
        assert axis_only.value() == 10.12
        assert store.write_count == 0
        events = []
        binding.changed.connect(events.append)
        binding.set_value((4.567, 5.678, 6.789))
        assert binding.value == (4.57, 5.68, 6.79)
        assert events == [binding.value]
        assert store.write_count == 1
        assert second.z_spin_box.value() == 6.79
    finally:
        first.deleteLater()
        second.deleteLater()
        axis_only.deleteLater()
        binding.dispose()
        flush()


def test_generic_store_external_refresh_metadata_and_partial_read_only(
    qt_application,
):
    store = TripleStore()
    binding = Float3Binding(store)
    view = Float3SpinBox(binding)
    try:
        store.values = (10, 20, 30)
        store.components[1].is_writable = False
        store.components[0].presentation = FloatPresentation(
            scale=0.01, suffix=" m", minimum=0, maximum=100
        )
        binding.refresh()
        assert binding.value == (10, 20, 30)
        assert view.x_spin_box.value() == 0.1
        assert view.x_spin_box.maximum() == 1
        assert not view.y_spin_box.isEnabled()
        assert view.z_spin_box.isEnabled()
        assert not binding.set_value((1, 2, 3))
        store.components[2].is_available = False
        binding.refresh()
        assert not any(
            axis.isEnabled()
            for axis in (view.x_spin_box, view.y_spin_box, view.z_spin_box)
        )
        assert binding.value == (10, 20, 30)
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "value", [(1, 2), (1, 2, 3, 4), "123", (1, True, 3), (1, float("nan"), 3)]
)
def test_invalid_values_do_not_write(qt_application, value):
    store = TripleStore()
    binding = Float3Binding(store)
    try:
        before = store.values
        with pytest.raises((TypeError, ValueError)):
            binding.set_value(value)
        assert store.values == before
        assert store.write_count == 0
    finally:
        binding.dispose()
        flush()


def test_generic_reentrant_scalar_and_bulk_updates(qt_application):
    store = TripleStore()
    binding = Float3Binding(store)
    try:

        def replace(values):
            if values[0] == 10:
                binding.set_value((40, 50, 60))

        binding.changed.connect(replace)
        binding.view_model.x.set_value_command.execute(10)
        assert binding.value == (40, 50, 60)
        assert (
            tuple(
                axis.value.value
                for axis in (
                    binding.view_model.x,
                    binding.view_model.y,
                    binding.view_model.z,
                )
            )
            == binding.value
        )
        binding.changed.connect(lambda _values: binding.dispose())
        binding.set_value((70, 80, 90))
        assert binding.is_disposed
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("readable_after_failure", [True, False])
def test_bulk_failure_recovers_actual_values_or_disables_input(
    qt_application, monkeypatch, readable_after_failure
):
    store = TripleStore()
    binding = Float3Binding(store)
    view = Float3SpinBox(binding)

    def read_failure():
        raise ValueError("cannot read after failure")

    def write_failure(_value):
        store.values = (40, 50, 60)
        if not readable_after_failure:
            monkeypatch.setattr(store, "read", read_failure)
        raise RuntimeError("original write failure")

    monkeypatch.setattr(store, "write", write_failure)
    try:
        with pytest.raises(RuntimeError, match="original write failure"):
            binding.set_value((10, 20, 30))
        if readable_after_failure:
            assert binding.value == (40, 50, 60)
            assert view.y_spin_box.value() == 50
        else:
            assert not binding.view_model.set_value_command.can_execute
            assert not any(
                axis.isEnabled()
                for axis in (view.x_spin_box, view.y_spin_box, view.z_spin_box)
            )
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


@pytest.fixture
def scene(qt_application, maya_standalone):
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    precision = (
        cmds.optionVar(q="channelsPrecision")
        if cmds.optionVar(exists="channelsPrecision")
        else None
    )
    cmds.currentUnit(linear="cm", angle="deg")
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield node
    sample.dispose()
    cmds.currentUnit(linear=units[0], angle=units[1])
    if precision is None:
        cmds.optionVar(remove="channelsPrecision")
    else:
        cmds.optionVar(intValue=("channelsPrecision", precision))
    if om.MObjectHandle(node.m_obj).isValid():
        cmds.delete(node.cmd_access_name)
    flush()


@pytest.mark.parametrize("precision", [3, 15])
def test_sample_units_precision_parent_changes_and_reopen(scene, precision):
    cmds.optionVar(intValue=("channelsPrecision", precision))
    name = scene.cmd_access_name
    cmds.setAttr(
        name + ".translate",
        100.123456789,
        200.234567891,
        300.345678912,
        type="double3",
    )
    baseline = tuple(om.MMessage.nodeCallbacks(scene.m_obj))
    before = tuple(scene.translate.get())
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    window = sample.show(name)
    widget = window.widget
    for group in (widget.translate, widget.rotate, widget.scale):
        for view in (group.x_spin_box, group.y_spin_box, group.z_spin_box):
            assert view.decimals() == precision
            press_enter(view)
    assert tuple(scene.translate.get()) == before
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    cmds.currentUnit(linear="m", angle="rad")
    assert widget.translate.x_spin_box.suffix() == " m"
    assert widget.rotate.z_spin_box.suffix() == " rad"
    assert widget.scale.y_spin_box.suffix() == ""
    widget.translate.x_spin_box.setValue(2)
    assert tuple(scene.translate.get()) == (200, before[1], before[2])
    cmds.setAttr(name + ".translate", 3, 4, 5, type="double3")
    flush()
    assert widget.translate_binding.value == (300, 400, 500)
    cmds.setAttr(name + ".ty", lock=True)
    assert not widget.translate.y_spin_box.isEnabled()
    assert widget.translate.z_spin_box.isEnabled()
    next_precision = 15 if precision == 3 else 3
    cmds.optionVar(intValue=("channelsPrecision", next_precision))
    assert widget.translate.z_spin_box.decimals() == precision
    with pytest.raises(Exception):
        sample.show("missingFloat3Sample")
    assert qt.isValid(window)
    replacement = sample.show(name)
    flush()
    assert not qt.isValid(window)
    assert replacement.widget.translate.x_spin_box.decimals() == next_precision
    replacement.close()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(scene.m_obj)) == baseline


def test_common_owner_destruction_and_binding_lifetime(scene):
    baseline = tuple(om.MMessage.nodeCallbacks(scene.m_obj))
    owner = qt.QWidget()
    binding = MayaFloat3PlugBinding(scene.rotate, parent=owner)
    child = Float3SpinBox(binding, owner)
    survivor = Float3SpinBox(binding)
    child.deleteLater()
    flush()
    assert not binding.is_disposed
    binding.set_value((45, 90, 135))
    assert survivor.y_spin_box.value() == 90
    owner.deleteLater()
    flush()
    assert binding.is_disposed
    assert not any(
        axis.isEnabled()
        for axis in (
            survivor.x_spin_box,
            survivor.y_spin_box,
            survivor.z_spin_box,
        )
    )
    assert tuple(om.MMessage.nodeCallbacks(scene.m_obj)) == baseline
    survivor.deleteLater()
    flush()


def test_unattached_or_disposed_view_model_is_rejected(qt_application):
    view_model = Float3ViewModel()
    with pytest.raises(RuntimeError):
        Float3SpinBox(view_model)
    view_model.dispose()
    with pytest.raises(RuntimeError):
        Float3SpinBox(view_model)
    view_model.deleteLater()
    flush()
