# coding: utf-8
from .._core import Attr, Plug


class CharPlug(Plug["CharAttr"]):
    pass


class CharAttr(Attr[CharPlug]):
    ATTR_TYPE = "char"
    PLUG_CLS = CharPlug
