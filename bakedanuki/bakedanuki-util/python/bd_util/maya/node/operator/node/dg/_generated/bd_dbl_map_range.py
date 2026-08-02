# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblMapRange(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_MapRange"

    input = DoubleField(default_value=0.0)
    i = input

    srcMin = DoubleField(default_value=0.0)
    smin = srcMin

    srcMax = DoubleField(default_value=1.0)
    smax = srcMax

    dstMin = DoubleField(default_value=0.0)
    dmin = dstMin

    dstMax = DoubleField(default_value=1.0)
    dmax = dstMax

    clamp = BoolField(default_value=True)
    c = clamp

    output = DoubleField(default_value=0.0, writable=False)
    o = output
