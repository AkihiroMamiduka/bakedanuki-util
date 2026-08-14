# coding: utf-8

# self
from ._base import (
    Short2CompoundBasePlugOperator,
    Short2CompoundBaseAttrOperator,
    Short2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.short import ShortField


class Short2PlugOperator(Short2CompoundBasePlugOperator["Short2AttrOperator"]):
    __slots__ = ()

    x = ShortField()
    y = ShortField()


class Short2AttrOperator(Short2CompoundBaseAttrOperator[Short2PlugOperator]):
    __slots__ = ()


class Short2Field(
    Short2CompoundBaseField[Short2AttrOperator, Short2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Short2AttrOperator
    PLUG_CLS = Short2PlugOperator
