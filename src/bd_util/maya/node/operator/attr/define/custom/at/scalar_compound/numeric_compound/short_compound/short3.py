# coding: utf-8

# self
from ._base import (
    ShortCompoundBasePlugOperator,
    ShortCompoundBaseAttrOperator,
    ShortCompoundBaseField,
)
from ......std.at.numeric_scalar_range.short import ShortField


class Short3PlugOperator(ShortCompoundBasePlugOperator["Short3AttrOperator"]):
    __slots__ = ()

    x = ShortField()
    y = ShortField()
    z = ShortField()


class Short3AttrOperator(ShortCompoundBaseAttrOperator[Short3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "short3"


class Short3Field(
    ShortCompoundBaseField[Short3AttrOperator, Short3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Short3AttrOperator
    PLUG_CLS = Short3PlugOperator
