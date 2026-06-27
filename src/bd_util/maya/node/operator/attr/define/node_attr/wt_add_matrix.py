# coding: utf-8

# self
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.dt.matrix import DataMatrixField


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
