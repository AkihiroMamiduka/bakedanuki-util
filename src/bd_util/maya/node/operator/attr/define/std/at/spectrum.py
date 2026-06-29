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
