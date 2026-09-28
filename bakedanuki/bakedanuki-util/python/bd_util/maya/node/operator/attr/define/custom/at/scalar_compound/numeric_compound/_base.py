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

A = TypeVar("A", bound="NumericCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="NumericCompoundBasePlugOperator[Any, Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[int | float])

S = TypeVar("S", bound=int | float)


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class NumericCompoundBasePlugOperator(ScalarCompoundBasePlugOperator[A, V, S]):
    """数値型の compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    CHILD_M_FN = om.MFnNumericAttribute


class NumericCompoundBaseAttrOperator(ScalarCompoundBaseAttrOperator[P]):
    """数値型の compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()


class NumericCompoundBaseField(ScalarCompoundBaseField[A, P]):
    """数値型の compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], NumericCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], NumericCompoundBasePlugOperator)
