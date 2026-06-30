# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class FloatComposite(DG):
    __slots__ = ()

    NODE_TYPE = "floatComposite"

    floatA = FloatField()
    _fa = floatA

    floatB = FloatField()
    _fb = floatB

    operation = ShortField()
    _op = operation

    factor = FloatField()
    _fx = factor

    outFloat = FloatField()
    of = outFloat
