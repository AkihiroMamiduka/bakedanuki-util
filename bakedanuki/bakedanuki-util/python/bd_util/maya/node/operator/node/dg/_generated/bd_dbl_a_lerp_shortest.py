# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblALerpShortest(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_LerpShortest"

    input1 = DoubleAngleField(default_value=0.0)
    i1 = input1

    input2 = DoubleAngleField(default_value=0.0)
    i2 = input2

    weight = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    w = weight

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
