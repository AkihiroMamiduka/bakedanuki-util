# coding: utf-8
from .._core import AttrOperator, PlugOperator


class TypedPlugOperator(PlugOperator["TypedAttrOperator"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "TypedPlugOperator does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "TypedPlugOperator does not support set operation"
        )


class TypedAttrOperator(AttrOperator[TypedPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "typed"
    PLUG_CLS = TypedPlugOperator
