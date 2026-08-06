# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_divide_multi import (
    FactorField,
    InputField,
    OutputField,
)


class GeneratedBdDblL3DivideMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_DivideMulti"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    factor = FactorField(multi=True, default_value=(1.0, 1.0, 1.0))
    f = factor

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
