# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hierarchy_test_node3 import (
    N1compoundField,
    N2compoundField,
    N3compoundField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedHierarchyTestNode3(DG):
    __slots__ = ()

    NODE_TYPE = "hierarchyTestNode3"

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

    n3single = FloatField(default_value=0.0)
    n3s = n3single

    n3compound = N3compoundField()
    n3c = n3compound
    n3level1M = n3compound.n3level1M
    n3m1 = n3level1M
    n3level1S = n3compound.n3level1S
    n3s1 = n3level1S
    n3level1C = n3compound.n3level1C
    n3c1 = n3level1C
