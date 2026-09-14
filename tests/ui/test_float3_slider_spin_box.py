# coding: utf-8
from dataclasses import dataclass
import gc
import weakref

import pytest

from bd_util.ui import (
    Float3Binding,
    Float3Label,
    Float3SliderSpinBox,
    Float3ViewModel,
    FloatPresentation,
    FloatSliderSpinBox,
    qt,
)
from bd_util.ui.binding.float3.view import slider_spin_box as view_module


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def editors(view):
    return view.x_editor, view.y_editor, view.z_editor


@dataclass
class Data:
    value: tuple[float, float, float] = (1.23456789, 2.34567891, 3.45678912)


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def test_axis_ranges_shared_views_and_precision_without_duplicate_writes(
    owner,
):
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
    view = Float3SliderSpinBox(
        binding,
        owner,
        minimum=(-10, -20, -30),
        maximum=[10, 20, 30],
        decimals=3,
    )
    linked = Float3SliderSpinBox(
        binding.view_model, owner, minimum=-100, maximum=100, decimals=6
    )
    label = Float3Label(binding, owner, decimals=9)
    assert data.writes == []
    assert view.view_model is binding.view_model
    for editor, component in zip(
        editors(view),
        (binding.view_model.x, binding.view_model.y, binding.view_model.z),
    ):
        assert isinstance(editor, FloatSliderSpinBox)
        assert (
            editor.slider.view_model is editor.spin_box.view_model is component
        )
    view.y_editor.slider.setSliderDown(True)
    view.y_editor.slider.setValue(750)
    assert data.writes == [(Data().value[0], 10, Data().value[2])]
    assert linked.y_editor.slider.value() == 550
    assert linked.y_spin_box.value() == 10
    assert label.y_label.text() == "10.000000000"
    view.y_editor.slider.setSliderDown(False)
    view.z_spin_box.setValue(45.125)
    assert data.writes[-1] == (Data().value[0], 10, 45.125)
    assert view.z_editor.slider.value() == 1000
    assert linked.z_spin_box.value() == 45.125
    assert len(data.writes) == 2
    view.x_editor.slider.setFloatRange(-1, 1)
    view.x_spin_box.setDecimals(6)
    assert len(data.writes) == 2
    assert data.value[0] == Data().value[0]
    binding.set_value((4, 5, 6))
    assert tuple(editor.spin_box.value() for editor in editors(view)) == (
        4,
        5,
        6,
    )


def test_axis_hard_limits_and_display_units_are_independent(owner):
    binding = Float3Binding.from_attribute(
        Data((0, 5, 2)),
        "value",
        parent=owner,
        presentation=(
            FloatPresentation(minimum=-5, maximum=5, scale=0.01, suffix=" m"),
            FloatPresentation(minimum=4, maximum=6),
            FloatPresentation(minimum=0, maximum=10),
        ),
    )
    view = Float3SliderSpinBox(
        binding, owner, minimum=-10, maximum=(10, 3, 1), single_step=0.25
    )
    view.x_editor.slider.setValue(1000)
    assert binding.value == (5, 5, 2)
    assert view.x_spin_box.text() == "0.050000 m"
    assert view.x_spin_box.singleStep() == 0.25
    assert not view.y_editor.slider.isEnabled()
    assert view.y_spin_box.isEnabled()
    view.y_spin_box.setValue(5.5)
    assert binding.value == (5, 5.5, 2)
    assert view.z_editor.slider.value() == 1000
    assert view.z_spin_box.value() == 2


def test_setter_can_correct_other_axes_and_failure_restores_all_views(owner):
    class CorrectingData:
        _value = (0, 1, 2)

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            if value[0] > 8:
                raise ValueError("rejected")
            x = round(value[0], 1)
            self._value = (x, x + 1, x + 2)

    binding = Float3Binding.from_attribute(
        CorrectingData(), "value", parent=owner
    )
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    view.x_editor.slider.setValue(346)
    assert binding.value == (3.5, 4.5, 5.5)
    assert tuple(editor.slider.value() for editor in editors(view)) == (
        350,
        450,
        550,
    )
    with pytest.raises(ValueError, match="rejected"):
        view.x_spin_box._request_value(9)
    assert tuple(editor.spin_box.value() for editor in editors(view)) == (
        3.5,
        4.5,
        5.5,
    )


