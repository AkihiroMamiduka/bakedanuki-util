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

A = TypeVar("A", bound="LongCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="LongCompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[int])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LongCompoundBasePlugOperator(
    NumericCompoundBasePlugOperator[A, V, int]
):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kLong

    # get
    def _get_child_value(self, child_plug: om.MPlug) -> int:
        return child_plug.asInt()

    # set
    def _set_child_value(self, child_plug: om.MPlug, value: int) -> None:
        self._node.modifier_manager.dg_mod.newPlugValueInt(child_plug, value)

    def _set_child_value_direct(
        self,
        child_plug: om.MPlug,
        value: int,
    ) -> None:
        child_plug.setInt(value)


class LongCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    __slots__ = ()


class LongCompoundBaseField(NumericCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], LongCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], LongCompoundBasePlugOperator)
