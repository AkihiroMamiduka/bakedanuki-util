# coding: utf-8
from __future__ import annotations

import math
import operator

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


def _assert_quat_close(actual, expected, *, abs=1.0e-12):
    assert tuple(actual) == pytest.approx(tuple(expected), abs=abs)


def test_accepts_identity_components_sequence_and_open_maya(maya_om):
    expected = (1.0, 2.0, 3.0, 4.0)
    values = (
        bdu.Quat(1.0, 2.0, 3.0, 4.0),
        bdu.Quat(expected),
        bdu.Quat(list(expected)),
        bdu.Quat(bdu.Quat(expected)),
        bdu.Quat(maya_om.MQuaternion(*expected)),
    )

    assert bdu.Quat() == bdu.Quat(0.0, 0.0, 0.0, 1.0)
    for value in values:
        assert value == bdu.Quat(*expected)
        assert all(isinstance(component, float) for component in value)


def test_sequence_input_is_a_snapshot():
    source = [1.0, 2.0, 3.0, 4.0]
    value = bdu.Quat(source)

    source[0] = 100.0

    assert value == bdu.Quat(1.0, 2.0, 3.0, 4.0)


@pytest.mark.parametrize(
    ("args", "error_type", "message"),
    (
        (((1.0, 2.0, 3.0),), ValueError, "exactly 4"),
        (("1, 2, 3, 4",), TypeError, "exactly 4"),
        (((1.0, 2.0, 3.0, object()),), TypeError, "value\\[3\\]"),
        ((1.0, 2.0), TypeError, "Quat requires"),
    ),
)
def test_constructor_rejects_invalid_values(args, error_type, message):
    with pytest.raises(error_type, match=message):
        bdu.Quat(*args)


@pytest.mark.parametrize(
    ("rotate_order_name", "maya_order"),
    (
        ("xyz", 0),
        ("yzx", 1),
        ("zxy", 2),
        ("xzy", 3),
        ("yxz", 4),
        ("zyx", 5),
    ),
)
def test_euler_conversion_uses_degrees_and_rotation_order(
    maya_om,
    rotate_order_name,
    maya_order,
):
    rotate = (17.0, -28.0, 39.0)
    radians = tuple(math.radians(component) for component in rotate)
    expected = maya_om.MEulerRotation(*radians, maya_order).asQuaternion()

    for rotate_order in (rotate_order_name, maya_order):
        value = bdu.Quat.from_euler(rotate, rotate_order=rotate_order)
        round_trip = bdu.Quat.from_euler(
            value.to_euler(rotate_order=rotate_order),
            rotate_order=rotate_order,
        )

        _assert_quat_close(value, expected)
        assert value.is_equivalent(round_trip, tolerance=1.0e-10)


def test_euler_conversion_accepts_case_insensitive_order():
    assert bdu.Quat.from_euler(
        (10.0, 20.0, 30.0), rotate_order="ZYX"
    ) == pytest.approx(
        bdu.Quat.from_euler((10.0, 20.0, 30.0), rotate_order="zyx")
    )


def test_to_euler_accepts_rotate_order_from_transform_plug(new_scene):
    nodes = bdu.Nodes()
    dst = nodes.create.transform(name="dst")
    dst.rotateOrder.set(3)
    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    expected = bdu.Quat.from_euler(
        (17.0, -28.0, 39.0),
        rotate_order=3,
    )
    dst.r.set(expected.to_euler(rotate_order=dst.rotateOrder.get()))
    nodes.modifier_manager.do_it_dg()

    assert expected.is_equivalent(dst.m.get().quat, tolerance=1.0e-10)


def test_euler_conversion_rejects_invalid_order():
    with pytest.raises(ValueError, match="Unsupported rotation order"):
        bdu.Quat.from_euler((0.0, 0.0, 0.0), rotate_order="invalid")

    for rotate_order in (-1, 6):
        with pytest.raises(
            ValueError, match="Unsupported rotation order index"
        ):
            bdu.Quat.from_euler(
                (0.0, 0.0, 0.0),
                rotate_order=rotate_order,
            )

    for rotate_order in (True, 0.0, object()):
        with pytest.raises(TypeError, match="rotate_order must be str or int"):
            bdu.Quat.from_euler(
                (0.0, 0.0, 0.0),
                rotate_order=rotate_order,
            )


def test_axis_angle_conversion_uses_degrees(maya_om):
    value = bdu.Quat.from_axis_angle((0.0, 1.0, 0.0), 45.0)
    expected = maya_om.MQuaternion(
        math.radians(45.0),
        maya_om.MVector(0.0, 1.0, 0.0),
    )

    axis, angle = value.to_axis_angle()

    _assert_quat_close(value, expected)
    assert isinstance(axis, bdu.Double3)
    assert axis == pytest.approx((0.0, 1.0, 0.0))
    assert angle == pytest.approx(45.0)


