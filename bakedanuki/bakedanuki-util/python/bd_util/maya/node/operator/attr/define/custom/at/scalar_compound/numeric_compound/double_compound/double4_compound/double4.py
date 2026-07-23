# coding: utf-8

# self
from ._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)
from .......std.at.numeric_scalar_range.double import DoubleField


class Double4PlugOperator(
    Double4CompoundBasePlugOperator["Double4AttrOperator"]
):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()
    w = DoubleField()


class Double4AttrOperator(
    Double4CompoundBaseAttrOperator[Double4PlugOperator]
):
    __slots__ = ()


class Double4Field(
    Double4CompoundBaseField[Double4AttrOperator, Double4PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Double4AttrOperator
    PLUG_CLS = Double4PlugOperator
