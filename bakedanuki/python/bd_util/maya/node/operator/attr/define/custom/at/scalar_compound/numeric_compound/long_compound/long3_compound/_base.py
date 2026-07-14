# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)

A = TypeVar("A", bound="Long3CompoundBaseAttrOperator")

P = TypeVar("P", bound="Long3CompoundBasePlugOperator")


class Long3CompoundBasePlugOperator(LongCompoundBasePlugOperator[A]):
    __slots__ = ()


class Long3CompoundBaseAttrOperator(LongCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "long3"


class Long3CompoundBaseField(LongCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Long3CompoundBasePlugOperator)
