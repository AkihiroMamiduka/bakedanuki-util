# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class CurveNormalizerAngle(DG):
    __slots__ = ()

    NODE_TYPE = "curveNormalizerAngle"

    scalar = DoubleField()
    sc = scalar

    animInput = DoubleAngleField()
    ai = animInput

    output = DoubleAngleField()
    o = output
