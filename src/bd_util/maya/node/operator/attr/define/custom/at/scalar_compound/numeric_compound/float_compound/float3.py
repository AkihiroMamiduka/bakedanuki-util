# coding: utf-8

# self
from ._base import (
    FloatCompoundBasePlugOperator,
    FloatCompoundBaseAttrOperator,
    FloatCompoundBaseField,
)
from ......std.at.numeric_scalar_range.float import FloatField


class Float3PlugOperator(FloatCompoundBasePlugOperator["Float3AttrOperator"]):
    __slots__ = ()

    x = FloatField()
    y = FloatField()
    z = FloatField()


class Float3AttrOperator(FloatCompoundBaseAttrOperator[Float3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class Float3Field(
    FloatCompoundBaseField[Float3AttrOperator, Float3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Float3AttrOperator
    PLUG_CLS = Float3PlugOperator
