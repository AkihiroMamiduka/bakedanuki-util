# coding: utf-8
from .._core import Attr, Plug


class TimePlug(Plug["TimeAttr"]):
    pass


class TimeAttr(Attr[TimePlug]):
    ATTR_TYPE = "time"
    PLUG_CLS = TimePlug
