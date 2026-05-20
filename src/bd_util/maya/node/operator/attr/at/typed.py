# coding: utf-8
from .._core import Attr, Plug


class TypedPlug(Plug["TypedAttr"]):
    __slots__ = ()


class TypedAttr(Attr[TypedPlug]):
    __slots__ = ()

    ATTR_TYPE = "typed"
    PLUG_CLS = TypedPlug
