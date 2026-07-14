# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)

A = TypeVar("A", bound="Long2CompoundBaseAttrOperator")

P = TypeVar("P", bound="Long2CompoundBasePlugOperator")


class Long2CompoundBasePlugOperator(LongCompoundBasePlugOperator[A]):
    __slots__ = ()


class Long2CompoundBaseAttrOperator(LongCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "long2"


class Long2CompoundBaseField(LongCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Long2CompoundBasePlugOperator)
