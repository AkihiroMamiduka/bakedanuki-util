# coding: utf-8
from __future__ import annotations

import pytest


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def test_data_matrix_plug_gets_transform_matrix_values(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    transform = maya_cmds.createNode("transform", name="test_transform")
    maya_cmds.setAttr(f"{transform}.translate", 1.0, 2.0, 3.0)
    maya_cmds.setAttr(f"{transform}.rotate", 10.0, 20.0, 30.0)
    maya_cmds.setAttr(f"{transform}.scale", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{transform}.shear", 0.1, 0.2, 0.3)
    node = bdu.Nodes().existing.transform(transform)
    matrix_plug = node.wm[0]

    value = matrix_plug.get()
    expected_quat = value.quat

    assert isinstance(value, bdu.TransformMatrix)
    current = matrix_plug.get()
    _assert_matrix_close(current.matrix, value.matrix)
    _assert_matrix_close(
        matrix_plug.transformation_matrix.asMatrix(),
        value.matrix,
    )
    assert isinstance(
        matrix_plug.transformation_matrix,
        maya_om.MTransformationMatrix,
    )
    assert isinstance(matrix_plug.translate, bdu.DoubleLinear3)
    assert isinstance(matrix_plug.rotate, bdu.DoubleAngle3)
    assert isinstance(
        matrix_plug.get_rotate(order="zyx"),
        bdu.DoubleAngle3,
    )
    assert isinstance(matrix_plug.scale, bdu.Double3)
    assert isinstance(matrix_plug.shear, bdu.Double3)
    assert isinstance(matrix_plug.quat, bdu.Quat)
    assert matrix_plug.translate == pytest.approx((1.0, 2.0, 3.0))
    assert matrix_plug.rotate == pytest.approx((10.0, 20.0, 30.0))
    assert matrix_plug.get_rotate(order="zyx") == pytest.approx(
        value.get_rotate(order="zyx")
    )
    assert matrix_plug.scale == pytest.approx((2.0, 3.0, 4.0))
    assert matrix_plug.shear == pytest.approx((0.1, 0.2, 0.3))
    assert matrix_plug.quat == pytest.approx(expected_quat)


def test_get_reads_current_plug_value(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    transform = maya_cmds.createNode("transform", name="test_transform")
    node = bdu.Nodes().existing.transform(transform)
    matrix_plug = node.wm[0]
    first = matrix_plug.get()

    maya_cmds.setAttr(f"{transform}.translateX", 8.0)

    second = matrix_plug.get()
    assert first is not second
    assert first.translate == pytest.approx((0.0, 0.0, 0.0))
    assert second.translate == pytest.approx((8.0, 0.0, 0.0))
    assert matrix_plug.translate == pytest.approx((8.0, 0.0, 0.0))


def test_unset_data_matrix_raises_value_error(new_scene, maya_cmds):
    import bd_util as bdu

    node_name = maya_cmds.createNode("wtAddMatrix", name="wt_add_matrix")
    node = bdu.Nodes().existing.wtAddMatrix(node_name)
    matrix_plug = node.wtMatrix[0].matrixIn

    with pytest.raises(ValueError, match="does not contain a matrix value"):
        matrix_plug.get()
    with pytest.raises(ValueError, match="does not contain a matrix value"):
        _ = matrix_plug.transformation_matrix
    with pytest.raises(ValueError, match="does not contain a matrix value"):
        _ = matrix_plug.translate


def test_data_matrix_set_direct_is_immediate(new_scene, maya_cmds, maya_om):
    import bd_util as bdu

    node_name = maya_cmds.createNode("wtAddMatrix", name="wt_add_matrix")
    node = bdu.Nodes().existing.wtAddMatrix(node_name)
    matrix_plug = node.wtMatrix[0].matrixIn
    value = maya_om.MTransformationMatrix()
    value.setTranslation(
        maya_om.MVector(1.0, 2.0, 3.0),
        maya_om.MSpace.kTransform,
    )
    flat = tuple(value.asMatrix())
    rows = tuple(flat[index : index + 4] for index in range(0, 16, 4))

    for source in (
        value.asMatrix(),
        value,
        bdu.TransformMatrix(value),
        list(flat),
        rows,
    ):
        matrix_plug.set_direct(source)

        actual = matrix_plug.get()
        assert isinstance(actual, bdu.TransformMatrix)
        _assert_matrix_close(actual.matrix, value.asMatrix())
        assert actual.translate == pytest.approx((1.0, 2.0, 3.0))


def test_transform_matrix_property_is_not_exposed(new_scene, maya_cmds):
    import bd_util as bdu

    transform = maya_cmds.createNode("transform", name="test_transform")
    matrix_plug = bdu.Nodes().existing.transform(transform).wm[0]

    assert not hasattr(matrix_plug, "transform_matrix")
