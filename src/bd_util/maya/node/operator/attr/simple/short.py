# coding: utf-8
from .._core import Attr, Plug


class ShortPlug(Plug["ShortAttr"]):
    pass


class ShortAttr(Attr[ShortPlug]):
    ATTR_TYPE = "short"
    PLUG_CLS = ShortPlug
