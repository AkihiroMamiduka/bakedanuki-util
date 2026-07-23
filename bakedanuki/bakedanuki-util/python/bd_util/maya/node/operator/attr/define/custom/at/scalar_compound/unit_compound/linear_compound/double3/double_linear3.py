# coding: utf-8

# self
from ._base import (
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBaseField,
)
from .......std.at.unit_scalar_range.double_linear import DoubleLinearField


class DoubleLinear3PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["DoubleLinear3AttrOperator"]
):
    __slots__ = ()

    x = DoubleLinearField()
    y = DoubleLinearField()
    z = DoubleLinearField()


class DoubleLinear3AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[DoubleLinear3PlugOperator]
):
    __slots__ = ()


class DoubleLinear3Field(
    DoubleLinear3CompoundBaseField[
        DoubleLinear3AttrOperator, DoubleLinear3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleLinear3AttrOperator
    PLUG_CLS = DoubleLinear3PlugOperator
