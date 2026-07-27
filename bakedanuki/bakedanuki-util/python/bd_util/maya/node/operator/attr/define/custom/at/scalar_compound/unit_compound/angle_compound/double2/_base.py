# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...........value import DoubleAngle2
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="DoubleAngle2CompoundBaseAttrOperator")

P = TypeVar("P", bound="DoubleAngle2CompoundBasePlugOperator")


class DoubleAngle2CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, DoubleAngle2]
):
    __slots__ = ()

    VALUE_TYPE = DoubleAngle2


class DoubleAngle2CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double2"


class DoubleAngle2CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleAngle2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleAngle2CompoundBasePlugOperator)
