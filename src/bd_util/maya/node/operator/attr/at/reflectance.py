# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .float3 import Float3AttrOperator, Float3PlugOperator

A = TypeVar("A", bound="Float3AttrOperator")

P = TypeVar("P", bound="Float3PlugOperator")


class ReflectancePlug(Float3PlugOperator["ReflectanceAttr"]):
    __slots__ = ()


class ReflectanceAttr(Float3AttrOperator[ReflectancePlug]):
    __slots__ = ()

    ATTR_TYPE = "reflectance"
    PLUG_CLS = cast(Type[P], ReflectancePlug)
