# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField


class _GeneratedApplyAbsBoolOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsBoolOverride"

    enabled = BoolField(default_value=True, readable=False)
    en = enabled

    out = BoolField(default_value=False, writable=False)
    o = out

    original = BoolField(default_value=False, readable=False)
    ori = original

    value = BoolField(default_value=False, readable=False)
    val = value
