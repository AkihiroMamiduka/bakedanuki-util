# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class CurveNormalizerAngle(DG):
    __slots__ = ()

    NODE_TYPE = "curveNormalizerAngle"

    scalar = DoubleField(default_value=1.0)
    sc = scalar

    animInput = DoubleAngleField(default_value=0.0)
    ai = animInput

    output = DoubleAngleField(default_value=0.0, writable=False)
    o = output
