# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import FloatLinear3
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="FloatLinear3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatLinear3CompoundBasePlugOperator[Any]")


class FloatLinear3CompoundBasePlugOperator(
    LinearCompoundBasePlugOperator[A, FloatLinear3]
):
    __slots__ = ()

    VALUE_TYPE = FloatLinear3


class FloatLinear3CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatLinear3CompoundBaseField(LinearCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatLinear3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatLinear3CompoundBasePlugOperator)
