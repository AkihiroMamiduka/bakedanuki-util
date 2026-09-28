# coding: utf-8
from typing import Any, ClassVar, TypeVar, Type, cast

from maya.api import OpenMaya as om

from ..........value.scalar_compound.scalar_compound_value import (
    ScalarCompoundValue,
)
from ........... import logger as u_logger
from .._base import (
    UnitCompoundBasePlugOperator,
    UnitCompoundBaseAttrOperator,
    UnitCompoundBaseField,
)

A = TypeVar("A", bound="LinearCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="LinearCompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[float])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LinearCompoundBasePlugOperator(UnitCompoundBasePlugOperator[A, V]):
    """距離 compound 属性の値を読み書きするプラグ操作の基底クラス。"""

    __slots__ = ()

    CHILD_M_ATTR_TYPE: ClassVar[int] = om.MFnUnitAttribute.kDistance

    def _prepare_child_limit_value(self, value: float) -> om.MDistance:
        return om.MDistance(value, om.MDistance.kCentimeters)

    def _get_child_value(self, child_plug: om.MPlug) -> float:
        return child_plug.asMDistance().asCentimeters()

    def _set_child_value(self, child_plug: om.MPlug, value: float) -> None:
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node.modifier_manager.dg_mod.newPlugValueMDistance(
            child_plug, value
        )

    def _set_child_value_direct(
        self,
        child_plug: om.MPlug,
        value: float,
    ) -> None:
        value = om.MDistance(value, om.MDistance.kCentimeters)
        child_plug.setMDistance(value)


class LinearCompoundBaseAttrOperator(UnitCompoundBaseAttrOperator[P]):
    """距離 compound 属性の定義を保持する基底クラス。"""

    __slots__ = ()


class LinearCompoundBaseField(UnitCompoundBaseField[A, P]):
    """距離 compound 属性の定義とプラグ操作を結ぶ基底クラス。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], LinearCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], LinearCompoundBasePlugOperator)
