# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
)

A = TypeVar("A", bound="DataNumericBaseAttrOperator")

P = TypeVar("P", bound="DataNumericBasePlugOperator")


class DataFloat2PlugOperator(DataNumericBasePlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        x, y = self._get_data()
        return [x, y]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Float, values)


class DataFloat2AttrOperator(DataNumericBaseAttrOperator[P]):
    __slots__ = ()

    DATA_TYPE = "float2"
    PLUG_CLS = cast(Type[P], DataFloat2PlugOperator)
