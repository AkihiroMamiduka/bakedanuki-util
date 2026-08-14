# coding: utf-8

# self
from ._base import (
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseAttrOperator,
    Double2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.double import DoubleField


class Double2PlugOperator(
    Double2CompoundBasePlugOperator["Double2AttrOperator"]
):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()


class Double2AttrOperator(
    Double2CompoundBaseAttrOperator[Double2PlugOperator]
):
    __slots__ = ()


class Double2Field(
    Double2CompoundBaseField[Double2AttrOperator, Double2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Double2AttrOperator
    PLUG_CLS = Double2PlugOperator
