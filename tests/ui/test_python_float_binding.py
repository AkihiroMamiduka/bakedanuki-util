# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds

from bd_util._sample.maya.ui.float_sample import minimal
from bd_util._sample.maya.ui.float_sample.data import WeightData
from bd_util.ui import FloatBinding, FloatPresentation, FloatSpinBox, qt


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


def test_attribute_binding_shares_views_and_refreshes_external_values(
    qt_application,
):
    data = WeightData()
    binding = FloatBinding.from_attribute(data, "weight")
    first = FloatSpinBox(binding, decimals=3)
    second = FloatSpinBox(binding.view_model, decimals=6)
    events = []
    binding.changed.connect(lambda value: events.append((value, data.weight)))
    try:
        assert binding.store.instance is data
        assert binding.view_model.store is binding.store
        press_enter(first)
        press_enter(second)
        assert data.weight == 0.123456789
        assert not binding.refresh()
        assert events == []
        first.setValue(0.5)
        assert second.value() == data.weight == binding.value == 0.5
        assert events == [(0.5, 0.5)]
        assert not binding.set_value(0.5)
        data.weight = 0.987654321
        assert binding.value == 0.5
        assert binding.refresh()
        assert binding.value == data.weight
        assert first.value() == 0.988
        assert second.value() == 0.987654
        first.deleteLater()
        flush()
        assert not binding.is_disposed
        assert binding.set_value(0.75)
        assert second.value() == 0.75
    finally:
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        binding.dispose()
        flush()


def test_presentation_converts_only_view_and_limits_python_requests(
    qt_application,
):
    data = WeightData(0.125)
    binding = FloatBinding.from_attribute(
        data,
        "weight",
        presentation=FloatPresentation(
            scale=100, suffix=" %", minimum=0, maximum=1
        ),
    )
    view = FloatSpinBox(binding, decimals=3)
    try:
        assert view.value() == 12.5
        assert view.suffix() == " %"
        assert (view.minimum(), view.maximum()) == (0, 100)
        view.setValue(75)
        assert binding.value == data.weight == 0.75
        with pytest.raises(ValueError):
            binding.set_value(1.5)
        assert data.weight == 0.75
        assert view.value() == 75
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "mode", ["round", "reject", "raise_before", "raise_after", "invalid"]
)
def test_property_setter_results_failures_and_recovery(qt_application, mode):
    class Data:
        _weight = 0.5

        @property
        def weight(self):
            return self._weight

        @weight.setter
        def weight(self, value):
            if mode == "reject":
                return
            if mode == "raise_before":
                raise ValueError("setter failed")
            self._weight = (
                float("nan") if mode == "invalid" else round(value, 2)
            )
            if mode == "raise_after":
                raise ValueError("setter failed")

    data = Data()
    binding = FloatBinding.from_attribute(data, "weight")
    view = FloatSpinBox(binding)
    events = []
    binding.changed.connect(events.append)
    try:
        if mode in ("raise_before", "raise_after", "invalid"):
            with pytest.raises(ValueError):
                binding.set_value(0.123456789)
        else:
            assert binding.set_value(0.123456789) == (mode == "round")
        expected = 0.12 if mode in ("round", "raise_after") else 0.5
        assert binding.value == view.value() == expected
        assert events == ([0.12] if expected == 0.12 else [])
        if mode == "invalid":
            assert not view.isEnabled()
            data._weight = 0.75
            assert binding.refresh()
            assert view.isEnabled()
            assert binding.value == view.value() == 0.75
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_read_only_and_deleted_attributes_disable_input(qt_application):
    @dataclass(frozen=True)
    class FrozenData:
        weight: float = 0.5

    frozen = FrozenData()
    binding = FloatBinding.from_attribute(frozen, "weight")
    view = FloatSpinBox(binding)
    try:
        assert not view.isEnabled()
        assert not binding.set_value(1)
        assert frozen.weight == 0.5
    finally:
        view.deleteLater()
        binding.dispose()
        flush()

    class Data:
        def __init__(self):
            self.weight = 0.5

    data = Data()
    binding = FloatBinding.from_attribute(data, "weight")
    view = FloatSpinBox(binding)
    try:
        del data.weight
        assert not binding.refresh()
        assert not view.isEnabled()
        assert not binding.set_value(1)
        data.weight = 0.25
        assert binding.refresh()
        assert view.isEnabled()
        assert view.value() == 0.25
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_owner_destruction_disables_surviving_view_and_keeps_data(
    qt_application,
):
    data = WeightData()
    owner = qt.QWidget()
    binding = FloatBinding.from_attribute(data, "weight", parent=owner)
    child = FloatSpinBox(binding, owner)
    survivor = FloatSpinBox(binding)
    binding.set_value(0.75)
    owner.deleteLater()
    flush()
    assert binding.is_disposed
    assert not qt.isValid(child)
    assert not survivor.isEnabled()
    assert data.weight == 0.75
    with pytest.raises(RuntimeError):
        binding.set_value(0.25)
    survivor.deleteLater()
    flush()


def test_notification_reentry_and_disposal_keep_actual_python_value(
    qt_application,
):
    data = WeightData()
    binding = FloatBinding.from_attribute(data, "weight")
    view = FloatSpinBox(binding)

    def replace(value):
        if value == 0.5:
            binding.set_value(0.75)

    binding.changed.connect(replace)
    try:
        binding.set_value(0.5)
        assert binding.value == data.weight == view.value() == 0.75
        binding.changed.connect(lambda _value: binding.dispose())
        binding.set_value(0.25)
        assert binding.is_disposed
        assert data.weight == 0.25
        assert not view.isEnabled()
    finally:
        binding.dispose()
        view.deleteLater()
        flush()


def test_constructor_failure_does_not_leave_owned_qobjects(qt_application):
    class UnreadableData:
        @property
        def weight(self):
            raise ValueError("cannot read")

    owner = qt.QObject()
    try:
        with pytest.raises(ValueError, match="cannot read"):
            FloatBinding.from_attribute(
                UnreadableData(), "weight", parent=owner
            )
        flush()
        assert not owner.children()
    finally:
        owner.deleteLater()
        flush()


def test_minimal_sample_shared_views_direct_data_refresh_and_reopen(
    qt_application, maya_standalone
):
    nodes_before = cmds.ls(long=True)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    try:
        window = minimal.show()
        assert minimal.show() is window
        widget = window.widget
        binding = widget.binding
        data = binding.store.instance
        assert widget.spin_box.value() == 0.123
        assert widget.linked_spin_box.value() == 0.123457
        widget.spin_box.setValue(0.5)
        assert data.weight == widget.linked_spin_box.value() == 0.5
        widget.set_data_button.click()
        assert data.weight == 0.25
        assert binding.value == widget.spin_box.value() == 0.5
        assert widget.data_label.text() == "Data value: 0.25"
        widget.refresh_button.click()
        assert binding.value == widget.linked_spin_box.value() == 0.25
        assert cmds.ls(long=True) == nodes_before
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        window.close()
        flush()
        assert binding.is_disposed
        assert data.weight == 0.25
        replacement = minimal.show()
        assert replacement is not window
        assert replacement.widget.binding.value == WeightData().weight
    finally:
        minimal.dispose()
        flush()
