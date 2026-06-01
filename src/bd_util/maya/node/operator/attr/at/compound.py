# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import AttrOperator, PlugOperator

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class CompoundPlug(PlugOperator[A]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "CompoundPlug does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "CompoundPlug does not support set operation"
        )


class CompoundAttr(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "compound"
    PLUG_CLS = cast(Type[P], CompoundPlug)
