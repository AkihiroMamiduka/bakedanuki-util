# coding: utf-8

from maya.api import OpenMaya as om

from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataStringArrayPlugOperator(
    DataArrayBasePlugOperator["DataStringArrayAttrOperator"]
):
    """`stringArray` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[str]:
        """stringArray dataプラグの現在値を文字列リストで取得する。"""
        return self._get_array_values(om.MFnStringArrayData)

    def set_direct(self, value: list[str]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: セットする値のリスト
        """
        self.plug.setMObject(om.MFnStringArrayData().create(value))

    def add_attr(self):
        """文字列配列属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kStringArray)


class DataStringArrayAttrOperator(
    DataArrayBaseAttrOperator[DataStringArrayPlugOperator]
):
    """`stringArray` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "stringArray"


class DataStringArrayField(
    DataArrayBaseField[
        DataStringArrayAttrOperator, DataStringArrayPlugOperator
    ]
):
    """`stringArray` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataStringArrayAttrOperator
    PLUG_CLS = DataStringArrayPlugOperator
