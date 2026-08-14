# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAAverageMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_AverageMulti"

    input = DoubleAngleField(multi=True, default_value=0.0)
    i = input

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
