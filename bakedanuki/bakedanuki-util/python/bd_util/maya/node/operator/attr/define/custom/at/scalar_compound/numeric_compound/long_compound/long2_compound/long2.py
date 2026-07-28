# coding: utf-8

# self
from ._base import (
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseAttrOperator,
    Long2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.long import LongField


class Long2PlugOperator(Long2CompoundBasePlugOperator["Long2AttrOperator"]):
    __slots__ = ()

    x = LongField()
    y = LongField()


class Long2AttrOperator(Long2CompoundBaseAttrOperator[Long2PlugOperator]):
    __slots__ = ()


class Long2Field(Long2CompoundBaseField[Long2AttrOperator, Long2PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Long2AttrOperator
    PLUG_CLS = Long2PlugOperator
