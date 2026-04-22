# coding: utf-8
from .._core import Attr, Plug


class SpectrumPlug(Plug["SpectrumAttr"]):
    pass


class SpectrumAttr(Attr[SpectrumPlug]):
    ATTR_TYPE = "spectrum"
    PLUG_CLS = SpectrumPlug
