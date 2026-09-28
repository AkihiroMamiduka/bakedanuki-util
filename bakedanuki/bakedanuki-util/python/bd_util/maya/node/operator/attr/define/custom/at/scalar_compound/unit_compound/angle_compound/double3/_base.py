# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import DoubleAngle3
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="DoubleAngle3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="DoubleAngle3CompoundBasePlugOperator[Any]")


class DoubleAngle3CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, DoubleAngle3]
):
    """3 成分の double 型の角度 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = DoubleAngle3


class DoubleAngle3CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    """3 成分の double 型の角度 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleAngle3CompoundBaseField(AngleCompoundBaseField[A, P]):
    """3 成分の double 型の角度 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleAngle3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleAngle3CompoundBasePlugOperator)
