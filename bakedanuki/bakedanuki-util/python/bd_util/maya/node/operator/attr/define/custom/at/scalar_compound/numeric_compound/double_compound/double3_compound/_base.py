# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Double3
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from ...._round import RoundCompoundPlugOperatorMixin

A = TypeVar("A", bound="Double3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Double3CompoundBasePlugOperator[Any]")


class Double3CompoundBasePlugOperator(
    RoundCompoundPlugOperatorMixin,
    DoubleCompoundBasePlugOperator[A, Double3],
):
    """3 成分の double 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Double3


class Double3CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    """3 成分の double 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3CompoundBaseField(DoubleCompoundBaseField[A, P]):
    """3 成分の double 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double3CompoundBasePlugOperator)
