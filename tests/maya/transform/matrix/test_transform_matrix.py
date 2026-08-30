# coding: utf-8
from __future__ import annotations

from array import array
import math

import pytest


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def _make_transformation_matrix(maya_om):
    value = maya_om.MTransformationMatrix()
    value.setTranslation(
        maya_om.MVector(1.0, 2.0, 3.0),
        maya_om.MSpace.kTransform,
    )
    value.setRotation(
        maya_om.MEulerRotation(
            math.radians(10.0),
            math.radians(20.0),
            math.radians(30.0),
        )
    )
    value.setScale((2.0, 3.0, 4.0), maya_om.MSpace.kTransform)
    value.setShear((0.1, 0.2, 0.3), maya_om.MSpace.kTransform)
    return value


def _flat_matrix_values():
    return (
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        4.0,
        5.0,
        6.0,
        1.0,
    )


def _matrix_rows(values):
    return tuple(values[index : index + 4] for index in range(0, 16, 4))


def test_can_import_from_public_packages(new_scene):
    import bd_util
    from bd_util.maya.transform import TransformMatrix
    from bd_util.maya.transform.matrix import (
        TransformMatrix as MatrixPackageTransformMatrix,
    )

    assert bd_util.TransformMatrix is TransformMatrix
    assert MatrixPackageTransformMatrix is TransformMatrix
    assert "TransformMatrix" in bd_util.__all__


def test_accepts_matrix_value_sources(new_scene, maya_om):
    from bd_util import (
        Double3,
        DoubleAngle3,
        DoubleLinear3,
        Quat,
        TransformMatrix,
    )

    source = _make_transformation_matrix(maya_om)
    wrappers = (
        TransformMatrix(source),
        TransformMatrix(source.asMatrix()),
        TransformMatrix(TransformMatrix(source)),
    )

    expected_quat = source.rotation(asQuaternion=True)
    for value in wrappers:
        assert isinstance(value.translate, DoubleLinear3)
        assert isinstance(value.rotate, DoubleAngle3)
        assert isinstance(value.scale, Double3)
        assert isinstance(value.shear, Double3)
        assert isinstance(value.quat, Quat)
        assert value.translate == pytest.approx((1.0, 2.0, 3.0))
        assert value.rotate == pytest.approx((10.0, 20.0, 30.0))
        assert value.scale == pytest.approx((2.0, 3.0, 4.0))
        assert value.shear == pytest.approx((0.1, 0.2, 0.3))
        assert value.quat == pytest.approx(
            (
                expected_quat.x,
                expected_quat.y,
                expected_quat.z,
                expected_quat.w,
            )
        )


def test_accepts_flat_and_four_by_four_matrix_sequences(
    new_scene,
    maya_om,
):
    from bd_util import TransformMatrix

    flat = _flat_matrix_values()
    rows = _matrix_rows(flat)
    sources = (
        list(flat),
        flat,
        [list(row) for row in rows],
        rows,
        [tuple(row) for row in rows],
        range(16),
        array("d", flat),
    )

    for source in sources:
        value = TransformMatrix(source)

        _assert_matrix_close(value.matrix, maya_om.MMatrix(source))


def test_matrix_sequence_input_is_a_snapshot(new_scene):
    from bd_util import TransformMatrix

    flat_source = list(_flat_matrix_values())
    row_source = [list(row) for row in _matrix_rows(flat_source)]
    from_flat = TransformMatrix(flat_source)
    from_rows = TransformMatrix(row_source)

    flat_source[12] = 100.0
    row_source[3][0] = 200.0

    assert from_flat.translate == pytest.approx((4.0, 5.0, 6.0))
    assert from_rows.translate == pytest.approx((4.0, 5.0, 6.0))


def test_component_defaults_create_identity_matrix(new_scene, maya_om):
    from bd_util import TransformMatrix

    value = TransformMatrix()

    _assert_matrix_close(value.matrix, maya_om.MMatrix())
    assert value.translate == pytest.approx((0.0, 0.0, 0.0))
    assert value.rotate == pytest.approx((0.0, 0.0, 0.0))
    assert value.scale == pytest.approx((1.0, 1.0, 1.0))
    assert value.shear == pytest.approx((0.0, 0.0, 0.0))


