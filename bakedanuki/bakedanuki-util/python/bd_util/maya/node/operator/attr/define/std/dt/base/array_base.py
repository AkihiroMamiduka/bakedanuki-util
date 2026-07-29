# coding: utf-8
from __future__ import annotations
from typing import Any, TypeVar, Type, cast

# self
from .._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField

A = TypeVar("A", bound="DataTypeAttrOperator[Any]")

P = TypeVar("P", bound="DataTypePlugOperator[Any]")


class DataArrayBasePlugOperator(DataTypePlugOperator[A]):
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


class DataArrayBaseAttrOperator(DataTypeAttrOperator[P]):
    __slots__ = ()

    DATA_TYPE = "abc"


class DataArrayBaseField(DataTypeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataArrayBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DataArrayBasePlugOperator)
