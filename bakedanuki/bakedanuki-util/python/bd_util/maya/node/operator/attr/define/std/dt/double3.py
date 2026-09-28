# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataDouble3PlugOperator(
    DataNumericBasePlugOperator["DataDouble3AttrOperator", float]
):
    """`double3` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[float]:
        """double3 dataプラグの現在値を3要素のfloatリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    def set_direct(self, value: list[float]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Double, value)


class DataDouble3AttrOperator(
    DataNumericBaseAttrOperator[DataDouble3PlugOperator]
):
    """`double3` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "double3"


class DataDouble3Field(
    DataNumericBaseField[DataDouble3AttrOperator, DataDouble3PlugOperator]
):
    """`double3` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataDouble3AttrOperator
    PLUG_CLS = DataDouble3PlugOperator
