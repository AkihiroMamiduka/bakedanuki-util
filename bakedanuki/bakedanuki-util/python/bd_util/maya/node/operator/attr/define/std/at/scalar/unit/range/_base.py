# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ........... import logger as u_logger
from .._base import (
    UnitBaseAttrOperator,
    UnitBasePlugOperator,
    UnitBaseField,
)

A = TypeVar("A", bound="UnitBaseAttrOperator")

P = TypeVar("P", bound="UnitBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class UnitRangeBasePlugOperator(UnitBasePlugOperator[A]):
    __slots__ = ()

    # set
    def set_min(self, value):
        self._fn_attr.setMin(value)

    def set_max(self, value):
        self._fn_attr.setMax(value)

    def set_soft_min(self, value):
        self._fn_attr.setSoftMin(value)

    def set_soft_max(self, value):
        self._fn_attr.setSoftMax(value)

    # add
    def _add_attr_base(self, mfn_numeric_data_type: int):
        super()._add_attr_base(mfn_numeric_data_type)

        # アトリビュート設定
        #   min
        v = self._oprt_attr.min_value
        if v is not None:
            self.set_min(v)
        #   max
        v = self._oprt_attr.max_value
        if v is not None:
            self.set_max(v)
        #   soft_min
        v = self._oprt_attr.soft_min_value
        if v is not None:
            self.set_soft_min(v)
        #   soft_max
        v = self._oprt_attr.soft_max_value
        if v is not None:
            self.set_soft_max(v)


class UnitRangeBaseAttrOperator(UnitBaseAttrOperator[P]):
    __slots__ = ()


class UnitRangeBaseField(UnitBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], UnitRangeBaseAttrOperator)
    PLUG_CLS = cast(Type[P], UnitRangeBasePlugOperator)
