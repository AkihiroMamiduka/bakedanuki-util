# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class Pi(DG):
    __slots__ = ()

    NODE_TYPE = "pi"

    output = DoubleAngleField(default_value=180.0, writable=False)
    o = output
