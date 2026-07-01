# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar.time import TimeField


class UnitToTimeConversion(DG):
    __slots__ = ()

    NODE_TYPE = "unitToTimeConversion"

    input = DoubleField()
    i = input

    output = TimeField()
    o = output

    conversionFactor = DoubleField()
    cf = conversionFactor
