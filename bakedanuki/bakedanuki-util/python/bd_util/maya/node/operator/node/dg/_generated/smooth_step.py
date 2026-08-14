# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedSmoothStep(DG):
    __slots__ = ()

    NODE_TYPE = "smoothStep"

    input = DoubleLinearField(default_value=0.0)
    i = input

    leftEdge = DoubleLinearField(default_value=0.0)
    le = leftEdge

    rightEdge = DoubleLinearField(default_value=1.0)
    re = rightEdge

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
