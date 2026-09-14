# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util.ui import (
    Float3Binding,
    Float3Label,
    Float3RangeSliderSpinBox,
    FloatPresentation,
    FloatRangeSliderSpinBox,
    qt,
)
from bd_util.ui.binding.float3.view import range_slider_spin_box as view_module


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def editors(view):
    return view.x_editor, view.y_editor, view.z_editor


def fields(editor):
    return (
        editor.minimum_spin_box,
        editor.slider,
        editor.maximum_spin_box,
        editor.spin_box,
        editor.step_spin_box,
    )


@dataclass
class Data:
    value: tuple[float, float, float] = (1.23456789, 2.34567891, 3.45678912)


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def test_axis_ranges_and_steps_are_local_without_losing_source_precision(
    owner,
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3RangeSliderSpinBox(
        binding,
        owner,
        minimum=(-10, -20, -30),
        maximum=[10, 20, 30],
        decimals=3,
        single_step=15,
        step_mode="multiplicative",
    )
    linked = Float3RangeSliderSpinBox(
        binding.view_model, owner, minimum=-100, maximum=100
    )
    label = Float3Label(binding, owner, decimals=9)
    refreshed = []
    binding.view_model.store_refreshed.connect(refreshed.append)
    view.y_editor.minimum_spin_box.setValue(-40)
    view.y_editor.step_spin_box.stepUp()
    assert view.y_editor.floatRange() == (-40, 20)
    assert view.y_editor.singleStep() == 150
    assert view.x_editor.floatRange() == (-10, 10)
    assert view.z_editor.floatRange() == (-30, 30)
    assert view.x_editor.singleStep() == view.z_editor.singleStep() == 15
    assert linked.y_editor.floatRange() == (-100, 100)
    assert linked.y_editor.singleStep() == 0.1
    assert refreshed == []
    assert binding.value == Data().value
    view.y_editor.step_spin_box.stepDown()
    view.y_editor.step_spin_box.stepDown()
    assert view.y_editor.singleStep() == 1.5
    view.y_editor.slider.setValue(750)
    assert binding.value == (Data().value[0], 5, Data().value[2])
    assert len(refreshed) == 1
    assert linked.y_spin_box.value() == 5
    assert label.y_label.text() == "5.000000000"
    view.y_spin_box.stepUp()
    assert binding.value == (Data().value[0], 6.5, Data().value[2])


def test_common_settings_forwarded_to_every_axis_and_unspecified_slider_stretches(
    owner,
):
    binding = Float3Binding.from_attribute(
        Data(),
        "value",
        parent=owner,
        presentation=FloatPresentation(suffix=" cm"),
    )
    view = Float3RangeSliderSpinBox(
        binding,
        owner,
        minimum=-100,
        maximum=100,
        steps=2000,
        decimals=3,
        single_step=15,
        step_increment=15,
        minimum_width=60,
        maximum_width=70,
        value_width=120,
        step_width=90,
        minimum_enabled=False,
        maximum_enabled=True,
        value_enabled=False,
        step_enabled=True,
        minimum_show_buttons=False,
        maximum_show_buttons=True,
        value_show_buttons=False,
        step_show_buttons=True,
        minimum_decimals=1,
        maximum_decimals=2,
        minimum_show_unit=True,
        maximum_show_unit=False,
        value_show_unit=True,
        step_show_unit=False,
    )
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(view)
    owner.resize(800, 300)
    owner.show()
    flush()
    assert view.focusProxy() is view.x_editor.slider
    widths = []
    for axis, editor in zip("XYZ", editors(view)):
        assert isinstance(editor, FloatRangeSliderSpinBox)
        assert editor.slider.maximum() == 2000
        assert (
            editor.minimum_spin_box.accessibleName()
            == f"{axis} slider minimum"
        )
        assert (
            editor.maximum_spin_box.accessibleName()
            == f"{axis} slider maximum"
        )
        assert editor.step_spin_box.accessibleName() == f"{axis} value step"
        numeric = (
            editor.minimum_spin_box,
            editor.maximum_spin_box,
            editor.spin_box,
            editor.step_spin_box,
        )
        for spin, width, enabled, buttons, suffix in zip(
            numeric,
            (60, 70, 120, 90),
            (False, True, False, True),
            (False, True, False, True),
            (" cm", "", " cm", ""),
        ):
            assert (
                spin.width()
                == spin.minimumWidth()
                == spin.maximumWidth()
                == width
            )
            assert spin.isEnabled() is enabled
            assert (
                spin.buttonSymbols()
                != qt.QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
            ) is buttons
            assert spin.suffix() == suffix
        assert editor.minimumDecimals() == 1
        assert editor.maximumDecimals() == 2
        assert editor.decimals() == 3
        editor.step_spin_box.stepUp()
        assert editor.singleStep() == 30
        widths.append(editor.slider.width())
    owner.resize(1000, 300)
    flush()
    assert all(
        editor.slider.width() > width
        for editor, width in zip(editors(view), widths)
    )


def test_default_fields_stretch_and_units_are_hidden(owner):
    binding = Float3Binding.from_attribute(
        Data(),
        "value",
        parent=owner,
        presentation=FloatPresentation(suffix=" deg"),
    )
    view = Float3RangeSliderSpinBox(binding, owner, minimum=0, maximum=100)
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(view)
    owner.resize(1600, 300)
    owner.show()
    flush()
    before = [
        [field.width() for field in fields(editor)] for editor in editors(view)
    ]
    owner.resize(1900, 300)
    flush()
    for editor, widths in zip(editors(view), before):
        assert editor.minimumDecimals() == editor.maximumDecimals() == 0
        for field, width in zip(fields(editor), widths):
            assert field.width() > width
        for spin in (
            editor.minimum_spin_box,
            editor.maximum_spin_box,
            editor.spin_box,
            editor.step_spin_box,
        ):
            assert spin.suffix() == ""


def test_hard_limits_and_rejected_range_only_affect_one_axis(owner):
    binding = Float3Binding.from_attribute(
        Data(),
        "value",
        parent=owner,
        presentation=(
            FloatPresentation(minimum=0, maximum=5),
            FloatPresentation(minimum=10, maximum=20),
            FloatPresentation(),
        ),
    )
    view = Float3RangeSliderSpinBox(binding, owner, minimum=0, maximum=10)
    assert view.x_editor.effectiveFloatRange() == (0, 5)
    assert view.y_editor.effectiveFloatRange() is None
    assert not view.y_editor.slider.isEnabled()
    assert view.y_spin_box.isEnabled()
    view.y_editor.maximum_spin_box.setValue(30)
    assert view.y_editor.effectiveFloatRange() == (10, 20)
    assert view.y_editor.slider.isEnabled()
    rejected = []
    view.z_editor.rangeEditRejected.connect(rejected.append)
    view.z_editor.minimum_spin_box.setValue(11)
    view.z_editor.minimum_spin_box.editingFinished.emit()
    assert len(rejected) >= 1
    assert view.z_editor.floatRange() == (0, 10)
    assert view.z_editor.minimum_spin_box.value() == 0
    assert view.x_editor.floatRange() == (0, 10)
    assert view.y_editor.floatRange() == (0, 30)
    assert binding.value == Data().value


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"maximum": (10, 10, 0)}, ValueError),
        ({"minimum_width": 0}, ValueError),
        ({"value_enabled": 1}, TypeError),
        ({"step_show_unit": "False"}, TypeError),
        ({"maximum_decimals": -1}, ValueError),
        ({"step_mode": "unknown"}, ValueError),
        ({"step_increment": 0}, ValueError),
    ],
)
def test_invalid_settings_leave_no_partial_widget_or_disposed_binding(
    owner, kwargs, error
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    before = owner.children()
    with pytest.raises(error):
        Float3RangeSliderSpinBox(
            binding, owner, **{"minimum": 0, "maximum": 10, **kwargs}
        )
    assert owner.children() == before
    flush()
    assert binding.set_value((4, 5, 6))


def test_partial_construction_failure_cleans_children_without_disposing_binding(
    owner, monkeypatch
):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    made = []

    def create_editor(vm, parent, **kwargs):
        if made:
            raise RuntimeError("construction failed")
        editor = FloatRangeSliderSpinBox(vm, parent, **kwargs)
        made.append(editor)
        return editor

    monkeypatch.setattr(view_module, "FloatRangeSliderSpinBox", create_editor)
    before = owner.children()
    with pytest.raises(RuntimeError, match="construction failed"):
        Float3RangeSliderSpinBox(binding, owner, minimum=0, maximum=10)
    assert owner.children() == before
    flush()
    assert not qt.isValid(made[0])
    assert binding.set_value((4, 5, 6))


def test_range_edits_and_lifecycle_finish_only_the_owning_drag(owner):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3RangeSliderSpinBox(binding, owner, minimum=0, maximum=10)
    other = Float3RangeSliderSpinBox(binding, owner, minimum=0, maximum=10)
    view.y_editor.slider.setSliderDown(True)
    view.y_editor.slider.setValue(700)
    other.y_editor.setFloatRange(-20, 20)
    view.x_editor.setFloatRange(-30, 30)
    other.close()
    assert binding.view_model.y.is_editing
    view.y_editor.setFloatRange(-10, 20)
    assert not binding.view_model.y.is_editing
    view.z_editor.slider.setSliderDown(True)
    view.z_editor.slider.setValue(800)
    view.close()
    assert not binding.view_model.z.is_editing
    assert binding.value == (Data().value[0], 7, 8)
    binding.dispose()
    assert all(
        not field.isEnabled()
        for editor in editors(view)
        for field in fields(editor)
    )


def test_tab_across_axis_commits_pending_step_and_minimum_before_value(owner):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3RangeSliderSpinBox(binding, owner, minimum=0, maximum=10)
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(view)
    owner.show()
    owner.activateWindow()
    view.x_editor.step_spin_box.setFocus()
    flush()
    view.x_editor.step_spin_box.lineEdit().setText("15")
    qt.QApplication.sendEvent(
        view.x_editor.step_spin_box,
        qt.QtGui.QKeyEvent(
            qt.QEvent.Type.KeyPress,
            qt.Qt.Key.Key_Tab,
            qt.Qt.KeyboardModifier.NoModifier,
        ),
    )
    flush()
    assert view.y_editor.minimum_spin_box.hasFocus()
    assert view.x_editor.singleStep() == 15
    view.y_editor.minimum_spin_box.lineEdit().setText("-20")
    view.z_spin_box.setFocus()
    flush()
    assert view.y_editor.floatRange() == (-20, 10)
    assert binding.value == Data().value
