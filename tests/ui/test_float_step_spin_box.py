# coding: utf-8
from dataclasses import dataclass
from sys import float_info

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatPresentation,
    FloatRangeSliderSpinBox,
    FloatStepSpinBox,
    FloatViewModel,
    qt,
)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def press(widget, key, modifiers=qt.Qt.KeyboardModifier.NoModifier):
    for kind in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        event = qt.QtGui.QKeyEvent(kind, key, modifiers)
        qt.QApplication.sendEvent(widget, event)


def enter(widget, text):
    widget.lineEdit().setText(text)
    press(widget, qt.Qt.Key.Key_Return)


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


@pytest.mark.parametrize("increment", [1, 15, 0.1])
def test_additive_step_uses_configured_increment_and_stays_positive(
    owner, increment
):
    spin = FloatStepSpinBox(owner, value=increment, step_increment=increment)
    spin.stepUp()
    assert spin.value() == 2 * increment
    spin.stepDown()
    assert spin.value() == increment
    spin.stepDown()
    assert spin.value() == increment
    assert (
        not spin.stepEnabled()
        & qt.QtWidgets.QAbstractSpinBox.StepEnabledFlag.StepDownEnabled
    )


def test_multiplicative_step_preserves_mantissa_and_repeated_round_trip(owner):
    spin = FloatStepSpinBox(owner, value=15, step_mode="multiplicative")
    for expected in (1.5, 0.15, 0.015, 0.0015, 0.00015):
        spin.stepDown()
        assert spin.value() == expected
        assert spin.cleanText() == str(expected)
    spin.stepBy(5)
    assert spin.value() == 15
    spin.stepUp()
    assert spin.value() == 150
    enter(spin, "2.5")
    spin.stepUp()
    assert spin.value() == 25


@pytest.mark.parametrize("mode", ["additive", "multiplicative"])
def test_direct_entry_pending_commit_invalid_input_and_locale(owner, mode):
    spin = FloatStepSpinBox(owner, value=15, step_mode=mode, step_increment=15)
    changes = []
    spin.valueChanged.connect(changes.append)
    spin.lineEdit().setText("2.5")
    assert spin.value() == 15
    assert changes == []
    spin.stepUp()
    assert spin.value() == (17.5 if mode == "additive" else 25)
    previous = spin.value()
    for text in ("0", "-1", "nan", "inf", ""):
        enter(spin, text)
        assert spin.value() == previous
    spin.setLocale(qt.QtCore.QLocale("de_DE"))
    enter(spin, "0,015")
    assert spin.value() == 0.015
    assert spin.cleanText() == "0,015"


def test_focus_loss_commits_and_wheel_requires_focus(owner):
    spin = FloatStepSpinBox(owner, value=15, step_mode="multiplicative")
    other = qt.QLineEdit(owner)
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(spin)
    layout.addWidget(other)
    owner.show()
    owner.activateWindow()
    spin.setFocus()
    flush()
    spin.lineEdit().setText("1.5")
    other.setFocus()
    flush()
    assert spin.value() == 1.5

    def wheel():
        event = qt.QtGui.QWheelEvent(
            qt.QtCore.QPointF(5, 5),
            qt.QtCore.QPointF(5, 5),
            qt.QtCore.QPoint(),
            qt.QtCore.QPoint(0, 120),
            qt.Qt.MouseButton.NoButton,
            qt.Qt.KeyboardModifier.NoModifier,
            qt.Qt.ScrollPhase.NoScrollPhase,
            False,
        )
        qt.QApplication.sendEvent(spin, event)

    wheel()
    assert spin.value() == 1.5
    spin.setFocus()
    flush()
    wheel()
    assert spin.value() == 15
    press(spin, qt.Qt.Key.Key_Down)
    assert spin.value() == 1.5


def test_keyboard_uses_pending_input_and_qt_multiple_step_keys(owner):
    spin = FloatStepSpinBox(owner, value=15, step_increment=15)
    spin.lineEdit().setText("30")
    press(spin, qt.Qt.Key.Key_Down)
    assert spin.value() == 15
    assert spin.cleanText() == "15"
    press(spin, qt.Qt.Key.Key_PageUp)
    assert spin.value() == 165
    spin.setValue(15)
    press(spin, qt.Qt.Key.Key_Up, qt.Qt.KeyboardModifier.ControlModifier)
    assert spin.value() == 165
    multiplicative = FloatStepSpinBox(
        owner, value=1.5, step_mode="multiplicative"
    )
    press(multiplicative, qt.Qt.Key.Key_PageUp)
    assert multiplicative.value() == 1.5e10
    press(multiplicative, qt.Qt.Key.Key_PageDown)
    assert multiplicative.value() == 1.5


@pytest.mark.parametrize(
    "mode,expected", [("additive", 30), ("multiplicative", 150)]
)
def test_arrow_buttons_apply_selected_mode(owner, mode, expected):
    spin = FloatStepSpinBox(owner, value=15, step_mode=mode, step_increment=15)
    owner.show()
    flush()
    option = qt.QtWidgets.QStyleOptionSpinBox()
    spin.initStyleOption(option)
    style = qt.QtWidgets.QStyle
    rectangle = spin.style().subControlRect(
        style.ComplexControl.CC_SpinBox,
        option,
        style.SubControl.SC_SpinBoxUp,
        spin,
    )
    for kind, held in (
        (qt.QEvent.Type.MouseButtonPress, qt.Qt.MouseButton.LeftButton),
        (qt.QEvent.Type.MouseButtonRelease, qt.Qt.MouseButton.NoButton),
    ):
        event = qt.QtGui.QMouseEvent(
            kind,
            qt.QtCore.QPointF(rectangle.center()),
            qt.QtCore.QPointF(spin.mapToGlobal(rectangle.center())),
            qt.Qt.MouseButton.LeftButton,
            held,
            qt.Qt.KeyboardModifier.NoModifier,
        )
        qt.QApplication.sendEvent(spin, event)
    assert spin.value() == expected


