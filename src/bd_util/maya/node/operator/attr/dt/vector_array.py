# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import DataArrayBaseAttr, DataArrayBasePlug

A = TypeVar("A", bound="DataArrayBaseAttr")

P = TypeVar("P", bound="DataArrayBasePlug")


class VectorArrayPlug(DataArrayBasePlug["DataVectorArrayAttr"]):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        return [
            (p.x, p.y, p.z, p.w)
            for p in self._get_array_values(om.MFnVectorArrayData)
        ]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnVectorArrayData, om.MVectorArray, values)


class DataVectorArrayAttr(DataArrayBaseAttr[VectorArrayPlug]):
    __slots__ = ()

    DATA_TYPE = "vectorArray"
    PLUG_CLS = cast(Type[P], VectorArrayPlug)
