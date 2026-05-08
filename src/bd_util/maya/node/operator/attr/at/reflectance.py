# coding: utf-8
from .._core import Attr, Plug


class ReflectancePlug(Plug["ReflectanceAttr"]):
    pass


class ReflectanceAttr(Attr[ReflectancePlug]):
    ATTR_TYPE = "reflectance"
    PLUG_CLS = ReflectancePlug
