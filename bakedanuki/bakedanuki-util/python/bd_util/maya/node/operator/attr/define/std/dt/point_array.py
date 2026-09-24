# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class PointArrayPlugOperator(
    DataArrayBasePlugOperator["DataPointArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[tuple[float, float, float, float]]:
        """pointArray dataプラグの現在値を4成分tupleのリストで取得する。"""
        return [
            (p.x, p.y, p.z, p.w)
            for p in self._get_array_values(om.MFnPointArrayData)
        ]

    # set
    def set_direct(
        self,
        value: list[tuple[float, float, float, float]],
    ) -> None:
        """MPlug に値を直接設定する。

        ModifierManager の履歴には入らない。

        Args:
            value:
                セットする値のリスト
        """
        points = [om.MPoint(*point) for point in value]
        self._set_values_after_create(
            om.MFnPointArrayData,
            om.MPointArray,
            points,
        )

    def add_attr(self):
        """point 配列属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kPointArray)


class DataPointArrayAttrOperator(
    DataArrayBaseAttrOperator[PointArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "pointArray"


class DataPointArrayField(
    DataArrayBaseField[DataPointArrayAttrOperator, PointArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataPointArrayAttrOperator
    PLUG_CLS = PointArrayPlugOperator
