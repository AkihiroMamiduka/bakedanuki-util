# coding: utf-8

# self
from ._base import (
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseAttrOperator,
    Long3CompoundBaseField,
)
from .......std.at.scalar.numeric.range.long import LongField


class Long3PlugOperator(Long3CompoundBasePlugOperator["Long3AttrOperator"]):
    __slots__ = ()

    x = LongField()
    y = LongField()
    z = LongField()


class Long3AttrOperator(Long3CompoundBaseAttrOperator[Long3PlugOperator]):
    __slots__ = ()


class Long3Field(
    Long3CompoundBaseField[Long3AttrOperator, Long3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Long3AttrOperator
    PLUG_CLS = Long3PlugOperator
