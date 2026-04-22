# coding: utf-8
from .._core import Node
from ...attr.at.matrix import MatrixAttr
from ...attr.node_attr.wt_add_matrix import WtMatrixAttr


class WtAddMatrix(Node):
    NODE_TYPE = "wtAddMatrix"

    wtMatrix = WtMatrixAttr(multi=True)
    i = wtMatrix
    matrixSum = MatrixAttr()
    o = matrixSum
