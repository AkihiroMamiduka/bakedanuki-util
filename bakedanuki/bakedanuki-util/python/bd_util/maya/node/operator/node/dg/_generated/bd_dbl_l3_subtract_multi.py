# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_subtract_multi import (
    InputField,
    OutputField,
)


class GeneratedBdDblL3SubtractMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_SubtractMulti"

    input = InputField(multi=True, default_value=(0.0, 0.0, 0.0))
    i = input

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
