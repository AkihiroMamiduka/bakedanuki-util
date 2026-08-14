# coding: utf-8
from collections.abc import Sequence
from typing import Any, TypeVar, Type, cast

# self
from ............value import Quat
from ............. import logger as u_logger
from .._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)

A = TypeVar("A", bound="QuatCompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="QuatCompoundBasePlugOperator[Any]")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class QuatCompoundBasePlugOperator(Double4CompoundBasePlugOperator[A]):
    __slots__ = ()

    VALUE_TYPE = Quat

    def get(self) -> Quat:
        return cast(Quat, super().get())

    @property
    def value(self) -> Quat:
        return self.get()

    @value.setter
    def value(self, value: Sequence[int | float]) -> None:
        self.set(value)

    @property
    def value_direct(self) -> Quat:
        return self.get()

    @value_direct.setter
    def value_direct(self, value: Sequence[int | float]) -> None:
        self.set_direct(value)


class QuatCompoundBaseAttrOperator(Double4CompoundBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double4"


class QuatCompoundBaseField(Double4CompoundBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], QuatCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], QuatCompoundBasePlugOperator)
