# coding: utf-8
"""整数Sliderの写像、入力、範囲と連続編集の寿命を検証する。"""

from dataclasses import dataclass

import pytest

from bd_util.ui import (
    IntBinding,
    IntLabel,
    IntPresentation,
    IntSlider,
    IntSpinBox,
    IntViewModel,
    qt,
)


@dataclass
class Data:
    """整数値をそのまま保持するPython正本。"""

    value: int = 42


def flush():
    """予約されたQt objectの破棄と通知を処理する。"""
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    qt.QApplication.processEvents()


@pytest.fixture
def owner(qt_application):
    """テストのWidgetとBindingを所有し、終了時に破棄する。"""
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


@pytest.mark.parametrize(
    "minimum,maximum,steps",
    [(0, 10, 1000), (-10, -1, 1000), (-5, 5, 3), (-(2**31), 2**31 - 1, 1000)],
)
def test_mapping_monotonic_exact_endpoints_and_integer_values(
    owner, minimum, maximum, steps
):
    """小範囲は全整数、広い範囲は整数のまま単調に両端まで操作する。"""
    vm = IntViewModel(minimum, owner)
    slider = IntSlider(
        vm, owner, minimum=minimum, maximum=maximum, steps=steps
    )
    expected_positions = min(steps, maximum - minimum)
    assert slider.maximum() == expected_positions
    values = []
    for position in range(expected_positions + 1):
        slider.setValue(position)
        assert type(vm.value.value) is int
        assert slider.value() == position
        values.append(vm.value.value)
    assert values[0] == minimum
    assert values[-1] == maximum
    assert all(a < b for a, b in zip(values, values[1:]))
    if maximum - minimum <= steps:
        assert values == list(range(minimum, maximum + 1))


def test_display_never_quantizes_shared_value_or_outside_source(owner):
    """位置表示・範囲変更は実値を保持し、別Viewも整数を共有する。"""
    data = Data(123456789)
    binding = IntBinding.from_attribute(data, "value", parent=owner)
    slider = IntSlider(binding, owner, minimum=-(2**31), maximum=2**31 - 1)
    spin = IntSpinBox(binding, owner)
    label = IntLabel(binding, owner)
    assert binding.value == spin.value() == data.value == 123456789
    assert label.text() == "123456789"
    slider.setSliderDown(True)
    slider.setSliderDown(False)
    slider.setIntRange(0, 10)
    assert slider.value() == 10
    assert data.value == 123456789
    slider.setValue(3)
    assert data.value == spin.value() == 3
    assert label.text() == "3"
    spin.setValue(-50)
    assert slider.value() == 0
    assert data.value == -50


def test_hard_range_intersection_empty_range_and_recovery(owner):
    """正本の制限と交差させ、操作不能でも数値欄と実値を維持する。"""
    binding = IntBinding.from_attribute(
        Data(20),
        "value",
        parent=owner,
        presentation=IntPresentation(minimum=-2, maximum=4),
    )
    slider = IntSlider(binding, owner, minimum=-10, maximum=10)
    spin = IntSpinBox(binding, owner)
    assert slider.intRange() == (-10, 10)
    assert slider.effectiveIntRange() == (-2, 4)
    assert binding.value == 20
    slider.setValue(0)
    assert binding.value == -2
    changes = []
    slider.intRangeChanged.connect(lambda a, b: changes.append((a, b)))
    slider.setIntRange(4, 10)
    assert slider.effectiveIntRange() is None
    assert not slider.isEnabled()
    assert spin.isEnabled()
    assert binding.value == -2
    slider.setIntRange(-1, 2)
    slider.setIntRange(-1, 2)
    assert changes == [(4, 10), (-1, 2)]
    assert slider.isEnabled()
    slider.setValue(3)
    assert binding.value == 2


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"minimum": 1, "maximum": 1}, ValueError),
        ({"minimum": 2, "maximum": 1}, ValueError),
        ({"minimum": -(2**31) - 1, "maximum": 1}, ValueError),
        ({"minimum": 0, "maximum": 2**31}, ValueError),
        ({"minimum": True, "maximum": 1}, TypeError),
        ({"minimum": 0, "maximum": 1.0}, TypeError),
        ({"minimum": "0", "maximum": 1}, TypeError),
        ({"minimum": 0, "maximum": 1, "steps": 0}, ValueError),
        ({"minimum": 0, "maximum": 1, "steps": 2**31}, ValueError),
        ({"minimum": 0, "maximum": 1, "steps": True}, TypeError),
        ({"minimum": 0, "maximum": 1, "steps": 1.0}, TypeError),
    ],
)
def test_invalid_config_has_no_widget_or_source_side_effects(
    owner, kwargs, error
):
    """不正引数は子Widgetの生成前に拒否する。"""
    vm = IntViewModel(parent=owner)
    before = owner.children()
    with pytest.raises(error):
        IntSlider(vm, owner, **kwargs)
    assert owner.children() == before


