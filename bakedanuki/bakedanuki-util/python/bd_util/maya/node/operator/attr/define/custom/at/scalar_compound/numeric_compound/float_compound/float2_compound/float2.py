# coding: utf-8

# self
from ._base import (
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBaseField,
)
from .......std.at.scalar.numeric.range.float import FloatField


class Float2PlugOperator(
    Float2CompoundBasePlugOperator["Float2AttrOperator"]
):
    __slots__ = ()

    x = FloatField()
    y = FloatField()


class Float2AttrOperator(Float2CompoundBaseAttrOperator[Float2PlugOperator]):
    __slots__ = ()


class Float2Field(
    Float2CompoundBaseField[Float2AttrOperator, Float2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Float2AttrOperator
    PLUG_CLS = Float2PlugOperator
