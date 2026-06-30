# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatCondition(DG):
    __slots__ = ()

    NODE_TYPE = "floatCondition"

    floatA = FloatField()
    _fa = floatA

    floatB = FloatField()
    _fb = floatB

    condition = BoolField()
    _cnd = condition

    outFloat = FloatField()
    of = outFloat
