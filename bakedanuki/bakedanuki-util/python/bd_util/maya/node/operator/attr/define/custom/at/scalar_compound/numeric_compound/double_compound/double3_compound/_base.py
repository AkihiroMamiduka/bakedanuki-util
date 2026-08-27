# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import Double3
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from ...._round import RoundCompoundPlugOperatorMixin

A = TypeVar("A", bound="Double3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Double3CompoundBasePlugOperator[Any]")


class Double3CompoundBasePlugOperator(
    RoundCompoundPlugOperatorMixin,
    DoubleCompoundBasePlugOperator[A, Double3],
):
    __slots__ = ()

    VALUE_TYPE = Double3


class Double3CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double3CompoundBasePlugOperator)
