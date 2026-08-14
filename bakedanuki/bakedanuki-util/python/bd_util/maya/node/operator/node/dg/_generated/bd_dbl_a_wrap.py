# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAWrap(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_Wrap"

    input = DoubleAngleField(default_value=0.0)
    i = input

    min = DoubleAngleField(default_value=-180.0)
    mn = min

    max = DoubleAngleField(default_value=180.0)
    mx = max

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
