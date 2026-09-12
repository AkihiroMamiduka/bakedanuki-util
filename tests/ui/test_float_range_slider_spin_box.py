# coding: utf-8
from dataclasses import dataclass
from sys import float_info

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatLabel,
    FloatPresentation,
    FloatRangeSliderSpinBox,
    FloatViewModel,
    qt,
)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def enter(spin_box, text):
    spin_box.lineEdit().setText(text)
    for kind in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        event = qt.QtGui.QKeyEvent(
            kind, qt.Qt.Key.Key_Return, qt.Qt.KeyboardModifier.NoModifier
        )
        qt.QApplication.sendEvent(spin_box, event)


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def test_range_changes_preserve_source_and_unedited_endpoint_precision(owner):
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
        minimum=-0.123456789,
        maximum=1.123456789,
        decimals=3,
        minimum_decimals=3,
        maximum_decimals=3,
    )
    other = FloatRangeSliderSpinBox(binding, owner, minimum=-10, maximum=10)
    label = FloatLabel(binding, owner, decimals=9)
    assert data.writes == []
    editor.minimum_spin_box.editingFinished.emit()
    assert editor.floatRange() == (-0.123456789, 1.123456789)
    enter(editor.maximum_spin_box, "2.5")
    assert editor.floatRange() == (-0.123456789, 2.5)
    assert other.floatRange() == (-10, 10)
    editor.setFloatRange(2, 4)
    assert editor.slider.value() == 0
    assert data.writes == []
    assert label.text() == "0.123456789"
    editor.slider.setValue(750)
    assert data.writes == [3.5]
    assert other.spin_box.value() == 3.5
    assert label.text() == "3.500000000"
    editor.spin_box.setValue(20)
    assert data.writes == [3.5, 20]
    assert editor.slider.value() == 1000


@pytest.mark.parametrize(
    "minimum,value", [(True, 1), (True, 2), (False, 0), (False, -1)]
)
def test_invalid_edit_restores_range_with_visible_reason(
    owner, minimum, value
):
    vm = FloatViewModel(0.5, owner)
    editor = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    rejected = []
    editor.rangeEditRejected.connect(rejected.append)
    spin = editor.minimum_spin_box if minimum else editor.maximum_spin_box
    enter(spin, str(value))
    assert editor.floatRange() == (0, 1)
    assert editor.minimum_spin_box.value() == 0
    assert editor.maximum_spin_box.value() == 1
    assert vm.value.value == 0.5
    assert len(rejected) == 1
    assert "Min < Max" in editor.range_status_label.text()
    assert not editor.range_status_label.isHidden()
    enter(spin, "-2" if minimum else "2")
    assert editor.range_status_label.isHidden()


@pytest.mark.parametrize(
    "bounds", [(1, 1), (2, 1), (float("nan"), 1), (0, float("inf"))]
)
def test_invalid_api_is_atomic_and_emits_no_range_notification(owner, bounds):
    editor = FloatRangeSliderSpinBox(
        FloatViewModel(parent=owner), owner, minimum=0, maximum=1
    )
    notifications = []
    editor.slider.floatRangeChanged.connect(
        lambda low, high: notifications.append((low, high))
    )
    with pytest.raises(ValueError):
        editor.setFloatRange(*bounds)
    assert editor.floatRange() == (0, 1)
    assert notifications == []
    editor.slider.setFloatRange(-2, 3)
    assert notifications == [(-2, 3)]
    assert editor.minimum_spin_box.value() == -2
    assert editor.maximum_spin_box.value() == 3
    editor.slider.setFloatRange(-2, 3)
    assert len(notifications) == 1


def test_hard_limits_are_visible_and_can_recover_an_empty_range(owner):
    vm = FloatViewModel(
        0.5, owner, presentation=FloatPresentation(minimum=0, maximum=1)
    )
    editor = FloatRangeSliderSpinBox(vm, owner, minimum=-10, maximum=10)
    assert editor.floatRange() == (-10, 10)
    assert editor.effectiveFloatRange() == (0, 1)
    assert "Usable range" in editor.range_status_label.text()
    editor.setFloatRange(2, 3)
    assert editor.effectiveFloatRange() is None
    assert not editor.slider.isEnabled()
    assert editor.spin_box.isEnabled()
    assert editor.minimum_spin_box.isEnabled()
    assert "No usable" in editor.range_status_label.text()
    enter(editor.minimum_spin_box, "0")
    assert editor.slider.isEnabled()
    assert editor.effectiveFloatRange() == (0, 1)
    editor.setFloatRange(0, 1)
    assert editor.range_status_label.isHidden()
    assert vm.value.value == 0.5


