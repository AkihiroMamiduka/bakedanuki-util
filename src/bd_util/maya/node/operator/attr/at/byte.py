# coding: utf-8
from .._core import Attr, Plug


class BytePlug(Plug["ByteAttr"]):
    pass


class ByteAttr(Attr[BytePlug]):
    ATTR_TYPE = "byte"
    PLUG_CLS = BytePlug
