# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class FloatMath(DG):
    __slots__ = ()

    NODE_TYPE = "floatMath"

    floatA = FloatField()
    _fa = floatA

    floatB = FloatField()
    _fb = floatB

    operation = LongField()
    _cnd = operation

    outFloat = FloatField()
    of = outFloat
