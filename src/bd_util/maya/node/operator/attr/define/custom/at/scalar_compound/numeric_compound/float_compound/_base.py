# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ........... import logger as u_logger
from .._base import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)

A = TypeVar("A", bound="FloatCompoundBaseAttrOperator")

P = TypeVar("P", bound="FloatCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class FloatCompoundBasePlugOperator(NumericCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kFloat

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asFloat()

    # set
    def _set_child_value(self, child_plug, value: float):
        self._node._dg_mod.newPlugValueFloat(child_plug, value)


class FloatCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    __slots__ = ()


class FloatCompoundBaseField(NumericCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatCompoundBasePlugOperator)
