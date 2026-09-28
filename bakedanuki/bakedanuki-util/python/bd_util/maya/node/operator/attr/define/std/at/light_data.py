# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator[Any]")

P = TypeVar("P", bound="PlugOperator[Any]")


class LightDataPlugOperator(PlugOperator[A]):
    """Maya の `lightData` 属性プラグを操作する。"""

    __slots__ = ()


class LightDataAttrOperator(AttrOperator[P]):
    """Maya の `lightData` 属性定義を表す。"""

    __slots__ = ()

    ATTR_TYPE = "lightData"


class LightDataField(AttributeField[A, P]):
    """ノードクラスに `lightData` 属性を定義する。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], LightDataAttrOperator)
    PLUG_CLS = cast(Type[P], LightDataPlugOperator)
