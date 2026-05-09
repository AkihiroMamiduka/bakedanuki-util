# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Double4Plug(Plug[A]):
    pass


class Double4Attr(Attr[P]):
    ATTR_TYPE = "double4"
    PLUG_CLS = cast(Type[P], Double4Plug)
