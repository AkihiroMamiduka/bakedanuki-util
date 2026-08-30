# coding: utf-8
from collections.abc import Sequence
from dataclasses import FrozenInstanceError
import operator

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


FLOATING_NUMERIC_CASES = (
    (bdu.Double2, (1.0, 2.0)),
    (bdu.Double3, (1.0, 2.0, 3.0)),
    (bdu.Double4, (1.0, 2.0, 3.0, 4.0)),
    (bdu.Float2, (1.0, 2.0)),
    (bdu.Float3, (1.0, 2.0, 3.0)),
)

NON_ARITHMETIC_CASES = (
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
)

VALUE_CASES = (
    *FLOATING_NUMERIC_CASES,
    *NON_ARITHMETIC_CASES,
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


@pytest.mark.parametrize(("value_type", "values"), FLOATING_NUMERIC_CASES)
def test_floating_numeric_value_supports_basic_arithmetic(value_type, values):
    value = value_type(*values)
    other_values = tuple(float(index + 4) for index in range(len(values)))
    other = value_type(*other_values)

    results = (
        (value + other, tuple(a + b for a, b in zip(values, other_values))),
        (value - other, tuple(a - b for a, b in zip(values, other_values))),
        (value * 2, tuple(component * 2.0 for component in values)),
        (2 * value, tuple(component * 2.0 for component in values)),
        (value / 2, tuple(component / 2.0 for component in values)),
        (-value, tuple(-component for component in values)),
    )

    for result, expected in results:
        assert type(result) is value_type
        assert result == pytest.approx(expected)
        assert result is not value
        assert all(isinstance(component, float) for component in result)

    assert value == value_type(*values)


@pytest.mark.parametrize(("value_type", "values"), FLOATING_NUMERIC_CASES)
def test_floating_numeric_value_rejects_ambiguous_operands(value_type, values):
    value = value_type(*values)

    for operation, other in (
        (operator.add, values),
        (operator.sub, values),
        (operator.mul, value),
        (operator.truediv, value),
        (operator.mul, True),
        (operator.truediv, True),
    ):
        with pytest.raises(TypeError):
            operation(value, other)

    with pytest.raises(TypeError):
        operator.truediv(2.0, value)
    with pytest.raises(ZeroDivisionError):
        value / 0.0


@pytest.mark.parametrize(("value_type", "values"), NON_ARITHMETIC_CASES)
def test_integer_and_unit_values_do_not_inherit_numeric_arithmetic(
    value_type,
    values,
):
    value = value_type(*values)

    for operation, operands in (
        (operator.add, (value, value)),
        (operator.sub, (value, value)),
        (operator.mul, (value, 2)),
        (operator.truediv, (value, 2)),
        (operator.neg, (value,)),
    ):
        with pytest.raises(TypeError):
            operation(*operands)


def test_floating_numeric_value_requires_the_same_concrete_type():
    double_value = bdu.Double3(1.0, 2.0, 3.0)
    float_value = bdu.Float3(1.0, 2.0, 3.0)

    with pytest.raises(TypeError):
        operator.add(double_value, float_value)
    with pytest.raises(TypeError):
        operator.sub(float_value, double_value)


def test_quat_is_not_a_double4_and_keeps_quaternion_only_arithmetic():
    value = bdu.Quat()

    assert not isinstance(value, bdu.Double4)
    assert not issubclass(bdu.Quat, bdu.Double4)
    assert isinstance(value * value, bdu.Quat)

    for operation in (operator.add, operator.sub, operator.truediv):
        with pytest.raises(TypeError):
            operation(value, value)


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