def test_from_vectors_matches_open_maya(maya_om):
    source = (1.0, 0.0, 0.0)
    target = (0.0, 1.0, 0.0)
    value = bdu.Quat.from_vectors(source, target, factor=0.5)
    expected = maya_om.MQuaternion(
        maya_om.MVector(*source),
        maya_om.MVector(*target),
        0.5,
    )

    _assert_quat_close(value, expected)


def test_from_matrix_accepts_transform_matrix_and_open_maya(maya_om):
    transformation = maya_om.MTransformationMatrix()
    transformation.setRotation(
        maya_om.MEulerRotation(
            math.radians(10.0),
            math.radians(20.0),
            math.radians(30.0),
        )
    )
    matrix = transformation.asMatrix()
    expected = transformation.rotation(asQuaternion=True)
    sources = (
        bdu.TransformMatrix(matrix),
        matrix,
        transformation,
        tuple(matrix),
        tuple(tuple(matrix)[index : index + 4] for index in range(0, 16, 4)),
    )

    for source in sources:
        _assert_quat_close(bdu.Quat.from_matrix(source), expected)


def test_from_matrix_rejects_non_matrix_source():
    with pytest.raises(TypeError, match="value must be TransformMatrix"):
        bdu.Quat.from_matrix(object())


def test_open_maya_value_is_a_copy(maya_om):
    value = bdu.Quat(1.0, 2.0, 3.0, 4.0)
    quaternion = value.quaternion

    quaternion.x = 100.0

    assert value == bdu.Quat(1.0, 2.0, 3.0, 4.0)


def test_length_and_state_queries():
    value = bdu.Quat(1.0, 2.0, 3.0, 4.0)

    assert value.length_squared == pytest.approx(30.0)
    assert value.length == pytest.approx(math.sqrt(30.0))
    assert value.is_finite()
    assert not value.is_zero()
    assert not value.is_unit()
    assert bdu.Quat().is_unit()
    assert bdu.Quat(1.0e-11, 0.0, 0.0, 0.0).is_zero()
    assert not bdu.Quat(float("nan"), 0.0, 0.0, 1.0).is_finite()


@pytest.mark.parametrize("tolerance", (-1.0, float("inf"), float("nan")))
def test_state_query_rejects_invalid_tolerance(tolerance):
    with pytest.raises(ValueError, match="finite and non-negative"):
        bdu.Quat().is_unit(tolerance)


def test_quaternion_operations_match_open_maya(maya_om):
    left = bdu.Quat(1.0, 2.0, 3.0, 4.0)
    right = bdu.Quat(0.5, -1.0, 2.0, 0.25)
    maya_left = left.quaternion
    maya_right = right.quaternion

    _assert_quat_close(left * right, maya_left * maya_right)
    _assert_quat_close(left * maya_right, maya_left * maya_right)
    _assert_quat_close(maya_left * right, maya_left * maya_right)
    _assert_quat_close(left.inverse(), maya_left.inverse())
    _assert_quat_close(left.conjugate(), maya_left.conjugate())
    _assert_quat_close(left.normalized(), maya_left.normal())
    _assert_quat_close(-left, -maya_left)

    for result in (
        left * right,
        left.inverse(),
        left.conjugate(),
        left.normalized(),
        -left,
    ):
        assert isinstance(result, bdu.Quat)


def test_multiplication_rejects_unsupported_operand():
    with pytest.raises(TypeError):
        operator.mul(bdu.Quat(), 2.0)

    with pytest.raises(TypeError):
        operator.mul(2.0, bdu.Quat())


@pytest.mark.parametrize("weight", (-0.5, 0.0, 0.25, 1.0, 1.5))
def test_slerp_matches_open_maya(maya_om, weight):
    source = bdu.Quat.from_axis_angle((1.0, 0.0, 0.0), 20.0)
    target = bdu.Quat.from_axis_angle((0.0, 1.0, 0.0), 80.0)
    expected = maya_om.MQuaternion.slerp(
        source.quaternion,
        target.quaternion,
        weight,
    )

    _assert_quat_close(source.slerp(target, weight), expected)


def test_raw_equality_and_maya_equivalence_are_distinct():
    value = bdu.Quat.from_axis_angle((0.0, 0.0, 1.0), 45.0)

    assert value != -value
    assert value.is_equivalent(-value)
    assert not value.is_equivalent(
        bdu.Quat(*(component * 2.0 for component in value))
    )


def test_zero_quaternion_follows_open_maya_edge_behavior():
    value = bdu.Quat(0.0, 0.0, 0.0, 0.0)

    assert value.normalized() == bdu.Quat()
    assert all(math.isnan(component) for component in value.inverse())

    with pytest.raises(ValueError, match="zero quaternion"):
        value.to_transform_matrix()


def test_transform_matrix_round_trip_preserves_rotation():
    value = bdu.Quat.from_euler(
        (10.0, 20.0, 30.0),
        rotate_order="zyx",
    )

    result = value.to_transform_matrix().quat

    assert value.is_equivalent(result, tolerance=1.0e-10)
