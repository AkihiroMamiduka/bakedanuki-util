# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .......... import logger as u_logger
from .._base import (
    ScalarCompoundBasePlugOperator,
    ScalarCompoundBaseAttrOperator,
    ScalarCompoundBaseField,
)

A = TypeVar("A", bound="UnitCompoundBaseAttrOperator")

P = TypeVar("P", bound="UnitCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class UnitCompoundBasePlugOperator(ScalarCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_FN = om.MFnUnitAttribute


class UnitCompoundBaseAttrOperator(ScalarCompoundBaseAttrOperator[P]):
    __slots__ = ()


class UnitCompoundBaseField(ScalarCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], UnitCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], UnitCompoundBasePlugOperator)
