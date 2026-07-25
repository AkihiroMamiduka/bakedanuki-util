# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hierarchy_test_node4 import (
    KitAField,
    KitBField,
    PntsField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedHierarchyTestNode4(DG):
    __slots__ = ()

    NODE_TYPE = "hierarchyTestNode4"

    envelope = FloatField(default_value=0.0, long_name=".envelope", short_name=".en")

    pnts = PntsField(multi=True, default_value=(1.0, 1.0, 1.0), long_name=".pnts", short_name=".pt")

    kitA = KitAField()
    ka = kitA
    envelope = kitA.envelope
    pnts = kitA.pnts

    kitB = KitBField()
    kb = kitB
    envelope = kitB.envelope
    pnts = kitB.pnts