def test_extreme_steps_saturate_finite_bounds_and_preserve_small_numbers(
    owner,
):
    spin = FloatStepSpinBox(owner, step_mode="multiplicative")
    spin.stepBy(2147483647)
    assert spin.value() == float_info.max
    spin.stepBy(-2147483647)
    assert spin.value() == 1e-323
    spin.stepDown()
    assert spin.value() == 1e-323
    for value in (1e-30, 0.12345678901234566, float_info.max):
        spin.setValue(value)
        assert spin.value() == value
        assert float(spin.cleanText()) == value


@pytest.mark.parametrize(
    "value,error",
    [
        (0, ValueError),
        (-1, ValueError),
        (float("nan"), ValueError),
        (float("inf"), ValueError),
        (True, TypeError),
        ("1", TypeError),
        (5e-324, ValueError),
    ],
)
def test_invalid_step_api_is_atomic(owner, value, error):
    spin = FloatStepSpinBox(owner, value=15)
    with pytest.raises(error):
        spin.setValue(value)
    assert spin.value() == 15
    vm = FloatViewModel(parent=owner)
    editor = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    with pytest.raises(error):
        editor.setSingleStep(value)
    assert editor.singleStep() == editor.step_spin_box.value() == 0.1


@pytest.mark.parametrize(
    "settings",
    [
        {"step_mode": "adaptive"},
        {"step_increment": 0},
        {"step_increment": float("inf")},
        {"single_step": 0},
    ],
)
def test_invalid_constructor_does_not_leave_children(owner, settings):
    vm = FloatViewModel(parent=owner)
    before = owner.children()
    with pytest.raises(ValueError):
        FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1, **settings)
    assert owner.children() == before


def test_step_changes_are_local_and_do_not_write_source_or_change_bound_steps(
    owner,
):
    class Data:
        _value = 0.123456789

        def __init__(self):
            self.writes = []

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self.writes.append(value)
            self._value = value

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=owner)
    editor = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-1,
        maximum=1,
        minimum_decimals=2,
        maximum_decimals=3,
        step_mode="multiplicative",
    )
    other = FloatRangeSliderSpinBox(binding, owner, minimum=-1, maximum=1)
    layout = editor.layout().itemAt(0).layout()
    assert layout.itemAt(3).widget() is editor.spin_box
    assert layout.itemAt(4).widget() is editor.step_spin_box
    enter(editor.step_spin_box, "0.001")
    editor.setDecimals(0)
    editor.setMinimumDecimals(3)
    editor.setMaximumDecimals(4)
    assert editor.step_spin_box.cleanText() == "0.001"
    assert editor.singleStep() == 0.001
    assert (
        editor.minimum_spin_box.singleStep()
        == editor.maximum_spin_box.singleStep()
        == 0.1
    )
    assert other.singleStep() == 0.1
    assert editor.slider.maximum() == 1000
    assert data.writes == []
    editor.setDecimals(9)
    editor.spin_box.stepUp()
    assert data.writes == [pytest.approx(0.124456789)]
    assert other.spin_box.value() == pytest.approx(0.124457)
    editor.setSingleStep(15)
    assert editor.step_spin_box.value() == 15
    assert len(data.writes) == 1


@pytest.mark.parametrize(
    "enabled,show_buttons,show_unit",
    [(True, True, True), (False, False, False)],
)
@pytest.mark.parametrize("physical", [False, True])
def test_step_configuration_survives_units_precision_lock_and_disposal(
    owner, enabled, show_buttons, show_unit, physical
):
    @dataclass
    class Data:
        value: float = 12.5

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    vm = binding.view_model
    editor = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=0,
        maximum=100,
        step_enabled=enabled,
        step_width=80,
        step_show_buttons=show_buttons,
        step_show_unit=show_unit,
        value_enabled=False,
    )
    editor.step_spin_box.setValue(15)
    assert editor.singleStep() == (15 if enabled else 0.1)
    editor.setSingleStep(1.5)
    editor.step_spin_box.lineEdit().setText("999")
    vm.set_presentation_adapter(
        lambda p: FloatPresentation(scale=0.01, suffix=" m")
    )
    editor.setDecimals(0)
    assert editor.step_spin_box.value() == editor.singleStep() == 1.5
    assert editor.step_spin_box.suffix() == (" m" if show_unit else "")
    assert "999" not in editor.step_spin_box.text()
    assert (
        editor.step_spin_box.minimumWidth()
        == editor.step_spin_box.maximumWidth()
        == 80
    )
    assert editor.step_spin_box.isEnabled() is enabled
    symbols = qt.QtWidgets.QAbstractSpinBox.ButtonSymbols
    assert editor.step_spin_box.buttonSymbols() == (
        symbols.UpDownArrows if show_buttons else symbols.NoButtons
    )
    assert binding.value == 12.5
    if physical:
        vm.deleteLater()
    else:
        binding.dispose()
    flush()
    assert not editor.step_spin_box.isEnabled()
    with pytest.raises(RuntimeError):
        editor.setSingleStep(1)
