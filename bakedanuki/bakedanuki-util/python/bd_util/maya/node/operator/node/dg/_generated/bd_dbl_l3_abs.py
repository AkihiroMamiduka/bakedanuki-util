# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_abs import (
    InputField,
    OutputField,
)


class GeneratedBdDblL3Abs(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_Abs"

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