def test_translate_only_keeps_identity_rotation_scale_and_shear(new_scene):
    from bd_util import TransformMatrix

    value = TransformMatrix(translate=(1.0, 2.0, 3.0))

    assert value.translate == pytest.approx((1.0, 2.0, 3.0))
    assert value.rotate == pytest.approx((0.0, 0.0, 0.0))
    assert value.scale == pytest.approx((1.0, 1.0, 1.0))
    assert value.shear == pytest.approx((0.0, 0.0, 0.0))


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
def test_euler_components_match_compose_matrix_node(
    new_scene,
    maya_cmds,
    maya_om,
    rotate_order_name,
    maya_order,
):
    from bd_util import TransformMatrix

    translate = (1.25, -2.5, 3.75)
    rotate = (17.0, -28.0, 39.0)
    scale = (2.0, -3.0, 4.0)
    shear = (0.1, -0.2, 0.3)
    values = (
        TransformMatrix(
            translate=translate,
            rotate=rotate,
            rotate_order=rotate_order,
            scale=scale,
            shear=shear,
        )
        for rotate_order in (rotate_order_name, maya_order)
    )
    node = maya_cmds.createNode("composeMatrix")
    maya_cmds.setAttr(f"{node}.useEulerRotation", True)
    maya_cmds.setAttr(f"{node}.inputRotateOrder", maya_order)
    maya_cmds.setAttr(f"{node}.inputTranslate", *translate)
    maya_cmds.setAttr(f"{node}.inputRotate", *rotate)
    maya_cmds.setAttr(f"{node}.inputScale", *scale)
    maya_cmds.setAttr(f"{node}.inputShear", *shear)

    expected = maya_om.MMatrix(maya_cmds.getAttr(f"{node}.outputMatrix"))

    for value in values:
        _assert_matrix_close(value.matrix, expected)


def test_quat_components_match_compose_matrix_node(
    new_scene,
    maya_cmds,
    maya_om,
):
    from bd_util import TransformMatrix

    translate = (1.25, -2.5, 3.75)
    quat = (1.0, 2.0, 3.0, 4.0)
    scale = (2.0, -3.0, 4.0)
    shear = (0.1, -0.2, 0.3)
    value = TransformMatrix(
        translate=translate,
        quat=quat,
        rotate_order="zyx",
        scale=scale,
        shear=shear,
    )
    node = maya_cmds.createNode("composeMatrix")
    maya_cmds.setAttr(f"{node}.useEulerRotation", False)
    maya_cmds.setAttr(f"{node}.inputRotateOrder", 5)
    maya_cmds.setAttr(f"{node}.inputTranslate", *translate)
    maya_cmds.setAttr(f"{node}.inputQuat", *quat)
    maya_cmds.setAttr(f"{node}.inputScale", *scale)
    maya_cmds.setAttr(f"{node}.inputShear", *shear)

    expected = maya_om.MMatrix(maya_cmds.getAttr(f"{node}.outputMatrix"))

    _assert_matrix_close(value.matrix, expected)


def test_component_input_accepts_public_value_types_and_is_a_snapshot(
    new_scene,
):
    import bd_util as bdu

    translate = [1.0, 2.0, 3.0]
    value = bdu.TransformMatrix(
        translate=translate,
        rotate=bdu.DoubleAngle3(10.0, 20.0, 30.0),
        scale=bdu.Double3(2.0, 3.0, 4.0),
        shear=bdu.Double3(0.1, 0.2, 0.3),
    )

    translate[0] = 100.0

    assert value.translate == pytest.approx((1.0, 2.0, 3.0))
    assert value.rotate == pytest.approx((10.0, 20.0, 30.0))
    assert value.scale == pytest.approx((2.0, 3.0, 4.0))
    assert value.shear == pytest.approx((0.1, 0.2, 0.3))

    quat_value = bdu.TransformMatrix(quat=bdu.Quat(1.0, 2.0, 3.0, 4.0))
    assert isinstance(quat_value.quat, bdu.Quat)


@pytest.mark.parametrize(
    ("name", "kwargs"),
    (
        ("translate", {"translate": (1.0, 2.0)}),
        ("rotate", {"rotate": (1.0, 2.0, 3.0, 4.0)}),
        ("quat", {"quat": (0.0, 0.0, 1.0)}),
        ("scale", {"scale": (1.0, 2.0)}),
        ("shear", {"shear": (1.0, 2.0, 3.0, 4.0)}),
        ("translate", {"translate": (1.0, "two", 3.0)}),
    ),
)
def test_rejects_invalid_transform_components(new_scene, name, kwargs):
    from bd_util import TransformMatrix

    with pytest.raises(
        ValueError,
        match=rf"{name} must contain exactly .* numeric values",
    ):
        TransformMatrix(**kwargs)