def test_owner_reentrancy_destruction_and_disposal(owner):
    """操作の所有者を一つに制限し、破棄と終了時の再開始を扱う。"""
    vm = IntViewModel(parent=owner)
    first, second = qt.QObject(owner), qt.QObject(owner)
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
    attempted = []
    vm.edit_finished.connect(lambda: attempted.append(vm.begin_edit(second)))
    vm.dispose()
    assert attempted == [False]
    assert events == ["start", "end", "start", "end"]


def send_key(slider, kind, key, repeat=False):
    """キーの実押下・解放・リピートをSliderへ送る。"""
    event = qt.QtGui.QKeyEvent(
        kind, key, qt.Qt.KeyboardModifier.NoModifier, "", repeat
    )
    qt.QApplication.sendEvent(slider, event)


def test_keyboard_repeat_escape_and_old_input(owner):
    """一押下のリピートをまとめ、途中終了後は古い入力を止める。"""
    vm = IntViewModel(parent=owner)
    slider = IntSlider(vm, owner, minimum=0, maximum=10)
    events = []
    slider.editStarted.connect(lambda: events.append("start"))
    slider.editFinished.connect(lambda: events.append("end"))
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Right)
    for _ in range(3):
        send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Right, True)
    assert vm.value.value == 4
    assert events == ["start"]
    slider.finish_edit()
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Right, True)
    assert vm.value.value == 4
    send_key(slider, qt.QEvent.Type.KeyRelease, qt.Qt.Key.Key_Right)
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_End)
    send_key(slider, qt.QEvent.Type.KeyPress, qt.Qt.Key.Key_Escape)
    assert vm.value.value == 10
    assert not vm.is_editing
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
def test_interruption_keeps_last_value(owner, event_type):
    """フォーカス喪失などで終了し、開始値へ戻さない。"""
    vm = IntViewModel(parent=owner)
    slider = IntSlider(vm, owner, minimum=0, maximum=10)
    slider.setSliderDown(True)
    slider.setValue(7)
    qt.QApplication.sendEvent(slider, qt.QEvent(event_type))
    assert not vm.is_editing
    assert not slider.isSliderDown()
    assert vm.value.value == 7


def test_setter_correction_rejection_and_reentrant_confirmation(owner):
    """setter補正・拒否・再入でも正本の確定整数を表示する。"""

    class Corrected:
        """偶数へ補正し、大きい入力を拒否する正本。"""

        _value = 0

        @property
        def value(self):
            """確定した整数を返す。"""
            return self._value

        @value.setter
        def value(self, value):
            """8を超える入力を拒否し、偶数へ切り下げる。"""
            if value > 8:
                raise ValueError("rejected")
            self._value = value // 2 * 2

    binding = IntBinding.from_attribute(Corrected(), "value", parent=owner)
    slider = IntSlider(binding, owner, minimum=0, maximum=10)
    slider.setValue(3)
    assert binding.value == slider.value() == 2
    slider.setSliderDown(True)
    with pytest.raises(ValueError, match="rejected"):
        slider._request_value(9)
    assert not binding.view_model.is_editing
    assert slider.value() == 2
    binding.changed.connect(lambda v: binding.set_value(6) if v == 4 else None)
    slider.setValue(4)
    assert binding.value == slider.value() == 6


