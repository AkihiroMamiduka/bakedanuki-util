# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class ApplyAbsBoolOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbsBoolOverride"

    enabled = BoolField()
    en = enabled

    out = BoolField()
    o = out

    original = BoolField()
    ori = original

    value = BoolField()
    val = value