def test_readonly_source_disables_every_editor(owner):
    class Readonly:
        @property
        def value(self):
            return (1, 2, 3)

    binding = Float3Binding.from_attribute(Readonly(), "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    assert all(
        not editor.slider.isEnabled() and not editor.spin_box.isEnabled()
        for editor in editors(view)
    )


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"minimum": (0, 0)}, ValueError),
        ({"maximum": (10, 10, 0)}, ValueError),
        ({"minimum": True}, TypeError),
        ({"minimum": "000"}, TypeError),
        ({"maximum": (10, 10, float("inf"))}, ValueError),
        ({"minimum": (0, True, 0)}, TypeError),
        ({"steps": 0}, ValueError),
        ({"steps": True}, TypeError),
        ({"decimals": -1}, ValueError),
        ({"single_step": 0}, ValueError),
    ],
)
def test_invalid_settings_are_checked_before_creating_any_axis(
    owner, kwargs, error
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    before = owner.children()
    with pytest.raises(error):
        Float3SliderSpinBox(
            binding, owner, **{"minimum": 0, "maximum": 10, **kwargs}
        )
    assert owner.children() == before
    assert binding.value == Data().value


@pytest.mark.parametrize("source_kind", ["wrong", "unattached", "disposed"])
def test_invalid_source_leaves_no_partial_widget(owner, source_kind):
    source = Float3ViewModel(owner)
    if source_kind == "disposed":
        source.dispose()
    elif source_kind == "wrong":
        source = object()
    before = owner.children()
    with pytest.raises(TypeError if source_kind == "wrong" else RuntimeError):
        Float3SliderSpinBox(source, owner, minimum=0, maximum=10)
    assert owner.children() == before


def test_partial_construction_failure_cleans_views_but_keeps_binding(
    owner, monkeypatch
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    made = []

    def create_editor(vm, parent, **kwargs):
        if made:
            raise RuntimeError("construction failed")
        editor = FloatSliderSpinBox(vm, parent, **kwargs)
        made.append(editor)
        return editor

    monkeypatch.setattr(view_module, "FloatSliderSpinBox", create_editor)
    before = owner.children()
    with pytest.raises(RuntimeError, match="construction failed"):
        Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    assert owner.children() == before
    flush()
    assert not qt.isValid(made[0])
    assert binding.set_value((4, 5, 6))


@pytest.mark.parametrize("action", ["close", "hide", "disable", "delete"])
def test_lifecycle_finishes_only_own_drag_and_retains_inline_binding(
    owner, action
):
    binding = Float3Binding.from_attribute(Data(), "value")
    reference = weakref.ref(binding)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    other = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    del binding
    gc.collect()
    shared = reference()
    assert shared is not None
    view.y_editor.slider.setSliderDown(True)
    view.y_editor.slider.setValue(700)
    other.close()
    assert shared.view_model.y.is_editing
    if action == "close":
        view.close()
    elif action == "hide":
        view.hide()
    elif action == "disable":
        view.setEnabled(False)
    else:
        view.deleteLater()
    flush()
    assert not shared.view_model.y.is_editing
    assert shared.value == (Data().value[0], 7, Data().value[2])
    assert shared.set_value((4, 5, 6))
    shared.dispose()


@pytest.mark.parametrize("termination", ["binding", "view_model", "component"])
def test_source_disposal_disables_all_axes(owner, termination):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    view.z_editor.slider.setSliderDown(True)
    view.z_editor.slider.setValue(700)
    if termination == "binding":
        binding.dispose()
    elif termination == "view_model":
        binding.view_model.deleteLater()
    else:
        binding.view_model.y.deleteLater()
    flush()
    assert all(
        not editor.slider.isEnabled() and not editor.spin_box.isEnabled()
        for editor in editors(view)
    )
    with pytest.raises(RuntimeError):
        _ = view.view_model


def test_pending_numeric_input_commits_before_focusing_another_axis(owner):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3SliderSpinBox(
        binding, owner, minimum=0, maximum=10, decimals=3
    )
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(view)
    owner.show()
    owner.activateWindow()
    view.setFocus()
    flush()
    assert view.focusProxy() is view.x_spin_box
    assert view.x_spin_box.hasFocus()
    view.x_spin_box.lineEdit().setText("0.375")
    assert binding.value == Data().value
    view.y_editor.slider.setFocus()
    flush()
    assert binding.value == (0.375, Data().value[1], Data().value[2])
    view.y_editor.slider.setSliderDown(True)
    view.y_editor.slider.setValue(700)
    view.z_spin_box.setFocus()
    flush()
    assert not binding.view_model.y.is_editing
    assert binding.value == (0.375, 7, Data().value[2])
