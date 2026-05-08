# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug
from ._core import DataTypeAttr, DataTypePlug


A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class DataShort3Plug(DataTypePlug[A]):
    pass


class DataShort3Attr(DataTypeAttr[P]):
    DATA_TYPE = "short3"
    PLUG_CLS = cast(Type[P], DataShort3Plug)
