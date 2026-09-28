# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Short2
from .._base import (
    ShortCompoundBasePlugOperator,
    ShortCompoundBaseAttrOperator,
    ShortCompoundBaseField,
)

A = TypeVar("A", bound="Short2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Short2CompoundBasePlugOperator[Any]")


class Short2CompoundBasePlugOperator(ShortCompoundBasePlugOperator[A, Short2]):
    """2 成分の short 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Short2


class Short2CompoundBaseAttrOperator(ShortCompoundBaseAttrOperator[P]):
    """2 成分の short 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "short2"


class Short2CompoundBaseField(ShortCompoundBaseField[A, P]):
    """2 成分の short 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Short2CompoundBasePlugOperator)
