# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblANegate(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_Negate"

    input = DoubleAngleField(default_value=0.0)
    i = input

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
