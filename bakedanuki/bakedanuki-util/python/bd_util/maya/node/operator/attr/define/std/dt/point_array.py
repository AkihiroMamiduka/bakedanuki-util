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
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[tuple[float, float, float, float]]):
                セットする値のリスト
        """
        points = [om.MPoint(*point) for point in value]
        self._set_values_after_create(
            om.MFnPointArrayData,
            om.MPointArray,
            points,
        )

    # add
    def add_attr(self):
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
