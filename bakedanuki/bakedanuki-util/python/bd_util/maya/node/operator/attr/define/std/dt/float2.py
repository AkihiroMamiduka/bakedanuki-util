# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataFloat2PlugOperator(
    DataNumericBasePlugOperator["DataFloat2AttrOperator", float]
):
    """`float2` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[float]:
        """float2 dataプラグの現在値を2要素のfloatリストで取得する。"""
        x, y = self._get_data()
        return [x, y]

    def set_direct(self, value: list[float]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Float, value)


class DataFloat2AttrOperator(
    DataNumericBaseAttrOperator[DataFloat2PlugOperator]
):
    """`float2` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "float2"


class DataFloat2Field(
    DataNumericBaseField[DataFloat2AttrOperator, DataFloat2PlugOperator]
):
    """`float2` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataFloat2AttrOperator
    PLUG_CLS = DataFloat2PlugOperator
