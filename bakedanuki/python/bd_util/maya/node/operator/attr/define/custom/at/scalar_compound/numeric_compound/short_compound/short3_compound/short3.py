# coding: utf-8

# self
from ._base import (
    Short3CompoundBasePlugOperator,
    Short3CompoundBaseAttrOperator,
    Short3CompoundBaseField,
)
from .......std.at.numeric_scalar_range.short import ShortField


class Short3PlugOperator(
    Short3CompoundBasePlugOperator["Short3AttrOperator"]
):
    __slots__ = ()

    x = ShortField()
    y = ShortField()
    z = ShortField()


class Short3AttrOperator(
    Short3CompoundBaseAttrOperator[Short3PlugOperator]
):
    __slots__ = ()


class Short3Field(
    Short3CompoundBaseField[Short3AttrOperator, Short3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Short3AttrOperator
    PLUG_CLS = Short3PlugOperator
