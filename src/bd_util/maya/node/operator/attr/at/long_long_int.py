# coding: utf-8
from .._core import Attr, Plug


class LongLongIntPlug(Plug["LongLongIntAttr"]):
    pass


class LongLongIntAttr(Attr[LongLongIntPlug]):
    ATTR_TYPE = "long long int"
    PLUG_CLS = LongLongIntPlug
