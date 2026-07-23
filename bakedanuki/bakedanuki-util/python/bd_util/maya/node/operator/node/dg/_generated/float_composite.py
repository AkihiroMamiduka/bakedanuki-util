# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField


class _GeneratedFloatComposite(DG):
    __slots__ = ()

    NODE_TYPE = "floatComposite"

    floatA = FloatField(default_value=1.0)
    fa = floatA

    floatB = FloatField(default_value=1.0)
    fb = floatB

    operation = ShortField(default_value=0, min_value=0, max_value=8)
    op = operation

    factor = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fx = factor

    outFloat = FloatField(default_value=0.0, writable=False)
    of = outFloat
