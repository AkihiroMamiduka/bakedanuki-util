# coding: utf-8

from maya.api import OpenMaya as om

from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataInt32ArrayPlugOperator(
    DataArrayBasePlugOperator["DataInt32ArrayAttrOperator"]
):
    __slots__ = ()

    def get(self) -> list[int]:
        """Int32Array data プラグの現在値を int リストで取得する。"""
        return self._get_array_values(om.MFnIntArrayData)

    def set_direct(self, value: list[int]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: セットする値のリスト
        """
        self._set_values(om.MFnIntArrayData, om.MIntArray, value)

    def add_attr(self):
        """int32 配列属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kIntArray)


class DataInt32ArrayAttrOperator(
    DataArrayBaseAttrOperator[DataInt32ArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "int32Array"


class DataInt32ArrayField(
    DataArrayBaseField[DataInt32ArrayAttrOperator, DataInt32ArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataInt32ArrayAttrOperator
    PLUG_CLS = DataInt32ArrayPlugOperator
