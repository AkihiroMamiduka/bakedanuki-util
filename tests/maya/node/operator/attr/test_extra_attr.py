# coding: utf-8
from __future__ import annotations

import pytest

from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr
from bd_util.maya.node.operator.node.dag.transform._core import Transform


pytestmark = pytest.mark.maya


class ExtraCompoundTransform(Transform):
    __slots__ = ()

    extraDouble4 = AddAttr.at.double4(
        default_value=[1.0, 2.0, 3.0, 4.0]
    )
    extraLimitedDouble4 = AddAttr.at.double4(
        default_value=[1.0, 2.0, 3.0, 4.0],
        min_value=[-1.0, -2.0, -3.0, -4.0],
        max_value=10.0,
        soft_min_value=0.0,
        soft_max_value=[1.0, 2.0, 3.0, 4.0],
    )
    extraQuat = AddAttr.at.quat()
    extraQuatCustom = AddAttr.at.quat(
        default_value=[0.1, 0.2, 0.3, 0.4]
    )
    extraFloat3 = AddAttr.at.float3()
    extraLong3 = AddAttr.at.long3()
    extraShort2 = AddAttr.at.short2()
    extraDoubleLinear2 = AddAttr.at.double_linear2(
        default_value=[1.0, 2.0]
    )
    extraDoubleLinear3 = AddAttr.at.double_linear3()
    extraDoubleAngle2 = AddAttr.at.double_angle2(
        default_value=[10.0, 20.0]
    )
    extraDoubleAngle3 = AddAttr.at.double_angle3()
    extraFloatLinear2 = AddAttr.at.float_linear2(
        default_value=[3.0, 4.0]
    )
    extraFloatAngle2 = AddAttr.at.float_angle2(
        default_value=[30.0, 40.0]
    )


@pytest.fixture
def extra_compound_node(modifier_manager):
    node = ExtraCompoundTransform.create(
        modifier_manager,
        name="extra_compound",
    )
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()
    return node


def test_double4_and_quat_defaults(extra_compound_node):
    node = extra_compound_node

    assert node.extraDouble4.get() == pytest.approx([1.0, 2.0, 3.0, 4.0])
    assert node.extraQuat.get() == pytest.approx([0.0, 0.0, 0.0, 1.0])
    assert node.extraQuatCustom.get() == pytest.approx([0.1, 0.2, 0.3, 0.4])
    assert node.extraDoubleLinear2.get() == pytest.approx([1.0, 2.0])
    assert node.extraDoubleAngle2.get() == pytest.approx([10.0, 20.0])
    assert node.extraFloatLinear2.get() == pytest.approx([3.0, 4.0])
    assert node.extraFloatAngle2.get() == pytest.approx([30.0, 40.0])


def test_compound_set_accepts_tuple_and_rejects_wrong_count(
    modifier_manager,
    extra_compound_node,
):
    node = extra_compound_node

    node.extraDouble4.set((4.0, 3.0, 2.0, 1.0))
    modifier_manager.do_it_dg()
    assert node.extraDouble4.get() == pytest.approx([4.0, 3.0, 2.0, 1.0])

    with pytest.raises(TypeError, match="Expected either set"):
        node.extraDouble4.set(9.0, 8.0)

    modifier_manager.do_it_dg()
    assert node.extraDouble4.get() == pytest.approx([4.0, 3.0, 2.0, 1.0])


def test_compound_set_direct_updates_immediately(extra_compound_node):
    node = extra_compound_node

    node.extraDouble4.set_direct(10.0, 20.0, 30.0, 40.0)
    assert node.extraDouble4.get() == pytest.approx(
        [10.0, 20.0, 30.0, 40.0]
    )

    node.extraFloat3.set_direct((1.25, 2.5, 3.75))
    assert node.extraFloat3.get() == pytest.approx([1.25, 2.5, 3.75])

    node.extraLong3.set_direct([1, 2, 3])
    assert node.extraLong3.get() == [1, 2, 3]

    node.extraShort2.set_direct(4, 5)
    assert node.extraShort2.get() == [4, 5]

    node.extraDoubleLinear3.set_direct(11.0, 12.0, 13.0)
    assert node.extraDoubleLinear3.get() == pytest.approx(
        [11.0, 12.0, 13.0]
    )
    node.extraDoubleLinear2.set_direct(21.0, 22.0)
    assert node.extraDoubleLinear2.get() == pytest.approx([21.0, 22.0])

    node.extraDoubleAngle3.set_direct(45.0, 90.0, 135.0)
    assert node.extraDoubleAngle3.get() == pytest.approx(
        [45.0, 90.0, 135.0]
    )
    node.extraDoubleAngle2.set_direct(15.0, 30.0)
    assert node.extraDoubleAngle2.get() == pytest.approx([15.0, 30.0])

    node.extraFloatLinear2.set_direct(31.0, 32.0)
    assert node.extraFloatLinear2.get() == pytest.approx([31.0, 32.0])

    node.extraFloatAngle2.set_direct(60.0, 120.0)
    assert node.extraFloatAngle2.get() == pytest.approx([60.0, 120.0])


