# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_weighted_sum_multi import InputField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblWeightedSumMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_WeightedSumMulti"

    input = InputField(multi=True, default_value=(0.0, 0.0))
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output
