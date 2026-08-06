# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAMapRange(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_MapRange"

    input = DoubleAngleField(default_value=0.0)
    i = input

    srcMin = DoubleAngleField(default_value=0.0)
    smin = srcMin

    srcMax = DoubleAngleField(default_value=57.29577951308232)
    smax = srcMax

    dstMin = DoubleAngleField(default_value=0.0)
    dmin = dstMin

    dstMax = DoubleAngleField(default_value=57.29577951308232)
    dmax = dstMax

    clamp = BoolField(default_value=True)
    c = clamp

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