def test_rejects_conflicting_rotation_and_source_inputs(new_scene, maya_om):
    from bd_util import TransformMatrix

    with pytest.raises(ValueError, match="rotate and quat"):
        TransformMatrix(
            rotate=(10.0, 20.0, 30.0),
            quat=(0.0, 0.0, 0.0, 1.0),
        )
    with pytest.raises(ValueError, match="zero quaternion"):
        TransformMatrix(quat=(0.0, 0.0, 0.0, 0.0))
    with pytest.raises(ValueError, match="cannot be combined"):
        TransformMatrix(
            maya_om.MMatrix(),
            translate=(1.0, 2.0, 3.0),
        )


def test_component_constructor_validates_rotate_order(new_scene):
    from bd_util import TransformMatrix

    uppercase = TransformMatrix(
        rotate=(0.0, 0.0, 0.0),
        rotate_order="ZYX",
    )

    assert uppercase.rotate == pytest.approx((0.0, 0.0, 0.0))
    assert TransformMatrix(rotate_order=5).rotate == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    with pytest.raises(ValueError, match="Unsupported rotation order"):
        TransformMatrix(rotate_order="invalid")
    with pytest.raises(ValueError, match="Unsupported rotation order index"):
        TransformMatrix(rotate_order=6)
    for rotate_order in (True, 0.0, object()):
        with pytest.raises(TypeError, match="rotate_order must be str or int"):
            TransformMatrix(rotate_order=rotate_order)


@pytest.mark.parametrize(
    "source",
    (
        (),
        (0.0,) * 15,
        (0.0,) * 17,
        ((0.0, 0.0, 0.0, 0.0),) * 3,
        (
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0),
        ),
        (object(),) * 16,
        ("0.0",) * 16,
    ),
)
def test_rejects_invalid_matrix_sequences(new_scene, source):
    from bd_util import TransformMatrix

    with pytest.raises(ValueError, match="exactly 16 numeric values"):
        TransformMatrix(source)


def test_accepts_matrix_plug_name_and_mplug(new_scene, maya_cmds, maya_om):
    from bd_util import TransformMatrix

    transform = maya_cmds.createNode("transform", name="test_transform")
    maya_cmds.setAttr(f"{transform}.translate", 1.0, 2.0, 3.0)
    plug_name = f"{transform}.worldMatrix[0]"

    selection = maya_om.MSelectionList()
    selection.add(plug_name)
    plug = selection.getPlug(0)

    from_name = TransformMatrix(plug_name)
    from_plug = TransformMatrix(plug)

    assert from_name.translate == pytest.approx((1.0, 2.0, 3.0))
    _assert_matrix_close(from_name.matrix, from_plug.matrix)


def test_plug_input_is_a_snapshot(new_scene, maya_cmds):
    from bd_util import TransformMatrix

    transform = maya_cmds.createNode("transform", name="test_transform")
    plug_name = f"{transform}.worldMatrix[0]"
    value = TransformMatrix(plug_name)

    maya_cmds.setAttr(f"{transform}.translateX", 8.0)

    assert value.translate == pytest.approx((0.0, 0.0, 0.0))
    assert TransformMatrix(plug_name).translate == pytest.approx(
        (8.0, 0.0, 0.0)
    )


def test_returned_open_maya_values_are_copies(new_scene, maya_om):
    from bd_util import TransformMatrix

    source = _make_transformation_matrix(maya_om)
    value = TransformMatrix(source)

    matrix = value.matrix
    matrix.setElement(3, 0, 20.0)
    transformation_matrix = value.transformation_matrix
    transformation_matrix.setTranslation(
        maya_om.MVector(30.0, 0.0, 0.0),
        maya_om.MSpace.kTransform,
    )
    source.setTranslation(
        maya_om.MVector(40.0, 0.0, 0.0),
        maya_om.MSpace.kTransform,
    )

    assert value.translate == pytest.approx((1.0, 2.0, 3.0))


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
def test_get_rotate_supports_maya_rotation_orders(
    new_scene,
    maya_om,
    rotate_order_name,
    maya_order,
):
    from bd_util import DoubleAngle3, TransformMatrix

    source = _make_transformation_matrix(maya_om)
    value = TransformMatrix(source)

    expected = source.rotation(asQuaternion=True).asMatrix()

    for rotate_order in (rotate_order_name, maya_order):
        rotate = value.get_rotate(rotate_order=rotate_order)
        assert isinstance(rotate, DoubleAngle3)
        actual = maya_om.MEulerRotation(
            *(math.radians(component) for component in rotate),
            maya_order,
        ).asMatrix()

        _assert_matrix_close(actual, expected)


