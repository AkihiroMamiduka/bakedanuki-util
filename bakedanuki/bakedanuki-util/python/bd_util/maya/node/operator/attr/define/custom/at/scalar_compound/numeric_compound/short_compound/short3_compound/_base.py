# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...........value import Short3
from .._base import (
    ShortCompoundBasePlugOperator,
    ShortCompoundBaseAttrOperator,
    ShortCompoundBaseField,
)

A = TypeVar("A", bound="Short3CompoundBaseAttrOperator")

P = TypeVar("P", bound="Short3CompoundBasePlugOperator")


class Short3CompoundBasePlugOperator(ShortCompoundBasePlugOperator[A, Short3]):
    __slots__ = ()

    VALUE_TYPE = Short3


class Short3CompoundBaseAttrOperator(ShortCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "short3"


class Short3CompoundBaseField(ShortCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Short3CompoundBasePlugOperator)
