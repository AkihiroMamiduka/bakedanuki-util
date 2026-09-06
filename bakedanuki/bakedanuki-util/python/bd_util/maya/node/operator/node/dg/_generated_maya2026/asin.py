# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedAsin(DG):
    __slots__ = ()

    NODE_TYPE = "asin"

    input = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    i = input

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
