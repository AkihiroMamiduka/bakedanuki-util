# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_clamp import (
    InputField,
    MaximumField,
    MinimumField,
    OutputField,
)


class GeneratedBdDbl3Clamp(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_Clamp"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    minimum = MinimumField(default_value=(0.0, 0.0, 0.0))
    min = minimum
    minimumX = minimum.minimumX
    minx = minimumX
    minimumY = minimum.minimumY
    miny = minimumY
    minimumZ = minimum.minimumZ
    minz = minimumZ

    maximum = MaximumField(default_value=(1.0, 1.0, 1.0))
    max = maximum
    maximumX = maximum.maximumX
    maxx = maximumX
    maximumY = maximum.maximumY
    maxy = maximumY
    maximumZ = maximum.maximumZ
    maxz = maximumZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
