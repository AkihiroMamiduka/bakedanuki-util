# coding: utf-8
from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


def test_class_attribute_access(plus_minus_average_cls):
    node_cls = plus_minus_average_cls

    assert node_cls.NODE_TYPE == "plusMinusAverage"

    assert node_cls.input1D.long_name == "input1D"
    assert node_cls.i1.long_name == "input1D"
    assert node_cls.i1.short_name == "i1"

    assert node_cls.input2D.long_name == "input2D"
    assert node_cls.input2D.input2Dx.long_name == "input2Dx"
    assert node_cls.input2D.input2Dy.long_name == "input2Dy"

    assert node_cls.input3D.long_name == "input3D"
    assert node_cls.input3D.input3Dx.long_name == "input3Dx"
    assert node_cls.input3D.input3Dy.long_name == "input3Dy"
    assert node_cls.input3D.input3Dz.long_name == "input3Dz"

    assert node_cls.output3Dx.long_name == "output3Dx"
    assert node_cls.o3x.long_name == "output3Dx"
    assert node_cls.output3Dy.long_name == "output3Dy"
    assert node_cls.o3y.long_name == "output3Dy"
    assert node_cls.output3Dz.long_name == "output3Dz"
    assert node_cls.o3z.long_name == "output3Dz"


def test_create_node(plus_minus_average_node, maya_cmds):
    node = plus_minus_average_node

    assert node.name == "test"
    assert str(node) == "test"
    assert node.exists()
    assert maya_cmds.nodeType(node.name) == "plusMinusAverage"


def test_plug_cache_and_aliases(plus_minus_average_node):
    node = plus_minus_average_node

    assert node.input1D is node.input1D
    assert node.i1 is node.input1D

    assert node.input3D is node.input3D
    assert node.i3 is node.input3D
    assert node.input3D[0] is node.input3D[0]
    assert node.input3D[0].input3Dx is node.input3D[0].input3Dx
    assert node.input3D[0].i3x is node.input3D[0].input3Dx

    assert node.output3D is node.o3
    assert node.output3Dx is node.output3Dx
    assert node.o3x is node.output3Dx
    assert node.output3D.output3Dx is node.output3Dx


def test_get_set_long_names(modifier_manager, plus_minus_average_node):
    node = plus_minus_average_node

    node.input1D[0].set(100.0)
    modifier_manager.do_it_dg()
    assert node.input1D[0].get() == pytest.approx(100.0)

    node.input2D[0].input2Dx.set(201.0)
    node.input2D[0].input2Dy.set(202.0)
    modifier_manager.do_it_dg()
    assert node.input2D[0].input2Dx.get() == pytest.approx(201.0)
    assert node.input2D[0].input2Dy.get() == pytest.approx(202.0)
    input2d = node.input2D[0].get()
    assert isinstance(input2d, bdu.Float2)
    assert input2d == pytest.approx([201.0, 202.0])

    node.input3D[0].input3Dx.set(301.0)
    node.input3D[0].input3Dy.set(302.0)
    node.input3D[0].input3Dz.set(303.0)
    modifier_manager.do_it_dg()
    assert node.input3D[0].input3Dx.get() == pytest.approx(301.0)
    assert node.input3D[0].input3Dy.get() == pytest.approx(302.0)
    assert node.input3D[0].input3Dz.get() == pytest.approx(303.0)
    input3d = node.input3D[0].get()
    assert isinstance(input3d, bdu.Float3)
    assert input3d == pytest.approx([301.0, 302.0, 303.0])


def test_get_set_short_names(modifier_manager, plus_minus_average_node):
    node = plus_minus_average_node

    node.i1[0].set(100.0)
    modifier_manager.do_it_dg()
    assert node.i1[0].get() == pytest.approx(100.0)
    assert node.input1D[0].get() == pytest.approx(100.0)

    node.i2[0].i2x.set(201.0)
    node.i2[0].i2y.set(202.0)
    modifier_manager.do_it_dg()
    assert node.i2[0].get() == pytest.approx([201.0, 202.0])
    assert node.input2D[0].get() == pytest.approx([201.0, 202.0])

    node.i3[0].i3x.set(301.0)
    node.i3[0].i3y.set(302.0)
    node.i3[0].i3z.set(303.0)
    modifier_manager.do_it_dg()
    assert node.i3[0].get() == pytest.approx([301.0, 302.0, 303.0])
    assert node.input3D[0].get() == pytest.approx([301.0, 302.0, 303.0])


def test_operation_enum(modifier_manager, plus_minus_average_node):
    node = plus_minus_average_node

    node.operation.set(node.operation.SUM)
    modifier_manager.do_it_dg()

    assert node.operation.get() == node.operation.SUM
    assert node.op.get() == node.operation.SUM
    assert node.operation.name_by_index(node.operation.SUM) == "Sum"
    assert node.operation.index_by_name("Average") == node.operation.AVERAGE


def test_connect_disconnect_methods(
    modifier_manager,
    plus_minus_average_cls,
):
    src = plus_minus_average_cls.create(modifier_manager, name="src")
    dst = plus_minus_average_cls.create(modifier_manager, name="dst")

    src.output3Dx.connect(dst.input3D[0].input3Dx)
    modifier_manager.do_it_dg()

    assert dst.input3D[0].input3Dx.src_plug == "src.output3Dx"

    src.output3Dx.disconnect(dst.input3D[0].input3Dx)
    modifier_manager.do_it_dg()

    assert dst.input3D[0].input3Dx.src_plug is None
