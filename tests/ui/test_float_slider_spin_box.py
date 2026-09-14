# coding: utf-8
import gc
from dataclasses import dataclass
from sys import float_info
from weakref import ref

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatLabel,
    FloatPresentation,
    FloatSlider,
    FloatSliderSpinBox,
    FloatSpinBox,
    FloatViewModel,
    qt,
)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def test_children_share_confirmation_without_duplicate_writes(owner):
    class Data:
        _value = 0.123456789
        writes = []

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self.writes.append(value)
            self._value = value

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=owner)
    editor = FloatSliderSpinBox(
        binding, owner, minimum=0, maximum=1, decimals=3
    )
    label = FloatLabel(binding, owner, decimals=9)
    assert isinstance(editor.slider, FloatSlider)
    assert isinstance(editor.spin_box, FloatSpinBox)
    assert (
        editor.slider.view_model
        is editor.spin_box.view_model
        is editor.view_model
    )
    assert editor.view_model is binding.view_model
    assert data.writes == []
    assert label.text() == "0.123456789"
    assert editor.slider.value() == 123
    editor.slider.setValue(750)
    assert data.writes == [0.75]
    assert editor.spin_box.value() == 0.75
    editor.spin_box.setValue(0.234)
    assert data.writes == [0.75, 0.234]
    assert editor.slider.value() == 234
    editor.spin_box.setDecimals(6)
    editor.slider.setFloatRange(-10, 10)
    assert data.writes == [0.75, 0.234]
    data._value = 3.123456789
    binding.refresh()
    assert label.text() == "3.123456789"
    assert editor.spin_box.value() == 3.123457
    assert data.writes == [0.75, 0.234]


def test_slider_range_does_not_limit_numeric_input(owner):
    @dataclass
    class Data:
        value: float = 0

    binding = FloatBinding.from_attribute(
        Data(),
        "value",
        parent=owner,
        presentation=FloatPresentation(minimum=-10, maximum=10),
    )
    editor = FloatSliderSpinBox(binding, owner, minimum=0, maximum=1)
    editor.spin_box.setValue(4.123456)
    assert binding.value == 4.123456
    assert editor.slider.value() == 1000
    editor.slider.setFloatRange(20, 30)
    assert not editor.slider.isEnabled()
    assert editor.spin_box.isEnabled()
    editor.spin_box.setValue(-5.25)
    assert binding.value == -5.25
    editor.slider.setFloatRange(-10, 10)
    assert editor.slider.isEnabled()
    assert binding.value == -5.25


def test_setter_correction_failure_and_readonly_state_are_shared(owner):
    class Data:
        _value = 0

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            if value > 0.8:
                raise ValueError("rejected")
            self._value = round(value, 1)

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    editor = FloatSliderSpinBox(binding, owner, minimum=0, maximum=1)
    editor.slider.setValue(345)
    assert editor.spin_box.value() == binding.value == 0.3
    assert editor.slider.value() == 300
    with pytest.raises(ValueError, match="rejected"):
        editor.spin_box._request_value(0.9)
    assert editor.spin_box.value() == binding.value == 0.3
    assert editor.slider.value() == 300

    class Readonly:
        @property
        def value(self):
            return 0.5

    readonly = FloatBinding.from_attribute(Readonly(), "value", parent=owner)
    view = FloatSliderSpinBox(readonly, owner, minimum=0, maximum=1)
    assert not view.slider.isEnabled()
    assert not view.spin_box.isEnabled()


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"minimum": 1, "maximum": 1}, ValueError),
        ({"steps": True}, TypeError),
        ({"steps": 0}, ValueError),
        ({"decimals": True}, TypeError),
        ({"decimals": -1}, ValueError),
        ({"single_step": 0}, ValueError),
        ({"single_step": float("nan")}, ValueError),
    ],
)
def test_invalid_child_settings_leave_no_partial_widget(owner, kwargs, error):
    vm = FloatViewModel(parent=owner)
    before = owner.children()
    settings = {"minimum": 0, "maximum": 1, **kwargs}
    with pytest.raises(error):
        FloatSliderSpinBox(vm, owner, **settings)
    assert owner.children() == before


def test_display_failure_cleans_children_without_disposing_source(owner):
    vm = FloatViewModel(
        float_info.max, owner, presentation=FloatPresentation(scale=2)
    )
    before = owner.children()
    with pytest.raises(ValueError):
        FloatSliderSpinBox(vm, owner, minimum=0, maximum=1)
    assert owner.children() == before
    flush()
    assert not vm.is_disposed
    assert vm.value.value == float_info.max
    assert vm.set_value_command.execute(0.5)


def test_inline_binding_is_retained_and_editor_deletion_keeps_shared_binding(
    owner,
):
    @dataclass
    class Data:
        value: float = 0.125

    binding = FloatBinding.from_attribute(Data(), "value")
    binding_ref = ref(binding)
    editor = FloatSliderSpinBox(binding, owner, minimum=0, maximum=1)
    del binding
    gc.collect()
    assert binding_ref() is not None
    shared = binding_ref()
    assert shared is not None
    editor.slider.setSliderDown(True)
    editor.slider.setValue(250)
    editor.deleteLater()
    flush()
    assert not shared.is_disposed
    assert not shared.view_model.is_editing
    assert shared.value == 0.25
    assert shared.set_value(0.75)
    shared.dispose()
    flush()


@pytest.mark.parametrize("physical", [False, True])
def test_source_end_disables_both_children(owner, physical):
    vm = FloatViewModel(0.5, owner)
    editor = FloatSliderSpinBox(vm, owner, minimum=0, maximum=1)
    if physical:
        vm.deleteLater()
        flush()
    else:
        vm.dispose()
    assert not editor.slider.isEnabled()
    assert not editor.spin_box.isEnabled()
    with pytest.raises(RuntimeError):
        _ = editor.view_model
    with pytest.raises(RuntimeError):
        FloatSliderSpinBox(vm, owner, minimum=0, maximum=1)


@pytest.mark.parametrize("action", ["close", "hide", "disable"])
def test_composite_lifecycle_finishes_its_drag(owner, action):
    vm = FloatViewModel(parent=owner)
    editor = FloatSliderSpinBox(vm, owner, minimum=0, maximum=1)
    editor.slider.setSliderDown(True)
    editor.slider.setValue(700)
    if action == "close":
        editor.close()
    elif action == "hide":
        editor.hide()
    else:
        editor.setEnabled(False)
    assert not vm.is_editing
    assert vm.value.value == 0.7


def test_focus_proxy_and_pending_numeric_input_before_drag(owner):
    vm = FloatViewModel(0.25, owner)
    editor = FloatSliderSpinBox(vm, owner, minimum=0, maximum=1, decimals=3)
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(editor)
    owner.show()
    owner.activateWindow()
    editor.setFocus()
    flush()
    assert editor.focusProxy() is editor.spin_box
    assert editor.spin_box.hasFocus()
    editor.spin_box.lineEdit().setText("0.375")
    assert vm.value.value == 0.25
    editor.slider.setFocus()
    flush()
    assert vm.value.value == 0.375
    assert editor.slider.value() == 375
    editor.slider.setSliderDown(True)
    editor.slider.setValue(700)
    editor.setFocus()
    flush()
    assert not vm.is_editing
    assert editor.spin_box.hasFocus()
    assert vm.value.value == 0.7
