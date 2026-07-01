# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class ApplyAbsStringOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsStringOverride"

    enabled = BoolField()
    en = enabled

    out = DataStringField()
    o = out

    original = DataStringField()
    ori = original

    value = DataStringField()
    val = value
