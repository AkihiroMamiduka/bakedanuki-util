# coding: utf-8
from .._core import DG
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedUnitConversion(DG):
    __slots__ = ()

    NODE_TYPE = "unitConversion"

    input = GenericField()
    i = input

    output = GenericField(writable=False)
    o = output

    conversionFactor = DoubleField(default_value=1.0)
    cf = conversionFactor
