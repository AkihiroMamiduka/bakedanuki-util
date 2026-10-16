# coding: utf-8
"""整数複合Viewの範囲・Step・保存・寿命を利用者の操作として検証する。"""

from dataclasses import dataclass
import json

import pytest

from bd_util.ui import (
    IntBinding,
    IntPresentation,
    IntRangeSliderSpinBox,
    IntSliderSpinBox,
    SettingsPath,
    UiStateManager,
    qt,
)


@dataclass
class Data:
    """整数の確定値を保持する正本。"""

    value: int = 42


def flush():
    """遅延破棄と表示イベントを処理する。"""
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    qt.QApplication.processEvents()


@pytest.fixture
def owner(qt_application):
    """テスト用WidgetとBindingを所有する。"""
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def make_editor(owner, *, presentation=None, **kwargs):
    """同じ初期値の正本と複合Viewを作る。"""
    binding = IntBinding.from_attribute(
        Data(), "value", parent=owner, presentation=presentation
    )
    editor = IntRangeSliderSpinBox(
        binding, owner, minimum=-100, maximum=100, **kwargs
    )
    return binding, editor


def make_manager(tmp_path):
    """テスト専用の保存先を使う。"""
    settings = qt.QtCore.QSettings(
        str(tmp_path / "int.ini"), qt.QtCore.QSettings.Format.IniFormat
    )
    return settings, UiStateManager(
        settings, SettingsPath("sample/editor_settings/main")
    )


@pytest.mark.parametrize("order", ["slider_value", "value_slider"])
def test_basic_layout_sync_exact_value_and_owner_lifetime(owner, order):
    """並び順を変えても整数の同期と共有Bindingの寿命を維持する。"""
    binding = IntBinding.from_attribute(Data(), "value", parent=owner)
    editor = IntSliderSpinBox(
        binding, owner, minimum=0, maximum=10, layout_order=order
    )
    first = editor.slider if order == "slider_value" else editor.spin_box
    assert editor.layoutOrder() == order
    assert editor.layout().itemAt(0).widget() is first
    assert editor.spin_box.value() == binding.value == 42
    assert editor.slider.value() == 10
    editor.spin_box.setValue(2147483647)
    assert binding.value == 2147483647
    editor.slider.setValue(3)
    assert editor.spin_box.value() == binding.value == 3
    editor.slider.setSliderDown(True)
    editor.slider.setValue(4)
    editor.hide()
    editor.deleteLater()
    flush()
    assert not binding.view_model.is_disposed
    assert not binding.view_model.is_editing
    binding.set_value(5)
    assert binding.value == 5


def test_range_step_are_local_settings_and_slider_steps_stay_independent(
    owner,
):
    """各行の範囲・Step編集は正本や共有する別行の設定へ書き込まない。"""
    binding, editor = make_editor(owner, step_mode="multiplicative")
    other = IntRangeSliderSpinBox(
        binding, owner, minimum=0, maximum=10, single_step=2
    )
    changes = []
    editor.settingsChanged.connect(
        lambda: changes.append((*editor.intRange(), editor.singleStep()))
    )
    editor.minimum_spin_box.setValue(-50)
    editor.maximum_spin_box.setValue(50)
    editor.step_spin_box.stepUp()
    assert binding.value == other.spin_box.value() == 42
    assert editor.singleStep() == 10
    assert other.intRange() == (0, 10)
    assert other.singleStep() == 2
    assert editor.minimum_spin_box.singleStep() == 1
    assert editor.maximum_spin_box.singleStep() == 1
    assert changes == [(-50, 100, 1), (-50, 50, 1), (-50, 50, 10)]
    editor.setSingleStep(10)
    assert len(changes) == 3
    editor.spin_box.stepUp()
    assert binding.value == 52
    assert editor.slider.value() == editor.slider.maximum()
    editor.slider.setValue(51)
    assert binding.value == 1
    assert editor.singleStep() == 10


def test_invalid_ui_range_restores_prior_range_and_notifies_reason(owner):
    """Min以下のMaxやMax以上のMinを確定できず、理由が見える。"""
    binding, editor = make_editor(owner)
    reasons = []
    changes = []
    editor.rangeEditRejected.connect(reasons.append)
    editor.settingsChanged.connect(lambda: changes.append(True))
    editor.minimum_spin_box.setValue(100)
    assert editor.intRange() == (-100, 100)
    assert editor.minimum_spin_box.value() == -100
    editor.maximum_spin_box.setValue(-101)
    assert editor.maximum_spin_box.value() == 100
    assert len(reasons) == 2
    assert editor.range_status_label.text() == reasons[-1]
    assert not editor.range_status_label.isHidden()
    assert binding.value == 42
    assert not changes
    editor.maximum_spin_box.setValue(200)
    assert editor.intRange() == (-100, 200)
    assert editor.range_status_label.isHidden()


