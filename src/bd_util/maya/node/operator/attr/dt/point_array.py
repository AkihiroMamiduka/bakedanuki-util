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


class PointArrayPlugOperator(
    DataArrayBasePlugOperator["DataPointArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        return [
            (p.x, p.y, p.z, p.w)
            for p in self._get_array_values(om.MFnPointArrayData)
        ]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnPointArrayData, om.MPointArray, values)


class DataPointArrayAttrOperator(
    DataArrayBaseAttrOperator[PointArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "pointArray"
    PLUG_CLS = cast(Type[P], PointArrayPlugOperator)
