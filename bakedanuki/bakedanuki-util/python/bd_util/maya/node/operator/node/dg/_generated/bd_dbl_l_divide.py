# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblLDivide(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL_Divide"

    input = DoubleLinearField(default_value=0.0)
    i = input

    factor = DoubleField(default_value=1.0)
    f = factor

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
