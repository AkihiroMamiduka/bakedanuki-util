# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import Long3
from .._base import (
    LongCompoundBasePlugOperator,
    LongCompoundBaseAttrOperator,
    LongCompoundBaseField,
)

A = TypeVar("A", bound="Long3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Long3CompoundBasePlugOperator[Any]")


class Long3CompoundBasePlugOperator(LongCompoundBasePlugOperator[A, Long3]):
    """3 成分の long 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Long3


class Long3CompoundBaseAttrOperator(LongCompoundBaseAttrOperator[P]):
    """3 成分の long 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "long3"


class Long3CompoundBaseField(LongCompoundBaseField[A, P]):
    """3 成分の long 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Long3CompoundBasePlugOperator)
