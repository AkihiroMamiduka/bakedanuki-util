# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class CompoundPlug(Plug[A]):
    pass


class CompoundAttr(Attr[P]):
    ATTR_TYPE = "compound"
    PLUG_CLS = cast(Type[P], CompoundPlug)
