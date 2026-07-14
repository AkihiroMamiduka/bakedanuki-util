# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Multiply(DG):
    __slots__ = ()

    NODE_TYPE = "multiply"

    input = DoubleLinearField(multi=True, default_value=0.0)
    i = input

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
