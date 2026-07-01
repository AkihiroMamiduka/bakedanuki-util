# coding: utf-8
from ._core import DG
from ...attr.define.std.at.matrix import MatrixField


class InverseMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "inverseMatrix"

    inputMatrix = MatrixField()
    imat = inputMatrix

    outputMatrix = MatrixField()
    omat = outputMatrix
