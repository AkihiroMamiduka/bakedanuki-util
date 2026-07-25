# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class _GeneratedPassMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "passMatrix"

    inMatrix = MatrixField()
    i = inMatrix

    inScale = DoubleField(default_value=2.0)
    s = inScale

    outMatrix = MatrixField(writable=False)
    o = outMatrix
