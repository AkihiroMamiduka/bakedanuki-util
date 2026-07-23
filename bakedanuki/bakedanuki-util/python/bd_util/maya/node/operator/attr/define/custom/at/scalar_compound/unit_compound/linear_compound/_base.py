# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ........... import logger as u_logger
from .._base import (
    UnitCompoundBasePlugOperator,
    UnitCompoundBaseAttrOperator,
    UnitCompoundBaseField,
)

A = TypeVar("A", bound="LinearCompoundBaseAttrOperator")

P = TypeVar("P", bound="LinearCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LinearCompoundBasePlugOperator(UnitCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnUnitAttribute.kDistance

    def _prepare_child_limit_value(self, value):
        return om.MDistance(value, om.MDistance.kCentimeters)

    # get
    def _get_child_value(self, child_plug: om.MPlug) -> float:
        return child_plug.asMDistance().asCentimeters()

    # set
    def _set_child_value(self, child_plug: om.MPlug, value: float) -> None:
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node._dg_mod.newPlugValueMDistance(child_plug, value)

    def _set_child_value_direct(
        self,
        child_plug: om.MPlug,
        value: float,
    ) -> None:
        value = om.MDistance(value, om.MDistance.kCentimeters)
        child_plug.setMDistance(value)


class LinearCompoundBaseAttrOperator(UnitCompoundBaseAttrOperator[P]):
    __slots__ = ()


class LinearCompoundBaseField(UnitCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], LinearCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], LinearCompoundBasePlugOperator)
