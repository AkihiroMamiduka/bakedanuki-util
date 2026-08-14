# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import FloatAngle2
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="FloatAngle2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatAngle2CompoundBasePlugOperator[Any]")


class FloatAngle2CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, FloatAngle2]
):
    __slots__ = ()

    VALUE_TYPE = FloatAngle2


class FloatAngle2CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class FloatAngle2CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatAngle2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatAngle2CompoundBasePlugOperator)
