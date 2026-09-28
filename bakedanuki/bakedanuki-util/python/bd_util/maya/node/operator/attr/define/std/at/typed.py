# coding: utf-8
from ...._core import AttrOperator, PlugOperator, AttributeField


class TypedPlugOperator(PlugOperator["TypedAttrOperator"]):
    """Maya の `typed` 属性プラグを操作する。"""

    __slots__ = ()


class TypedAttrOperator(AttrOperator[TypedPlugOperator]):
    """Maya の `typed` 属性定義を表す。"""

    __slots__ = ()

    ATTR_TYPE = "typed"


class TypedField(AttributeField[TypedAttrOperator, TypedPlugOperator]):
    """ノードクラスに `typed` 属性を定義する。"""

    __slots__ = ()

    ATTR_CLS = TypedAttrOperator
    PLUG_CLS = TypedPlugOperator
