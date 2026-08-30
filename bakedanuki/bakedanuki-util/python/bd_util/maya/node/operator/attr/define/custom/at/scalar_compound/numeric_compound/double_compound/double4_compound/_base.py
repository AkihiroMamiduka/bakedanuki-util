# coding: utf-8
from typing import Any, Generic, TypeVar, Type, cast

# self
from ...........value.scalar_compound.scalar_compound_value import (
    ScalarCompoundValue,
)
from ............ import logger as u_logger
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)

A = TypeVar("A", bound="Double4CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Double4CompoundBasePlugOperator[Any, Any]")

V = TypeVar("V", bound=ScalarCompoundValue[float])


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class Double4CompoundBasePlugOperator(
    DoubleCompoundBasePlugOperator[A, V],
    Generic[A, V],
):
    __slots__ = ()


class Double4CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double4"


class Double4CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double4CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double4CompoundBasePlugOperator)
