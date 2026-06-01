# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .float3 import Float3AttrOperator, Float3PlugOperator

A = TypeVar("A", bound="Float3AttrOperator")

P = TypeVar("P", bound="Float3PlugOperator")


class SpectrumPlugOperator(Float3PlugOperator["SpectrumAttrOperator"]):
    __slots__ = ()


class SpectrumAttrOperator(Float3AttrOperator[SpectrumPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "spectrum"
    PLUG_CLS = cast(Type[P], SpectrumPlugOperator)
