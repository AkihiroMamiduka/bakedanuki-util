# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class DataTypePlug(Plug[A]):
    __slots__ = ()


class DataTypeAttr(Attr[P]):
    __slots__ = ()

    ATTR_TYPE = "typed"
    PLUG_CLS = cast(Type[P], DataTypePlug)
