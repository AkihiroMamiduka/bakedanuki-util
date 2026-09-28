# coding: utf-8

from maya.api import OpenMaya as om

from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataDoubleArrayPlugOperator(
    DataArrayBasePlugOperator["DataDoubleArrayAttrOperator"]
):
    """`doubleArray` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[float]:
        """doubleArray dataプラグの現在値をfloatリストで取得する。"""
        return self._get_array_values(om.MFnDoubleArrayData)

    def set_direct(self, value: list[float]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: セットする値のリスト
        """
        self._set_values(om.MFnDoubleArrayData, om.MDoubleArray, value)

    def add_attr(self):
        """double 配列属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kDoubleArray)


class DataDoubleArrayAttrOperator(
    DataArrayBaseAttrOperator[DataDoubleArrayPlugOperator]
):
    """`doubleArray` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "doubleArray"


class DataDoubleArrayField(
    DataArrayBaseField[
        DataDoubleArrayAttrOperator, DataDoubleArrayPlugOperator
    ]
):
    """`doubleArray` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataDoubleArrayAttrOperator
    PLUG_CLS = DataDoubleArrayPlugOperator
