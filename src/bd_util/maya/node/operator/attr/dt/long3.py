# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug
from ._core import DataTypeAttr, DataTypePlug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class DataLong3Plug(DataTypePlug[A]):
    pass


class DataLong3Attr(DataTypeAttr[P]):
    DATA_TYPE = "long3"
    PLUG_CLS = cast(Type[P], DataLong3Plug)
