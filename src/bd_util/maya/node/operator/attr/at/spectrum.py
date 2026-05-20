# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .float3 import Float3Attr, Float3Plug

A = TypeVar("A", bound="Float3Attr")

P = TypeVar("P", bound="Float3Plug")


class SpectrumPlug(Float3Plug["SpectrumAttr"]):
    __slots__ = ()


class SpectrumAttr(Float3Attr[SpectrumPlug]):
    __slots__ = ()

    ATTR_TYPE = "spectrum"
    PLUG_CLS = cast(Type[P], SpectrumPlug)
