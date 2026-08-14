# coding: utf-8
from typing import Any, Never
from ...._core import AttrOperator, PlugOperator, AttributeField


class TypedPlugOperator(PlugOperator["TypedAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> Never:
        raise NotImplementedError(
            "TypedPlugOperator does not support get operation"
        )

    # set
    def set(self, value: Any) -> Never:
        raise NotImplementedError(
            "TypedPlugOperator does not support set operation"
        )


class TypedAttrOperator(AttrOperator[TypedPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "typed"


class TypedField(AttributeField[TypedAttrOperator, TypedPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TypedAttrOperator
    PLUG_CLS = TypedPlugOperator
