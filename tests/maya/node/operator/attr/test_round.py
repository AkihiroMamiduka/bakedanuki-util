# coding: utf-8
from __future__ import annotations

import builtins

import pytest

import bd_util as bdu
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr
from bd_util.maya.node.operator.node.dag.transform._core import Transform

pytestmark = pytest.mark.maya


class RoundTransform(Transform):
    __slots__ = ()

    extraFloat = AddAttr.at.float(default_value=0.0)
    extraDouble = AddAttr.at.double(default_value=0.0)
    extraFloatAngle = AddAttr.at.float_angle(default_value=0.0)
    extraFloatLinear = AddAttr.at.float_linear(default_value=0.0)
    extraTime = AddAttr.at.time(default_value=0.0)
    extraFloat3 = AddAttr.at.float3(default_value=(0.0, 0.0, 0.0))
    extraDouble4 = AddAttr.at.double4(default_value=(0.0, 0.0, 0.0, 0.0))
    extraFloatAngle3 = AddAttr.at.float_angle3(default_value=(0.0, 0.0, 0.0))


@pytest.fixture
def round_node(modifier_manager):
    node = RoundTransform.create(modifier_manager, name="round_test")
    modifier_manager.do_it_dg()
    return node


def _get_plug(node, plug_path):
    plug = node
    for name in plug_path.split("."):
        plug = getattr(plug, name)
    return plug


@pytest.mark.parametrize(
    ("plug_path", "value", "ndigits"),
    (
        ("extraFloat", 1.23456, 3),
        ("extraDouble", -1.23456, 3),
        ("rotate.rotateX", 42.55555, 2),
        ("translate.translateX", 12.34567, 3),
        ("extraFloatAngle", -32.55555, 2),
        ("extraFloatLinear", 7.65432, 3),
        ("extraTime", 18.55555, 2),
        ("extraDouble", 1234.5, -2),
        ("extraDouble", 2.5, 0),
        ("extraDouble", 3.5, 0),
    ),
)
def test_scalar_round_uses_python_round(
    modifier_manager,
    round_node,
    plug_path,
    value,
    ndigits,
):
    plug = _get_plug(round_node, plug_path)
    plug.set(value)
    modifier_manager.do_it_dg()

    plug.round(ndigits)
    modifier_manager.do_it_dg()

    assert plug.get() == pytest.approx(builtins.round(value, ndigits))


@pytest.mark.parametrize(
    ("plug_path", "values", "ndigits"),
    (
        ("scale", (1.23456, -2.34567, 3.45678), 3),
        ("translate", (12.34567, -23.45678, 34.56789), 2),
        ("rotate", (42.55555, -84.44444, 126.33333), 2),
        ("extraFloat3", (1.23456, -2.34567, 3.45678), 3),
        ("extraDouble4", (1.23456, -2.34567, 3.45678, -4.56789), 2),
        ("extraFloatAngle3", (32.55555, -64.44444, 96.33333), 2),
    ),
)
def test_compound_round_preserves_value_type(
    modifier_manager,
    round_node,
    plug_path,
    values,
    ndigits,
):
    plug = _get_plug(round_node, plug_path)
    plug.set(values)
    modifier_manager.do_it_dg()
    value_type = type(plug.get())

    plug.round(ndigits)
    modifier_manager.do_it_dg()

    rounded_value = plug.get()
    assert type(rounded_value) is value_type
    assert rounded_value.as_tuple() == pytest.approx(
        tuple(builtins.round(value, ndigits) for value in values)
    )


def test_round_queues_modifier_and_supports_undo_redo(
    modifier_manager,
    maya_cmds,
):
    original_value = 1.23456
    rounded_value = builtins.round(original_value, 3)
    node_name = maya_cmds.createNode("transform", name="round_undo_test")
    maya_cmds.setAttr(f"{node_name}.translateX", original_value)
    node = bdu.Nodes(modifier_manager=modifier_manager).existing.transform(
        node_name
    )
    plug = node.translate.translateX

    plug.round(3)
    assert plug.get() == pytest.approx(original_value)

    modifier_manager.do_it_dg()
    assert plug.get() == pytest.approx(rounded_value)

    modifier_manager.undo_it()
    assert plug.get() == pytest.approx(original_value)

    modifier_manager.redo_it()
    assert plug.get() == pytest.approx(rounded_value)
