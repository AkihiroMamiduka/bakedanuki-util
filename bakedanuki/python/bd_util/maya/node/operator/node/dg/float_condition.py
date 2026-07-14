# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatCondition(DG):
    __slots__ = ()

    NODE_TYPE = "floatCondition"

    floatA = FloatField(default_value=1.0)
    fa = floatA

    floatB = FloatField(default_value=1.0)
    fb = floatB

    condition = BoolField(default_value=False)
    cnd = condition

    outFloat = FloatField(default_value=0.0, writable=False)
    of = outFloat
