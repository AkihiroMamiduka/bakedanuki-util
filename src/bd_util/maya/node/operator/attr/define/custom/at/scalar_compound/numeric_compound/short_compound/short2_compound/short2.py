# coding: utf-8

# self
from .._base import (
    ShortCompoundBasePlugOperator,
    ShortCompoundBaseAttrOperator,
    ShortCompoundBaseField,
)
from .......std.at.numeric_scalar_range.short import ShortField


class Short2PlugOperator(ShortCompoundBasePlugOperator["Short2AttrOperator"]):
    __slots__ = ()

    x = ShortField()
    y = ShortField()


class Short2AttrOperator(ShortCompoundBaseAttrOperator[Short2PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "short2"


class Short2Field(
    ShortCompoundBaseField[Short2AttrOperator, Short2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Short2AttrOperator
    PLUG_CLS = Short2PlugOperator