def test_units_and_precision_discard_pending_text_without_writes(owner):
    @dataclass
    class Data:
        value: float = 12.3456789

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=owner)
    editor = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-123.456789,
        maximum=200,
        decimals=6,
        minimum_decimals=6,
        maximum_decimals=4,
        maximum_show_unit=True,
    )
    editor.minimum_spin_box.lineEdit().setText("-999")
    binding.view_model.set_presentation_adapter(
        lambda p: FloatPresentation(0.01, " m")
    )
    assert editor.minimum_spin_box.value() == -1.234568
    assert editor.maximum_spin_box.suffix() == " m"
    enter(editor.maximum_spin_box, "3 m")
    assert editor.floatRange() == (-123.456789, 300)
    editor.setDecimals(2)
    assert editor.minimum_spin_box.value() == -1.234568
    assert editor.maximumDecimals() == 4
    editor.setMinimumDecimals(2)
    assert editor.minimum_spin_box.value() == -1.23
    assert editor.spin_box.value() == 0.12
    editor.setDecimals(9)
    editor.setMinimumDecimals(9)
    assert editor.minimum_spin_box.value() == -1.23456789
    assert editor.spin_box.value() == 0.123456789
    assert binding.value == data.value == 12.3456789
    assert editor.floatRange() == (-123.456789, 300)
    editor.setSingleStep(0.25)
    assert editor.singleStep() == editor.maximum_spin_box.singleStep() == 0.25


def test_precision_restores_hard_limits_without_changing_value(owner):
    vm = FloatViewModel(
        0.123456,
        owner,
        presentation=FloatPresentation(minimum=0.123456, maximum=0.987654),
    )
    editor = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    editor.setDecimals(1)
    editor.setDecimals(6)
    assert vm.value.value == editor.spin_box.value() == 0.123456
    assert editor.spin_box.minimum() == 0.123456
    assert editor.spin_box.maximum() == 0.987654


def test_readonly_value_still_allows_view_range_edits(owner):
    class Data:
        @property
        def value(self):
            return 0.5

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    editor = FloatRangeSliderSpinBox(binding, owner, minimum=0, maximum=1)
    assert not editor.slider.isEnabled()
    assert not editor.spin_box.isEnabled()
    assert editor.minimum_spin_box.isEnabled()
    enter(editor.minimum_spin_box, "-1")
    assert editor.floatRange() == (-1, 1)
    assert binding.value == 0.5


@pytest.mark.parametrize("physical", [False, True])
def test_dispose_or_qobject_deletion_stops_all_inputs(owner, physical):
    vm = FloatViewModel(0.5, owner)
    editor = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    if physical:
        vm.deleteLater()
        flush()
    else:
        vm.dispose()
    for spin in (
        editor.minimum_spin_box,
        editor.maximum_spin_box,
        editor.spin_box,
        editor.slider,
    ):
        assert not spin.isEnabled()
    with pytest.raises(RuntimeError):
        editor.setFloatRange(-10, 10)


def test_range_change_finishes_only_its_own_gesture(owner):
    vm = FloatViewModel(0.5, owner)
    first = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    second = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    first.slider.setSliderDown(True)
    first.slider.setValue(700)
    second.setFloatRange(0, 2)
    assert vm.is_editing
    enter(first.maximum_spin_box, "3")
    assert not vm.is_editing
    assert vm.value.value == 0.7
    first.slider.setSliderDown(True)
    first.close()
    assert not vm.is_editing
    first.deleteLater()
    flush()
    assert vm.set_value_command.execute(0.4)
    assert second.spin_box.value() == 0.4


def test_focus_out_commits_pending_bound_before_slider_input(owner):
    vm = FloatViewModel(0.5, owner)
    editor = FloatRangeSliderSpinBox(vm, owner, minimum=0, maximum=1)
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(editor)
    owner.show()
    owner.activateWindow()
    editor.maximum_spin_box.setFocus()
    flush()
    editor.maximum_spin_box.lineEdit().setText("2")
    assert editor.floatRange() == (0, 1)
    editor.slider.setFocus()
    flush()
    assert editor.floatRange() == (0, 2)
    assert vm.value.value == 0.5
    editor.slider.setValue(500)
    assert vm.value.value == 1


