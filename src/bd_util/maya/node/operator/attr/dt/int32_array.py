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


class DataInt32ArrayPlugOperator(
    DataArrayBasePlugOperator["DataInt32ArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        return self._get_array_values(om.MFnIntArrayData)

    # set
    def set(self, values: list[int]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[int]): セットする値のリスト
        """
        self._set_values(om.MFnIntArrayData, om.MIntArray, values)


class DataInt32ArrayAttrOperator(
    DataArrayBaseAttrOperator[DataInt32ArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "int32Array"
    PLUG_CLS = cast(Type[P], DataInt32ArrayPlugOperator)
