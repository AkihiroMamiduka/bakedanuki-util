# coding: utf-8

# self
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)
from .......std.at.numeric_scalar_range.long import LongField


class Long3PlugOperator(LongCompoundBasePlugOperator["Long3AttrOperator"]):
    __slots__ = ()

    x = LongField()
    y = LongField()
    z = LongField()


class Long3AttrOperator(LongCompoundBaseAttrOperator[Long3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "long3"


class Long3Field(LongCompoundBaseField[Long3AttrOperator, Long3PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Long3AttrOperator
    PLUG_CLS = Long3PlugOperator
