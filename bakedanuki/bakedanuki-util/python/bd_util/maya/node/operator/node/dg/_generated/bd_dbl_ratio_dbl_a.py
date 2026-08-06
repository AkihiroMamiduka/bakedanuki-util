# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblRatioDblA(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_RatioDblA"

    input = DoubleAngleField(default_value=0.0)
    i = input

    base = DoubleAngleField(default_value=360.0)
    b = base

    output = DoubleField(default_value=0.0, writable=False)
    o = output
