# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.time import TimeField


class GeneratedUnitToTimeConversion(DG):
    __slots__ = ()

    NODE_TYPE = "unitToTimeConversion"

    input = DoubleField(default_value=0.0)
    i = input

    output = TimeField(default_value=0.0, writable=False)
    o = output

    conversionFactor = DoubleField(default_value=1.0)
    cf = conversionFactor
