# coding: utf-8
from ._core import DG
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class UnitConversion(DG):
    __slots__ = ()

    NODE_TYPE = "unitConversion"

    input = GenericField()
    i = input

    output = GenericField()
    o = output

    conversionFactor = DoubleField()
    cf = conversionFactor
