# coding: utf-8


# self
from ._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)
from ......std.at.unit_scalar_range.double_linear import DoubleLinearField


class DoubleLinear3PlugOperator(
    LinearCompoundBasePlugOperator["DoubleLinear3AttrOperator"]
):
    __slots__ = ()

    x = DoubleLinearField()
    y = DoubleLinearField()
    z = DoubleLinearField()


class DoubleLinear3AttrOperator(
    LinearCompoundBaseAttrOperator[DoubleLinear3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleLinear3Field(
    LinearCompoundBaseField[
        DoubleLinear3AttrOperator, DoubleLinear3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleLinear3AttrOperator
    PLUG_CLS = DoubleLinear3PlugOperator
