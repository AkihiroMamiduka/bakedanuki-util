# coding: utf-8
from .._core import DG
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class _GeneratedSin(DG):
    __slots__ = ()

    NODE_TYPE = "sin"

    input = DoubleAngleField(default_value=0.0)
    i = input

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
