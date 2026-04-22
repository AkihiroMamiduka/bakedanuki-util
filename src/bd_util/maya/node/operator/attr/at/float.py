# coding: utf-8
from .._core import Attr, Plug


class FloatPlug(Plug["FloatAttr"]):
    pass


class FloatAttr(Attr[FloatPlug]):
    ATTR_TYPE = "float"
    PLUG_CLS = FloatPlug
