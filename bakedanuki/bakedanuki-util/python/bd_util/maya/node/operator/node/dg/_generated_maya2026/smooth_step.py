# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedSmoothStep(DG):
    __slots__ = ()

    NODE_TYPE = "smoothStep"

    input = DoubleField(default_value=0.0)
    i = input

    leftEdge = DoubleField(default_value=0.0)
    le = leftEdge

    rightEdge = DoubleField(default_value=1.0)
    re = rightEdge

    output = DoubleField(default_value=0.0, writable=False)
    o = output
