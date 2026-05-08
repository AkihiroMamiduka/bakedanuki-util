# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Double2Plug(Plug[A]):
    pass


class Double2Attr(Attr[P]):
    ATTR_TYPE = "double2"
    PLUG_CLS = cast(Type[P], Double2Plug)
