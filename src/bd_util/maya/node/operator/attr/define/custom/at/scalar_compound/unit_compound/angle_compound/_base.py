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

A = TypeVar("A", bound="AngleCompoundBaseAttrOperator")

P = TypeVar("P", bound="AngleCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class AngleCompoundBasePlugOperator(UnitCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnUnitAttribute.kAngle

    def _prepare_child_default_value(self, value):
        return om.MAngle(value, om.MAngle.kDegrees).asRadians()

    def _prepare_child_limit_value(self, value):
        return om.MAngle(value, om.MAngle.kDegrees)

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asMAngle().asDegrees()

    # set
    def _set_child_value(self, child_plug, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            child_plug, om.MAngle(value, om.MAngle.kDegrees)
        )

    def _set_child_value_direct(self, child_plug, value: float):
        child_plug.setMAngle(om.MAngle(value, om.MAngle.kDegrees))


class AngleCompoundBaseAttrOperator(UnitCompoundBaseAttrOperator[P]):
    __slots__ = ()


class AngleCompoundBaseField(UnitCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], AngleCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], AngleCompoundBasePlugOperator)
