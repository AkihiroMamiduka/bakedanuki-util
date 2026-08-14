# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...........value import Double4
from ............ import logger as u_logger
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)

A = TypeVar("A", bound="Double4CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Double4CompoundBasePlugOperator[Any]")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class Double4CompoundBasePlugOperator(
    DoubleCompoundBasePlugOperator[A, Double4]
):
    __slots__ = ()

    VALUE_TYPE = Double4


class Double4CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double4"


class Double4CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double4CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double4CompoundBasePlugOperator)
