# coding: utf-8
from .._core import Attr, Plug


class Short3Plug(Plug["Short3Attr"]):
    pass


class Short3Attr(Attr[Short3Plug]):
    ATTR_TYPE = "short3"
    PLUG_CLS = Short3Plug
