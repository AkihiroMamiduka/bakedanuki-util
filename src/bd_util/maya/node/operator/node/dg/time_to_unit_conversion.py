# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar.time import TimeField


class TimeToUnitConversion(DG):
    __slots__ = ()

    NODE_TYPE = "timeToUnitConversion"

    input = TimeField()
    i = input

    output = DoubleField()
    o = output

    conversionFactor = DoubleField()
    cf = conversionFactor
