# coding: utf-8
from .._core import Attr, Plug


class GenericPlug(Plug["GenericAttr"]):
    pass


class GenericAttr(Attr[GenericPlug]):
    ATTR_TYPE = "generic"
    PLUG_CLS = GenericPlug
