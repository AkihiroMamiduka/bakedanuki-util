# coding: utf-8

# self
from .._core import Attr, Plug
from ..at.double import DoubleAttr
from ..at.matrix import MatrixAttr


class WtMatrixPlug(Plug["WtMatrixAttr"]):
    matrixIn = MatrixAttr()
    m = matrixIn

    weightIn = DoubleAttr()
    w = weightIn


class WtMatrixAttr(Attr[WtMatrixPlug]):
    ATTR_TYPE: str = "TdataCompound"
    PLUG_CLS = WtMatrixPlug

    matrixIn = MatrixAttr()
    m = matrixIn

    weightIn = DoubleAttr()
    w = weightIn
