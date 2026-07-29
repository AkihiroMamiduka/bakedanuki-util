# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator[Any]")

P = TypeVar("P", bound="PlugOperator[Any]")


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


class LightDataField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], LightDataAttrOperator)
    PLUG_CLS = cast(Type[P], LightDataPlugOperator)
