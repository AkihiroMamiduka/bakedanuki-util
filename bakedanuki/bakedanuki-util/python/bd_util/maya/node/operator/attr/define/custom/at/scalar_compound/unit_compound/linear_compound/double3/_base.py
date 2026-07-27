# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...........value import DoubleLinear3
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="DoubleLinear3CompoundBaseAttrOperator")

P = TypeVar("P", bound="DoubleLinear3CompoundBasePlugOperator")


class DoubleLinear3CompoundBasePlugOperator(
    LinearCompoundBasePlugOperator[A, DoubleLinear3]
):
    __slots__ = ()

    VALUE_TYPE = DoubleLinear3


class DoubleLinear3CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleLinear3CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleLinear3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleLinear3CompoundBasePlugOperator)