def test_display_overflow_disables_bounds_and_recovers_without_data_loss(
    owner,
):
    @dataclass
    class Data:
        value: float = 0

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    editor = FloatRangeSliderSpinBox(
        binding, owner, minimum=-float_info.max, maximum=float_info.max
    )
    binding.view_model.set_presentation_adapter(
        lambda p: FloatPresentation(2, " units")
    )
    assert not editor.minimum_spin_box.isEnabled()
    assert "cannot be displayed" in editor.range_status_label.text()
    assert editor.floatRange() == (-float_info.max, float_info.max)
    editor.setFloatRange(-10, 10)
    assert editor.minimum_spin_box.isEnabled()
    assert editor.maximum_spin_box.value() == 20
    assert binding.value == 0


@pytest.mark.parametrize(
    "field,value,error",
    [
        ("slider_width", 0, ValueError),
        ("minimum_width", -1, ValueError),
        ("maximum_width", 16777216, ValueError),
        ("value_width", True, TypeError),
        ("slider_width", 80.5, TypeError),
        ("maximum_width", "80", TypeError),
    ],
)
def test_invalid_widths_leave_no_partial_widget(owner, field, value, error):
    vm = FloatViewModel(parent=owner)
    before = owner.children()
    with pytest.raises(error):
        FloatRangeSliderSpinBox(
            vm, owner, minimum=0, maximum=1, **{field: value}
        )
    assert owner.children() == before


@pytest.mark.parametrize(
    "field,value",
    [
        ("minimum_enabled", 0),
        ("maximum_enabled", None),
        ("value_enabled", 1),
        ("minimum_show_buttons", "False"),
        ("maximum_show_buttons", None),
        ("value_show_buttons", 0),
        ("value_show_unit", "False"),
        ("minimum_show_unit", 0),
        ("maximum_show_unit", None),
    ],
)
def test_invalid_flags_leave_no_partial_widget(owner, field, value):
    vm = FloatViewModel(parent=owner)
    before = owner.children()
    with pytest.raises(TypeError):
        FloatRangeSliderSpinBox(
            vm, owner, minimum=0, maximum=1, **{field: value}
        )
    assert owner.children() == before


@pytest.mark.parametrize(
    "widths",
    [
        (None, None, None, None),
        (None, 60, 70, 90),
        (160, None, 70, None),
        (160, 60, 70, 90),
    ],
)
def test_widths_fix_requested_fields_and_stretch_unspecified_fields(
    owner, widths
):
    editor = FloatRangeSliderSpinBox(
        FloatViewModel(parent=owner),
        owner,
        minimum=-100,
        maximum=100,
        slider_width=widths[0],
        minimum_width=widths[1],
        maximum_width=widths[2],
        value_width=widths[3],
    )
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(editor)
    owner.resize(2000, 200)
    owner.show()
    flush()
    children = (
        editor.slider,
        editor.minimum_spin_box,
        editor.maximum_spin_box,
        editor.spin_box,
    )
    before = [child.width() for child in children]
    owner.resize(2600, 200)
    flush()
    growth = []
    for child, requested, previous in zip(children, widths, before):
        if requested is not None:
            assert child.width() == previous == requested
        else:
            assert child.width() > previous
            growth.append(child.width() - previous)
    if growth:
        assert max(growth) - min(growth) <= 1


def test_fixed_widths_and_absent_prefix_survive_units_range_and_precision(
    owner,
):
    @dataclass
    class Data:
        value: float = 0.125

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    vm = binding.view_model
    editor = FloatRangeSliderSpinBox(
        vm,
        owner,
        minimum=-100,
        maximum=100,
        slider_width=160,
        minimum_width=40,
        maximum_width=50,
        value_width=60,
        minimum_show_buttons=False,
        maximum_show_buttons=False,
        value_show_buttons=False,
    )
    vm.set_presentation_adapter(
        lambda p: FloatPresentation(scale=0.01, suffix=" m")
    )
    editor.setFloatRange(-123456.789, 123456.789)
    editor.setDecimals(15)
    editor.setMinimumDecimals(15)
    editor.setMaximumDecimals(15)
    assert editor.minimum_spin_box.suffix() == ""
    assert editor.maximum_spin_box.value() == pytest.approx(1234.56789)
    for child, width in (
        (editor.slider, 160),
        (editor.minimum_spin_box, 40),
        (editor.maximum_spin_box, 50),
        (editor.spin_box, 60),
    ):
        assert child.minimumWidth() == child.maximumWidth() == width
    assert (
        editor.minimum_spin_box.prefix()
        == editor.maximum_spin_box.prefix()
        == ""
    )
    assert "minimum" in editor.minimum_spin_box.toolTip()
    assert "maximum" in editor.maximum_spin_box.toolTip()
    assert editor.minimum_spin_box.accessibleName() == "Slider minimum"
    assert editor.maximum_spin_box.accessibleName() == "Slider maximum"
    assert vm.value.value == 0.125


