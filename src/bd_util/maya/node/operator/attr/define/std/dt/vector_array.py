# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataVectorArrayPlugOperator(
    DataArrayBasePlugOperator["DataVectorArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        return [
            (p.x, p.y, p.z, p.w)
            for p in self._get_array_values(om.MFnVectorArrayData)
        ]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnVectorArrayData, om.MVectorArray, values)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kVectorArray)


class DataVectorArrayAttrOperator(
    DataArrayBaseAttrOperator[DataVectorArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "vectorArray"


class DataVectorArrayField(
    DataArrayBaseField[
        DataVectorArrayAttrOperator, DataVectorArrayPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataVectorArrayAttrOperator
    PLUG_CLS = DataVectorArrayPlugOperator
