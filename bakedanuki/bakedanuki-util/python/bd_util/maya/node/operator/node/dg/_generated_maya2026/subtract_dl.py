# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedSubtractDL(DG):
    __slots__ = ()

    NODE_TYPE = "subtractDL"

    input1 = DoubleLinearField(default_value=0.0)
    i1 = input1

    input2 = DoubleLinearField(default_value=0.0)
    i2 = input2

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
