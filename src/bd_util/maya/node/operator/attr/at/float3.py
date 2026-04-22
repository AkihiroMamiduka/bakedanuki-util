# coding: utf-8
from .._core import Attr, Plug


class Float3Plug(Plug["Float3Attr"]):
    pass


class Float3Attr(Attr[Float3Plug]):
    ATTR_TYPE = "float3"
    PLUG_CLS = Float3Plug
