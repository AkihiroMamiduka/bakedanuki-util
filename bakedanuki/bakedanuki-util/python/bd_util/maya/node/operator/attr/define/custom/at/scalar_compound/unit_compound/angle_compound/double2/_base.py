# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import DoubleAngle2
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="DoubleAngle2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="DoubleAngle2CompoundBasePlugOperator[Any]")


class DoubleAngle2CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, DoubleAngle2]
):
    """2 成分の double 型の角度 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = DoubleAngle2


class DoubleAngle2CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    """2 成分の double 型の角度 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "double2"


class DoubleAngle2CompoundBaseField(AngleCompoundBaseField[A, P]):
    """2 成分の double 型の角度 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleAngle2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleAngle2CompoundBasePlugOperator)
