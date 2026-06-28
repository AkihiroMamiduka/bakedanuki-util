# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from .......std.at.numeric_scalar_range.double import DoubleField

A = TypeVar("A", bound="Double3CompoundBaseAttrOperator")

P = TypeVar("P", bound="Double3CompoundBasePlugOperator")


class Double3CompoundBasePlugOperator(DoubleCompoundBasePlugOperator[A]):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()


class Double3CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double3CompoundBasePlugOperator)


class Double3PlugOperator(
    Double3CompoundBasePlugOperator["Double3AttrOperator"]
):
    __slots__ = ()


class Double3AttrOperator(
    Double3CompoundBaseAttrOperator[Double3PlugOperator]
):
    __slots__ = ()


class Double3Field(
    Double3CompoundBaseField[Double3AttrOperator, Double3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Double3AttrOperator
    PLUG_CLS = Double3PlugOperator
