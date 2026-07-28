# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...........value import Short2
from .._base import (
    ShortCompoundBasePlugOperator,
    ShortCompoundBaseAttrOperator,
    ShortCompoundBaseField,
)

A = TypeVar("A", bound="Short2CompoundBaseAttrOperator")

P = TypeVar("P", bound="Short2CompoundBasePlugOperator")


class Short2CompoundBasePlugOperator(ShortCompoundBasePlugOperator[A, Short2]):
    __slots__ = ()

    VALUE_TYPE = Short2


class Short2CompoundBaseAttrOperator(ShortCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "short2"


class Short2CompoundBaseField(ShortCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Short2CompoundBasePlugOperator)
