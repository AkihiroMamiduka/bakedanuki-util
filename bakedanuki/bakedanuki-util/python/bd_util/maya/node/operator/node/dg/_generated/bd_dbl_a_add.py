# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAAdd(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_Add"

    input1 = DoubleAngleField(default_value=0.0)
    i1 = input1

    input2 = DoubleAngleField(default_value=0.0)
    i2 = input2

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