def test_readonly_and_disposed_models_disable_slider(owner):
    """readonly・終了後の入力を止め、終了済み入力元を再利用しない。"""

    class ReadOnly:
        """読み取り専用整数。"""

        @property
        def value(self):
            """固定整数を返す。"""
            return 4

    binding = IntBinding.from_attribute(ReadOnly(), "value", parent=owner)
    slider = IntSlider(binding, owner, minimum=0, maximum=10)
    assert not slider.isEnabled()
    slider.setValue(7)
    assert slider.value() == binding.value == 4
    vm = IntViewModel(parent=owner)
    active = IntSlider(vm, owner, minimum=0, maximum=10)
    active.setSliderDown(True)
    vm.dispose()
    assert not active.isEnabled()
    assert not active.isSliderDown()
    with pytest.raises(RuntimeError):
        _ = active.view_model
    with pytest.raises(RuntimeError):
        IntSlider(vm, owner, minimum=0, maximum=10)


def test_maximum_qt_position_count_and_halfway_rounding(owner):
    """最大分割数でも端点を保持し、丸めの同点では大きい整数を選ぶ。"""
    vm = IntViewModel(-(2**31), owner)
    slider = IntSlider(
        vm, owner, minimum=-(2**31), maximum=2**31 - 1, steps=2**31 - 1
    )
    previous = -(2**31)
    for position in (1, 2**30, 2**31 - 2, 2**31 - 1):
        slider.setValue(position)
        assert type(vm.value.value) is int
        assert vm.value.value > previous
        previous = vm.value.value
    assert vm.value.value == 2**31 - 1
    rounded = IntSlider(vm, owner, minimum=-3, maximum=0, steps=2)
    rounded.setValue(1)
    assert vm.value.value == -1


def send_mouse(slider, kind, point, button, buttons):
    """Qtのつまみ・溝操作を実際のマウスイベントで送る。"""
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
def test_mouse_starts_edit_before_first_write_and_finishes(owner, groove):
    """つまみと溝の最初の変更から解放までを一操作として通知する。"""
    vm = IntViewModel(25, owner)
    slider = IntSlider(vm, owner, minimum=0, maximum=100)
    slider.resize(400, 30)
    option = qt.QtWidgets.QStyleOptionSlider()
    slider.initStyleOption(option)
    handle = slider.style().subControlRect(
        qt.QtWidgets.QStyle.ComplexControl.CC_Slider,
        option,
        qt.QtWidgets.QStyle.SubControl.SC_SliderHandle,
        slider,
    )
    start = qt.QPoint(350, handle.center().y()) if groove else handle.center()
    confirmations = []
    vm.value.changed.connect(
        lambda v: confirmations.append((v, vm.is_editing))
    )
    send_mouse(
        slider,
        qt.QEvent.Type.MouseButtonPress,
        start,
        qt.Qt.MouseButton.LeftButton,
        qt.Qt.MouseButton.LeftButton,
    )
    if not groove:
        send_mouse(
            slider,
            qt.QEvent.Type.MouseMove,
            start + qt.QPoint(100, 0),
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
    assert confirmations
    assert all(editing for _, editing in confirmations)
    assert not vm.is_editing


def test_wheel_requires_focus_and_external_handler_uses_integers(owner):
    """未フォーカスのホイールを拒否し、独自入力先にも整数を渡す。"""
    vm = IntViewModel(parent=owner)
    slider = IntSlider(vm, owner, minimum=0, maximum=10)
    received = []

    def handle(value):
        """外側で整数を確定したことを通知する。"""
        received.append(value)
        vm.set_value_command.execute(value)
        return True

    slider.setValueRequestHandler(handle)
    event = qt.QtGui.QWheelEvent(
        qt.QPointF(5, 5),
        qt.QPointF(5, 5),
        qt.QPoint(),
        qt.QPoint(0, 120),
        qt.Qt.MouseButton.NoButton,
        qt.Qt.KeyboardModifier.NoModifier,
        qt.Qt.ScrollPhase.NoScrollPhase,
        False,
    )
    qt.QApplication.sendEvent(slider, event)
    assert not event.isAccepted()
    assert not received
    slider.setValue(7)
    assert received == [7]
    assert type(received[0]) is int
