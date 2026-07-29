# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import FloatAngle3
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="FloatAngle3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatAngle3CompoundBasePlugOperator[Any]")


class FloatAngle3CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, FloatAngle3]
):
    __slots__ = ()

    VALUE_TYPE = FloatAngle3


class FloatAngle3CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatAngle3CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatAngle3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatAngle3CompoundBasePlugOperator)
