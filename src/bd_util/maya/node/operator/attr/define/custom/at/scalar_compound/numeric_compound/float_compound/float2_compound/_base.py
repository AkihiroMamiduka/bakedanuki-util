# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    FloatCompoundBasePlugOperator,
    FloatCompoundBaseAttrOperator,
    FloatCompoundBaseField,
)

A = TypeVar("A", bound="Float2CompoundBaseAttrOperator")

P = TypeVar("P", bound="Float2CompoundBasePlugOperator")


class Float2CompoundBasePlugOperator(FloatCompoundBasePlugOperator[A]):
    __slots__ = ()


class Float2CompoundBaseAttrOperator(FloatCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class Float2CompoundBaseField(FloatCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Float2CompoundBasePlugOperator)