@pytest.mark.parametrize(
    "minimum_enabled,maximum_enabled",
    [(True, True), (True, False), (False, True), (False, False)],
)
def test_range_input_flags_survive_refresh_and_do_not_block_range_api(
    owner, minimum_enabled, maximum_enabled
):
    @dataclass
    class Data:
        value: float = 0.5

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    vm = binding.view_model
    editor = FloatRangeSliderSpinBox(
        vm,
        owner,
        minimum=-1,
        maximum=1,
        minimum_enabled=minimum_enabled,
        maximum_enabled=maximum_enabled,
    )
    vm.set_presentation_adapter(
        lambda p: FloatPresentation(scale=2, suffix=" units")
    )
    editor.setDecimals(3)
    editor.setFloatRange(-2, 2)
    for spin_box, enabled in (
        (editor.minimum_spin_box, minimum_enabled),
        (editor.maximum_spin_box, maximum_enabled),
    ):
        assert spin_box.isEnabled() is enabled
    editor.minimum_spin_box.setValue(-6)
    editor.maximum_spin_box.setValue(6)
    assert editor.floatRange() == (
        -3 if minimum_enabled else -2,
        3 if maximum_enabled else 2,
    )
    editor.setFloatRange(-5, 5)
    assert editor.minimum_spin_box.value() == -10
    assert editor.maximum_spin_box.value() == 10
    assert editor.slider.isEnabled()
    assert editor.spin_box.isEnabled()
    editor.slider.setValue(750)
    assert vm.value.value == 2.5
    editor.spin_box.setValue(6)
    assert vm.value.value == 3
    vm.dispose()
    assert not editor.minimum_spin_box.isEnabled()
    assert not editor.maximum_spin_box.isEnabled()


def test_overflow_recovery_preserves_explicitly_disabled_input(owner):
    @dataclass
    class Data:
        value: float = 0

    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    vm = binding.view_model
    editor = FloatRangeSliderSpinBox(
        vm,
        owner,
        minimum=-float_info.max,
        maximum=float_info.max,
        minimum_enabled=False,
        maximum_enabled=True,
    )
    vm.set_presentation_adapter(lambda p: FloatPresentation(scale=2))
    assert not editor.minimum_spin_box.isEnabled()
    assert not editor.maximum_spin_box.isEnabled()
    editor.setFloatRange(-1, 1)
    assert not editor.minimum_spin_box.isEnabled()
    assert editor.maximum_spin_box.isEnabled()
    assert vm.value.value == 0


@pytest.mark.parametrize(
    "visibility",
    [
        (True, True, True),
        (False, False, False),
        (True, False, False),
        (False, True, False),
        (False, False, True),
    ],
)
def test_button_visibility_preserves_text_and_keyboard_input(
    owner, visibility
):
    vm = FloatViewModel(0.5, owner)
    editor = FloatRangeSliderSpinBox(
        vm,
        owner,
        minimum=-1,
        maximum=1,
        single_step=0.25,
        minimum_show_buttons=visibility[0],
        maximum_show_buttons=visibility[1],
        value_show_buttons=visibility[2],
    )
    symbols = qt.QtWidgets.QAbstractSpinBox.ButtonSymbols
    editor.setDecimals(3)
    editor.setMinimumDecimals(1)
    editor.setMaximumDecimals(2)
    editor.setFloatRange(-2, 2)
    for spin_box, show_buttons in zip(
        (
            editor.minimum_spin_box,
            editor.maximum_spin_box,
            editor.spin_box,
        ),
        visibility,
    ):
        expected = symbols.UpDownArrows if show_buttons else symbols.NoButtons
        assert spin_box.buttonSymbols() == expected
    enter(editor.minimum_spin_box, "-3")
    enter(editor.maximum_spin_box, "3")
    assert vm.value.value == 0.5
    assert editor.floatRange() == (-3, 3)
    event = qt.QtGui.QKeyEvent(
        qt.QEvent.Type.KeyPress,
        qt.Qt.Key.Key_Up,
        qt.Qt.KeyboardModifier.NoModifier,
    )
    qt.QApplication.sendEvent(editor.spin_box, event)
    assert vm.value.value == 0.75
    enter(editor.spin_box, "1.25")
    assert vm.value.value == 1.25


