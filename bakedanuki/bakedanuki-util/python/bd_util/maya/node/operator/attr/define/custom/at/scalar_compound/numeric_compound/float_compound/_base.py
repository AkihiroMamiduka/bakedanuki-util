# coding: utf-8
from typing import Any, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ..........value.scalar_compound.scalar_compound_value import (
    ScalarCompoundValue,
)
from ........... import logger as u_logger
from .._base import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)

A = TypeVar("A", bound="FloatCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="FloatCompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[float])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class FloatCompoundBasePlugOperator(NumericCompoundBasePlugOperator[A, V]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kFloat

    # get
    def _get_child_value(self, child_plug: om.MPlug) -> float:
        return child_plug.asFloat()

    # set
    def _set_child_value(self, child_plug: om.MPlug, value: float) -> None:
        self._node.modifier_manager.dg_mod.newPlugValueFloat(child_plug, value)

    def _set_child_value_direct(
        self,
        child_plug: om.MPlug,
        value: float,
    ) -> None:
        child_plug.setFloat(value)


class FloatCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    __slots__ = ()


class FloatCompoundBaseField(NumericCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatCompoundBasePlugOperator)
