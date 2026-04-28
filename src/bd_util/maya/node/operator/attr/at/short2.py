# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Short2Plug(Plug[A]):
    pass


class Short2Attr(Attr[P]):
    ATTR_TYPE = "short2"
    PLUG_CLS = cast(Type[P], Short2Plug)
