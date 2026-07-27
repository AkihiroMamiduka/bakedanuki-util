# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField


class GeneratedHoldMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "holdMatrix"

    inMatrix = MatrixField()
    i = inMatrix

    outMatrix = MatrixField()
    o = outMatrix
