# coding: utf-8


# self
from ._base import (
    FloatLinear2CompoundBasePlugOperator,
    FloatLinear2CompoundBaseAttrOperator,
    FloatLinear2CompoundBaseField,
)

from .......std.at.scalar.unit.range.float_linear import FloatLinearField


class FloatLinear2PlugOperator(
    FloatLinear2CompoundBasePlugOperator["FloatLinear2AttrOperator"]
):
    __slots__ = ()

    x = FloatLinearField()
    y = FloatLinearField()


class FloatLinear2AttrOperator(
    FloatLinear2CompoundBaseAttrOperator[FloatLinear2PlugOperator]
):
    __slots__ = ()


class FloatLinear2Field(
    FloatLinear2CompoundBaseField[
        FloatLinear2AttrOperator, FloatLinear2PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FloatLinear2AttrOperator
    PLUG_CLS = FloatLinear2PlugOperator
