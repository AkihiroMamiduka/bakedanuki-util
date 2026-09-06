# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedSin(DG):
    __slots__ = ()

    NODE_TYPE = "sin"

    input = DoubleAngleField(default_value=0.0)
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output
