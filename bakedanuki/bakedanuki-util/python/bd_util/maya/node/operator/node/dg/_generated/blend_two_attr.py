# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class _GeneratedBlendTwoAttr(DG):
    __slots__ = ()

    NODE_TYPE = "blendTwoAttr"

    input = DoubleField(multi=True, default_value=0.0)
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output

    current = LongField(default_value=0)
    c = current

    attributesBlender = FloatField(default_value=0.0)
    ab = attributesBlender
