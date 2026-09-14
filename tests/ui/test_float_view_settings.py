# coding: utf-8
from dataclasses import dataclass, replace
import json
from sys import float_info

import pytest

from bd_util.ui import (
    FloatBinding,
    Float3Binding,
    FloatRangeSliderSpinBox,
    Float3RangeSliderSpinBox,
    FloatPresentation,
    SettingsPath,
    UiStateManager,
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


@pytest.fixture
def settings(tmp_path):
    return qt.QtCore.QSettings(
        str(tmp_path / "ui.ini"), qt.QtCore.QSettings.Format.IniFormat
    )


def manager(settings, path="sample/editor_settings/main"):
    return UiStateManager(settings, SettingsPath(path))


def make_editor(owner, *, value=1.23456789012345, presentation=None, **kwargs):
    @dataclass
    class Data:
        number: float = value

    binding = FloatBinding.from_attribute(
        Data(), "number", parent=owner, presentation=presentation
    )
    editor = FloatRangeSliderSpinBox(
        binding, owner, minimum=-10, maximum=10, **kwargs
    )
    return binding, editor


def state_key(key="value"):
    return f"editor_settings/main/ui_state/widgets/{key}/state"


def read_payload(settings, key="value"):
    return json.loads(bytes(settings.value(state_key(key))))


def write_payload(settings, payload, key="value"):
    settings.setValue(
        state_key(key),
        qt.QtCore.QByteArray(json.dumps(payload).encode("utf-8")),
    )


@pytest.mark.parametrize(
    "step", [0.0012345678901234567, 1e-323, float_info.max]
)
def test_roundtrip_keeps_unrounded_settings_and_source_value(
    owner, settings, step
):
    binding, first = make_editor(owner, decimals=0, minimum_decimals=0)
    original = binding.value
    source = manager(settings)
    source.register_float_range_slider_spin_box("value", first)
    first.setFloatRange(-1.2345678901234567, 9.876543210987654)
    first.setSingleStep(step)
    assert source.save_cached()
    _, second = make_editor(
        owner,
        decimals=2,
        minimum_enabled=False,
        maximum_enabled=False,
        step_enabled=False,
        step_mode="multiplicative",
    )
    restored = manager(settings)
    restored.register_float_range_slider_spin_box("value", second)
    observed = []
    second.settingsChanged.connect(
        lambda: observed.append((*second.floatRange(), second.singleStep()))
    )
    assert restored.restore() == frozenset({"value"})
    assert second.floatRange() == first.floatRange()
    assert second.singleStep() == step
    assert observed == [(*first.floatRange(), step)]
    assert second.step_spin_box.stepMode() == "multiplicative"
    assert not second.minimum_spin_box.isEnabled()
    assert binding.value == original
    assert second.view_model.value.value == original
    assert set(read_payload(settings)) == {
        "version",
        "unit_kind",
        "minimum",
        "maximum",
        "single_step",
    }


def test_only_confirmed_range_step_and_kind_changes_notify(owner, settings):
    binding, editor = make_editor(owner)
    state = manager(settings)
    state.register_float_range_slider_spin_box("value", editor)
    changed = []
    editor.settingsChanged.connect(
        lambda: changed.append((*editor.floatRange(), editor.singleStep()))
    )
    editor.setFloatRange(-20, 20)
    editor.setSingleStep(15)
    editor.setSingleStep(15)
    editor.step_spin_box.stepDown()
    assert len(changed) == 3
    editor.minimum_spin_box.lineEdit().setText("-30")
    assert len(changed) == 3
    editor.setDecimals(3)
    editor.setMinimumDecimals(2)
    binding.view_model.set_presentation_adapter(
        lambda p: replace(p, scale=0.01, suffix=" m")
    )
    editor.slider.setSliderDown(True)
    for position in (100, 200, 300):
        editor.slider.setValue(position)
    editor.slider.setSliderDown(False)
    assert len(changed) == 3
    assert not settings.contains(state_key())
    binding.view_model.set_presentation_adapter(
        lambda p: replace(p, unit_kind="distance")
    )
    assert len(changed) == 4
    assert state.save_cached()
    assert read_payload(settings)["unit_kind"] == "distance"


@pytest.mark.parametrize(
    "update",
    [
        {"version": 2},
        {"version": True},
        {"version": 1.0},
        {"unit_kind": "angle"},
        {"unit_kind": None},
        {"minimum": 20},
        {"minimum": True},
        {"maximum": float("inf")},
        {"minimum": float("nan")},
        {"maximum": "10"},
        {"single_step": 0},
        {"single_step": -1},
        {"single_step": True},
        {"single_step": float("inf")},
        {"single_step": 5e-324},
    ],
)
def test_invalid_state_is_rejected_before_any_setting_is_applied(
    owner, settings, update
):
    binding, editor = make_editor(owner)
    state = manager(settings)
    state.register_float_range_slider_spin_box("value", editor)
    assert state.save()
    data = read_payload(settings)
    data.update(minimum=-100, maximum=100, single_step=15)
    data.update(update)
    if update == {"minimum": 20}:
        data["maximum"] = 10
    write_payload(settings, data)
    changes = []
    editor.settingsChanged.connect(lambda: changes.append(True))
    assert state.restore() == frozenset()
    assert editor.floatRange() == (-10, 10)
    assert editor.singleStep() == 0.1
    assert binding.value == 1.23456789012345
    assert not changes
    assert not settings.contains(state_key())


@pytest.mark.parametrize(
    "raw",
    [
        qt.QtCore.QByteArray(b"{"),
        qt.QtCore.QByteArray(b"[]"),
        qt.QtCore.QByteArray(b"{}"),
        qt.QtCore.QByteArray(b"\xff"),
        "text",
        123,
    ],
)
def test_malformed_or_missing_state_keeps_initial_settings(
    owner, settings, raw
):
    _, editor = make_editor(owner)
    state = manager(settings)
    state.register_float_range_slider_spin_box("value", editor)
    assert not state.restore()
    state.save()
    settings.setValue(state_key(), raw)
    assert not state.restore()
    assert editor.floatRange() == (-10, 10)
    assert editor.singleStep() == 0.1


def test_range_display_overflow_is_rejected_and_hard_limits_do_not_replace_range(
    owner, settings
):
    _, editor = make_editor(owner)
    first = manager(settings)
    first.register_float_range_slider_spin_box("value", editor)
    editor.setFloatRange(-100, 100)
    editor.setSingleStep(15)
    first.save()
    _, limited = make_editor(
        owner, value=0.5, presentation=FloatPresentation(minimum=0, maximum=1)
    )
    second = manager(settings)
    second.register_float_range_slider_spin_box("value", limited)
    assert second.restore() == frozenset({"value"})
    assert limited.floatRange() == (-100, 100)
    assert limited.effectiveFloatRange() == (0, 1)
    _, overflow = make_editor(
        owner, value=0, presentation=FloatPresentation(scale=1e307)
    )
    third = manager(settings)
    third.register_float_range_slider_spin_box("value", overflow)
    assert not third.restore()
    assert overflow.floatRange() == (-10, 10)
    assert overflow.singleStep() == 0.1


def test_axes_and_shared_views_save_independently_and_invalid_y_keeps_x_z(
    owner, settings
):
    @dataclass
    class Data:
        value: tuple[float, float, float] = (
            1.23456789,
            2.34567891,
            3.45678912,
        )

    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3RangeSliderSpinBox(binding, owner, minimum=-10, maximum=10)
    linked = Float3RangeSliderSpinBox(
        binding, owner, minimum=-100, maximum=100
    )
    first = manager(settings)
    first.register_float3_range_slider_spin_box("position", view)
    first.register_float3_range_slider_spin_box("linked", linked)
    assert first.registered_keys == (
        "position_x",
        "position_y",
        "position_z",
        "linked_x",
        "linked_y",
        "linked_z",
    )
    for i, axis in enumerate((view.x_editor, view.y_editor, view.z_editor), 1):
        axis.setFloatRange(-20 * i, 20 * i)
        axis.setSingleStep(i * 15)
    linked.x_editor.setSingleStep(0.001)
    first.save_cached()
    payload = read_payload(settings, "position_y")
    payload["single_step"] = -1
    write_payload(settings, payload, "position_y")
    restored = Float3RangeSliderSpinBox(binding, owner, minimum=-5, maximum=5)
    second = manager(settings)
    second.register_float3_range_slider_spin_box("position", restored)
    assert second.restore() == frozenset({"position_x", "position_z"})
    assert restored.x_editor.floatRange() == (-20, 20)
    assert restored.y_editor.floatRange() == (-5, 5)
    assert restored.y_editor.singleStep() == 0.1
    assert restored.z_editor.floatRange() == (-60, 60)
    assert restored.z_editor.singleStep() == 45
    second.save_cached()
    assert read_payload(settings, "linked_x")["single_step"] == 0.001
    assert binding.value == Data().value


def test_registration_validates_all_axes_before_mutating_registry(
    owner, settings
):
    @dataclass
    class Data:
        value: tuple[float, float, float] = (1, 2, 3)

    view = Float3RangeSliderSpinBox(
        Float3Binding.from_attribute(Data(), "value", parent=owner),
        owner,
        minimum=0,
        maximum=10,
    )
    state = manager(settings)
    state.register_float_range_slider_spin_box("position_z", view.z_editor)
    with pytest.raises(ValueError):
        state.register_float3_range_slider_spin_box("position", view)
    assert state.registered_keys == ("position_z",)
    with pytest.raises(TypeError):
        state.register_float_range_slider_spin_box("wrong", owner)
    with pytest.raises(TypeError):
        state.register_float3_range_slider_spin_box("wrong", view.x_editor)
    with pytest.raises(ValueError):
        state.register_float_range_slider_spin_box("bad/key", view.x_editor)
    view.view_model.dispose()
    with pytest.raises(RuntimeError):
        state.register_float3_range_slider_spin_box("disposed", view)
    assert state.registered_keys == ("position_z",)


@pytest.mark.parametrize("termination", ["binding", "widget", "component"])
def test_disposal_preserves_cached_settings_without_reading_dead_source(
    owner, settings, termination
):
    binding, editor = make_editor(owner)
    state = manager(settings)
    state.register_float_range_slider_spin_box("value", editor)
    editor.setFloatRange(-25, 25)
    editor.setSingleStep(2.5)
    if termination == "binding":
        binding.dispose()
    elif termination == "component":
        binding.view_model.deleteLater()
    else:
        editor.deleteLater()
    flush()
    assert state.save()
    assert read_payload(settings)["single_step"] == 2.5
    assert not state.restore()
    assert settings.contains(state_key())
    _, replacement = make_editor(owner)
    next_state = manager(settings)
    next_state.register_float_range_slider_spin_box("value", replacement)
    assert next_state.restore() == frozenset({"value"})
    assert replacement.floatRange() == (-25, 25)


def test_settings_path_separates_layout_reset_from_editor_preferences(
    owner, settings
):
    _, editor = make_editor(owner)
    preferences = manager(settings)
    preferences.register_float_range_slider_spin_box("value", editor)
    editor.setSingleStep(15)
    assert preferences.save_cached()
    layout = manager(settings, "sample/windows/main")
    tabs = qt.QTabWidget(owner)
    tabs.addTab(qt.QWidget(), "One")
    layout.register_tab_widget("tabs", tabs)
    assert layout.save()
    assert layout.clear()
    assert settings.contains(state_key())
    assert read_payload(settings)["single_step"] == 15


@pytest.mark.parametrize("kind", ["number", "distance", "angle"])
def test_presentation_carries_explicit_unit_kind(kind):
    assert FloatPresentation(unit_kind=kind).unit_kind == kind
    with pytest.raises(ValueError):
        FloatPresentation(unit_kind="cm")
