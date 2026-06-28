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

A = TypeVar("A", bound="LongCompoundBaseAttrOperator")

P = TypeVar("P", bound="LongCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class LongCompoundBasePlugOperator(NumericCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kLong

    # get
    def _get_child_value(self, child_plug) -> int:
        return child_plug.asInt()

    # set
    def _set_child_value(self, child_plug, value: int):
        self._node._dg_mod.newPlugValueInt(child_plug, value)


class LongCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    __slots__ = ()


class LongCompoundBaseField(NumericCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], LongCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], LongCompoundBasePlugOperator)
