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
