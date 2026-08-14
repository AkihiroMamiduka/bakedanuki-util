# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblLMapRange(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL_MapRange"

    input = DoubleLinearField(default_value=0.0)
    i = input

    srcMin = DoubleLinearField(default_value=0.0)
    smin = srcMin

    srcMax = DoubleLinearField(default_value=1.0)
    smax = srcMax

    dstMin = DoubleLinearField(default_value=0.0)
    dmin = dstMin

    dstMax = DoubleLinearField(default_value=1.0)
    dmax = dstMax

    clamp = BoolField(default_value=True)
    c = clamp

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
