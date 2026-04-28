# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Long3Plug(Plug[A]):
    pass


class Long3Attr(Attr[P]):
    ATTR_TYPE = "long3"
    PLUG_CLS = cast(Type[P], Long3Plug)
