# coding: utf-8
from .._core import AttrOperator, PlugOperator


class MessagePlugOperator(PlugOperator["MessageAttrOperator"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "MessagePlugOperator does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "MessagePlugOperator does not support set operation"
        )


class MessageAttrOperator(AttrOperator[MessagePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "message"
    PLUG_CLS = MessagePlugOperator
