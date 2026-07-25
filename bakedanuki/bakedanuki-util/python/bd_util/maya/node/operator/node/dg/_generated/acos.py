# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField


class _GeneratedAcos(DG):
    __slots__ = ()

    NODE_TYPE = "acos"

    input = DoubleLinearField(default_value=0.0, min_value=-1.0, max_value=1.0)
    i = input

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
