# coding: utf-8
from ._core import DG
from ...attr.dt.matrix import DataMatrixAttrOperator
from ...attr.node_attr.wt_add_matrix import WtMatrixAttrOperator


class WtAddMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "wtAddMatrix"

    wtMatrix = WtMatrixAttrOperator(multi=True)
    i = wtMatrix

    matrixSum = DataMatrixAttrOperator()
    o = matrixSum
