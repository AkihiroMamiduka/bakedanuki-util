# coding: utf-8
from dataclasses import dataclass
from types import SimpleNamespace

import pytest

from bd_util.ui import FloatPresentation, PythonFloat3AttributeStore


@dataclass
class Data:
    offset: tuple[float, float, float] = (1, 2, 3)


@dataclass(slots=True)
class SlotsData:
    offset: tuple[float, float, float] = (1, 2, 3)


class PropertyData:
    def __init__(self):
        self._offset = (1, 2, 3)
        self.reads = 0
        self.writes = []

    @property
    def offset(self):
        self.reads += 1
        return self._offset

    @offset.setter
    def offset(self, value):
        self.writes.append(value)
        self._offset = value


@pytest.mark.parametrize("factory", [Data, SlotsData, PropertyData])
def test_tuple_attribute_and_components_share_one_source(factory):
    data = factory()
    original = data.offset
    store = PythonFloat3AttributeStore(data, "offset")
    assert store.instance is data
    assert store.attribute_name == "offset"
    assert store.is_available and store.is_writable
    assert data.offset is original
    assert all(type(value) is float for value in store.read())
    assert store.write((4, 5, 6)) == data.offset == (4, 5, 6)
    assert all(type(value) is float for value in data.offset)
    assert (
        tuple(component.read() for component in store.components)
        == data.offset
    )


def test_availability_does_not_evaluate_getter_or_setter():
    data = PropertyData()
    store = PythonFloat3AttributeStore(data, "offset")
    assert data.reads == 1
    for _ in range(3):
        assert store.is_available and store.is_writable
        for component in store.components:
            assert component.is_available and component.is_writable
    assert data.reads == 1
    assert data.writes == []


def test_axis_write_uses_latest_other_components_and_calls_setter_once():
    data = PropertyData()
    store = PythonFloat3AttributeStore(data, "offset")
    data._offset = (100, 2.1234567890123, 3.9876543210123)
    assert store.components[0].write(10.25) == 10.25
    assert data.offset == (10.25, 2.1234567890123, 3.9876543210123)
    assert data.writes == [data.offset]
    store.write((4, 5, 6))
    assert data.writes == [
        (10.25, 2.1234567890123, 3.9876543210123),
        (4, 5, 6),
    ]


def test_common_and_per_axis_presentations_limit_only_requested_components():
    data = PropertyData()
    common = FloatPresentation(minimum=0, maximum=10)
    shared = PythonFloat3AttributeStore(data, "offset", presentation=common)
    assert all(item is common for item in shared.presentations)
    presentations = (
        FloatPresentation(scale=0.01, suffix=" m", minimum=0, maximum=10),
        FloatPresentation(minimum=0, maximum=20),
        FloatPresentation(minimum=-5, maximum=5),
    )
    store = PythonFloat3AttributeStore(
        data, "offset", presentation=presentations
    )
    assert store.presentations == presentations
    for index, component in enumerate(store.components):
        assert component.presentation is presentations[index]
    for invalid in ((-1, 2, 3), (1, 21, 3), (1, 2, 6)):
        with pytest.raises(ValueError):
            store.write(invalid)
    assert data.writes == []
    assert store.write((0, 20, -5)) == (0, 20, -5)
    data._offset = (1, 25, 3)
    assert store.components[0].write(2) == 2
    assert data.offset == (2, 25, 3)
    before = data.writes.copy()
    with pytest.raises(ValueError):
        store.components[0].write(11)
    with pytest.raises(ValueError):
        store.write((3, 25, 3))
    assert data.writes == before


@pytest.mark.parametrize(
    "value",
    [
        None,
        "123",
        (1, 2),
        (1, 2, 3, 4),
        (1, True, 3),
        (1, "2", 3),
        (1, float("nan"), 3),
        (1, float("inf"), 3),
    ],
)
def test_invalid_values_are_rejected_before_any_setter_call(value):
    data = PropertyData()
    store = PythonFloat3AttributeStore(data, "offset")
    with pytest.raises((TypeError, ValueError)):
        store.write(value)
    assert data.offset == (1, 2, 3)
    assert data.writes == []
    with pytest.raises((TypeError, ValueError)):
        PythonFloat3AttributeStore(SimpleNamespace(offset=value), "offset")


def test_storage_requires_tuple_and_does_not_silently_convert_list():
    data = SimpleNamespace(offset=[1, 2, 3])
    original = data.offset
    with pytest.raises(TypeError, match="tuple"):
        PythonFloat3AttributeStore(data, "offset")
    assert data.offset is original


@pytest.mark.parametrize(
    "presentation",
    [
        [],
        (),
        (FloatPresentation(),),
        (FloatPresentation(), None, FloatPresentation()),
        1,
    ],
)
def test_invalid_presentations_do_not_read_or_write_data(presentation):
    data = PropertyData()
    with pytest.raises((TypeError, ValueError)):
        PythonFloat3AttributeStore(data, "offset", presentation=presentation)
    assert data.reads == 0
    assert data.writes == []


@pytest.mark.parametrize("frozen", [True, False])
def test_frozen_dataclass_and_read_only_property_disable_all_components(
    frozen,
):
    @dataclass(frozen=True, slots=True)
    class FrozenData:
        offset: tuple[float, float, float] = (1, 2, 3)

    class ReadOnlyData:
        @property
        def offset(self):
            return (1, 2, 3)

    store = PythonFloat3AttributeStore(
        FrozenData() if frozen else ReadOnlyData(), "offset"
    )
    assert store.is_available
    assert not store.is_writable
    for component in store.components:
        assert not component.is_writable
        with pytest.raises(RuntimeError):
            component.write(2)
    with pytest.raises(RuntimeError):
        store.write((4, 5, 6))


def test_deleted_attribute_invalid_value_and_restoration():
    data = SimpleNamespace(offset=(1, 2, 3))
    store = PythonFloat3AttributeStore(data, "offset")
    del data.offset
    assert not store.is_available
    assert not store.is_writable
    with pytest.raises(RuntimeError):
        store.read()
    with pytest.raises(RuntimeError):
        store.components[0].write(2)
    data.offset = (1, float("nan"), 3)
    with pytest.raises(ValueError):
        store.read()
    data.offset = (7, 8, 9)
    assert store.read() == (7, 8, 9)
