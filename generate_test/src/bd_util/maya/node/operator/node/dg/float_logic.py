# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class FloatLogic(DG):
    __slots__ = ()

    NODE_TYPE = "floatLogic"

    floatA = FloatField()
    _aa = floatA

    floatB = FloatField()
    _ab = floatB

    operation = LongField()
    _op = operation

    outBool = BoolField()
    ob = outBool
