# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatPresentation,
    FloatSpinBox,
    FloatValue,
    FloatViewModel,
    qt,
)


@dataclass
class Store:
    value: float = 1.234567891
    is_available: bool = True
    is_writable: bool = True
    presentation: FloatPresentation = FloatPresentation()
    writes: int = 0
    mode: str = "normal"

    def read(self) -> float:
        return self.value

    def write(self, value: float) -> float:
        self.writes += 1
        if self.mode == "reject":
            return self.value
        self.value = round(value, 2) if self.mode == "round" else value
        if self.mode == "fail_after_write":
            raise ValueError("setter failed")
        return self.value


def press_key(widget, key, text=""):
    event = qt.QtGui.QKeyEvent(
        qt.QEvent.Type.KeyPress, key, qt.Qt.KeyboardModifier.NoModifier, text
    )
    qt.QApplication.sendEvent(widget, event)


def type_text(widget, text):
    for character in text:
        press_key(widget, ord(character.upper()), character)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@pytest.mark.parametrize(
    "value",
    [True, False, "1.0", None, float("nan"), float("inf"), -float("inf")],
)
def test_invalid_scalar_values_are_rejected(qt_application, value):
    with pytest.raises((TypeError, ValueError)):
        FloatValue(value)
    vm = FloatViewModel()
    try:
        with pytest.raises((TypeError, ValueError)):
            vm.set_value_command.execute(value)
        assert vm.value.value == 0.0
    finally:
        vm.deleteLater()
        flush()


def test_value_and_command_keep_exact_changes(qt_application):
    vm = FloatViewModel(1.0)
    changes = []
    vm.value.changed.connect(changes.append)
    try:
        assert not vm.set_value_command.execute(1)
        assert vm.set_value_command.execute(1.0 + 1e-12)
        assert changes == [1.0 + 1e-12]
    finally:
        vm.deleteLater()
        flush()


def test_render_and_unedited_return_preserve_precision(qt_application):
    store = Store()
    binding = FloatBinding(store)
    view = FloatSpinBox(binding, decimals=6)
    try:
        assert view.value() == 1.234568
        press_key(view, qt.Qt.Key.Key_Return)
        binding.refresh()
        assert store.value == 1.234567891
        assert store.writes == 0
        assert binding.value == store.value
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_keyboard_commit_steps_and_shared_views(qt_application):
    store = Store(value=1.0)
    binding = FloatBinding(store)
    first = FloatSpinBox(binding, single_step=0.25)
    second = FloatSpinBox(binding.view_model)
    try:
        first.selectAll()
        type_text(first, "600")
        assert store.value == 1.0
        assert store.writes == 0
        press_key(first, qt.Qt.Key.Key_Return)
        assert store.value == second.value() == 600.0
        assert store.writes == 1
        first.stepUp()
        assert store.value == second.value() == 600.25
        assert store.writes == 2
        first.deleteLater()
        flush()
        binding.set_value(-1000.0)
        assert second.value() == -1000.0
    finally:
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "mode, expected", [("round", 2.56), ("reject", 1.234567891)]
)
def test_setter_actual_value_is_rendered(qt_application, mode, expected):
    store = Store(mode=mode)
    binding = FloatBinding(store)
    view = FloatSpinBox(binding)
    try:
        view.setValue(2.555)
        assert binding.value == expected
        assert view.value() == round(expected, 6)
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_failed_write_recovers_actual_value(qt_application):
    store = Store(mode="fail_after_write")
    binding = FloatBinding(store)
    try:
        with pytest.raises(ValueError, match="setter failed"):
            binding.set_value(4.25)
        assert binding.value == store.value == 4.25
    finally:
        binding.dispose()
        flush()


def test_presentation_change_cancels_pending_text_without_writing(
    qt_application,
):
    store = Store(
        value=100.0,
        presentation=FloatPresentation(
            suffix=" cm", minimum=-200.0, maximum=300.0
        ),
    )
    binding = FloatBinding(store)
    view = FloatSpinBox(binding)
    changes = []
    binding.changed.connect(changes.append)
    try:
        view.selectAll()
        type_text(view, "250")
        store.presentation = FloatPresentation(0.01, " m", -200.0, 300.0)
        assert not binding.refresh()
        assert view.value() == 1.0
        assert view.suffix() == " m"
        assert (view.minimum(), view.maximum()) == (-2.0, 3.0)
        press_key(view, qt.Qt.Key.Key_Return)
        assert store.writes == 0
        assert changes == []
        view.setValue(2.5)
        assert store.value == 250.0
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_unwritable_disposed_and_destroyed_sources(qt_application):
    store = Store()
    binding = FloatBinding(store)
    view = FloatSpinBox(binding)
    try:
        store.is_writable = False
        store.value = 42.0
        binding.refresh()
        assert not view.isEnabled()
        assert view.value() == 42.0
        view.setValue(8.0)
        assert view.value() == store.value == 42.0
        assert store.writes == 0
        binding.dispose()
        with pytest.raises(RuntimeError):
            FloatSpinBox(binding)
        flush()
        assert not view.isEnabled()
        with pytest.raises(RuntimeError):
            _ = view.view_model
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


def test_input_enabled_combines_local_setting_with_store_writability(
    qt_application,
):
    owner = qt.QWidget()
    store = Store()
    binding = FloatBinding(store, parent=owner)
    view = FloatSpinBox(binding, owner)
    try:
        view.setInputEnabled(False)
        for writable in (False, True):
            store.is_writable = writable
            store.value = 2.5
            binding.refresh()
            assert not view.isEnabled()
            assert view.value() == 2.5
        view.setValue(5)
        assert store.writes == 0
        assert view.value() == 2.5
        store.is_writable = False
        binding.refresh()
        view.setInputEnabled(True)
        assert view.isInputEnabled()
        assert not view.isEnabled()
        store.is_writable = True
        binding.refresh()
        assert view.isEnabled()
        view.setValue(5)
        assert store.value == 5
        with pytest.raises(TypeError):
            view.setInputEnabled(1)
        assert view.isInputEnabled()
    finally:
        owner.deleteLater()
        flush()


def test_shared_parent_destruction_does_not_reenter_views(qt_application):
    owner = qt.QWidget()
    binding = FloatBinding(Store(), parent=owner)
    view = FloatSpinBox(binding, owner)
    owner.deleteLater()
    flush()
    assert binding.is_disposed
    assert not qt.isValid(view)
