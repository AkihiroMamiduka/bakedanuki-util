# coding: utf-8
from ._core import DG
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class PassMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "passMatrix"

    inMatrix = MatrixField()
    i = inMatrix

    inScale = DoubleField()
    s = inScale

    outMatrix = MatrixField()
    o = outMatrix
