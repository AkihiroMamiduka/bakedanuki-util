# coding: utf-8
from .._core import Attr, Plug


class MessagePlug(Plug["MessageAttr"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError("MessagePlug does not support get operation")

    # set
    def set(self, value):
        raise NotImplementedError("MessagePlug does not support set operation")


class MessageAttr(Attr[MessagePlug]):
    __slots__ = ()

    ATTR_TYPE = "message"
    PLUG_CLS = MessagePlug
