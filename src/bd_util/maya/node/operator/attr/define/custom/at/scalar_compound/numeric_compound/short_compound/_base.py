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

A = TypeVar("A", bound="ShortCompoundBaseAttrOperator")

P = TypeVar("P", bound="ShortCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ShortCompoundBasePlugOperator(NumericCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kShort

    # get
    def _get_child_value(self, child_plug) -> int:
        return child_plug.asShort()

    # set
    def _set_child_value(self, child_plug, value: int):
        self._node._dg_mod.newPlugValueShort(child_plug, value)


class ShortCompoundBaseAttrOperator(NumericCompoundBaseAttrOperator[P]):
    __slots__ = ()


class ShortCompoundBaseField(NumericCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ShortCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], ShortCompoundBasePlugOperator)
