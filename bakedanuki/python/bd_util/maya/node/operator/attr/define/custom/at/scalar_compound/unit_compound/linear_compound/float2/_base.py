# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="FloatLinear2CompoundBaseAttrOperator")

P = TypeVar("P", bound="FloatLinear2CompoundBasePlugOperator")


class FloatLinear2CompoundBasePlugOperator(LinearCompoundBasePlugOperator[A]):
    __slots__ = ()


class FloatLinear2CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class FloatLinear2CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatLinear2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatLinear2CompoundBasePlugOperator)
