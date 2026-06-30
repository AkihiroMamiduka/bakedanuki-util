# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatMask(DG):
    __slots__ = ()

    NODE_TYPE = "floatMask"

    inFloat = FloatField()
    _f = inFloat

    mask = FloatField()
    _m = mask

    outFloat = FloatField()
    of = outFloat
