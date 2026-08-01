# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_sub_multi import (
    InputField,
    OutputField,
)


class GeneratedBdDbl3SubMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3SubMulti"

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
