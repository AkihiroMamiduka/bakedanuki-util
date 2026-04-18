# coding: utf-8

# self
from .._core import Attr, Plug
from ..simple.double import DoubleAttr
from ..simple.matrix import MatrixAttr


class WtMatrixPlug(Plug["WtMatrixAttr"]):
    matrixIn = MatrixAttr()
    weightIn = DoubleAttr()


class WtMatrixAttr(Attr[WtMatrixPlug]):
    ATTR_TYPE: str = "TdataCompound"
    PLUG_CLS = WtMatrixPlug

    matrixIn = MatrixAttr()
    weightIn = DoubleAttr()
