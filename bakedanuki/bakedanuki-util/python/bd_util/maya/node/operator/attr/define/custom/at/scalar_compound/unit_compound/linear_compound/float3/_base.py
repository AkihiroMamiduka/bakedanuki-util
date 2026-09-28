# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import FloatLinear3
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="FloatLinear3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatLinear3CompoundBasePlugOperator[Any]")


class FloatLinear3CompoundBasePlugOperator(
    LinearCompoundBasePlugOperator[A, FloatLinear3]
):
    """3 成分の float 型の距離 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = FloatLinear3


class FloatLinear3CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    """3 成分の float 型の距離 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatLinear3CompoundBaseField(LinearCompoundBaseField[A, P]):
    """3 成分の float 型の距離 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatLinear3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatLinear3CompoundBasePlugOperator)
