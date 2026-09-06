# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedAtan2DL(DG):
    __slots__ = ()

    NODE_TYPE = "atan2DL"

    input1 = DoubleLinearField(default_value=0.0)
    i1 = input1

    input2 = DoubleLinearField(default_value=0.0)
    i2 = input2

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
