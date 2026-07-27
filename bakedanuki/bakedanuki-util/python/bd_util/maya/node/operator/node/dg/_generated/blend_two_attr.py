# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedBlendTwoAttr(DG):
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
