# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
)

A = TypeVar("A", bound="DataArrayBaseAttrOperator")

P = TypeVar("P", bound="DataArrayBasePlugOperator")


class DataDoubleArrayPlugOperator(
    DataArrayBasePlugOperator["DataDoubleArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        return self._get_array_values(om.MFnDoubleArrayData)

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnDoubleArrayData, om.MDoubleArray, values)


class DataDoubleArrayAttrOperator(
    DataArrayBaseAttrOperator[DataDoubleArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "doubleArray"
    PLUG_CLS = cast(Type[P], DataDoubleArrayPlugOperator)
