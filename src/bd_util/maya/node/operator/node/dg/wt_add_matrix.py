# coding: utf-8
from ._core import DG
from ...attr.dt.matrix import DataMatrixAttr
from ...attr.node_attr.wt_add_matrix import WtMatrixAttr


class WtAddMatrix(DG):
    NODE_TYPE = "wtAddMatrix"

    wtMatrix = WtMatrixAttr(multi=True)
    i = wtMatrix

    matrixSum = DataMatrixAttr()
    o = matrixSum
