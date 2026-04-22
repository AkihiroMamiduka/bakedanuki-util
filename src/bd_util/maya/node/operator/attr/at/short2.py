# coding: utf-8
from .._core import Attr, Plug


class Short2Plug(Plug["Short2Attr"]):
    pass


class Short2Attr(Attr[Short2Plug]):
    ATTR_TYPE = "short2"
    PLUG_CLS = Short2Plug
