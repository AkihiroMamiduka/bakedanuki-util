# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .float3 import Float3Attr, Float3Plug

A = TypeVar("A", bound="Float3Attr")

P = TypeVar("P", bound="Float3Plug")


class ReflectancePlug(Float3Plug["ReflectanceAttr"]):
    __slots__ = ()


class ReflectanceAttr(Float3Attr[ReflectancePlug]):
    __slots__ = ()

    ATTR_TYPE = "reflectance"
    PLUG_CLS = cast(Type[P], ReflectancePlug)
