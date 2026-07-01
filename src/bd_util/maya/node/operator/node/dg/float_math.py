# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class FloatMath(DG):
    __slots__ = ()

    NODE_TYPE = "floatMath"

    floatA = FloatField()
    fa = floatA

    floatB = FloatField()
    fb = floatB

    operation = LongField()
    cnd = operation

    outFloat = FloatField()
    of = outFloat
