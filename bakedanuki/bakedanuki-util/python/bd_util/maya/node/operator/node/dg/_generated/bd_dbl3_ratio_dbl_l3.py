# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_ratio_dbl_l3 import (
    BaseField,
    InputField,
    OutputField,
)


class GeneratedBdDbl3RatioDblL3(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_RatioDblL3"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    base = BaseField(default_value=(1.0, 1.0, 1.0))
    b = base
    baseX = base.baseX
    bx = baseX
    baseY = base.baseY
    by = baseY
    baseZ = base.baseZ
    bz = baseZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
