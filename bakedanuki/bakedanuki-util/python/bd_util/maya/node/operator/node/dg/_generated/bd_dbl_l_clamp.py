# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblLClamp(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL_Clamp"

    input = DoubleLinearField(default_value=0.0)
    i = input

    min = DoubleLinearField(default_value=0.0)
    mn = min

    max = DoubleLinearField(default_value=1.0)
    mx = max

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
