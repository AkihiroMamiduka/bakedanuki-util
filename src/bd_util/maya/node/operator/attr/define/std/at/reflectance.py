# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)

A = TypeVar("A", bound="Float3CompoundBaseAttrOperator")

P = TypeVar("P", bound="Float3CompoundBasePlugOperator")


class ReflectancePlugOperator(
    Float3CompoundBasePlugOperator["ReflectanceAttrOperator"]
):
    __slots__ = ()
    _SUFFIXES = ("r", "g", "b")


class ReflectanceAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectancePlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "reflectance"


class ReflectanceField(Float3CompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ReflectanceAttrOperator)
    PLUG_CLS = cast(Type[P], ReflectancePlugOperator)
