# coding: utf-8
from .._core import Attr, Plug


class LongPlug(Plug["LongAttr"]):
    pass


class LongAttr(Attr[LongPlug]):
    ATTR_TYPE = "long"
    PLUG_CLS = LongPlug
