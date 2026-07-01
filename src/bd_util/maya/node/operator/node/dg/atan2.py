# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Atan2(DG):
    __slots__ = ()

    NODE_TYPE = "atan2"

    input1 = DoubleLinearField()
    i1 = input1

    input2 = DoubleLinearField()
    i2 = input2

    output = DoubleAngleField()
    o = output
