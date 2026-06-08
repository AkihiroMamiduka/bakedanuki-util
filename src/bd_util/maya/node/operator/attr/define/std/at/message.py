# coding: utf-8
from ...._core import AttrOperator, PlugOperator, AttributeField


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


class MessageField(AttributeField[MessageAttrOperator, MessagePlugOperator]):
    __slots__ = ()

    ATTR_CLS = MessageAttrOperator
    PLUG_CLS = MessagePlugOperator
