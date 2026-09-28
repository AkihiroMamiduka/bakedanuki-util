# coding: utf-8
from typing import Any, ClassVar, TypeVar, Type, cast

from maya.api import OpenMaya as om

from ..........value.scalar_compound.scalar_compound_value import (
    ScalarCompoundValue,
)
from ........... import logger as u_logger
from .._base import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)

A = TypeVar("A", bound="DoubleCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="DoubleCompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[float])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class DoubleCompoundBasePlugOperator(
    NumericCompoundBasePlugOperator[A, V, float]
):
    """double 型 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    CHILD_M_ATTR_TYPE: ClassVar[int] = om.MFnNumericData.kDouble

    def _get_child_value(self, child_plug: om.MPlug) -> float:
        return child_plug.asDouble()

    def _set_child_value(self, child_plug: om.MPlug, value: float) -> None:
        self._node.modifier_manager.dg_mod.newPlugValueDouble(
            child_plug, value
        )

    def _set_child_value_direct(
        self,
        child_plug: om.MPlug,
        value: float,
    ) -> None:
        child_plug.setDouble(value)


class DoubleCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    """double 型 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()


class DoubleCompoundBaseField(NumericCompoundBaseField[A, P]):
    """double 型 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], DoubleCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DoubleCompoundBasePlugOperator)
