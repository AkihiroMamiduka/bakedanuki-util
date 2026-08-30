# coding: utf-8

# self
from ...........value import Double4
from ._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)
from ...._round import RoundCompoundPlugOperatorMixin
from .......std.at.scalar.numeric.range.double import DoubleField


class Double4PlugOperator(
    RoundCompoundPlugOperatorMixin,
    Double4CompoundBasePlugOperator["Double4AttrOperator", Double4],
):
    __slots__ = ()

    VALUE_TYPE = Double4

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
