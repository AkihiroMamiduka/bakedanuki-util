# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_weighted_sum_multi import (
    InputField,
    OutputField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblL3WeightedSumMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_WeightedSumMulti"

    input = InputField(multi=True)
    i = input

    valueX = DoubleLinearField()
    vx = valueX

    valueY = DoubleLinearField()
    vy = valueY

    valueZ = DoubleLinearField()
    vz = valueZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
