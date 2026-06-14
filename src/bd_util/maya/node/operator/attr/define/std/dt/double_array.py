# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataDoubleArrayPlugOperator(
    DataArrayBasePlugOperator["DataDoubleArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        return self._get_array_values(om.MFnDoubleArrayData)

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnDoubleArrayData, om.MDoubleArray, values)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kDoubleArray)


class DataDoubleArrayAttrOperator(
    DataArrayBaseAttrOperator[DataDoubleArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "doubleArray"


class DataDoubleArrayField(
    DataArrayBaseField[
        DataDoubleArrayAttrOperator, DataDoubleArrayPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataDoubleArrayAttrOperator
    PLUG_CLS = DataDoubleArrayPlugOperator
