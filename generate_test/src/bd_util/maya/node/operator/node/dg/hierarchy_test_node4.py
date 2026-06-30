# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hierarchy_test_node4 import (
    .pntsField,
    KitAField,
    KitBField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class HierarchyTestNode4(DG):
    __slots__ = ()

    NODE_TYPE = "hierarchyTestNode4"

    .envelope = FloatField()
    .en = .envelope

    .pnts = .pntsField(multi=True)
    .pt = .pnts

    kitA = KitAField()
    ka = kitA
    envelope = kitA.envelope
    ka.env = envelope
    pnts = kitA.pnts
    ka.pt = pnts

    kitB = KitBField()
    kb = kitB
    envelope = kitB.envelope
    kb.env = envelope
    pnts = kitB.pnts
    kb.pt = pnts
