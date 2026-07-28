# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedPi(DG):
    __slots__ = ()

    NODE_TYPE = "pi"

    output = DoubleAngleField(default_value=180.0, writable=False)
    o = output
