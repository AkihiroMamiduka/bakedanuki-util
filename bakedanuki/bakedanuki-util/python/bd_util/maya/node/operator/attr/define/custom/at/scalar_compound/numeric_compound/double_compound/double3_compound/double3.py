# coding: utf-8

# self
from ._base import (
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBaseField,
)
from .......std.at.numeric_scalar_range.double import DoubleField


class Double3PlugOperator(
    Double3CompoundBasePlugOperator["Double3AttrOperator"]
):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()


class Double3AttrOperator(
    Double3CompoundBaseAttrOperator[Double3PlugOperator]
):
    __slots__ = ()


class Double3Field(
    Double3CompoundBaseField[Double3AttrOperator, Double3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Double3AttrOperator
    PLUG_CLS = Double3PlugOperator
