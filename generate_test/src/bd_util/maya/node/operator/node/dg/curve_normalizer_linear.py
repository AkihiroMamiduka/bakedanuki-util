# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class CurveNormalizerLinear(DG):
    __slots__ = ()

    NODE_TYPE = "curveNormalizerLinear"

    scalar = DoubleField()
    sc = scalar

    animInput = DoubleLinearField()
    ai = animInput

    output = DoubleLinearField()
    o = output
