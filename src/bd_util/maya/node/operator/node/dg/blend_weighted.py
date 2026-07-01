# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class BlendWeighted(DG):
    __slots__ = ()

    NODE_TYPE = "blendWeighted"

    input = DoubleField(multi=True)
    i = input

    output = DoubleField()
    o = output

    current = LongField()
    c = current

    weight = FloatField(multi=True)
    w = weight
