# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataLong3PlugOperator(
    DataNumericBasePlugOperator["DataLong3AttrOperator", int]
):
    """`long3` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[int]:
        """long3 dataプラグの現在値を3要素のintリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    def set_direct(self, value: list[int]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Long, value)


class DataLong3AttrOperator(
    DataNumericBaseAttrOperator[DataLong3PlugOperator]
):
    """`long3` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "long3"


class DataLong3Field(
    DataNumericBaseField[DataLong3AttrOperator, DataLong3PlugOperator]
):
    """`long3` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataLong3AttrOperator
    PLUG_CLS = DataLong3PlugOperator
