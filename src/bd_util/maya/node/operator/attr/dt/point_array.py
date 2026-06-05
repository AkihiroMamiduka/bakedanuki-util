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
    def get(self) -> list[float]:
        return [
            (p.x, p.y, p.z, p.w)
            for p in self._get_array_values(om.MFnPointArrayData)
        ]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnPointArrayData, om.MPointArray, values)


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
