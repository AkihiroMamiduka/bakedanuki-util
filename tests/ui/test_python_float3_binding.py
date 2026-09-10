# coding: utf-8
from dataclasses import dataclass
from types import SimpleNamespace

import pytest
from maya import cmds

from bd_util._sample.maya.ui.float3_sample import minimal
from bd_util._sample.maya.ui.float3_sample.data import OffsetData
from bd_util.ui import (
    Float3Binding,
    Float3SpinBox,
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


def axes(view):
    return view.x_spin_box, view.y_spin_box, view.z_spin_box


def test_shared_views_precision_latest_other_axes_and_external_refresh(
    qt_application,
):
    data = OffsetData()
    binding = Float3Binding.from_attribute(data, "offset")
    first = Float3SpinBox(binding, decimals=3)
    second = Float3SpinBox(binding.view_model, decimals=6)
    single = FloatSpinBox(binding.view_model.x)
    events = []
    binding.changed.connect(events.append)
    try:
        before = data.offset
        for view in axes(first):
            qt.QApplication.sendEvent(
                view,
                qt.QtGui.QKeyEvent(
                    qt.QEvent.Type.KeyPress,
                    qt.Qt.Key.Key_Return,
                    qt.Qt.KeyboardModifier.NoModifier,
                ),
            )
        assert data.offset == before
        assert events == []
        data.offset = (before[0], 20.1234567890123, 30.9876543210123)
        first.x_spin_box.setValue(10.125)
        assert (
            binding.value
            == data.offset
            == (10.125, 20.1234567890123, 30.9876543210123)
        )
        assert second.y_spin_box.value() == 20.123457
        assert single.value() == 10.125
        assert events == [data.offset]
        events.clear()
        assert binding.set_value([4.123456789, 5.234567891, 6.345678912])
        assert type(data.offset) is tuple
        assert events == [data.offset]
        first.deleteLater()
        flush()
        assert not binding.is_disposed
        data.offset = (7, 8, 9)
        assert binding.value != data.offset
        assert binding.refresh()
        assert second.z_spin_box.value() == 9
    finally:
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        single.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("keep_x", [False, True])
def test_setter_correction_of_all_axes_even_when_edited_axis_is_unchanged(
    qt_application, keep_x
):
    class Data:
        _offset = (1.0, 2.0, 3.0)
        writes = 0

        @property
        def offset(self):
            return self._offset

        @offset.setter
        def offset(self, value):
            self.writes += 1
            self._offset = (
                self._offset[0] if keep_x else value[0],
                value[0] * 2,
                value[0] * 3,
            )

    data = Data()
    binding = Float3Binding.from_attribute(data, "offset")
    view = Float3SpinBox(binding)
    events = []
    binding.changed.connect(events.append)
    try:
        assert binding.view_model.x.set_value_command.execute(10) == (
            not keep_x
        )
        expected = (1 if keep_x else 10, 20, 30)
        assert binding.value == data.offset == expected
        assert tuple(axis.value() for axis in axes(view)) == expected
        assert events == [expected]
        assert data.writes == 1
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_same_axis_request_refreshes_external_other_axes(qt_application):
    data = OffsetData((1, 2, 3))
    binding = Float3Binding.from_attribute(data, "offset")
    try:
        data.offset = (1, 20, 30)
        assert not binding.view_model.x.set_value_command.execute(1)
        assert binding.value == (1, 20, 30)
        assert binding.view_model.y.value.value == 20
    finally:
        binding.dispose()
        flush()


def test_per_axis_units_and_limits_keep_public_values(qt_application):
    data = OffsetData((100, 0.5, 180))
    binding = Float3Binding.from_attribute(
        data,
        "offset",
        presentation=(
            FloatPresentation(scale=0.01, suffix=" m", minimum=0, maximum=200),
            FloatPresentation(scale=100, suffix=" %", minimum=0, maximum=1),
            FloatPresentation(suffix=" deg", minimum=-180, maximum=180),
        ),
    )
    view = Float3SpinBox(binding)
    try:
        assert tuple(axis.value() for axis in axes(view)) == (1, 50, 180)
        assert tuple(axis.suffix() for axis in axes(view)) == (
            " m",
            " %",
            " deg",
        )
        view.y_spin_box.setValue(75)
        assert data.offset == (100, 0.75, 180)
        with pytest.raises(ValueError):
            binding.set_value((150, 1.5, 90))
        assert binding.value == data.offset == (100, 0.75, 180)
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("axis_edit", [True, False])
@pytest.mark.parametrize(
    "mode", ["round", "reject", "before", "after", "invalid", "unreadable"]
)
def test_setter_normalization_rejection_failures_and_recovery(
    qt_application, axis_edit, mode
):
    class Data:
        _offset = (1, 2, 3)
        broken = False
        writes = 0

        @property
        def offset(self):
            if self.broken:
                raise ValueError("getter failed")
            return self._offset

        @offset.setter
        def offset(self, value):
            self.writes += 1
            if mode == "reject":
                return
            if mode == "before":
                raise RuntimeError("setter failed")
            self._offset = tuple(round(item, 2) for item in value)
            if mode == "invalid":
                self._offset = (1, float("nan"), 3)
            if mode == "unreadable":
                self.broken = True
            if mode in ("after", "unreadable"):
                raise RuntimeError("setter failed")

    data = Data()
    binding = Float3Binding.from_attribute(data, "offset")
    view = Float3SpinBox(binding)
    events = []
    binding.changed.connect(events.append)
    request = (
        (4.123456789, 2, 3)
        if axis_edit
        else (4.123456789, 5.234567891, 6.345678912)
    )
    try:

        def execute():
            if axis_edit:
                return binding.view_model.x.set_value_command.execute(
                    request[0]
                )
            return binding.set_value(request)

        if mode in ("before", "after", "unreadable"):
            with pytest.raises(RuntimeError, match="setter failed"):
                execute()
        elif mode == "invalid":
            with pytest.raises(ValueError):
                execute()
        else:
            assert execute() == (mode == "round")
        expected = (
            tuple(round(item, 2) for item in request)
            if mode in ("round", "after")
            else (1, 2, 3)
        )
        assert binding.value == expected
        assert tuple(axis.value() for axis in axes(view)) == expected
        assert events == ([expected] if mode in ("round", "after") else [])
        assert data.writes == 1
        if mode in ("invalid", "unreadable"):
            assert not binding.view_model.set_value_command.can_execute
            assert not any(axis.isEnabled() for axis in axes(view))
            data._offset = (7, 8, 9)
            data.broken = False
            assert binding.refresh()
            assert binding.value == (7, 8, 9)
            assert all(axis.isEnabled() for axis in axes(view))
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_read_only_and_attribute_deletion_disable_whole_group(qt_application):
    @dataclass(frozen=True)
    class FrozenData:
        offset: tuple[float, float, float] = (1, 2, 3)

    for data in (FrozenData(), SimpleNamespace(offset=(1, 2, 3))):
        binding = Float3Binding.from_attribute(data, "offset")
        view = Float3SpinBox(binding)
        try:
            if isinstance(data, SimpleNamespace):
                del data.offset
                assert not binding.view_model.x.set_value_command.execute(2)
            assert not any(axis.isEnabled() for axis in axes(view))
            assert not binding.set_value((4, 5, 6))
        finally:
            view.deleteLater()
            binding.dispose()
            flush()


@pytest.mark.parametrize("bulk_request", [False, True])
@pytest.mark.parametrize("failure", ["invalid", "unreadable", "deleted"])
def test_external_source_failure_disables_all_axes_until_refresh(
    qt_application, bulk_request, failure
):
    class Data:
        _offset = (1, 2, 3)
        broken = False
        writes = 0

        @property
        def offset(self):
            if self.broken:
                raise ValueError("getter failed")
            return self._offset

        @offset.setter
        def offset(self, value):
            self.writes += 1
            self._offset = value

    data = (
        SimpleNamespace(offset=(1, 2, 3)) if failure == "deleted" else Data()
    )
    binding = Float3Binding.from_attribute(data, "offset")
    view = Float3SpinBox(binding)
    events = []
    binding.changed.connect(events.append)
    try:
        if failure == "deleted":
            del data.offset
        elif failure == "invalid":
            data._offset = (1, float("nan"), 3)
        else:
            data.broken = True

        def execute():
            return (
                binding.set_value((4, 5, 6))
                if bulk_request
                else binding.refresh()
            )

        if failure == "deleted":
            assert not execute()
        else:
            with pytest.raises(ValueError):
                execute()
            assert data.writes == 0
        assert binding.value == (1, 2, 3)
        assert events == []
        assert not binding.view_model.set_value_command.can_execute
        assert not any(axis.isEnabled() for axis in axes(view))
        assert not binding.set_value((4, 5, 6))
        if failure == "deleted":
            data.offset = (7, 8, 9)
        else:
            data._offset = (7, 8, 9)
            data.broken = False
        assert binding.refresh()
        assert binding.value == (7, 8, 9)
        assert events == [(7, 8, 9)]
        assert all(axis.isEnabled() for axis in axes(view))
        assert binding.set_value((4, 5, 6))
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_reentrant_update_disposal_and_shared_owner_lifetime(qt_application):
    data = OffsetData()
    owner = qt.QWidget()
    binding = Float3Binding.from_attribute(data, "offset", parent=owner)
    child = Float3SpinBox(binding, owner)
    survivor = Float3SpinBox(binding)

    def replace(value):
        if value[0] == 10:
            binding.set_value((40, 50, 60))

    binding.changed.connect(replace)
    try:
        binding.view_model.x.set_value_command.execute(10)
        assert binding.value == data.offset == (40, 50, 60)
        assert tuple(axis.value() for axis in axes(survivor)) == (40, 50, 60)
        child.deleteLater()
        flush()
        assert not binding.is_disposed
        owner.deleteLater()
        flush()
        assert binding.is_disposed
        assert not any(axis.isEnabled() for axis in axes(survivor))
        assert data.offset == (40, 50, 60)
    finally:
        if qt.isValid(owner):
            owner.deleteLater()
        survivor.deleteLater()
        flush()


def test_setter_notification_can_dispose_binding(qt_application):
    data = OffsetData()
    binding = Float3Binding.from_attribute(data, "offset")
    view = Float3SpinBox(binding)
    binding.changed.connect(lambda _value: binding.dispose())
    try:
        binding.view_model.x.set_value_command.execute(10)
        assert binding.is_disposed
        assert data.offset[0] == 10
        assert not any(axis.isEnabled() for axis in axes(view))
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_invalid_constructor_does_not_leave_owned_qobjects(qt_application):
    owner = qt.QObject()
    try:
        with pytest.raises(TypeError):
            Float3Binding.from_attribute(
                SimpleNamespace(offset=[1, 2, 3]), "offset", parent=owner
            )
        flush()
        assert not owner.children()
    finally:
        owner.deleteLater()
        flush()


def test_minimal_sample_bulk_direct_assignment_refresh_and_reopen(
    qt_application, maya_standalone
):
    before_nodes = cmds.ls(long=True)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    try:
        window = minimal.show()
        assert minimal.show() is window
        widget = window.widget
        binding = widget.binding
        data = binding.store.instance
        widget.spin_box.x_spin_box.setValue(10.125)
        assert data.offset == (10.125, 2.3456789123, 3.4567891234)
        widget.set_value_button.click()
        assert binding.value == (4, 5, 6)
        widget.set_data_button.click()
        assert data.offset == (7, 8, 9)
        assert binding.value == (4, 5, 6)
        widget.refresh_button.click()
        assert tuple(
            axis.value() for axis in axes(widget.linked_spin_box)
        ) == (7, 8, 9)
        assert cmds.ls(long=True) == before_nodes
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        window.close()
        flush()
        assert binding.is_disposed
        assert data.offset == (7, 8, 9)
        replacement = minimal.show()
        assert replacement is not window
        assert replacement.widget.binding.value == OffsetData().offset
    finally:
        minimal.dispose()
        flush()
