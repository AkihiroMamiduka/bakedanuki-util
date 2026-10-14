# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util.ui import (
    IntBinding,
    IntLabel,
    IntPresentation,
    IntSpinBox,
    PythonIntAttributeStore,
    qt,
)


def flush():
    """遅延破棄と遅延signalを処理する。"""
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@dataclass
class Data:
    """テスト用の整数正本。"""

    value: int = 0


@pytest.mark.parametrize("value", [-(2**31), -1, 0, 1, 2**31 - 1])
def test_int32_boundaries_keep_exact_values(qt_application, value):
    """符号付き32-bit全域をQt Viewまで整数のまま保持する。"""
    data = Data(value)
    binding = IntBinding.from_attribute(data, "value")
    spin = IntSpinBox(binding)
    label = IntLabel(binding.view_model)
    try:
        assert binding.value == spin.value() == value
        assert label.text() == str(value)
        assert binding.store.instance is data
        assert binding.store.read() == value
    finally:
        spin.deleteLater()
        label.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("value", [True, False, 1.0, "1", 2**31, -(2**31) - 1])
def test_invalid_values_are_rejected_before_setter(qt_application, value):
    """bool、非整数と範囲外の値をsetterへ渡さない。"""
    data = Data(5)
    binding = IntBinding.from_attribute(data, "value")
    try:
        with pytest.raises((TypeError, ValueError)):
            binding.set_value(value)
        assert data.value == binding.value == 5
        with pytest.raises((TypeError, ValueError)):
            PythonIntAttributeStore(Data(value), "value")
    finally:
        binding.dispose()
        flush()


def test_views_share_binding_and_external_refresh(qt_application):
    """共有View、入力停止と外部変更の再同期を確認する。"""
    data = Data(3)
    binding = IntBinding.from_attribute(data, "value")
    first = IntSpinBox(binding, wheel_requires_focus=True)
    second = IntSpinBox(binding.view_model)
    label = IntLabel(binding)
    events = []
    binding.changed.connect(events.append)
    try:
        assert (first.minimum(), first.maximum()) == (-(2**31), 2**31 - 1)
        assert first.wheel_requires_focus()
        first.setValue(9)
        assert data.value == binding.value == second.value() == 9
        assert label.text() == "9"
        assert events == [9]
        first.setInputEnabled(False)
        first.setValue(10)
        assert data.value == first.value() == 9
        data.value = -123456789
        assert binding.refresh()
        assert first.value() == second.value() == -123456789
        assert label.text() == "-123456789"
        assert events == [9, -123456789]
    finally:
        first.deleteLater()
        second.deleteLater()
        label.deleteLater()
        binding.dispose()
        flush()


def test_limits_validate_requests_without_rewriting_external_values(
    qt_application,
):
    """hard limitの外にある外部実値も表示し、入力だけを拒否する。"""
    data = Data(8)
    presentation = IntPresentation(minimum=-2, maximum=5)
    binding = IntBinding.from_attribute(
        data, "value", presentation=presentation
    )
    spin = IntSpinBox(binding)
    try:
        assert binding.store.presentation is presentation
        assert spin.value() == 8
        assert (spin.minimum(), spin.maximum()) == (-2, 8)
        with pytest.raises(ValueError):
            binding.set_value(6)
        assert data.value == binding.value == 8
        assert binding.set_value(5)
        assert (spin.minimum(), spin.maximum()) == (-2, 5)
        assert spin.value() == 5
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


def test_setter_actual_and_failure_recovery(qt_application):
    """setterが補正・失敗した場合、正本の実値へ表示を戻す。"""

    class Clamped:
        """入力を0から10へ制限する正本。"""

        _value = 4
        raise_after = False

        @property
        def value(self):
            """現在値を返す。"""
            return self._value

        @value.setter
        def value(self, value):
            """入力を補正し、必要なら書込み後に失敗する。"""
            self._value = max(0, min(10, value))
            if self.raise_after:
                raise RuntimeError("setter failed")

    data = Clamped()
    binding = IntBinding.from_attribute(data, "value")
    spin = IntSpinBox(binding)
    try:
        assert binding.set_value(100)
        assert data.value == binding.value == spin.value() == 10
        data.raise_after = True
        with pytest.raises(RuntimeError, match="setter failed"):
            binding.set_value(3)
        assert data.value == binding.value == spin.value() == 3
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


def test_read_only_and_disposal_stop_input(qt_application):
    """読み取り専用属性と所有者破棄で入力を止める。"""

    @dataclass(frozen=True)
    class Frozen:
        """変更不可の整数正本。"""

        value: int = 4

    frozen = IntBinding.from_attribute(Frozen(), "value")
    frozen_spin = IntSpinBox(frozen)
    try:
        assert not frozen_spin.isEnabled()
        assert not frozen.set_value(5)
    finally:
        frozen_spin.deleteLater()
        frozen.dispose()
        flush()

    data = Data(4)
    owner = qt.QWidget()
    binding = IntBinding.from_attribute(data, "value", parent=owner)
    survivor = IntSpinBox(binding)
    owner.deleteLater()
    flush()
    try:
        assert binding.is_disposed
        assert not survivor.isEnabled()
        assert data.value == 4
        with pytest.raises(RuntimeError):
            binding.set_value(5)
    finally:
        survivor.deleteLater()
        flush()


def test_invalid_presentation_and_range(qt_application):
    """範囲の型、順序と32-bit境界を生成時に検証する。"""
    for options in (
        {"minimum": True},
        {"maximum": 2**31},
        {"minimum": 2, "maximum": 1},
    ):
        with pytest.raises((TypeError, ValueError)):
            IntPresentation(**options)
    with pytest.raises(TypeError):
        IntBinding.from_attribute(Data(), "value", presentation={})
