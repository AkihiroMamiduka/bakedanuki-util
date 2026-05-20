# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class LightDataPlug(Plug[A]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "LightDataPlug does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "LightDataPlug does not support set operation"
        )


class LightDataAttr(Attr[P]):
    __slots__ = ()

    ATTR_TYPE = "lightData"
    PLUG_CLS = cast(Type[P], LightDataPlug)
