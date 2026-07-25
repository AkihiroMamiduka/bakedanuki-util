# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedApplyAbsEnumOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsEnumOverride"

    enabled = BoolField(default_value=True, readable=False)
    en = enabled

    out = LongField(default_value=0, writable=False)
    o = out

    original = LongField(default_value=0, readable=False)
    ori = original

    value = LongField(default_value=0, readable=False)
    val = value
