# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import DataArrayBaseAttr, DataArrayBasePlug

A = TypeVar("A", bound="DataArrayBaseAttr")

P = TypeVar("P", bound="DataArrayBasePlug")


class DataStringArrayPlug(DataArrayBasePlug["DataStringArrayAttr"]):
    __slots__ = ()

    # get
    def get(self) -> list[str]:
        return self._get_array_values(om.MFnStringArrayData)

    # set
    def set(self, values: list[str]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[str]): セットする値のリスト
        """
        self._set_values(om.MFnStringArrayData, om.MStringArray, values)


class DataStringArrayAttr(DataArrayBaseAttr[DataStringArrayPlug]):
    __slots__ = ()

    DATA_TYPE = "stringArray"
    PLUG_CLS = cast(Type[P], DataStringArrayPlug)
