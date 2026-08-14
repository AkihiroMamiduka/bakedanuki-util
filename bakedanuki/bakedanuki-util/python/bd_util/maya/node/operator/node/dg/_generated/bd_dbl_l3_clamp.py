# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_clamp import (
    InputField,
    MaxField,
    MinField,
    OutputField,
)


class GeneratedBdDblL3Clamp(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_Clamp"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    min = MinField(default_value=(0.0, 0.0, 0.0))
    mn = min
    minX = min.minX
    mnx = minX
    minY = min.minY
    mny = minY
    minZ = min.minZ
    mnz = minZ

    max = MaxField(default_value=(1.0, 1.0, 1.0))
    mx = max
    maxX = max.maxX
    mxx = maxX
    maxY = max.maxY
    mxy = maxY
    maxZ = max.maxZ
    mxz = maxZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
