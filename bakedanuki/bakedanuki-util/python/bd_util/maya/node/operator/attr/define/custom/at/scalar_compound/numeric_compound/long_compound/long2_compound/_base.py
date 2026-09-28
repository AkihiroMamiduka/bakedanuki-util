# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Long2
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)

A = TypeVar("A", bound="Long2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Long2CompoundBasePlugOperator[Any]")


class Long2CompoundBasePlugOperator(LongCompoundBasePlugOperator[A, Long2]):
    """2 成分の long 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Long2


class Long2CompoundBaseAttrOperator(LongCompoundBaseAttrOperator[P]):
    """2 成分の long 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "long2"


class Long2CompoundBaseField(LongCompoundBaseField[A, P]):
    """2 成分の long 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Long2CompoundBasePlugOperator)
