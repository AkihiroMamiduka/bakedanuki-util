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

A = TypeVar("A", bound="NumericCompoundBaseAttrOperator")

P = TypeVar("P", bound="NumericCompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class NumericCompoundBasePlugOperator(ScalarCompoundBasePlugOperator[A]):
    __slots__ = ()

    CHILD_M_FN = om.MFnNumericAttribute


class NumericCompoundBaseAttrOperator(ScalarCompoundBaseAttrOperator[P]):
    __slots__ = ()


class NumericCompoundBaseField(ScalarCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], NumericCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], NumericCompoundBasePlugOperator)
