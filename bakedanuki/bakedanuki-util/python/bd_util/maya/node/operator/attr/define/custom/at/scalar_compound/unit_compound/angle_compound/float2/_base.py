# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import FloatAngle2
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="FloatAngle2CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatAngle2CompoundBasePlugOperator[Any]")


class FloatAngle2CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, FloatAngle2]
):
    """2 成分の float 型の角度 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = FloatAngle2


class FloatAngle2CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    """2 成分の float 型の角度 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "float2"


class FloatAngle2CompoundBaseField(AngleCompoundBaseField[A, P]):
    """2 成分の float 型の角度 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatAngle2CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatAngle2CompoundBasePlugOperator)
