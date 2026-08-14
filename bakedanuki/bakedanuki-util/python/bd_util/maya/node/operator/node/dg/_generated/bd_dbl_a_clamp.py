# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAClamp(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_Clamp"

    input = DoubleAngleField(default_value=0.0)
    i = input

    min = DoubleAngleField(default_value=0.0)
    mn = min

    max = DoubleAngleField(default_value=57.29577951308232)
    mx = max

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
