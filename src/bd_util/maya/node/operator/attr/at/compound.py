# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class CompoundPlugOperator(PlugOperator[A]):
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


class CompoundAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "compound"


class CompoundField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], CompoundAttrOperator)
    PLUG_CLS = cast(Type[P], CompoundPlugOperator)
