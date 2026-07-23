# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedApplyAbsStringOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsStringOverride"

    enabled = BoolField(default_value=True, readable=False)
    en = enabled

    out = DataStringField(writable=False)
    o = out

    original = DataStringField(readable=False)
    ori = original

    value = DataStringField(readable=False)
    val = value