def test_compound_set_direct_rejects_wrong_count(extra_compound_node):
    node = extra_compound_node

    node.extraDouble4.set_direct(1.0, 2.0, 3.0, 4.0)

    with pytest.raises(TypeError, match="Expected either set_direct"):
        node.extraDouble4.set_direct(9.0, 8.0)

    assert node.extraDouble4.get() == pytest.approx([1.0, 2.0, 3.0, 4.0])


def test_double4_and_quat_child_names(extra_compound_node, maya_cmds):
    node = extra_compound_node

    assert maya_cmds.attributeQuery(
        "extraDouble4",
        node=node.name,
        listChildren=True,
    ) == [
        "extraDouble4X",
        "extraDouble4Y",
        "extraDouble4Z",
        "extraDouble4W",
    ]
    assert maya_cmds.attributeQuery(
        "extraQuat",
        node=node.name,
        listChildren=True,
    ) == [
        "extraQuatX",
        "extraQuatY",
        "extraQuatZ",
        "extraQuatW",
    ]


def test_double4_and_quat_lookup(extra_compound_node):
    from bd_util.maya.node.operator.attr.lookup import lookup_attr_cls

    node = extra_compound_node

    assert lookup_attr_cls(node.name, "extraDouble4").__name__ == (
        "Double4AttrOperator"
    )
    assert lookup_attr_cls(node.name, "extraQuat").__name__ == (
        "Quat4AttrOperator"
    )


def test_same_compound_type_child_names_do_not_bleed(extra_compound_node):
    node = extra_compound_node

    assert (
        node.extraDouble4.x.plug_name
        == "extra_compound.extraDouble4.extraDouble4X"
    )
    assert (
        node.extraLimitedDouble4.x.plug_name
        == "extra_compound.extraLimitedDouble4.extraLimitedDouble4X"
    )
    assert (
        node.extraDouble4.x.plug_name
        == "extra_compound.extraDouble4.extraDouble4X"
    )


def _query_limit(maya_cmds, node, attr_name, flag):
    return maya_cmds.attributeQuery(
        attr_name,
        node=node.name,
        **{flag: True},
    )[0]


def test_double4_child_limits_from_add_attr(extra_compound_node, maya_cmds):
    node = extra_compound_node

    child_names = [
        "extraLimitedDouble4X",
        "extraLimitedDouble4Y",
        "extraLimitedDouble4Z",
        "extraLimitedDouble4W",
    ]

    assert [
        _query_limit(maya_cmds, node, child_name, "minimum")
        for child_name in child_names
    ] == pytest.approx([-1.0, -2.0, -3.0, -4.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "maximum")
        for child_name in child_names
    ] == pytest.approx([10.0, 10.0, 10.0, 10.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMin")
        for child_name in child_names
    ] == pytest.approx([0.0, 0.0, 0.0, 0.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMax")
        for child_name in child_names
    ] == pytest.approx([1.0, 2.0, 3.0, 4.0])


def test_double4_child_limits_can_be_changed(extra_compound_node, maya_cmds):
    node = extra_compound_node

    node.extraDouble4.set_min([-4.0, -3.0, -2.0, -1.0])
    node.extraDouble4.set_max(4.0)
    node.extraDouble4.set_soft_min([-2.0, -1.0, 0.0, 1.0])
    node.extraDouble4.set_soft_max(2.0)

    child_names = [
        "extraDouble4X",
        "extraDouble4Y",
        "extraDouble4Z",
        "extraDouble4W",
    ]

    assert [
        _query_limit(maya_cmds, node, child_name, "minimum")
        for child_name in child_names
    ] == pytest.approx([-4.0, -3.0, -2.0, -1.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "maximum")
        for child_name in child_names
    ] == pytest.approx([4.0, 4.0, 4.0, 4.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMin")
        for child_name in child_names
    ] == pytest.approx([-2.0, -1.0, 0.0, 1.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMax")
        for child_name in child_names
    ] == pytest.approx([2.0, 2.0, 2.0, 2.0])
