# coding: utf-8
from .._core import Attr, Plug


class TypedPlug(Plug["TypedAttr"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError("TypedPlug does not support get operation")

    # set
    def set(self, value):
        raise NotImplementedError("TypedPlug does not support set operation")


class TypedAttr(Attr[TypedPlug]):
    __slots__ = ()

    ATTR_TYPE = "typed"
    PLUG_CLS = TypedPlug
