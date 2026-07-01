# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatConstant(DG):
    __slots__ = ()

    NODE_TYPE = "floatConstant"

    inFloat = FloatField()
    f = inFloat

    outFloat = FloatField()
    of = outFloat
