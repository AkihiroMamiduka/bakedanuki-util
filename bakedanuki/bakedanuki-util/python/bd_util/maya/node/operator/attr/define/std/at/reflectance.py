# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)

A = TypeVar("A", bound="Float3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Float3CompoundBasePlugOperator[Any]")


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
