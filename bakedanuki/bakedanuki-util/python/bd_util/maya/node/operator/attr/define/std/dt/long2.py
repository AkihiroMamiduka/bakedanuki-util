# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataLong2PlugOperator(
    DataNumericBasePlugOperator["DataLong2AttrOperator", int]
):
    """`long2` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[int]:
        """long2 dataプラグの現在値を2要素のintリストで取得する。"""
        x, y = self._get_data()
        return [x, y]

    def set_direct(self, value: list[int]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Long, value)


class DataLong2AttrOperator(
    DataNumericBaseAttrOperator[DataLong2PlugOperator]
):
    """`long2` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "long2"


class DataLong2Field(
    DataNumericBaseField[DataLong2AttrOperator, DataLong2PlugOperator]
):
    """`long2` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataLong2AttrOperator
    PLUG_CLS = DataLong2PlugOperator
