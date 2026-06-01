# coding: utf-8
from .._core import AttrOperator, PlugOperator


class MessagePlug(PlugOperator["MessageAttr"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError("MessagePlug does not support get operation")

    # set
    def set(self, value):
        raise NotImplementedError("MessagePlug does not support set operation")


class MessageAttr(AttrOperator[MessagePlug]):
    __slots__ = ()

    ATTR_TYPE = "message"
    PLUG_CLS = MessagePlug
