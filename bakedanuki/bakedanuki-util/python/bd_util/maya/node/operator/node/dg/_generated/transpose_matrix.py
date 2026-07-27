# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField


class GeneratedTransposeMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "transposeMatrix"

    inputMatrix = MatrixField()
    imat = inputMatrix

    outputMatrix = MatrixField(writable=False)
    omat = outputMatrix
