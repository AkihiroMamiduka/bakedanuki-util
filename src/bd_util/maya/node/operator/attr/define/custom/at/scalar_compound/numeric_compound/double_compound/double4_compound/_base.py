# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ............ import logger as u_logger
from .._base import (
    DoubleCompoundBasePlugOperator,
    DoubleCompoundBaseAttrOperator,
    DoubleCompoundBaseField,
)
from .......std.at.numeric_scalar_range.double import DoubleField

A = TypeVar("A", bound="Double4CompoundBaseAttrOperator")

P = TypeVar("P", bound="Double4CompoundBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class Double4CompoundBasePlugOperator(DoubleCompoundBasePlugOperator[A]):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()
    w = DoubleField()


class Double4CompoundBaseAttrOperator(DoubleCompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double4"


class Double4CompoundBaseField(DoubleCompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double4CompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], Double4CompoundBasePlugOperator)
