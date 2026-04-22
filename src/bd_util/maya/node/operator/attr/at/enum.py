# coding: utf-8
from .._core import Attr, Plug


class EnumPlug(Plug["EnumAttr"]):
    pass


class EnumAttr(Attr[EnumPlug]):
    ATTR_TYPE = "enum"
    PLUG_CLS = EnumPlug
    enum_names: list[str] = []
