# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedFloatConstant(DG):
    __slots__ = ()

    NODE_TYPE = "floatConstant"

    inFloat = FloatField(default_value=1.0)
    f = inFloat

    outFloat = FloatField(default_value=0.0, writable=False)
    of = outFloat
