# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class ApplyAbsIntOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsIntOverride"

    enabled = BoolField()
    en = enabled

    out = LongField()
    o = out

    original = LongField()
    ori = original

    value = LongField()
    val = value
