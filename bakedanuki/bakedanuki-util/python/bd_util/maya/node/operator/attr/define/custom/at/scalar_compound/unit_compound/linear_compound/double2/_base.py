# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import DoubleLinear2
from .._base import (
    LinearCompoundBasePlugOperator,
    LinearCompoundBaseAttrOperator,
    LinearCompoundBaseField,
)

A = TypeVar("A", bound="DoubleLinear2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="DoubleLinear2CompoundBasePlugOperator[Any]")


class DoubleLinear2CompoundBasePlugOperator(
    LinearCompoundBasePlugOperator[A, DoubleLinear2]
):
    """2 成分の double 型の距離 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = DoubleLinear2


class DoubleLinear2CompoundBaseAttrOperator(LinearCompoundBaseAttrOperator[P]):
    """2 成分の double 型の距離 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "double2"


class DoubleLinear2CompoundBaseField(LinearCompoundBaseField[A, P]):
    """2 成分の double 型の距離 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleLinear2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleLinear2CompoundBasePlugOperator)
