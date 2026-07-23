# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class _GeneratedFloatMath(DG):
    __slots__ = ()

    NODE_TYPE = "floatMath"

    floatA = FloatField(default_value=1.0)
    fa = floatA

    floatB = FloatField(default_value=1.0)
    fb = floatB

    operation = LongField(default_value=0, min_value=0, max_value=8)
    cnd = operation

    outFloat = FloatField(default_value=0.0, writable=False)
    of = outFloat
