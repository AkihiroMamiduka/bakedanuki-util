# coding: utf-8

# self
from ..at.compound import CompoundAttrOperator, CompoundPlugOperator
from ..at.double import DoubleAttrOperator
from ..dt.matrix import DataMatrixAttrOperator


class WtMatrixPlugOperator(CompoundPlugOperator["WtMatrixAttrOperator"]):
    matrixIn = DataMatrixAttrOperator()
    m = matrixIn

    weightIn = DoubleAttrOperator()
    w = weightIn


class WtMatrixAttrOperator(CompoundAttrOperator[WtMatrixPlugOperator]):
    PLUG_CLS = WtMatrixPlugOperator

    matrixIn = DataMatrixAttrOperator()
    m = matrixIn

    weightIn = DoubleAttrOperator()
    w = weightIn
