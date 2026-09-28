# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)

A = TypeVar("A", bound="Float3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Float3CompoundBasePlugOperator[Any]")


class ReflectancePlugOperator(
    Float3CompoundBasePlugOperator["ReflectanceAttrOperator"]
):
    """Maya の `reflectance` 属性の RGB 成分を操作する。"""

    __slots__ = ()
    _SUFFIXES = ("r", "g", "b")


class ReflectanceAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectancePlugOperator]
):
    """Maya の `reflectance` 属性定義を表す。"""

    __slots__ = ()

    ATTR_TYPE = "reflectance"


class ReflectanceField(Float3CompoundBaseField[A, P]):
    """ノードクラスに `reflectance` 属性を定義する。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], ReflectanceAttrOperator)
    PLUG_CLS = cast(Type[P], ReflectancePlugOperator)
