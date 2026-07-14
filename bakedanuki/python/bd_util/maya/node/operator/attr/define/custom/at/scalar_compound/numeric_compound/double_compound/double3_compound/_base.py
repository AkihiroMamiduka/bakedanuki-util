# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)

A = TypeVar("A", bound="Double3CompoundBaseAttrOperator")

P = TypeVar("P", bound="Double3CompoundBasePlugOperator")


class Double3CompoundBasePlugOperator(DoubleCompoundBasePlugOperator[A]):
    __slots__ = ()


class Double3CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double3CompoundBasePlugOperator)
