# coding: utf-8
from .._core import Attr, Plug


class Float2Plug(Plug["Float2Attr"]):
    pass


class Float2Attr(Attr[Float2Plug]):
    ATTR_TYPE = "float2"
    PLUG_CLS = Float2Plug
