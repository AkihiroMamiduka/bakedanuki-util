# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedBdDblAValue(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblA_Value"

    value = DoubleAngleField(default_value=0.0)
    v = value
