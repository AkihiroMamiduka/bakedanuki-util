# coding: utf-8
from dataclasses import dataclass
from types import SimpleNamespace

import pytest

from bd_util.ui import FloatPresentation, PythonFloatAttributeStore


@dataclass
class Data:
    value: float = 0.5


@dataclass(slots=True)
class SlotsData:
    value: float = 0.5


@dataclass(frozen=True)
class FrozenData:
    value: float = 0.5


@dataclass(frozen=True, slots=True)
class FrozenSlotsData:
    value: float = 0.5


class PropertyData:
    def __init__(self, value=0.5):
        self._value = value
        self.reads = 0
        self.writes = 0

    @property
    def value(self):
        self.reads += 1
        return self._value

    @value.setter
    def value(self, value):
        self.writes += 1
        self._value = value


class ReadOnlyData:
    @property
    def value(self):
        return 0.5


class ValueDescriptor:
    def __get__(self, instance, owner=None):
        return self if instance is None else instance._value

    def __set__(self, instance, value):
        instance._value = round(value, 2)


class DescriptorData:
    value = ValueDescriptor()

    def __init__(self):
        self._value = 0.5


@pytest.mark.parametrize(
    "factory", [Data, SlotsData, PropertyData, DescriptorData]
)
def test_supported_attributes_read_write_and_preserve_instance(factory):
    data = factory()
    store = PythonFloatAttributeStore(data, "value")
    assert store.instance is data
    assert store.attribute_name == "value"
    assert store.is_available and store.is_writable
    assert store.presentation == FloatPresentation()
    assert store.write(2.5) == data.value == 2.5
    assert type(store.read()) is float


def test_initial_read_and_availability_do_not_call_setter_or_repeat_getter():
    data = PropertyData(1)
    store = PythonFloatAttributeStore(data, "value")
    assert data.reads == 1
    assert data.writes == 0
    assert type(data._value) is int
    for _ in range(3):
        assert store.is_available and store.is_writable
    assert data.reads == 1
    assert store.read() == 1.0
    assert store.write(2) == 2.0
    assert type(data._value) is float
    assert data.writes == 1


@pytest.mark.parametrize(
    "factory", [FrozenData, FrozenSlotsData, ReadOnlyData]
)
def test_read_only_attributes_are_readable_and_reject_writes(factory):
    data = factory()
    store = PythonFloatAttributeStore(data, "value")
    assert store.is_available
    assert not store.is_writable
    assert store.read() == 0.5
    with pytest.raises(RuntimeError):
        store.write(1)
    assert data.value == 0.5


@pytest.mark.parametrize(
    "value",
    [True, False, "0.5", None, float("nan"), float("inf"), -float("inf")],
)
def test_invalid_initial_values_and_write_requests_are_rejected(value):
    with pytest.raises((TypeError, ValueError)):
        PythonFloatAttributeStore(Data(value), "value")
    data = PropertyData()
    store = PythonFloatAttributeStore(data, "value")
    with pytest.raises((TypeError, ValueError)):
        store.write(value)
    assert data._value == 0.5
    assert data.writes == 0


@pytest.mark.parametrize(
    "attribute_name", [None, 1, "", "missing", "child.value"]
)
def test_invalid_attribute_names_do_not_create_or_traverse_attributes(
    attribute_name,
):
    data = Data()
    before = vars(data).copy()
    with pytest.raises((TypeError, ValueError, AttributeError)):
        PythonFloatAttributeStore(data, attribute_name)
    assert vars(data) == before


def test_dynamic_only_attributes_are_rejected_without_calling_getattr():
    class DynamicData:
        calls = 0

        def __getattr__(self, name):
            self.calls += 1
            return 0.5

    data = DynamicData()
    with pytest.raises(AttributeError):
        PythonFloatAttributeStore(data, "value")
    assert data.calls == 0


def test_explicit_presentation_limits_requests_in_public_units():
    data = PropertyData(100.0)
    presentation = FloatPresentation(
        scale=0.01, suffix=" m", minimum=0.0, maximum=300.0
    )
    store = PythonFloatAttributeStore(data, "value", presentation=presentation)
    assert store.presentation is presentation
    assert store.read() == 100.0
    assert store.write(200) == data._value == 200.0
    writes = data.writes
    for value in (-0.01, 300.01):
        with pytest.raises(ValueError):
            store.write(value)
        assert data._value == 200.0
        assert data.writes == writes
    assert store.write(0) == 0
    assert store.write(300) == 300


def test_range_does_not_rewrite_external_values_and_setter_actuals():
    data = PropertyData(2.0)
    store = PythonFloatAttributeStore(
        data, "value", presentation=FloatPresentation(minimum=0, maximum=1)
    )
    assert store.read() == 2.0
    assert data.writes == 0
    data._value = -2.0
    assert store.read() == -2.0
    normalized = PythonFloatAttributeStore(DescriptorData(), "value")
    assert normalized.write(0.123456789) == 0.12


def test_attribute_deletion_invalid_value_and_restoration_are_observed():
    data = SimpleNamespace(value=0.5)
    store = PythonFloatAttributeStore(data, "value")
    del data.value
    assert not store.is_available
    assert not store.is_writable
    with pytest.raises(RuntimeError):
        store.read()
    with pytest.raises(RuntimeError):
        store.write(1)
    data.value = float("nan")
    assert store.is_available
    with pytest.raises(ValueError):
        store.read()
    data.value = 0.75
    assert store.is_writable
    assert store.read() == 0.75


def test_invalid_presentation_and_getter_exceptions_are_not_hidden():
    with pytest.raises(TypeError, match="presentation"):
        PythonFloatAttributeStore(Data(), "value", presentation={})

    class UnreadableData:
        @property
        def value(self):
            raise ValueError("getter failed")

    with pytest.raises(ValueError, match="getter failed"):
        PythonFloatAttributeStore(UnreadableData(), "value")
