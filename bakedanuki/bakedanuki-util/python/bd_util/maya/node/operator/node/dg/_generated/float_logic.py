# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class _GeneratedFloatLogic(DG):
    __slots__ = ()

    NODE_TYPE = "floatLogic"

    floatA = FloatField(default_value=1.0)
    aa = floatA

    floatB = FloatField(default_value=1.0)
    ab = floatB

    operation = LongField(default_value=0)
    op = operation

    outBool = BoolField(default_value=False, writable=False)
    ob = outBool
