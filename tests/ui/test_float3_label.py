# coding: utf-8
from dataclasses import dataclass
import gc
from sys import float_info
import weakref

import pytest

from bd_util.ui import (
    Float3Binding,
    Float3Label,
    Float3SpinBox,
    Float3ViewModel,
    FloatLabel,
    FloatPresentation,
    qt,
)
from bd_util.ui.binding.float3.view import label as label_module


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def labels(view):
    return view.x_label, view.y_label, view.z_label


def texts(view):
    return tuple(label.text() for label in labels(view))


@dataclass
class Data:
    value: tuple[float, float, float] = (1.23456789, 2.34567891, 3.45678912)


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def test_shared_axis_and_tuple_changes_preserve_source_precision(owner):
    class RecordingData:
        def __init__(self):
            self._value = Data().value
            self.writes = []

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self.writes.append(value)
            self._value = value

    data = RecordingData()
    binding = Float3Binding.from_attribute(data, "value", parent=owner)
    first = Float3Label(binding, owner, decimals=3)
    second = Float3Label(binding.view_model, owner, decimals=6)
    spin = Float3SpinBox(binding, owner, decimals=3)
    assert texts(first) == ("1.235", "2.346", "3.457")
    assert texts(second) == ("1.234568", "2.345679", "3.456789")
    first.setDecimals(9)
    assert texts(first) == ("1.234567890", "2.345678910", "3.456789120")
    assert binding.value == data.value == Data().value
    assert data.writes == []
    spin.y_spin_box.setValue(0.125)
    assert data.writes == [(Data().value[0], 0.125, Data().value[2])]
    assert first.y_label.text() == "0.125000000"
    assert second.y_label.text() == "0.125000"
    binding.set_value((4.125, 5.25, 6.5))
    assert texts(second) == ("4.125000", "5.250000", "6.500000")
    first.x_label.setDecimals(0)
    first.setDecimals(9)
    assert first.decimals() == 9
    assert all(label.decimals() == 9 for label in labels(first))
    assert len(data.writes) == 2
    first.deleteLater()
    flush()
    binding.set_value((7, 8, 9))
    assert texts(second) == ("7.000000", "8.000000", "9.000000")
    assert not binding.is_disposed


def test_readonly_values_outside_limits_stay_selectable_and_unclamped(owner):
    class ReadonlyData:
        @property
        def value(self):
            return (-100.125, 0.5, 100.125)

    binding = Float3Binding.from_attribute(
        ReadonlyData(),
        "value",
        parent=owner,
        presentation=FloatPresentation(minimum=0, maximum=1),
    )
    view = Float3Label(binding, owner, decimals=3)
    spin = Float3SpinBox(binding, owner)
    assert texts(view) == ("-100.125", "0.500", "100.125")
    assert not spin.x_spin_box.isEnabled()
    for axis, label in zip(("X", "Y", "Z"), labels(view)):
        assert isinstance(label, FloatLabel)
        assert label.accessibleName() == axis
        assert label.isEnabled()
        assert label.textFormat() == qt.Qt.TextFormat.PlainText
        label.setSelection(0, len(label.text()))
        assert label.selectedText() == label.text()


def test_component_presentation_overflow_and_locale_are_independent(owner):
    data = Data((100, 2.675, float_info.max))
    binding = Float3Binding.from_attribute(
        data,
        "value",
        parent=owner,
        presentation=(
            FloatPresentation(scale=0.01, suffix=" m"),
            FloatPresentation(suffix=" <unit>"),
            FloatPresentation(scale=2, suffix=" huge"),
        ),
    )
    view = Float3Label(binding, owner, decimals=3)
    assert texts(view) == ("1.000 m", "2.675 <unit>", "— huge")
    view.setLocale(qt.QtCore.QLocale("de_DE"))
    assert texts(view) == ("1,000 m", "2,675 <unit>", "— huge")
    data.value = (200, 1.125, 2)
    assert view.x_label.text() == "1,000 m"
    binding.refresh()
    assert texts(view) == ("2,000 m", "1,125 <unit>", "4,000 huge")


def test_each_axis_can_copy_displayed_text_without_writes(
    owner, qt_application, saved_clipboard
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3Label(binding, owner, decimals=3)
    for label in labels(view):
        label.setSelection(0, len(label.text()))
        binding.refresh()
        assert label.selectedText() == label.text()
        qt_application.processEvents()
        qt.QApplication.sendEvent(
            label,
            qt.QtGui.QKeyEvent(
                qt.QEvent.Type.KeyPress,
                qt.Qt.Key.Key_C,
                qt.Qt.KeyboardModifier.ControlModifier,
            ),
        )
        qt_application.processEvents()
        assert saved_clipboard.text() == label.text()
    assert binding.value == Data().value


@pytest.mark.parametrize("termination", ["binding", "view_model", "component"])
def test_disposal_preserves_last_text_and_disables_each_value(
    owner, termination
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3Label(binding, owner, decimals=3)
    before = texts(view)
    vm = binding.view_model
    if termination == "binding":
        binding.dispose()
    elif termination == "view_model":
        vm.deleteLater()
    else:
        vm.y.deleteLater()
    flush()
    assert all(not label.isEnabled() for label in labels(view))
    view.setDecimals(8)
    view.setLocale(qt.QtCore.QLocale("de_DE"))
    assert texts(view) == before
    with pytest.raises(RuntimeError):
        _ = view.view_model


def test_view_retains_binding_when_only_widget_is_kept(owner):
    binding = Float3Binding.from_attribute(Data(), "value")
    reference = weakref.ref(binding)
    view = Float3Label(binding, owner)
    del binding
    gc.collect()
    assert reference() is not None
    view.view_model.set_value_command.execute((4, 5, 6))
    assert texts(view) == ("4.000000", "5.000000", "6.000000")
    reference().dispose()


@pytest.mark.parametrize(
    "decimals,error",
    [(-1, ValueError), (324, ValueError), (True, TypeError), (1.5, TypeError)],
)
def test_invalid_precision_is_atomic_before_and_after_construction(
    owner, decimals, error
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    children = owner.children()
    with pytest.raises(error):
        Float3Label(binding, owner, decimals=decimals)
    assert owner.children() == children
    view = Float3Label(binding, owner, decimals=3)
    with pytest.raises(error):
        view.setDecimals(decimals)
    assert view.decimals() == 3
    assert texts(view) == ("1.235", "2.346", "3.457")


@pytest.mark.parametrize("source_kind", ["wrong", "unattached", "disposed"])
def test_invalid_source_leaves_no_partial_widget(owner, source_kind):
    source = Float3ViewModel(owner)
    if source_kind == "disposed":
        source.dispose()
    elif source_kind == "wrong":
        source = object()
    children = owner.children()
    with pytest.raises(TypeError if source_kind == "wrong" else RuntimeError):
        Float3Label(source, owner)
    assert owner.children() == children


def test_partial_construction_failure_keeps_shared_binding_alive(
    owner, monkeypatch
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    made = []

    def create_label(vm, parent, *, decimals):
        if made:
            raise RuntimeError("construction failed")
        result = FloatLabel(vm, parent, decimals=decimals)
        made.append(result)
        return result

    monkeypatch.setattr(label_module, "FloatLabel", create_label)
    children = owner.children()
    with pytest.raises(RuntimeError, match="construction failed"):
        Float3Label(binding, owner)
    assert owner.children() == children
    flush()
    assert not qt.isValid(made[0])
    assert binding.set_value((4, 5, 6))
