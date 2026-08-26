# coding: utf-8
from __future__ import annotations

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
    ("order", "maya_order"),
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
    order,
    maya_order,
):
    from bd_util import DoubleAngle3, TransformMatrix

    source = _make_transformation_matrix(maya_om)
    value = TransformMatrix(source)

    rotate = value.get_rotate(order=order)
    assert isinstance(rotate, DoubleAngle3)
    actual = maya_om.MEulerRotation(
        *(math.radians(component) for component in rotate),
        maya_order,
    ).asMatrix()
    expected = source.rotation(asQuaternion=True).asMatrix()

    _assert_matrix_close(actual, expected)


def test_get_rotate_validates_order(new_scene, maya_om):
    from bd_util import TransformMatrix

    value = TransformMatrix(maya_om.MMatrix())

    assert value.get_rotate(order="XYZ") == pytest.approx((0.0, 0.0, 0.0))
    with pytest.raises(ValueError, match="Unsupported rotation order"):
        value.get_rotate(order="invalid")
    with pytest.raises(TypeError, match="order must be str"):
        value.get_rotate(order=0)


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


def test_constructor_reports_invalid_plug(new_scene, maya_cmds):
    from bd_util import TransformMatrix

    transform = maya_cmds.createNode("transform", name="test_transform")

    with pytest.raises(ValueError, match="Could not resolve matrix plug"):
        TransformMatrix("missing.worldMatrix[0]")
    with pytest.raises(TypeError, match="Plug must be a matrix plug"):
        TransformMatrix(f"{transform}.translateX")
