# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class DataTypePlugOperator(PlugOperator[A]):
    __slots__ = ()


class DataTypeAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "typed"


class DataTypeField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataTypeAttrOperator)
    PLUG_CLS = cast(Type[P], DataTypePlugOperator)
