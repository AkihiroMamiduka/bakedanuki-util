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


class DataDouble3PlugOperator(DataNumericBasePlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Double, values)


class DataDouble3AttrOperator(DataNumericBaseAttrOperator[P]):
    __slots__ = ()

    DATA_TYPE = "double3"
    PLUG_CLS = cast(Type[P], DataDouble3PlugOperator)
