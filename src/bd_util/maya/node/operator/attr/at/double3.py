# coding: utf-8
from .._core import Attr, Plug


class Double3Plug(Plug["Double3Attr"]):
    pass


class Double3Attr(Attr[Double3Plug]):
    ATTR_TYPE = "double3"
    PLUG_CLS = Double3Plug
