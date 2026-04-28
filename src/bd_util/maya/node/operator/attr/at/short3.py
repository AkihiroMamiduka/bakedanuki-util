# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Short3Plug(Plug[A]):
    pass


class Short3Attr(Attr[P]):
    ATTR_TYPE = "short3"
    PLUG_CLS = cast(Type[P], Short3Plug)
