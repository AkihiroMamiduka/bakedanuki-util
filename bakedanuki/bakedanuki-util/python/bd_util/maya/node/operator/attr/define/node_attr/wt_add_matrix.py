# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.dt.matrix import DataMatrixField


class WtMatrixPlugOperator(
    CompoundPlugOperator["WtMatrixAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("matrixIn", "m"),
        ("weightIn", "w"),
    )

    matrixIn = DataMatrixField()
    m = matrixIn

    weightIn = DoubleField(default_value=0.0)
    w = weightIn


class WtMatrixAttrOperator(
    CompoundAttrOperator[WtMatrixPlugOperator]
):
    __slots__ = ()

    matrixIn = DataMatrixField()
    m = matrixIn

    weightIn = DoubleField(default_value=0.0)
    w = weightIn


class WtMatrixField(
    CompoundField[WtMatrixAttrOperator, WtMatrixPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WtMatrixAttrOperator
    PLUG_CLS = WtMatrixPlugOperator
