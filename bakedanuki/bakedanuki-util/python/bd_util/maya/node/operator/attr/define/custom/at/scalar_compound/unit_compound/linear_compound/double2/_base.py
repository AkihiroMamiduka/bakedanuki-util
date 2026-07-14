# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="DoubleLinear2CompoundBaseAttrOperator")

P = TypeVar("P", bound="DoubleLinear2CompoundBasePlugOperator")


class DoubleLinear2CompoundBasePlugOperator(LinearCompoundBasePlugOperator[A]):
    __slots__ = ()


class DoubleLinear2CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double2"


class DoubleLinear2CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleLinear2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleLinear2CompoundBasePlugOperator)
