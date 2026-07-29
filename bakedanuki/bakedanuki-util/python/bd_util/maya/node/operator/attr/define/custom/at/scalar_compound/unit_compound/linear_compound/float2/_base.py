# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import FloatLinear2
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="FloatLinear2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatLinear2CompoundBasePlugOperator[Any]")


class FloatLinear2CompoundBasePlugOperator(
    LinearCompoundBasePlugOperator[A, FloatLinear2]
):
    __slots__ = ()

    VALUE_TYPE = FloatLinear2


class FloatLinear2CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class FloatLinear2CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatLinear2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatLinear2CompoundBasePlugOperator)
