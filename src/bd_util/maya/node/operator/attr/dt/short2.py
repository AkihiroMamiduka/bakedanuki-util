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


class DataShort2PlugOperator(DataNumericBasePlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        x, y = self._get_data()
        return [x, y]

    # set
    def set(self, values: list[int]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[int]): x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Short, values)


class DataShort2AttrOperator(DataNumericBaseAttrOperator[P]):
    __slots__ = ()

    DATA_TYPE = "short2"
    PLUG_CLS = cast(Type[P], DataShort2PlugOperator)
