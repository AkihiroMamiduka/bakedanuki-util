# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import Double2
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from ...._round import RoundCompoundPlugOperatorMixin

A = TypeVar("A", bound="Double2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Double2CompoundBasePlugOperator[Any]")


class Double2CompoundBasePlugOperator(
    RoundCompoundPlugOperatorMixin,
    DoubleCompoundBasePlugOperator[A, Double2],
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
