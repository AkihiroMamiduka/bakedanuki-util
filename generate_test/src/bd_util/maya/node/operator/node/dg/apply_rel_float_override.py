# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ApplyRelFloatOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyRelFloatOverride"

    enabled = BoolField()
    en = enabled

    out = FloatField()
    o = out

    original = FloatField()
    ori = original

    multiply = FloatField()
    mul = multiply

    offset = FloatField()
    ofs = offset
