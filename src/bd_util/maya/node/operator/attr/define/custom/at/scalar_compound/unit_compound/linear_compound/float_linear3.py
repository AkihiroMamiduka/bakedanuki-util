# coding: utf-8


# self
from ._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

from ......std.at.unit_scalar_range.float_linear import FloatLinearField


class FloatLinear3PlugOperator(
    LinearCompoundBasePlugOperator["FloatLinear3AttrOperator"]
):
    __slots__ = ()

    x = FloatLinearField()
    y = FloatLinearField()
    z = FloatLinearField()


class FloatLinear3AttrOperator(
    LinearCompoundBaseAttrOperator[FloatLinear3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatLinear3Field(
    LinearCompoundBaseField[FloatLinear3AttrOperator, FloatLinear3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatLinear3AttrOperator
    PLUG_CLS = FloatLinear3PlugOperator
