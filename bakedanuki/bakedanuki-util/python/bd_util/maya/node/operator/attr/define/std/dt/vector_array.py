# coding: utf-8

from maya.api import OpenMaya as om

from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataVectorArrayPlugOperator(
    DataArrayBasePlugOperator["DataVectorArrayAttrOperator"]
):
    """`vectorArray` データプラグを扱う。"""

    __slots__ = ()

    def get(self) -> list[tuple[float, float, float]]:
        """vectorArray dataプラグの現在値を3成分tupleのリストで取得する。"""
        return [
            (p.x, p.y, p.z)
            for p in self._get_array_values(om.MFnVectorArrayData)
        ]

    def set_direct(
        self,
        value: list[tuple[float, float, float]],
    ) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value:
                セットする値のリスト
        """
        vectors = [om.MVector(*vector) for vector in value]
        self._set_values_after_create(
            om.MFnVectorArrayData,
            om.MVectorArray,
            vectors,
        )

    def add_attr(self):
        """vector 配列属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kVectorArray)


class DataVectorArrayAttrOperator(
    DataArrayBaseAttrOperator[DataVectorArrayPlugOperator]
):
    """`vectorArray` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "vectorArray"


class DataVectorArrayField(
    DataArrayBaseField[
        DataVectorArrayAttrOperator, DataVectorArrayPlugOperator
    ]
):
    """`vectorArray` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataVectorArrayAttrOperator
    PLUG_CLS = DataVectorArrayPlugOperator
