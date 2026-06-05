# coding: utf-8

# self
from ..at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..at.double import DoubleField
from ..dt.matrix import DataMatrixField


class WtMatrixPlugOperator(CompoundPlugOperator["WtMatrixAttrOperator"]):
    __slots__ = ()

    matrixIn = DataMatrixField()
    m = matrixIn

    weightIn = DoubleField()
    w = weightIn


class WtMatrixAttrOperator(CompoundAttrOperator[WtMatrixPlugOperator]):
    __slots__ = ()

    matrixIn = DataMatrixField()
    m = matrixIn

    weightIn = DoubleField()
    w = weightIn


class WtMatrixField(CompoundField[WtMatrixAttrOperator, WtMatrixPlugOperator]):
    __slots__ = ()

    ATTR_CLS = WtMatrixAttrOperator
    PLUG_CLS = WtMatrixPlugOperator
