# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.unit_scalar.time import TimeField


class _GeneratedUnitToTimeConversion(DG):
    __slots__ = ()

    NODE_TYPE = "unitToTimeConversion"

    input = DoubleField(default_value=0.0)
    i = input

    output = TimeField(default_value=0.0, writable=False)
    o = output

    conversionFactor = DoubleField(default_value=1.0)
    cf = conversionFactor
