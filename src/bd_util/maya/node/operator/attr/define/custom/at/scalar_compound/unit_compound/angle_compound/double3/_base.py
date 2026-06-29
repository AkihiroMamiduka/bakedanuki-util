# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="DoubleAngle3CompoundBaseAttrOperator")

P = TypeVar("P", bound="DoubleAngle3CompoundBasePlugOperator")


class DoubleAngle3CompoundBasePlugOperator(AngleCompoundBasePlugOperator[A]):
    __slots__ = ()


class DoubleAngle3CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleAngle3CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleAngle3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleAngle3CompoundBasePlugOperator)
