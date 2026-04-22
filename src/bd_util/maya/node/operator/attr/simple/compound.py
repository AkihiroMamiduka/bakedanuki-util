# coding: utf-8
from .._core import Attr, Plug


class CompoundPlug(Plug["CompoundAttr"]):
    pass


class CompoundAttr(Attr[CompoundPlug]):
    ATTR_TYPE = "compound"
    PLUG_CLS = CompoundPlug
