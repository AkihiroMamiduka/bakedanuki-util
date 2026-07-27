# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...........value import Double2
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)

A = TypeVar("A", bound="Double2CompoundBaseAttrOperator")

P = TypeVar("P", bound="Double2CompoundBasePlugOperator")


class Double2CompoundBasePlugOperator(
    DoubleCompoundBasePlugOperator[A, Double2]
):
    __slots__ = ()

    VALUE_TYPE = Double2


class Double2CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double2"


class Double2CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double2CompoundBasePlugOperator)
