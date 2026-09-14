# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util.ui import Float3Binding, Float3SliderSpinBox, qt


@dataclass
class Data:
    value: tuple[float, float, float] = (1, 2, 3)


@pytest.fixture
def owner(qt_application):
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def assert_values(binding, view, expected):
    assert binding.value == expected
    assert (
        tuple(
            component.value.value
            for component in (
                binding.view_model.x,
                binding.view_model.y,
                binding.view_model.z,
            )
        )
        == expected
    )
    assert (
        tuple(
            spin.value()
            for spin in (view.x_spin_box, view.y_spin_box, view.z_spin_box)
        )
        == expected
    )


def test_axis_confirmation_and_same_value_refresh_finish_synchronously_once(
    owner,
):
    data = Data()
    binding = Float3Binding.from_attribute(data, "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    changed, refreshed = [], []
    binding.changed.connect(changed.append)
    binding.view_model.store_refreshed.connect(refreshed.append)
    for value in (4, 5, 6):
        changed.clear()
        refreshed.clear()
        assert binding.view_model.x.set_value_command.execute(value)
        assert_values(binding, view, (value, 2, 3))
        assert changed == refreshed == [(value, 2, 3)]
    data.value = (6, 7, 8)
    changed.clear()
    refreshed.clear()
    assert not binding.view_model.x.set_value_command.execute(6)
    assert_values(binding, view, (6, 7, 8))
    assert changed == refreshed == [(6, 7, 8)]


@pytest.mark.parametrize("nested", ["axis", "bulk", "direct"])
def test_nested_component_slot_publishes_complete_tuple_at_outer_completion(
    owner, nested
):
    data = Data()
    binding = Float3Binding.from_attribute(data, "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    changed, refreshed = [], []

    def edit_again(value):
        if value != 4:
            return
        if nested == "axis":
            binding.view_model.y.set_value_command.execute(5)
        elif nested == "bulk":
            binding.set_value((6, 7, 8))
        else:
            data.value = (4, 8, 9)
            binding.refresh()

    binding.view_model.x.value.changed.connect(edit_again)
    binding.changed.connect(changed.append)
    binding.view_model.store_refreshed.connect(refreshed.append)
    binding.view_model.x.set_value_command.execute(4)
    expected = {"axis": (4, 5, 3), "bulk": (6, 7, 8), "direct": (4, 8, 9)}[
        nested
    ]
    assert_values(binding, view, expected)
    assert changed == refreshed == [expected]


@pytest.mark.parametrize("signal", ["changed", "store_refreshed"])
def test_group_confirmation_slot_can_require_another_refresh(owner, signal):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    observed = []

    def edit_again(value):
        if value == (4, 2, 3):
            binding.view_model.y.set_value_command.execute(5)

    target = (
        binding.changed
        if signal == "changed"
        else binding.view_model.store_refreshed
    )
    target.connect(edit_again)
    binding.view_model.store_refreshed.connect(observed.append)
    binding.view_model.x.set_value_command.execute(4)
    assert_values(binding, view, (4, 5, 3))
    assert observed == [(4, 2, 3), (4, 5, 3)]


@pytest.mark.parametrize("error", [RuntimeError, KeyboardInterrupt])
@pytest.mark.parametrize("unreadable", [False, True])
def test_failed_or_interrupted_write_closes_batch_and_preserves_original_error(
    owner, error, unreadable
):
    class FailingData:
        _value = (1, 2, 3)
        fail = True
        broken = False

        @property
        def value(self):
            if self.broken:
                raise ValueError("read failed")
            return self._value

        @value.setter
        def value(self, value):
            self._value = value
            if self.fail:
                self.broken = unreadable
                raise error("original failure")

    data = FailingData()
    binding = Float3Binding.from_attribute(data, "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    with pytest.raises(error, match="original failure"):
        binding.view_model.x.set_value_command.execute(4)
    if unreadable:
        assert not binding.view_model.set_value_command.can_execute
    else:
        assert_values(binding, view, (4, 2, 3))
    data.fail = data.broken = False
    binding.refresh()
    assert_values(binding, view, (4, 2, 3))
    refreshed = []
    binding.view_model.store_refreshed.connect(refreshed.append)
    binding.view_model.y.set_value_command.execute(5)
    assert_values(binding, view, (4, 5, 3))
    assert refreshed == [(4, 5, 3)]


def test_component_slot_can_dispose_binding_before_batch_finishes(owner):
    binding = Float3Binding.from_attribute(Data(), "value", parent=owner)
    view = Float3SliderSpinBox(binding, owner, minimum=0, maximum=10)
    refreshed = []
    binding.view_model.store_refreshed.connect(refreshed.append)
    binding.view_model.x.value.changed.connect(
        lambda _value: binding.dispose()
    )
    binding.view_model.x.set_value_command.execute(4)
    assert binding.is_disposed
    assert refreshed == []
    assert all(
        not spin.isEnabled()
        for spin in (view.x_spin_box, view.y_spin_box, view.z_spin_box)
    )
