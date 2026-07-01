# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Negate(DG):
    __slots__ = ()

    NODE_TYPE = "negate"

    input = DoubleLinearField()
    i = input

    output = DoubleLinearField()
    o = output
