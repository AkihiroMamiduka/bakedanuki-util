# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAMultiplyMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_MultiplyMulti"

    input = DoubleAngleField(default_value=0.0)
    i = input

    factor = DoubleField(multi=True, default_value=1.0)
    f = factor

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
