# coding: utf-8
from .._core import Attr, Plug


class AddrPlug(Plug["AddrAttr"]):
    pass


class AddrAttr(Attr[AddrPlug]):
    ATTR_TYPE = "addr"
    PLUG_CLS = AddrPlug
