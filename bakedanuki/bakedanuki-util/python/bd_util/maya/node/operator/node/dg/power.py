# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Power(DG):
    __slots__ = ()

    NODE_TYPE = "power"

    input = DoubleLinearField(default_value=0.0)
    i = input

    exponent = DoubleLinearField(default_value=2.0)
    e = exponent

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
