# coding: utf-8
from .._core import Attr, Plug


class DoubleLinearPlug(Plug["DoubleLinearAttr"]):
    pass


class DoubleLinearAttr(Attr[DoubleLinearPlug]):
    ATTR_TYPE = "doubleLinear"
    PLUG_CLS = DoubleLinearPlug
