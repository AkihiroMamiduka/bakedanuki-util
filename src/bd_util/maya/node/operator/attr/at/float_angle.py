# coding: utf-8
from .._core import Attr, Plug


class FloatAnglePlug(Plug["FloatAngleAttr"]):
    pass


class FloatAngleAttr(Attr[FloatAnglePlug]):
    ATTR_TYPE = "floatAngle"
    PLUG_CLS = FloatAnglePlug
