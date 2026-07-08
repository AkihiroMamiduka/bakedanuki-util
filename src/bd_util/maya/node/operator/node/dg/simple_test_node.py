# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.simple_test_node import CompoundValueField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SimpleTestNode(DG):
    __slots__ = ()

    NODE_TYPE = "simpleTestNode"

    single = FloatField(default_value=0.0)
    s = single

    compound = CompoundValueField(default_value=(0.0, 0.0, 0.0))
    c = compound
    level1S1 = compound.level1S1
    l1s1 = level1S1
    level1S2 = compound.level1S2
    l1s2 = level1S2
    level1S3 = compound.level1S3
    l1s3 = level1S3

    flag = BoolField(default_value=False)
    f = flag
