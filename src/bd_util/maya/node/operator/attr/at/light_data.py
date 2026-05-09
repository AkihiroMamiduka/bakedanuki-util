# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class LightDataPlug(Plug[A]):
    pass


class LightDataAttr(Attr[P]):
    ATTR_TYPE = "lightData"
    PLUG_CLS = cast(Type[P], LightDataPlug)