@pytest.mark.parametrize("field", ["minimum_decimals", "maximum_decimals"])
@pytest.mark.parametrize(
    "value,error",
    [(-1, ValueError), (324, ValueError), (True, TypeError), (1.5, TypeError)],
)
def test_invalid_bound_precision_leaves_no_partial_widget(
    owner, field, value, error
):
    vm = FloatViewModel(parent=owner)
    before = owner.children()
    with pytest.raises(error):
        FloatRangeSliderSpinBox(
            vm, owner, minimum=0, maximum=1, **{field: value}
        )
    assert owner.children() == before


def test_default_bound_precision_preserves_fractional_range_until_edited(
    owner,
):
    vm = FloatViewModel(0.123456789, owner)
    editor = FloatRangeSliderSpinBox(
        vm, owner, minimum=-0.123456789, maximum=0.234567891
    )
    ranges, values = [], []
    editor.slider.floatRangeChanged.connect(
        lambda *bounds: ranges.append(bounds)
    )
    vm.value.changed.connect(values.append)
    assert editor.minimumDecimals() == editor.maximumDecimals() == 0
    assert (
        editor.minimum_spin_box.value() == editor.maximum_spin_box.value() == 0
    )
    enter(editor.minimum_spin_box, editor.minimum_spin_box.text())
    enter(editor.maximum_spin_box, editor.maximum_spin_box.text())
    assert ranges == values == []
    assert editor.slider.isEnabled()
    editor.setMinimumDecimals(9)
    editor.setMaximumDecimals(9)
    assert editor.minimum_spin_box.value() == -0.123456789
    assert editor.maximum_spin_box.value() == 0.234567891
    assert editor.decimals() == 6
    editor.setMinimumDecimals(0)
    assert editor.maximumDecimals() == 9
    editor.minimum_spin_box.stepDown()
    assert editor.floatRange() == (-1, 0.234567891)
    assert values == []


def test_bound_steps_follow_each_precision_without_changing_current_step(
    owner,
):
    vm = FloatViewModel(0.5, owner)
    editor = FloatRangeSliderSpinBox(
        vm,
        owner,
        minimum=-2,
        maximum=2,
        single_step=0.001,
        minimum_decimals=0,
        maximum_decimals=2,
    )
    assert editor.singleStep() == 0.001
    editor.minimum_spin_box.stepDown()
    editor.maximum_spin_box.stepUp()
    assert editor.floatRange() == (-3, 2.01)
    editor.setMaximumDecimals(0)
    editor.setSingleStep(10)
    assert editor.singleStep() == 10
    assert (
        editor.minimum_spin_box.singleStep()
        == editor.maximum_spin_box.singleStep()
        == 1
    )
    editor.maximum_spin_box.stepUp()
    assert editor.floatRange() == (-3, 3)
    assert vm.value.value == 0.5


@pytest.mark.parametrize("physical", [False, True])
def test_value_disabled_keeps_slider_and_shared_views_live(owner, physical):
    @dataclass
    class Data:
        value: float = 0.25

    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=owner)
    vm = binding.view_model
    editor = FloatRangeSliderSpinBox(
        binding, owner, minimum=0, maximum=1, value_enabled=False
    )
    other = FloatRangeSliderSpinBox(binding, owner, minimum=0, maximum=1)
    assert not editor.spin_box.isEnabled()
    assert not editor.spin_box.isInputEnabled()
    assert editor.focusProxy() is editor.slider
    editor.spin_box.setValue(0.75)
    assert binding.value == editor.spin_box.value() == 0.25
    editor.slider.setValue(500)
    assert (
        binding.value
        == other.spin_box.value()
        == editor.spin_box.value()
        == 0.5
    )
    other.spin_box.setValue(0.75)
    assert editor.spin_box.value() == 0.75
    data.value = 0.125
    binding.refresh()
    vm.set_presentation_adapter(lambda p: FloatPresentation(2, " units"))
    editor.setDecimals(4)
    assert editor.spin_box.value() == 0.25
    assert not editor.spin_box.isEnabled()
    assert (
        editor.minimum_spin_box.isEnabled()
        and editor.maximum_spin_box.isEnabled()
    )
    if physical:
        vm.deleteLater()
        flush()
    else:
        binding.dispose()
    editor.spin_box.setInputEnabled(True)
    assert not editor.spin_box.isEnabled()
    assert not editor.slider.isEnabled()


