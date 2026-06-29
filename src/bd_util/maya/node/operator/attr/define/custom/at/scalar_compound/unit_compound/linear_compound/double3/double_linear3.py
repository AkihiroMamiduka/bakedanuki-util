# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)
from .......std.at.unit_scalar_range.double_linear import DoubleLinearField

A = TypeVar("A", bound="DoubleLinear3CompoundBaseAttrOperator")

P = TypeVar("P", bound="DoubleLinear3CompoundBasePlugOperator")


class DoubleLinear3CompoundBasePlugOperator(LinearCompoundBasePlugOperator[A]):
    __slots__ = ()

    x = DoubleLinearField()
    y = DoubleLinearField()
    z = DoubleLinearField()


class DoubleLinear3CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleLinear3CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleLinear3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleLinear3CompoundBasePlugOperator)


class DoubleLinear3PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["DoubleLinear3AttrOperator"]
):
    __slots__ = ()


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
