# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_divide import (
    FactorField,
    InputField,
    OutputField,
)


class GeneratedBdDblL3Divide(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_Divide"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    factor = FactorField(default_value=(1.0, 1.0, 1.0))
    f = factor
    factorX = factor.factorX
    fx = factorX
    factorY = factor.factorY
    fy = factorY
    factorZ = factor.factorZ
    fz = factorZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
