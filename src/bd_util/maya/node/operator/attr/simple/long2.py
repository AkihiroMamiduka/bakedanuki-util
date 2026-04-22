# coding: utf-8
from .._core import Attr, Plug


class Long2Plug(Plug["Long2Attr"]):
    pass


class Long2Attr(Attr[Long2Plug]):
    ATTR_TYPE = "long2"
    PLUG_CLS = Long2Plug
