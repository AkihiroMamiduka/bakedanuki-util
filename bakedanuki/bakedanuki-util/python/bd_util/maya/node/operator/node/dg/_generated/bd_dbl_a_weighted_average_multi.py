# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_a_weighted_average_multi import (
    InputField,
)
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAWeightedAverageMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_WeightedAverageMulti"

    input = InputField(multi=True, default_value=(0.0, 0.0))
    i = input

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
