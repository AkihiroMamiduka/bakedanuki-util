# coding: utf-8

# self
from ._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from ......std.at.numeric_scalar_range.double import DoubleField


class Double3PlugOperator(
    DoubleCompoundBasePlugOperator["Double3AttrOperator"]
):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()


class Double3AttrOperator(DoubleCompoundBaseAttrOperator[Double3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3Field(
    DoubleCompoundBaseField[Double3AttrOperator, Double3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Double3AttrOperator
    PLUG_CLS = Double3PlugOperator
