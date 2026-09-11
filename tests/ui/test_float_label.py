# coding: utf-8
from dataclasses import dataclass
from sys import float_info

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatLabel,
    FloatPresentation,
    FloatSpinBox,
    FloatViewModel,
    qt,
)


@dataclass
class Store:
    value: float = 1.234567891234
    is_available: bool = True
    is_writable: bool = True
    presentation: FloatPresentation = FloatPresentation()
    writes: int = 0

    def read(self):
        return self.value

    def write(self, value):
        self.writes += 1
        self.value = value
        return value


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def test_shared_views_preserve_precision_and_display_without_clamping(
    qt_application,
):
    store = Store(
        presentation=FloatPresentation(suffix=" cm", minimum=0, maximum=1)
    )
    binding = FloatBinding(store)
    first = FloatLabel(binding, decimals=3)
    second = FloatLabel(binding.view_model, decimals=6)
    spin = FloatSpinBox(binding, decimals=3)
    try:
        assert first.text() == "1.235 cm"
        assert second.text() == "1.234568 cm"
        assert spin.value() == 1
        assert binding.value == store.value == 1.234567891234
        first.setDecimals(9)
        assert first.decimals() == 9
        assert first.text() == "1.234567891 cm"
        assert store.writes == 0
        spin.setValue(0.75)
        assert first.text() == "0.750000000 cm"
        assert second.text() == "0.750000 cm"
        assert store.writes == 1
        first.deleteLater()
        flush()
        binding.set_value(0.5)
        assert second.text() == "0.500000 cm"
    finally:
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        spin.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("locale_name", ["C", "en_US", "de_DE"])
@pytest.mark.parametrize("value", [2.675, 2.555, -0.00001, 1234.125])
def test_format_matches_spinbox_and_locale_change_does_not_write(
    qt_application, locale_name, value
):
    store = Store(value=value)
    binding = FloatBinding(store)
    label = FloatLabel(binding, decimals=2)
    spin = FloatSpinBox(binding, decimals=2)
    try:
        locale = qt.QtCore.QLocale(locale_name)
        spin.setLocale(locale)
        label.setLocale(locale)
        assert label.text() == spin.text()
        assert binding.value == store.value == value
        assert store.writes == 0
    finally:
        label.deleteLater()
        spin.deleteLater()
        binding.dispose()
        flush()


def test_presentation_only_change_plain_text_and_copy_selection(
    qt_application,
):
    store = Store(value=100, presentation=FloatPresentation(suffix=" cm"))
    binding = FloatBinding(store)
    label = FloatLabel(binding, decimals=3)
    clipboard = qt_application.clipboard()
    saved = qt.QtCore.QMimeData()
    original = clipboard.mimeData()
    if original is not None:
        for mime in original.formats():
            saved.setData(mime, original.data(mime))
    try:
        store.presentation = FloatPresentation(scale=0.01, suffix=" <m>")
        binding.refresh()
        assert label.text() == "1.000 <m>"
        assert label.textFormat() == qt.Qt.TextFormat.PlainText
        assert store.value == 100
        assert store.writes == 0
        label.setSelection(0, len(label.text()))
        binding.refresh()
        assert label.selectedText() == "1.000 <m>"
        qt.QApplication.sendEvent(
            label,
            qt.QtGui.QKeyEvent(
                qt.QEvent.Type.KeyPress,
                qt.Qt.Key.Key_C,
                qt.Qt.KeyboardModifier.ControlModifier,
            ),
        )
        assert clipboard.text() == "1.000 <m>"
    finally:
        clipboard.setMimeData(saved)
        label.deleteLater()
        binding.dispose()
        flush()


def test_readonly_stays_enabled_and_explicit_dispose_is_not_editability(
    qt_application,
):
    store = Store(is_writable=False)
    binding = FloatBinding(store)
    vm = binding.view_model
    label = FloatLabel(binding, decimals=3)
    events = []
    vm.disposed.connect(lambda: events.append("disposed"))
    try:
        assert not vm.set_value_command.can_execute
        assert label.isEnabled()
        store.value = 8.25
        binding.refresh()
        assert label.text() == "8.250"
        assert label.isEnabled()
        vm.dispose()
        vm.dispose()
        assert events == ["disposed"]
        assert label.text() == "8.250"
        assert not label.isEnabled()
        with pytest.raises(RuntimeError, match="終了"):
            FloatLabel(vm)
        with pytest.raises(RuntimeError, match="終了"):
            _ = label.view_model
        label.setDecimals(6)
        assert label.text() == "8.250"
    finally:
        label.deleteLater()
        binding.dispose()
        flush()


