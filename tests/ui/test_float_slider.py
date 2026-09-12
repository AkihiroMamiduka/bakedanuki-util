# coding: utf-8
from dataclasses import dataclass
from sys import float_info

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatLabel,
    FloatPresentation,
    FloatSlider,
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
def widgets(qt_application):
    owner = qt.QWidget()
    yield owner
    owner.deleteLater()
    flush()


def test_views_share_exact_value_without_quantization_writes(widgets):
    @dataclass
    class Data:
        value: float = 0.123456789

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=widgets)
    slider = FloatSlider(binding, widgets, minimum=0, maximum=1)
    spin = FloatSpinBox(binding, widgets, decimals=6)
    label = FloatLabel(binding, widgets, decimals=9)
    changes = []
    binding.changed.connect(changes.append)
    assert slider.value() == 123
    assert data.value == 0.123456789
    slider.setSliderDown(True)
    slider.setSliderDown(False)
    assert not changes
    slider.setValue(750)
    assert binding.value == data.value == spin.value() == 0.75
    assert label.text() == "0.750000000"
    spin.setValue(0.234567)
    assert slider.value() == 235
    assert data.value == 0.234567
    data.value = 3.123456789
    binding.refresh()
    assert slider.value() == 1000
    assert data.value == 3.123456789
    slider.setFloatRange(-10, 10)
    assert data.value == 3.123456789


@pytest.mark.parametrize(
    "minimum,maximum,value",
    [
        (-float_info.max, float_info.max, 0),
        (1e-300, 3e-300, 2e-300),
        (-3e-300, -1e-300, -2e-300),
        (1e300, 1.2e300, 1.1e300),
    ],
)
def test_finite_mapping_and_exact_endpoints(widgets, minimum, maximum, value):
    vm = FloatViewModel(value, widgets)
    slider = FloatSlider(vm, widgets, minimum=minimum, maximum=maximum)
    assert slider.value() == 500
    assert vm.value.value == value
    slider.setValue(0)
    assert vm.value.value == minimum
    slider.setValue(1000)
    assert vm.value.value == maximum


def test_hard_limits_intersect_operating_range_without_clamping_source(
    widgets,
):
    @dataclass
    class Data:
        value: float = 20

    data = Data()
    binding = FloatBinding.from_attribute(
        data,
        "value",
        parent=widgets,
        presentation=FloatPresentation(minimum=-2, maximum=4),
    )
    slider = FloatSlider(binding, widgets, minimum=-10, maximum=10)
    assert slider.floatRange() == (-10, 10)
    assert slider.effectiveFloatRange() == (-2, 4)
    assert data.value == 20
    slider.setValue(0)
    assert data.value == -2
    slider.setFloatRange(5, 10)
    assert slider.effectiveFloatRange() is None
    assert not slider.isEnabled()
    assert data.value == -2
    slider.setFloatRange(0, 1)
    assert slider.isEnabled()
    slider.setValue(1000)
    assert data.value == 1


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"minimum": 1, "maximum": 1}, ValueError),
        ({"minimum": 2, "maximum": 1}, ValueError),
        ({"minimum": float("nan"), "maximum": 1}, ValueError),
        ({"minimum": 0, "maximum": float("inf")}, ValueError),
        ({"minimum": False, "maximum": 1}, TypeError),
        ({"minimum": 0, "maximum": 1, "steps": True}, TypeError),
        ({"minimum": 0, "maximum": 1, "steps": 1.5}, TypeError),
        ({"minimum": 0, "maximum": 1, "steps": 0}, ValueError),
        ({"minimum": 0, "maximum": 1, "steps": 2147483648}, ValueError),
    ],
)
def test_invalid_configuration_precedes_widget_creation(
    widgets, kwargs, error
):
    vm = FloatViewModel(parent=widgets)
    before = widgets.children()
    with pytest.raises(error):
        FloatSlider(vm, widgets, **kwargs)
    assert widgets.children() == before


def test_setter_correction_failure_and_reentrant_values(widgets):
    class Data:
        _value = 0.0

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            if value > 0.8:
                raise ValueError("rejected")
            self._value = round(value, 1)

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=widgets)
    slider = FloatSlider(binding, widgets, minimum=0, maximum=1)
    slider.setValue(345)
    assert data.value == 0.3
    assert slider.value() == 300
    slider.setSliderDown(True)
    with pytest.raises(ValueError, match="rejected"):
        slider._request_value(900)
    assert not binding.view_model.is_editing
    assert slider.value() == 300
    binding.changed.connect(
        lambda value: binding.set_value(0.6) if value == 0.5 else None
    )
    slider.setValue(500)
    assert data.value == 0.6
    assert slider.value() == 600


def test_readonly_and_disposed_sources_disable_input(widgets):
    class Readonly:
        @property
        def value(self):
            return 0.25

    binding = FloatBinding.from_attribute(Readonly(), "value", parent=widgets)
    slider = FloatSlider(binding, widgets, minimum=0, maximum=1)
    assert not slider.isEnabled()
    slider.setValue(500)
    assert slider.value() == 250
    vm = FloatViewModel(0.5, widgets)
    active = FloatSlider(vm, widgets, minimum=0, maximum=1)
    active.setSliderDown(True)
    vm.dispose()
    assert not active.isEnabled()
    assert not active.isSliderDown()
    with pytest.raises(RuntimeError):
        _ = active.view_model
    with pytest.raises(RuntimeError):
        FloatSlider(vm, widgets, minimum=0, maximum=1)


