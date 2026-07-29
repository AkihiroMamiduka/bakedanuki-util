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

A = TypeVar("A", bound="ShortCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="ShortCompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[int])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ShortCompoundBasePlugOperator(NumericCompoundBasePlugOperator[A, V]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kShort

    # get
    def _get_child_value(self, child_plug: om.MPlug) -> int:
        return child_plug.asShort()

    # set
    def _set_child_value(self, child_plug: om.MPlug, value: int) -> None:
        self._node._dg_mod.newPlugValueShort(child_plug, value)

    def _set_child_value_direct(
        self,
        child_plug: om.MPlug,
        value: int,
    ) -> None:
        child_plug.setShort(value)


class ShortCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    __slots__ = ()


class ShortCompoundBaseField(NumericCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ShortCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], ShortCompoundBasePlugOperator)
