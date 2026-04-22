# coding: utf-8
from .._core import Attr, Plug


class BoolPlug(Plug["BoolAttr"]):
    pass


class BoolAttr(Attr[BoolPlug]):
    ATTR_TYPE = "bool"
    PLUG_CLS = BoolPlug
