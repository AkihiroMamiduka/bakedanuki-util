# coding: utf-8
from .._core import Attr, Plug


class DoubleAnglePlug(Plug["DoubleAngleAttr"]):
    pass


class DoubleAngleAttr(Attr[DoubleAnglePlug]):
    ATTR_TYPE = "doubleAngle"
    PLUG_CLS = DoubleAnglePlug
