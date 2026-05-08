# coding: utf-8

# self
from ..at.compound import CompoundAttr, CompoundPlug
from ..at.double import DoubleAttr
from ..dt.matrix import DataMatrixAttr


class WtMatrixPlug(CompoundPlug["WtMatrixAttr"]):
    matrixIn = DataMatrixAttr()
    m = matrixIn

    weightIn = DoubleAttr()
    w = weightIn


class WtMatrixAttr(CompoundAttr[WtMatrixPlug]):
    PLUG_CLS = WtMatrixPlug

    matrixIn = DataMatrixAttr()
    m = matrixIn

    weightIn = DoubleAttr()
    w = weightIn
