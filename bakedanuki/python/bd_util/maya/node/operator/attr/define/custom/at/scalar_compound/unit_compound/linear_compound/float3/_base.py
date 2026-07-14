# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="FloatLinear3CompoundBaseAttrOperator")

P = TypeVar("P", bound="FloatLinear3CompoundBasePlugOperator")


class FloatLinear3CompoundBasePlugOperator(LinearCompoundBasePlugOperator[A]):
    __slots__ = ()


class FloatLinear3CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatLinear3CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatLinear3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatLinear3CompoundBasePlugOperator)
