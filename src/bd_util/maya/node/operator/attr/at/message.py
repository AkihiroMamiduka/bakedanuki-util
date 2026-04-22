# coding: utf-8
from .._core import Attr, Plug


class MessagePlug(Plug["MessageAttr"]):
    pass


class MessageAttr(Attr[MessagePlug]):
    ATTR_TYPE = "message"
    PLUG_CLS = MessagePlug
