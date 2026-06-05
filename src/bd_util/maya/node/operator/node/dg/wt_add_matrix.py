# coding: utf-8
from ._core import DG
from ...attr.dt.matrix import DataMatrixField
from ...attr.node_attr.wt_add_matrix import WtMatrixField


class WtAddMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "wtAddMatrix"

    wtMatrix = WtMatrixField(multi=True)
    i = wtMatrix

    matrixSum = DataMatrixField()
    o = matrixSum
