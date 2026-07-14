# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hierarchy_test_node2 import (
    N1compoundField,
    N2compoundField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class HierarchyTestNode2(DG):
    __slots__ = ()

    NODE_TYPE = "hierarchyTestNode2"

    n1single = FloatField(default_value=0.0)
    n1s = n1single

    n1compound = N1compoundField()
    n1c = n1compound
    n1level1M = n1compound.n1level1M
    n1m1 = n1level1M
    n1level1S = n1compound.n1level1S
    n1s1 = n1level1S
    n1level1C = n1compound.n1level1C
    n1c1 = n1level1C

    n2single = FloatField(default_value=0.0)
    n2s = n2single

    n2compound = N2compoundField()
    n2c = n2compound
    n2level1M = n2compound.n2level1M
    n2m1 = n2level1M
    n2level1S = n2compound.n2level1S
    n2s1 = n2level1S
    n2level1C = n2compound.n2level1C
    n2c1 = n2level1C
