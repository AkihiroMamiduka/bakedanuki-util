# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.wt_add_matrix import WtMatrixField
from ....attr.define.std.dt.matrix import DataMatrixField


class _GeneratedWtAddMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "wtAddMatrix"

    wtMatrix = WtMatrixField(multi=True)
    i = wtMatrix

    matrixSum = DataMatrixField(writable=False)
    o = matrixSum
