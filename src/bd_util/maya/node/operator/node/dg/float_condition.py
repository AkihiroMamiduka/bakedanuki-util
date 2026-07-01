# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatCondition(DG):
    __slots__ = ()

    NODE_TYPE = "floatCondition"

    floatA = FloatField()
    fa = floatA

    floatB = FloatField()
    fb = floatB

    condition = BoolField()
    cnd = condition

    outFloat = FloatField()
    of = outFloat
