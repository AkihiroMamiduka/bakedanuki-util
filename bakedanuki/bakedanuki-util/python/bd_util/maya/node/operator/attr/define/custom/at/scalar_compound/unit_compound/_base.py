# coding: utf-8
from typing import Any, TypeVar, Type, cast

from maya.api import OpenMaya as om

from .........value.scalar_compound.scalar_compound_value import (
    ScalarCompoundValue,
)
from .......... import logger as u_logger
from .._base import (
    ScalarCompoundBasePlugOperator,
    ScalarCompoundBaseAttrOperator,
    ScalarCompoundBaseField,
)
from .._round import RoundCompoundPlugOperatorMixin

A = TypeVar("A", bound="UnitCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="UnitCompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[float])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class UnitCompoundBasePlugOperator(
    RoundCompoundPlugOperatorMixin,
    ScalarCompoundBasePlugOperator[A, V, float],
):
    """単位付き compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    CHILD_M_FN = om.MFnUnitAttribute


class UnitCompoundBaseAttrOperator(ScalarCompoundBaseAttrOperator[P]):
    """単位付き compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()


class UnitCompoundBaseField(ScalarCompoundBaseField[A, P]):
    """単位付き compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], UnitCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], UnitCompoundBasePlugOperator)
