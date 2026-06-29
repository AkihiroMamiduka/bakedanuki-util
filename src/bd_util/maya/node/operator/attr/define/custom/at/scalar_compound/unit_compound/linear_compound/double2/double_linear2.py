# coding: utf-8

# self
from ._base import (
    DoubleLinear2CompoundBasePlugOperator,
    DoubleLinear2CompoundBaseAttrOperator,
    DoubleLinear2CompoundBaseField,
)
from .......std.at.unit_scalar_range.double_linear import DoubleLinearField


class DoubleLinear2PlugOperator(
    DoubleLinear2CompoundBasePlugOperator["DoubleLinear2AttrOperator"]
):
    __slots__ = ()

    x = DoubleLinearField()
    y = DoubleLinearField()
    z = DoubleLinearField()


class DoubleLinear2AttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[DoubleLinear2PlugOperator]
):
    __slots__ = ()


class DoubleLinear2Field(
    DoubleLinear2CompoundBaseField[
        DoubleLinear2AttrOperator, DoubleLinear2PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleLinear2AttrOperator
    PLUG_CLS = DoubleLinear2PlugOperator
