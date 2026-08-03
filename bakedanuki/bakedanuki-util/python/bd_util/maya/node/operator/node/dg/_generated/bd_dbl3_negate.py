# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_negate import (
    InputField,
    OutputField,
)


class GeneratedBdDbl3Negate(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_Negate"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
