# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class GreaterThan(DG):
    __slots__ = ()

    NODE_TYPE = "greaterThan"

    input1 = DoubleLinearField()
    i1 = input1

    input2 = DoubleLinearField()
    i2 = input2

    output = BoolField()
    o = output
