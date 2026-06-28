# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)
from ......std.at.unit_scalar_range.double_angle import DoubleAngleField

A = TypeVar("A", bound="DoubleAngle3CompoundBaseAttrOperator")

P = TypeVar("P", bound="DoubleAngle3CompoundBasePlugOperator")


class DoubleAngle3CompoundBasePlugOperator(AngleCompoundBasePlugOperator[A]):
    __slots__ = ()

    x = DoubleAngleField()
    y = DoubleAngleField()
    z = DoubleAngleField()


class DoubleAngle3CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleAngle3CompoundBaseField(AngleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleAngle3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleAngle3CompoundBasePlugOperator)


class DoubleAngle3PlugOperator(
    DoubleAngle3CompoundBasePlugOperator["DoubleAngle3AttrOperator"]
):
    __slots__ = ()


class DoubleAngle3AttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[DoubleAngle3PlugOperator]
):
    __slots__ = ()


class DoubleAngle3Field(
    DoubleAngle3CompoundBaseField[
        DoubleAngle3AttrOperator, DoubleAngle3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngle3AttrOperator
    PLUG_CLS = DoubleAngle3PlugOperator
