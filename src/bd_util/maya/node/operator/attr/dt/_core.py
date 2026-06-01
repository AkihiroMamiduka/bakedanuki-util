# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from .._core import AttrOperator, PlugOperator

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class DataTypePlug(PlugOperator[A]):
    __slots__ = ()


class DataTypeAttr(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "typed"
    PLUG_CLS = cast(Type[P], DataTypePlug)
