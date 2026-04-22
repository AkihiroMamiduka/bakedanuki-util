# coding: utf-8
from .._core import Attr, Plug


class Long3Plug(Plug["Long3Attr"]):
    pass


class Long3Attr(Attr[Long3Plug]):
    ATTR_TYPE = "long3"
    PLUG_CLS = Long3Plug
