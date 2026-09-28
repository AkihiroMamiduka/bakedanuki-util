# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataShort2PlugOperator(
    DataNumericBasePlugOperator["DataShort2AttrOperator", int]
):
    """`short2` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[int]:
        """short2 dataプラグの現在値を2要素のintリストで取得する。"""
        x, y = self._get_data()
        return [x, y]

    def set_direct(self, value: list[int]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Short, value)


class DataShort2AttrOperator(
    DataNumericBaseAttrOperator[DataShort2PlugOperator]
):
    """`short2` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "short2"


class DataShort2Field(
    DataNumericBaseField[DataShort2AttrOperator, DataShort2PlugOperator]
):
    """`short2` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataShort2AttrOperator
    PLUG_CLS = DataShort2PlugOperator
