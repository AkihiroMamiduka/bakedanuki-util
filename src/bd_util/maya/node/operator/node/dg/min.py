# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Min(DG):
    __slots__ = ()

    NODE_TYPE = "min"

    input = DoubleLinearField(multi=True)
    i = input

    output = DoubleLinearField()
    o = output
