# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Float2
from .._base import (
    FloatCompoundBasePlugOperator,
    FloatCompoundBaseAttrOperator,
    FloatCompoundBaseField,
)

A = TypeVar("A", bound="Float2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Float2CompoundBasePlugOperator[Any]")


class Float2CompoundBasePlugOperator(FloatCompoundBasePlugOperator[A, Float2]):
    """2 成分の float 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Float2


class Float2CompoundBaseAttrOperator(FloatCompoundBaseAttrOperator[P]):
    """2 成分の float 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "float2"


class Float2CompoundBaseField(FloatCompoundBaseField[A, P]):
    """2 成分の float 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Float2CompoundBasePlugOperator)
