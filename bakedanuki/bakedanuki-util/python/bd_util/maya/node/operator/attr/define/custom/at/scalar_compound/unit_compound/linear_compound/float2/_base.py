# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import FloatLinear2
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="FloatLinear2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatLinear2CompoundBasePlugOperator[Any]")


class FloatLinear2CompoundBasePlugOperator(
    LinearCompoundBasePlugOperator[A, FloatLinear2]
):
    """2 成分の float 型の距離 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = FloatLinear2


class FloatLinear2CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    """2 成分の float 型の距離 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "float2"


class FloatLinear2CompoundBaseField(LinearCompoundBaseField[A, P]):
    """2 成分の float 型の距離 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatLinear2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatLinear2CompoundBasePlugOperator)
