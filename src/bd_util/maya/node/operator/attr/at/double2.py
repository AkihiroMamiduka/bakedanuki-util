# coding: utf-8
from .._core import Attr, Plug


class Double2Plug(Plug["Double2Attr"]):
    pass


class Double2Attr(Attr[Double2Plug]):
    ATTR_TYPE = "double2"
    PLUG_CLS = Double2Plug
