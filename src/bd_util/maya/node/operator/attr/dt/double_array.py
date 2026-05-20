# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import DataArrayBaseAttr, DataArrayBasePlug

A = TypeVar("A", bound="DataArrayBaseAttr")

P = TypeVar("P", bound="DataArrayBasePlug")


class DataDoubleArrayPlug(DataArrayBasePlug["DataDoubleArrayAttr"]):
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


class DataDoubleArrayAttr(DataArrayBaseAttr[DataDoubleArrayPlug]):
    __slots__ = ()

    DATA_TYPE = "doubleArray"
    PLUG_CLS = cast(Type[P], DataDoubleArrayPlug)
