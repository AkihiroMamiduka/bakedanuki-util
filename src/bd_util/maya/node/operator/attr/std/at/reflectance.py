# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .float3 import Float3AttrOperator, Float3PlugOperator, Float3Field

A = TypeVar("A", bound="Float3AttrOperator")

P = TypeVar("P", bound="Float3PlugOperator")


class ReflectancePlugOperator(Float3PlugOperator["ReflectanceAttrOperator"]):
    __slots__ = ()


class ReflectanceAttrOperator(Float3AttrOperator[ReflectancePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "reflectance"


class ReflectanceField(Float3Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ReflectanceAttrOperator)
    PLUG_CLS = cast(Type[P], ReflectancePlugOperator)
