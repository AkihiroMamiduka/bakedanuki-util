# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    FloatCompoundBasePlugOperator,
    FloatCompoundBaseAttrOperator,
    FloatCompoundBaseField,
)

A = TypeVar("A", bound="Float3CompoundBaseAttrOperator")

P = TypeVar("P", bound="Float3CompoundBasePlugOperator")


class Float3CompoundBasePlugOperator(FloatCompoundBasePlugOperator[A]):
    __slots__ = ()


class Float3CompoundBaseAttrOperator(FloatCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class Float3CompoundBaseField(FloatCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Float3CompoundBasePlugOperator)
