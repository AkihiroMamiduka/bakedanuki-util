# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Double3Plug(Plug[A]):
    pass


class Double3Attr(Attr[P]):
    ATTR_TYPE = "double3"
    PLUG_CLS = cast(Type[P], Double3Plug)
