# coding: utf-8
from collections.abc import Sequence
from dataclasses import FrozenInstanceError
import operator

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


VALUE_CASES = (
    (bdu.Double2, (1.0, 2.0)),
    (bdu.Double3, (1.0, 2.0, 3.0)),
    (bdu.Double4, (1.0, 2.0, 3.0, 4.0)),
    (bdu.Float2, (1.0, 2.0)),
    (bdu.Float3, (1.0, 2.0, 3.0)),
    (bdu.Long2, (1, 2)),
    (bdu.Long3, (1, 2, 3)),
    (bdu.Short2, (1, 2)),
    (bdu.Short3, (1, 2, 3)),
    (bdu.DoubleLinear2, (1.0, 2.0)),
    (bdu.DoubleLinear3, (1.0, 2.0, 3.0)),
    (bdu.FloatLinear2, (1.0, 2.0)),
    (bdu.FloatLinear3, (1.0, 2.0, 3.0)),
    (bdu.DoubleAngle2, (1.0, 2.0)),
    (bdu.DoubleAngle3, (1.0, 2.0, 3.0)),
    (bdu.FloatAngle2, (1.0, 2.0)),
    (bdu.FloatAngle3, (1.0, 2.0, 3.0)),
    (bdu.Quat, (0.0, 0.0, 0.0, 1.0)),
)


@pytest.mark.parametrize(("value_type", "values"), VALUE_CASES)
def test_scalar_compound_value_is_immutable_sequence(value_type, values):
    value = value_type(*values)

    assert isinstance(value, Sequence)
    assert len(value) == len(values)
    assert tuple(value) == values
    assert value.as_tuple() == values
    assert value[0] == values[0]
    assert value[:] == values
    assert value.x == values[0]
    assert value.y == values[1]
    assert hash(value) == hash(value_type(*values))

    if len(values) >= 3:
        assert value.z == values[2]
    if len(values) == 4:
        assert value.w == values[3]

    with pytest.raises(FrozenInstanceError):
        value.x = values[0]
    with pytest.raises(TypeError):
        operator.add(value, value)


def test_scalar_compound_value_type_is_part_of_equality():
    assert bdu.Double2(1.0, 2.0) != bdu.Float2(1.0, 2.0)
    assert bdu.Double2(1.0, 2.0) != [1.0, 2.0]
    assert bdu.Quat(0.0, 0.0, 0.0, 1.0) != bdu.Double4(
        0.0,
        0.0,
        0.0,
        1.0,
    )


def test_scalar_compound_value_from_values_validates_length():
    assert bdu.Double2.from_values((1.0, 2.0)) == bdu.Double2(1.0, 2.0)

    with pytest.raises(ValueError, match="requires 2 values"):
        bdu.Double2.from_values((1.0,))