def test_requested_range_hard_intersection_and_disjoint_range(owner):
    """hard limitと交差しても要求範囲・範囲外の実値を保持する。"""
    binding, editor = make_editor(
        owner, presentation=IntPresentation(minimum=0, maximum=10)
    )
    assert editor.intRange() == (-100, 100)
    assert editor.effectiveIntRange() == (0, 10)
    assert editor.spin_box.value() == 42
    assert "0 ～ 10" in editor.range_status_label.text()
    editor.setIntRange(20, 30)
    assert editor.effectiveIntRange() is None
    assert not editor.slider.isEnabled()
    assert editor.spin_box.isEnabled()
    assert editor.minimum_spin_box.isEnabled()
    assert binding.value == 42
    editor.setIntRange(0, 5)
    assert editor.slider.isEnabled()
    assert editor.effectiveIntRange() == (0, 5)
    assert editor.spin_box.value() == 42


def test_invalid_api_settings_and_constructor_leave_owner_unchanged(owner):
    """APIの不正入力を暗黙変換せず、部分生成も残さない。"""
    binding, editor = make_editor(owner)
    for lower, upper in [
        (True, 100),
        (-1.5, 100),
        (-(2**31) - 1, 100),
        (1, 1),
    ]:
        with pytest.raises((ValueError, TypeError)):
            editor.setIntRange(lower, upper)
        assert editor.intRange() == (-100, 100)
    for step in [True, 1.5, 0, -1, 2**31]:
        with pytest.raises((ValueError, TypeError)):
            editor.setSingleStep(step)
        assert editor.singleStep() == 1
    before = owner.children()
    for kwargs in [
        {"step_width": True},
        {"value_width": 0},
        {"minimum_enabled": 1},
        {"maximum_show_buttons": None},
        {"steps": 0},
        {"step_mode": "wrong"},
        {"value_select_all_on_mouse_focus": 1},
    ]:
        with pytest.raises((ValueError, TypeError)):
            IntRangeSliderSpinBox(
                binding, owner, minimum=0, maximum=10, **kwargs
            )
        assert owner.children() == before


def test_disabled_fields_are_independent_and_disposal_stops_all_inputs(owner):
    """局所無効欄は設定を保持し、Binding終了で全入力を停止する。"""
    binding, editor = make_editor(
        owner,
        minimum_enabled=False,
        step_enabled=False,
        value_enabled=False,
        minimum_show_buttons=False,
    )
    editor.minimum_spin_box.setValue(-50)
    editor.step_spin_box.setValue(5)
    assert editor.intRange() == (-100, 100)
    assert editor.singleStep() == 1
    assert editor.slider.isEnabled()
    assert not editor.spin_box.isEnabled()
    assert editor.focusProxy() is editor.slider
    assert editor.minimum_spin_box.buttonSymbols() == (
        qt.QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
    )
    binding.dispose()
    for child in (
        editor.slider,
        editor.spin_box,
        editor.minimum_spin_box,
        editor.maximum_spin_box,
        editor.step_spin_box,
    ):
        assert not child.isEnabled()
    with pytest.raises(RuntimeError):
        editor.setIntRange(0, 10)
    with pytest.raises(RuntimeError):
        editor.setSingleStep(2)


@pytest.mark.parametrize("fixed", [False, True])
def test_all_fields_visible_at_minimum_width_with_fixed_or_flexible_layout(
    owner, fixed
):
    """最小幅でもStepを含む5部品が表示され、固定幅は押し潰されない。"""
    widths = (
        dict(
            minimum_width=120,
            slider_width=180,
            maximum_width=120,
            value_width=120,
            step_width=90,
        )
        if fixed
        else {}
    )
    _, editor = make_editor(owner, **widths)
    editor.setWindowFlag(qt.Qt.WindowType.Window)
    editor.show()
    editor.resize(editor.minimumSizeHint())
    flush()
    children = (
        editor.minimum_spin_box,
        editor.slider,
        editor.maximum_spin_box,
        editor.spin_box,
        editor.step_spin_box,
    )
    for child in children:
        assert child.isVisible()
        assert child.width() > 0
        assert editor.rect().contains(child.geometry())
    if fixed:
        assert [child.width() for child in children] == [
            120,
            180,
            120,
            120,
            90,
        ]
    editor.close()


