# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hierarchy_test_node1 import N1compoundField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedHierarchyTestNode1(DG):
    __slots__ = ()

    NODE_TYPE = "hierarchyTestNode1"

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
