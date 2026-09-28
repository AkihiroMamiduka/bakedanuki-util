# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ............value import Quat
from ............. import logger as u_logger
from .._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)

A = TypeVar("A", bound="QuatCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="QuatCompoundBasePlugOperator[Any]")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class QuatCompoundBasePlugOperator(Double4CompoundBasePlugOperator[A, Quat]):
    """4 成分の四元数 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    VALUE_TYPE = Quat


class QuatCompoundBaseAttrOperator(Double4CompoundBaseAttrOperator[P]):
    """4 成分の四元数 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()

    ATTR_TYPE = "double4"


class QuatCompoundBaseField(Double4CompoundBaseField[A, P]):
    """4 成分の四元数 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], QuatCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], QuatCompoundBasePlugOperator)
