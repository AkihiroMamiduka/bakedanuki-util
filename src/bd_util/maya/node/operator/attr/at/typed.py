# coding: utf-8
from .._core import Attr, Plug


class TypedPlug(Plug["TypedAttr"]):
    pass


class TypedAttr(Attr[TypedPlug]):
    ATTR_TYPE = "typed"
    PLUG_CLS = TypedPlug
