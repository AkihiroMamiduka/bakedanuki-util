# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="FloatAngle2CompoundBaseAttrOperator")

P = TypeVar("P", bound="FloatAngle2CompoundBasePlugOperator")


class FloatAngle2CompoundBasePlugOperator(AngleCompoundBasePlugOperator[A]):
    __slots__ = ()


class FloatAngle2CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class FloatAngle2CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatAngle2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatAngle2CompoundBasePlugOperator)
