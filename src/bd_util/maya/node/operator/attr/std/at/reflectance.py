# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .float3 import Float3AttrOperator, Float3PlugOperator, Float3Field

A = TypeVar("A", bound="Float3AttrOperator")

P = TypeVar("P", bound="Float3PlugOperator")


class ReflectancePlug(Float3PlugOperator["ReflectanceAttr"]):
    __slots__ = ()


class ReflectanceAttr(Float3AttrOperator[ReflectancePlug]):
    __slots__ = ()

    ATTR_TYPE = "reflectance"


class ReflectanceField(Float3Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ReflectanceAttr)
    PLUG_CLS = cast(Type[P], ReflectancePlug)
