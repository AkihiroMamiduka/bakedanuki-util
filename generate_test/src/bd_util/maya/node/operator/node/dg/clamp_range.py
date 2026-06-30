# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class ClampRange(DG):
    __slots__ = ()

    NODE_TYPE = "clampRange"

    input = DoubleLinearField()
    i = input

    minimum = DoubleLinearField()
    min = minimum

    maximum = DoubleLinearField()
    max = maximum

    output = DoubleLinearField()
    o = output
