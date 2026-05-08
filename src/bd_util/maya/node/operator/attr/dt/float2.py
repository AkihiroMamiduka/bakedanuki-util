# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug
from ._core import DataTypeAttr, DataTypePlug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class DataFloat2Plug(DataTypePlug[A]):
    pass


class DataFloat2Attr(DataTypeAttr[P]):
    DATA_TYPE = "float2"
    PLUG_CLS = cast(Type[P], DataFloat2Plug)
