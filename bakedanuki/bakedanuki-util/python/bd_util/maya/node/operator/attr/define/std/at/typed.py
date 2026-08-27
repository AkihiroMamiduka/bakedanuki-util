# coding: utf-8
from ...._core import AttrOperator, PlugOperator, AttributeField


class TypedPlugOperator(PlugOperator["TypedAttrOperator"]):
    __slots__ = ()


class TypedAttrOperator(AttrOperator[TypedPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "typed"


class TypedField(AttributeField[TypedAttrOperator, TypedPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TypedAttrOperator
    PLUG_CLS = TypedPlugOperator
