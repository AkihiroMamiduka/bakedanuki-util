# coding: utf-8
from __future__ import annotations

import pytest


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def _make_transformation_matrix(maya_om):
    value = maya_om.MTransformationMatrix()
    value.setTranslation(
        maya_om.MVector(1.0, 2.0, 3.0),
        maya_om.MSpace.kTransform,
    )
    value.setRotation(maya_om.MEulerRotation(0.1, 0.2, 0.3))
    value.setScale((2.0, 3.0, 4.0), maya_om.MSpace.kTransform)
    return value


def test_matrix_plug_gets_transform_matrix(new_scene, maya_cmds):
    import bd_util as bdu

    node_name = maya_cmds.createNode("composeMatrix", name="compose_matrix")
    maya_cmds.setAttr(f"{node_name}.inputTranslate", 1.0, 2.0, 3.0)
    matrix_plug = bdu.Nodes().existing.composeMatrix(node_name).outputMatrix

    value = matrix_plug.get()

    assert isinstance(value, bdu.TransformMatrix)
    assert value.translate == pytest.approx((1.0, 2.0, 3.0))


def test_matrix_plug_set_accepts_supported_matrix_values(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("multMatrix", name="mult_matrix")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.multMatrix(node_name)
    value = _make_transformation_matrix(maya_om)
    flat = tuple(value.asMatrix())
    rows = tuple(flat[index : index + 4] for index in range(0, 16, 4))
    sources = (
        value.asMatrix(),
        value,
        bdu.TransformMatrix(value),
        list(flat),
        rows,
    )

    for index, source in enumerate(sources):
        node.matrixIn[index].set(source)
    mod.do_it_dg()

    for index in range(len(sources)):
        actual = node.matrixIn[index].get()
        assert isinstance(actual, bdu.TransformMatrix)
        _assert_matrix_close(actual.matrix, value.asMatrix())
