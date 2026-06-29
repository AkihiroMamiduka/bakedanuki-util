# coding: utf-8


# self
from ._base import (
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBaseField,
)

from .......std.at.unit_scalar_range.float_linear import FloatLinearField


class FloatLinear3PlugOperator(
    FloatLinear3CompoundBasePlugOperator["FloatLinear3AttrOperator"]
):
    __slots__ = ()

    x = FloatLinearField()
    y = FloatLinearField()
    z = FloatLinearField()


class FloatLinear3AttrOperator(
    FloatLinear3CompoundBaseAttrOperator[FloatLinear3PlugOperator]
):
    __slots__ = ()


class FloatLinear3Field(
    FloatLinear3CompoundBaseField[
        FloatLinear3AttrOperator, FloatLinear3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FloatLinear3AttrOperator
    PLUG_CLS = FloatLinear3PlugOperator
