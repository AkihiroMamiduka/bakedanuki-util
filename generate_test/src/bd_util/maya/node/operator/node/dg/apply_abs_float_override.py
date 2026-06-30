# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ApplyAbsFloatOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsFloatOverride"

    enabled = BoolField()
    en = enabled

    out = FloatField()
    o = out

    original = FloatField()
    ori = original

    value = FloatField()
    val = value
