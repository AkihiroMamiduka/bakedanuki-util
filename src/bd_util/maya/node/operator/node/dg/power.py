# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Power(DG):
    __slots__ = ()

    NODE_TYPE = "power"

    input = DoubleLinearField()
    i = input

    exponent = DoubleLinearField()
    e = exponent

    output = DoubleLinearField()
    o = output
