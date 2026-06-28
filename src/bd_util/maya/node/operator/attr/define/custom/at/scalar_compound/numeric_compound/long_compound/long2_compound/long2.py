# coding: utf-8

# self
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)
from .......std.at.numeric_scalar_range.long import LongField


class Long2PlugOperator(LongCompoundBasePlugOperator["Long2AttrOperator"]):
    __slots__ = ()

    x = LongField()
    y = LongField()


class Long2AttrOperator(LongCompoundBaseAttrOperator[Long2PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "long2"


class Long2Field(LongCompoundBaseField[Long2AttrOperator, Long2PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Long2AttrOperator
    PLUG_CLS = Long2PlugOperator
