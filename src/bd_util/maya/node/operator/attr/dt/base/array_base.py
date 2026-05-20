# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# self
from .._core import DataTypeAttr, DataTypePlug

A = TypeVar("A", bound="DataTypeAttr")

P = TypeVar("P", bound="DataTypePlug")


class DataArrayBasePlug(DataTypePlug[A]):
    __slots__ = ()

    # get
    def _get_array_data(self, fn_data_cls) -> list:
        return fn_data_cls(self.plug.asMObject()).array()

    def _get_array_values(self, fn_data_cls) -> list:
        return list(self._get_array_data(fn_data_cls))

    # set
    def _set_values(self, fn_data_cls, array_cls, values: list[float]):
        """
        値をセットするヘルパー

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self.plug.setMObject(fn_data_cls().create(array_cls(values)))


class DataArrayBaseAttr(DataTypeAttr[P]):
    __slots__ = ()

    DATA_TYPE = "abc"
    PLUG_CLS = cast(Type[P], DataArrayBasePlug)
