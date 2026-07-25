# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField


class _GeneratedCurveNormalizerLinear(DG):
    __slots__ = ()

    NODE_TYPE = "curveNormalizerLinear"

    scalar = DoubleField(default_value=1.0)
    sc = scalar

    animInput = DoubleLinearField(default_value=0.0)
    ai = animInput

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
