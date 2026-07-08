# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class InverseLerp(DG):
    __slots__ = ()

    NODE_TYPE = "inverseLerp"

    input1 = DoubleLinearField(default_value=0.0)
    i1 = input1

    input2 = DoubleLinearField(default_value=0.0)
    i2 = input2

    interpolation = DoubleLinearField(default_value=0.0)
    i = interpolation

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
