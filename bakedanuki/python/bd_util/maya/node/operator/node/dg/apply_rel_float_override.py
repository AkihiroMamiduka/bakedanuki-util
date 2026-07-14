# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ApplyRelFloatOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyRelFloatOverride"

    enabled = BoolField(default_value=True, readable=False)
    en = enabled

    out = FloatField(default_value=0.0, writable=False)
    o = out

    original = FloatField(default_value=0.0, readable=False)
    ori = original

    multiply = FloatField(default_value=1.0, readable=False)
    mul = multiply

    offset = FloatField(default_value=0.0, readable=False)
    ofs = offset
