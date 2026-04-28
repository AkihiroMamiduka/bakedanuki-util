# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Float3Plug(Plug[A]):
    pass


class Float3Attr(Attr[P]):
    ATTR_TYPE = "float3"
    PLUG_CLS = cast(Type[P], Float3Plug)
