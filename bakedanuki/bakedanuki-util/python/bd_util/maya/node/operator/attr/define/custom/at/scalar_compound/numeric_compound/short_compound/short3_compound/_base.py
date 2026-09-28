# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Short3
from .._base import (
    ShortCompoundBasePlugOperator,
    ShortCompoundBaseAttrOperator,
    ShortCompoundBaseField,
)

A = TypeVar("A", bound="Short3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Short3CompoundBasePlugOperator[Any]")


class Short3CompoundBasePlugOperator(ShortCompoundBasePlugOperator[A, Short3]):
    """3 成分の short 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Short3


class Short3CompoundBaseAttrOperator(ShortCompoundBaseAttrOperator[P]):
    """3 成分の short 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "short3"


class Short3CompoundBaseField(ShortCompoundBaseField[A, P]):
    """3 成分の short 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Short3CompoundBasePlugOperator)
