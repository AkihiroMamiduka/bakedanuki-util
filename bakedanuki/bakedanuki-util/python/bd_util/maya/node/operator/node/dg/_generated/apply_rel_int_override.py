# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedApplyRelIntOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyRelIntOverride"

    enabled = BoolField(default_value=True, readable=False)
    en = enabled

    out = LongField(default_value=0, writable=False)
    o = out

    original = LongField(default_value=0, readable=False)
    ori = original

    multiply = FloatField(default_value=1.0, readable=False)
    mul = multiply

    offset = FloatField(default_value=0.0, readable=False)
    ofs = offset