def test_memory_viewmodel_and_factory_binding_remain_alive(qt_application):
    label = FloatLabel(FloatBinding(Store()), decimals=3)
    vm = FloatViewModel(42)
    memory = FloatLabel(vm)
    try:
        assert label.view_model.set_value_command.execute(2.5)
        assert label.text() == "2.500"
        assert memory.text() == "42.000000"
        vm.set_value_command.execute(7.25)
        assert memory.text() == "7.250000"
    finally:
        label.view_model.dispose()
        label.deleteLater()
        memory.deleteLater()
        vm.deleteLater()
        flush()


@pytest.mark.parametrize("shared_parent", [False, True])
def test_owner_destruction_keeps_surviving_label_safe(
    qt_application, shared_parent
):
    owner = qt.QWidget()
    binding = FloatBinding(Store(), parent=owner)
    label = FloatLabel(binding, owner if shared_parent else None)
    text = label.text()
    owner.deleteLater()
    flush()
    assert binding.is_disposed
    if shared_parent:
        assert not qt.isValid(label)
    else:
        assert not label.isEnabled()
        assert label.text() == text
        label.deleteLater()
        flush()


@pytest.mark.parametrize("mode", ["round", "reject", "after"])
def test_python_setter_correction_or_failure_is_reflected(
    qt_application, mode
):
    class Data:
        _value = 1.23456789

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            if mode == "reject":
                return
            self._value = round(value, 1)
            if mode == "after":
                raise ValueError("setter failed")

    data = Data()
    binding = FloatBinding.from_attribute(data, "value")
    label = FloatLabel(binding, decimals=3)
    try:
        if mode == "after":
            with pytest.raises(ValueError, match="setter failed"):
                binding.set_value(2.34567)
        else:
            binding.set_value(2.34567)
        assert label.text() == ("1.235" if mode == "reject" else "2.300")
        assert label.isEnabled()
    finally:
        label.deleteLater()
        binding.dispose()
        flush()


def test_external_assignment_and_reentrant_command_use_latest_source(
    qt_application,
):
    @dataclass
    class Data:
        value: float = 1.0

    data = Data()
    binding = FloatBinding.from_attribute(data, "value")

    def replace(value):
        if value == 5:
            binding.set_value(10)

    binding.changed.connect(replace)
    label = FloatLabel(binding, decimals=3)
    try:
        data.value = 2.5
        assert label.text() == "1.000"
        binding.refresh()
        assert label.text() == "2.500"
        binding.set_value(5)
        assert label.text() == "10.000"
        assert data.value == binding.value == 10
    finally:
        label.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("value", [True, 1.5, "3", -1, 324])
def test_invalid_decimals_do_not_create_widget_or_modify_label(
    qt_application, value
):
    vm = FloatViewModel(1.23456)
    owner = qt.QWidget()
    label = FloatLabel(vm, owner, decimals=3)
    try:
        with pytest.raises((TypeError, ValueError)):
            FloatLabel(vm, owner, decimals=value)
        assert owner.children() == [label]
        with pytest.raises((TypeError, ValueError)):
            label.setDecimals(value)
        assert label.decimals() == 3
        assert label.text() == "1.235"
    finally:
        vm.deleteLater()
        owner.deleteLater()
        flush()


def test_extreme_values_and_display_overflow_do_not_modify_source(
    qt_application,
):
    vm = FloatViewModel(float_info.max)
    label = FloatLabel(vm, decimals=0)
    try:
        assert label.text() == format(float_info.max, ".0f")
        vm.set_value_command.execute(1e-320)
        label.setDecimals(323)
        assert label.text().endswith("1000")
        assert vm.value.value == 1e-320
    finally:
        label.deleteLater()
        vm.deleteLater()
        flush()
    store = Store(
        value=float_info.max,
        presentation=FloatPresentation(scale=2, suffix=" units"),
    )
    binding = FloatBinding(store)
    label = FloatLabel(binding)
    try:
        assert label.text() == "— units"
        store.presentation = FloatPresentation()
        binding.refresh()
        assert label.text().endswith(".000000")
        assert store.value == float_info.max
        assert store.writes == 0
    finally:
        label.deleteLater()
        binding.dispose()
        flush()
