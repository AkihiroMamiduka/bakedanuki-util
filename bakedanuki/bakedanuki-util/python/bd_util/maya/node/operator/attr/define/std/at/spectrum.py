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


class SpectrumPlugOperator(
    Float3CompoundBasePlugOperator["SpectrumAttrOperator"]
):
    __slots__ = ()
    _SUFFIXES = ("r", "g", "b")


class SpectrumAttrOperator(
    Float3CompoundBaseAttrOperator[SpectrumPlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "spectrum"


class SpectrumField(Float3CompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], SpectrumAttrOperator)
    PLUG_CLS = cast(Type[P], SpectrumPlugOperator)
