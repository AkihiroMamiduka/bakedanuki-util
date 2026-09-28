# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataShort3PlugOperator(
    DataNumericBasePlugOperator["DataShort3AttrOperator", int]
):
    """`short3` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[int]:
        """short3 dataプラグの現在値を3要素のintリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    def set_direct(self, value: list[int]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Short, value)


class DataShort3AttrOperator(
    DataNumericBaseAttrOperator[DataShort3PlugOperator]
):
    """`short3` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "short3"


class DataShort3Field(
    DataNumericBaseField[DataShort3AttrOperator, DataShort3PlugOperator]
):
    """`short3` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataShort3AttrOperator
    PLUG_CLS = DataShort3PlugOperator
