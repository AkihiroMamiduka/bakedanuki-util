# coding: utf-8
from .._core import Attr, Plug


class FltMatrixPlug(Plug["FltMatrixAttr"]):
    pass


class FltMatrixAttr(Attr[FltMatrixPlug]):
    ATTR_TYPE = "fltMatrix"
    PLUG_CLS = FltMatrixPlug
