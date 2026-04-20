# coding: utf-8
from .._core import Attr, Plug


class DoublePlug(Plug["DoubleAttr"]):
    pass


class DoubleAttr(Attr[DoublePlug]):
    ATTR_TYPE = "double"
    PLUG_CLS = DoublePlug
