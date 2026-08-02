# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblClamp(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_Clamp"

    input = DoubleField(default_value=0.0)
    i = input

    min = DoubleField(default_value=0.0)
    mn = min

    max = DoubleField(default_value=1.0)
    mx = max

    output = DoubleField(default_value=0.0, writable=False)
    o = output