@pytest.mark.parametrize(
    "minimum_show_unit,maximum_show_unit",
    [(False, False), (False, True), (True, False), (True, True)],
)
def test_unit_visibility_keeps_conversion_limits_precision_and_other_views(
    owner,
    minimum_show_unit,
    maximum_show_unit,
):
    @dataclass
    class Data:
        value: float = 123.456789

    data = Data()
    binding = FloatBinding.from_attribute(
        data,
        "value",
        parent=owner,
        presentation=FloatPresentation(0.01, " m", minimum=0, maximum=200),
    )
    editor = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-100,
        maximum=300,
        decimals=6,
        minimum_show_unit=minimum_show_unit,
        maximum_show_unit=maximum_show_unit,
    )
    other = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-100,
        maximum=300,
        decimals=6,
        value_show_unit=True,
    )
    label = FloatLabel(binding, owner, decimals=6)
    assert not editor.spin_box.isUnitVisible()
    assert editor.spin_box.suffix() == ""
    assert editor.spin_box.text() == "1.234568"
    assert editor.spin_box.minimum() == 0
    assert editor.spin_box.maximum() == 2
    assert editor.minimum_spin_box.suffix() == (
        " m" if minimum_show_unit else ""
    )
    assert editor.maximum_spin_box.suffix() == (
        " m" if maximum_show_unit else ""
    )
    assert (
        other.minimum_spin_box.suffix()
        == other.maximum_spin_box.suffix()
        == ""
    )
    assert other.spin_box.text() == label.text() == "1.234568 m"
    changes = []
    binding.changed.connect(changes.append)
    editor.spin_box.lineEdit().setText("99")
    editor.spin_box.setUnitVisible(True)
    enter(editor.spin_box, editor.spin_box.text())
    editor.spin_box.setUnitVisible(False)
    editor.setDecimals(9)
    assert editor.spin_box.text() == "1.234567890"
    assert data.value == 123.456789
    assert changes == []
    binding.view_model.set_presentation_adapter(
        lambda p: FloatPresentation(0.001, " units", minimum=0, maximum=200)
    )
    assert editor.spin_box.suffix() == ""
    assert editor.spin_box.value() == pytest.approx(0.123456789)
    assert editor.spin_box.maximum() == 0.2
    assert other.spin_box.suffix() == " units"
    assert editor.minimum_spin_box.suffix() == (
        " units" if minimum_show_unit else ""
    )
    assert editor.maximum_spin_box.suffix() == (
        " units" if maximum_show_unit else ""
    )
    enter(editor.spin_box, "0.15")
    assert binding.value == data.value == 150
    assert label.text() == other.spin_box.text() == "0.150000 units"
    assert editor.floatRange() == (-100, 300)
    editor.setMinimumDecimals(3)
    editor.setMaximumDecimals(3)
    enter(editor.minimum_spin_box, "-0.2" + editor.minimum_spin_box.suffix())
    enter(editor.maximum_spin_box, "0.5" + editor.maximum_spin_box.suffix())
    assert editor.floatRange() == (-200, 500)
    assert other.floatRange() == (-100, 300)
    assert editor.minimum_spin_box.suffix() == (
        " units" if minimum_show_unit else ""
    )
    assert editor.maximum_spin_box.suffix() == (
        " units" if maximum_show_unit else ""
    )
    assert binding.value == data.value == 150
    assert changes == [150]
    editor.spin_box.setInputEnabled(False)
    editor.spin_box.setUnitVisible(True)
    assert editor.spin_box.text() == "0.150000000 units"
    assert not editor.spin_box.isEnabled()
    with pytest.raises(TypeError):
        editor.spin_box.setUnitVisible(0)
    assert editor.spin_box.isUnitVisible()
    binding.dispose()
    with pytest.raises(RuntimeError):
        editor.spin_box.setUnitVisible(False)
