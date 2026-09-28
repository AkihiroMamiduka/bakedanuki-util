# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...........value import FloatAngle3
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)

A = TypeVar("A", bound="FloatAngle3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatAngle3CompoundBasePlugOperator[Any]")


class FloatAngle3CompoundBasePlugOperator(
    AngleCompoundBasePlugOperator[A, FloatAngle3]
):
    """3 成分の float 型の角度 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = FloatAngle3


class FloatAngle3CompoundBaseAttrOperator(AngleCompoundBaseAttrOperator[P]):
    """3 成分の float 型の角度 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatAngle3CompoundBaseField(AngleCompoundBaseField[A, P]):
    """3 成分の float 型の角度 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatAngle3CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatAngle3CompoundBasePlugOperator)
