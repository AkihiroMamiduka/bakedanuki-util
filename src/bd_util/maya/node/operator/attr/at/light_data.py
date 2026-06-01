# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import AttrOperator, PlugOperator

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class LightDataPlugOperator(PlugOperator[A]):
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


class LightDataAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "lightData"
    PLUG_CLS = cast(Type[P], LightDataPlugOperator)
