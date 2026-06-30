# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class ApplyRelIntOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyRelIntOverride"

    enabled = BoolField()
    en = enabled

    out = LongField()
    o = out

    original = LongField()
    ori = original

    multiply = FloatField()
    mul = multiply

    offset = FloatField()
    ofs = offset
