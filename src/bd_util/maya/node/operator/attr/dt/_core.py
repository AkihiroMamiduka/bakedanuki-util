# coding: utf-8
from __future__ import annotations

from .._core import Attr, Plug


class DataTypePlug(Plug["DataTypeAttr"]):
    pass


class DataTypeAttr(Attr[DataTypePlug]):
    ATTR_TYPE = "typed"
    PLUG_CLS = DataTypePlug
