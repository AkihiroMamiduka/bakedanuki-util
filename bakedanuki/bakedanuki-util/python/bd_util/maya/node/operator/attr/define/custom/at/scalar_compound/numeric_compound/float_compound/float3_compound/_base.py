# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Float3
from .._base import (
    FloatCompoundBasePlugOperator,
    FloatCompoundBaseAttrOperator,
    FloatCompoundBaseField,
)

A = TypeVar("A", bound="Float3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Float3CompoundBasePlugOperator[Any]")


class Float3CompoundBasePlugOperator(FloatCompoundBasePlugOperator[A, Float3]):
    """3 成分の float 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Float3


class Float3CompoundBaseAttrOperator(FloatCompoundBaseAttrOperator[P]):
    """3 成分の float 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "float3"


class Float3CompoundBaseField(FloatCompoundBaseField[A, P]):
    """3 成分の float 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Float3CompoundBasePlugOperator)
