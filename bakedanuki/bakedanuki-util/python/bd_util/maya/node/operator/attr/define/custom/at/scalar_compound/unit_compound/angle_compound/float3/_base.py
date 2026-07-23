# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="FloatAngle3CompoundBaseAttrOperator")

P = TypeVar("P", bound="FloatAngle3CompoundBasePlugOperator")


class FloatAngle3CompoundBasePlugOperator(AngleCompoundBasePlugOperator[A]):
    __slots__ = ()


class FloatAngle3CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatAngle3CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatAngle3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatAngle3CompoundBasePlugOperator)
