# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hierarchy_test_node4 import (
    KitAField,
    KitBField,
    PntsField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class HierarchyTestNode4(DG):
    __slots__ = ()

    NODE_TYPE = "hierarchyTestNode4"

    envelope = FloatField(long_name=".envelope", short_name=".en")

    pnts = PntsField(multi=True, long_name=".pnts", short_name=".pt")

    kitA = KitAField()
    ka = kitA
    envelope = kitA.envelope
    pnts = kitA.pnts

    kitB = KitBField()
    kb = kitB
    envelope = kitB.envelope
    pnts = kitB.pnts