def test_get_rotate_validates_order(new_scene, maya_om):
    from bd_util import TransformMatrix

    value = TransformMatrix(maya_om.MMatrix())

    assert value.get_rotate(rotate_order="XYZ") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert value.get_rotate(rotate_order=0) == pytest.approx((0.0, 0.0, 0.0))
    with pytest.raises(ValueError, match="Unsupported rotation order"):
        value.get_rotate(rotate_order="invalid")
    with pytest.raises(ValueError, match="Unsupported rotation order index"):
        value.get_rotate(rotate_order=-1)
    for rotate_order in (True, 0.0, object()):
        with pytest.raises(TypeError, match="rotate_order must be str or int"):
            value.get_rotate(rotate_order=rotate_order)


def test_multiplies_transform_matrices(new_scene, maya_om):
    from bd_util import TransformMatrix

    left_source = maya_om.MTransformationMatrix()
    left_source.setRotation(
        maya_om.MEulerRotation(0.0, 0.0, math.radians(90.0))
    )
    right_source = maya_om.MTransformationMatrix()
    right_source.setTranslation(
        maya_om.MVector(2.0, 3.0, 4.0),
        maya_om.MSpace.kTransform,
    )
    left = TransformMatrix(left_source)
    right = TransformMatrix(right_source)

    result = left * right

    assert isinstance(result, TransformMatrix)
    _assert_matrix_close(
        result.matrix,
        left_source.asMatrix() * right_source.asMatrix(),
    )


def test_multiplies_mmatrix_on_either_side(new_scene, maya_om):
    from bd_util import TransformMatrix

    left_source = maya_om.MTransformationMatrix()
    left_source.setRotation(
        maya_om.MEulerRotation(0.0, 0.0, math.radians(90.0))
    )
    right_source = maya_om.MTransformationMatrix()
    right_source.setTranslation(
        maya_om.MVector(2.0, 3.0, 4.0),
        maya_om.MSpace.kTransform,
    )
    left = TransformMatrix(left_source)
    right = right_source.asMatrix()

    left_result = left * right
    right_result = right * left

    assert isinstance(left_result, TransformMatrix)
    assert isinstance(right_result, TransformMatrix)
    _assert_matrix_close(
        left_result.matrix,
        left_source.asMatrix() * right,
    )
    _assert_matrix_close(
        right_result.matrix,
        right * left_source.asMatrix(),
    )


def test_world_matrix_times_parent_inverse_matrix_returns_local_matrix(
    new_scene,
    maya_cmds,
):
    from bd_util import TransformMatrix

    parent = maya_cmds.createNode("transform", name="dst_parent")
    dst = maya_cmds.createNode("transform", name="dst", parent=parent)
    src = maya_cmds.createNode("transform", name="src")
    maya_cmds.setAttr(f"{parent}.translate", 3.0, 4.0, 5.0)
    maya_cmds.setAttr(f"{parent}.rotate", 15.0, 25.0, 35.0)
    maya_cmds.setAttr(f"{src}.translate", 7.0, 8.0, 9.0)
    maya_cmds.setAttr(f"{src}.rotate", 10.0, 20.0, 30.0)

    local = TransformMatrix(f"{src}.wm[0]") * TransformMatrix(f"{dst}.pim[0]")

    src_world = maya_cmds.xform(src, query=True, matrix=True, worldSpace=True)
    maya_cmds.xform(dst, matrix=src_world, worldSpace=True)
    expected = TransformMatrix(f"{dst}.m")

    _assert_matrix_close(local.matrix, expected.matrix)


def test_inverse_returns_transform_matrix(new_scene, maya_om):
    from bd_util import TransformMatrix

    value = TransformMatrix(_make_transformation_matrix(maya_om))

    inverse = value.inverse()

    assert isinstance(inverse, TransformMatrix)
    _assert_matrix_close(
        value.matrix * inverse.matrix,
        maya_om.MMatrix(),
    )


def test_constructor_rejects_unsupported_value(new_scene):
    from bd_util import TransformMatrix

    with pytest.raises(TypeError, match="value must be"):
        TransformMatrix(object())
    with pytest.raises(TypeError, match="value must be"):
        TransformMatrix(None)
    with pytest.raises(TypeError, match="value must be"):
        TransformMatrix(value for value in range(16))


def test_constructor_preserves_keyword_value_input(new_scene, maya_om):
    from bd_util import TransformMatrix

    value = TransformMatrix(value=maya_om.MMatrix())

    _assert_matrix_close(value.matrix, maya_om.MMatrix())


def test_constructor_reports_invalid_plug(new_scene, maya_cmds):
    from bd_util import TransformMatrix

    transform = maya_cmds.createNode("transform", name="test_transform")

    with pytest.raises(ValueError, match="Could not resolve matrix plug"):
        TransformMatrix("missing.worldMatrix[0]")
    with pytest.raises(TypeError, match="Plug must be a matrix plug"):
        TransformMatrix(f"{transform}.translateX")
