# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_double3_div_multi import (
    InputField,
    OutputField,
)


class GeneratedBdDouble3DivMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDouble3DivMulti"

    input = InputField(multi=True, default_value=(1.0, 1.0, 1.0))
    i = input

    output = OutputField(default_value=(1.0, 1.0, 1.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
