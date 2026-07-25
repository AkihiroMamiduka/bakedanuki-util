# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField


class _GeneratedClampRange(DG):
    __slots__ = ()

    NODE_TYPE = "clampRange"

    input = DoubleLinearField(default_value=0.0)
    i = input

    minimum = DoubleLinearField(default_value=0.0)
    min = minimum

    maximum = DoubleLinearField(default_value=1.0)
    max = maximum

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
