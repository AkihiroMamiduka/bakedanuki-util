# coding: utf-8

# self
from ._base import (
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBaseField,
)
from .......std.at.scalar.numeric.range.float import FloatField


class Float3PlugOperator(
    Float3CompoundBasePlugOperator["Float3AttrOperator"]
):
    __slots__ = ()

    x = FloatField()
    y = FloatField()
    z = FloatField()


class Float3AttrOperator(Float3CompoundBaseAttrOperator[Float3PlugOperator]):
    __slots__ = ()


class Float3Field(
    Float3CompoundBaseField[Float3AttrOperator, Float3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Float3AttrOperator
    PLUG_CLS = Float3PlugOperator
