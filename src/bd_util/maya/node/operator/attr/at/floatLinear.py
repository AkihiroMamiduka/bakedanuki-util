# coding: utf-8
from .._core import Attr, Plug


class FloatLinearPlug(Plug["FloatLinearAttr"]):
    pass


class FloatLinearAttr(Attr[FloatLinearPlug]):
    ATTR_TYPE = "floatLinear"
    PLUG_CLS = FloatLinearPlug
