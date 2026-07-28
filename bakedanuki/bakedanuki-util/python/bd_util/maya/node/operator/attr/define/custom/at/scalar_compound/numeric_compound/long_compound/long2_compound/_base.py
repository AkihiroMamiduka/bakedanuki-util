# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...........value import Long2
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)

A = TypeVar("A", bound="Long2CompoundBaseAttrOperator")

P = TypeVar("P", bound="Long2CompoundBasePlugOperator")


class Long2CompoundBasePlugOperator(LongCompoundBasePlugOperator[A, Long2]):
    __slots__ = ()

    VALUE_TYPE = Long2


class Long2CompoundBaseAttrOperator(LongCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "long2"


class Long2CompoundBaseField(LongCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Long2CompoundBasePlugOperator)