def test_edit_owner_lifetime_and_competing_views(widgets):
    vm = FloatViewModel(parent=widgets)
    first, second = qt.QObject(widgets), qt.QObject(widgets)
    events = []
    vm.edit_started.connect(lambda: events.append("start"))
    vm.edit_finished.connect(lambda: events.append("end"))
    assert vm.begin_edit(first)
    assert vm.begin_edit(first)
    with pytest.raises(RuntimeError, match="別のView"):
        vm.begin_edit(second)
    vm.end_edit(second)
    assert vm.is_editing
    first.deleteLater()
    flush()
    assert not vm.is_editing
    assert events == ["start", "end"]
    assert vm.begin_edit(second)
    vm.dispose()
    assert events == ["start", "end", "start", "end"]


@pytest.mark.parametrize(
    "event_type",
    [
        qt.QEvent.Type.Hide,
        qt.QEvent.Type.FocusOut,
        qt.QEvent.Type.WindowDeactivate,
        qt.QEvent.Type.UngrabMouse,
    ],
)
def test_interrupted_gesture_ends_without_rolling_back(widgets, event_type):
    vm = FloatViewModel(parent=widgets)
    slider = FloatSlider(vm, widgets, minimum=0, maximum=1)
    slider.setSliderDown(True)
    slider.setValue(700)
    qt.QApplication.sendEvent(slider, qt.QEvent(event_type))
    assert not vm.is_editing
    assert not slider.isSliderDown()
    assert vm.value.value == 0.7


def send_key(slider, event_type, key, repeat=False):
    event = qt.QtGui.QKeyEvent(
        event_type, key, qt.Qt.KeyboardModifier.NoModifier, "", repeat
    )
    qt.QApplication.sendEvent(slider, event)


def test_keyboard_repeat_and_escape_keep_last_confirmation(widgets):
    vm = FloatViewModel(parent=widgets)
    slider = FloatSlider(vm, widgets, minimum=0, maximum=1)
    events = []
    vm.edit_started.connect(lambda: events.append("start"))
    vm.edit_finished.connect(lambda: events.append("end"))
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Right)
    for _ in range(4):
        send_key(slider, qt.QEvent.Type.KeyRelease, qt.Qt.Key.Key_Right, True)
        send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Right, True)
    assert events == ["start"]
    assert vm.value.value == 0.005
    send_key(slider, qt.QEvent.Type.KeyRelease, qt.Qt.Key.Key_Right)
    assert events == ["start", "end"]
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_End)
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Escape)
    assert not vm.is_editing
    assert vm.value.value == 1


def test_range_or_units_end_gesture_without_writing(widgets):
    @dataclass
    class Data:
        value: float = 50

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=widgets)
    slider = FloatSlider(binding, widgets, minimum=0, maximum=100)
    slider.setSliderDown(True)
    binding.view_model.set_presentation_adapter(
        lambda p: FloatPresentation(0.01, " m")
    )
    assert not binding.view_model.is_editing
    assert slider.value() == 500
    assert slider.floatRange() == (0, 100)
    assert data.value == 50
    slider.setSliderDown(True)
    slider.setFloatRange(0, 200)
    assert not binding.view_model.is_editing
    assert slider.value() == 250
    with pytest.raises(ValueError):
        slider.setFloatRange(1, 1)
    assert slider.floatRange() == (0, 200)


def send_mouse(slider, kind, point, button, buttons):
    position = qt.QPointF(point)
    event = qt.QtGui.QMouseEvent(
        kind,
        position,
        position,
        button,
        buttons,
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(slider, event)


@pytest.mark.parametrize("groove", [False, True])
def test_real_mouse_events_begin_before_first_change_and_finish(
    widgets, groove
):
    vm = FloatViewModel(0.25, widgets)
    slider = FloatSlider(vm, widgets, minimum=0, maximum=1)
    slider.resize(400, 30)
    option = qt.QtWidgets.QStyleOptionSlider()
    slider.initStyleOption(option)
    style = slider.style()
    handle = style.subControlRect(
        qt.QtWidgets.QStyle.ComplexControl.CC_Slider,
        option,
        qt.QtWidgets.QStyle.SubControl.SC_SliderHandle,
        slider,
    )
    start = handle.center()
    if groove:
        start = qt.QPoint(350, start.y())
    values = []
    vm.value.changed.connect(
        lambda value: values.append((value, vm.is_editing))
    )
    send_mouse(
        slider,
        qt.QEvent.Type.MouseButtonPress,
        start,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.LeftButton,
    )
    assert vm.is_editing
    if not groove:
        for offset in (50, 100, 150):
            send_mouse(
                slider,
                qt.QEvent.Type.MouseMove,
                start + qt.QPoint(offset, 0),
                qt.Qt.MouseButton.NoButton,
                qt.Qt.MouseButton.LeftButton,
            )
    send_mouse(
        slider,
        qt.QEvent.Type.MouseButtonRelease,
        start,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.NoButton,
    )
    assert values
    assert all(editing for _, editing in values)
    assert not vm.is_editing


def test_disposal_rejects_reentrant_edit_restart(widgets):
    vm = FloatViewModel(parent=widgets)
    assert vm.begin_edit(widgets)
    attempted = []
    vm.edit_finished.connect(lambda: attempted.append(vm.begin_edit(widgets)))
    vm.dispose()
    assert attempted == [False]
    assert not vm.is_editing
