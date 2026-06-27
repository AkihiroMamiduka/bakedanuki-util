# coding: utf-8

# self
from ._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from ......std.at.numeric_scalar_range.double import DoubleField


class Double2PlugOperator(
    DoubleCompoundBasePlugOperator["Double2AttrOperator"]
):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()


class Double2AttrOperator(DoubleCompoundBaseAttrOperator[Double2PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double2"


class Double2Field(
    DoubleCompoundBaseField[Double2AttrOperator, Double2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Double2AttrOperator
    PLUG_CLS = Double2PlugOperator
