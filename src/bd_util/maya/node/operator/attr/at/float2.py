# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Float2Plug(Plug[A]):
    def get(self) -> tuple[float, float]:
        return list(super().get()[0])


class Float2Attr(Attr[P]):
    ATTR_TYPE = "float2"
    PLUG_CLS = cast(Type[P], Float2Plug)