def test_roundtrip_int32_cached_after_delete_and_one_complete_notification(
    owner, tmp_path
):
    """全32-bit両端と最大Stepを整数保存し、破棄後にも最後の設定を保存する。"""
    settings, manager = make_manager(tmp_path)
    binding, editor = make_editor(owner)
    manager.register_int_range_slider_spin_box("value", editor)
    editor.setIntRange(-(2**31), 2**31 - 1)
    editor.setSingleStep(2**31 - 1)
    editor.deleteLater()
    flush()
    assert manager.save_cached()
    state_key = "editor_settings/main/ui_state/widgets/value/state"
    payload = json.loads(bytes(settings.value(state_key)))
    assert payload == {
        "version": 1,
        "minimum": -(2**31),
        "maximum": 2**31 - 1,
        "single_step": 2**31 - 1,
    }
    assert all(type(value) is int for value in payload.values())
    _, other = make_editor(
        owner, step_mode="multiplicative", step_enabled=False
    )
    restored = UiStateManager(settings, manager.settings_path)
    restored.register_int_range_slider_spin_box("value", other)
    changes = []
    other.settingsChanged.connect(
        lambda: changes.append((*other.intRange(), other.singleStep()))
    )
    assert restored.restore() == frozenset({"value"})
    assert changes == [(-(2**31), 2**31 - 1, 2**31 - 1)]
    assert other.step_spin_box.stepMode() == "multiplicative"
    assert not other.step_spin_box.isEnabled()
    assert other.spin_box.value() == binding.value == 42


@pytest.mark.parametrize(
    "update",
    [
        {"version": True},
        {"version": 1.0},
        {"version": 2},
        {"minimum": True},
        {"minimum": -(2**31) - 1},
        {"maximum": 2**31},
        {"maximum": 100.0},
        {"minimum": "-10"},
        {"minimum": None},
        {"minimum": 100},
        {"single_step": 0},
        {"single_step": 1.0},
        {"single_step": True},
        {"single_step": 2**31},
    ],
)
def test_invalid_saved_state_is_rejected_without_partial_restore(
    owner, tmp_path, update
):
    """保存値の一項目が壊れても一部を適用せず、その行の保存値を削除する。"""
    settings, manager = make_manager(tmp_path)
    binding, editor = make_editor(owner)
    manager.register_int_range_slider_spin_box("value", editor)
    assert manager.save()
    key = "editor_settings/main/ui_state/widgets/value/state"
    payload = {"version": 1, "minimum": -10, "maximum": 100, "single_step": 15}
    payload.update(update)
    settings.setValue(
        key, qt.QtCore.QByteArray(json.dumps(payload).encode("utf-8"))
    )
    changes = []
    editor.settingsChanged.connect(lambda: changes.append(True))
    assert manager.restore() == frozenset()
    assert editor.intRange() == (-100, 100)
    assert editor.singleStep() == 1
    assert binding.value == 42
    assert not changes
    assert not settings.contains(key)


@pytest.mark.parametrize("raw", [b"{", b"[]", b"\xff", b"null"])
def test_malformed_payload_is_ignored(owner, tmp_path, raw):
    """壊れたJSONや不正な型で現在の設定を変更しない。"""
    settings, manager = make_manager(tmp_path)
    _, editor = make_editor(owner)
    manager.register_int_range_slider_spin_box("value", editor)
    assert manager.save()
    settings.setValue(
        "editor_settings/main/ui_state/widgets/value/state",
        qt.QtCore.QByteArray(raw),
    )
    assert manager.restore() == frozenset()
    assert editor.intRange() == (-100, 100)


def test_registration_rejects_wrong_type_duplicate_and_disposed(
    owner, tmp_path
):
    """明示登録は型・キー・寿命を検証し、失敗した登録を残さない。"""
    _, manager = make_manager(tmp_path)
    binding, editor = make_editor(owner)
    with pytest.raises(TypeError):
        manager.register_int_range_slider_spin_box("wrong", qt.QSpinBox(owner))
    manager.register_int_range_slider_spin_box("value", editor)
    with pytest.raises(ValueError):
        manager.register_int_range_slider_spin_box("value", editor)
    binding.dispose()
    with pytest.raises(RuntimeError):
        manager.register_int_range_slider_spin_box("disposed", editor)
    assert manager.registered_keys == ("value",)
