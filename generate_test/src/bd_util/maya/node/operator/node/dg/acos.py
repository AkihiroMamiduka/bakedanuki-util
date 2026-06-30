# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Acos(DG):
    __slots__ = ()

    NODE_TYPE = "acos"

    input = DoubleLinearField()
    i = input

    output = DoubleAngleField()
    o = output
