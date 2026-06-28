# coding: utf-8

# self
from ._base import (
    FloatCompoundBasePlugOperator,
    FloatCompoundBaseAttrOperator,
    FloatCompoundBaseField,
)
from ......std.at.numeric_scalar_range.float import FloatField


class Float2PlugOperator(FloatCompoundBasePlugOperator["Float2AttrOperator"]):
    __slots__ = ()

    x = FloatField()
    y = FloatField()


class Float2AttrOperator(FloatCompoundBaseAttrOperator[Float2PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class Float2Field(
    FloatCompoundBaseField[Float2AttrOperator, Float2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Float2AttrOperator
    PLUG_CLS = Float2PlugOperator
