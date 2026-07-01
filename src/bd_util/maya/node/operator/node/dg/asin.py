# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Asin(DG):
    __slots__ = ()

    NODE_TYPE = "asin"

    input = DoubleLinearField()
    i = input

    output = DoubleAngleField()
    o = output
