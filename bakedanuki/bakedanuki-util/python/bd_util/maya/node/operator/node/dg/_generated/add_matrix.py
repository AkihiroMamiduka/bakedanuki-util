# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField


class _GeneratedAddMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "addMatrix"

    matrixIn = MatrixField(multi=True)
    i = matrixIn

    matrixSum = MatrixField(writable=False)
    o = matrixSum
