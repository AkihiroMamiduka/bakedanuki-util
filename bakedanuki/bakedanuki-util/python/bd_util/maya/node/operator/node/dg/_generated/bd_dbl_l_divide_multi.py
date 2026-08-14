# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblLDivideMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL_DivideMulti"

    input = DoubleLinearField(default_value=0.0)
    i = input

    factor = DoubleField(multi=True, default_value=1.0)
    f = factor

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
