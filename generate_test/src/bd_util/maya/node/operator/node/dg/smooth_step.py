# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class SmoothStep(DG):
    __slots__ = ()

    NODE_TYPE = "smoothStep"

    input = DoubleLinearField()
    i = input

    leftEdge = DoubleLinearField()
    le = leftEdge

    rightEdge = DoubleLinearField()
    re = rightEdge

    output = DoubleLinearField()
    o = output
