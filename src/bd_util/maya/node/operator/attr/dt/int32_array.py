# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataInt32ArrayPlugOperator(
    DataArrayBasePlugOperator["DataInt32ArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        return self._get_array_values(om.MFnIntArrayData)

    # set
    def set(self, values: list[int]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[int]): セットする値のリスト
        """
        self._set_values(om.MFnIntArrayData, om.MIntArray, values)


class DataInt32ArrayAttrOperator(
    DataArrayBaseAttrOperator[DataInt32ArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "int32Array"


class DataInt32ArrayField(
    DataArrayBaseField[DataInt32ArrayAttrOperator, DataInt32ArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataInt32ArrayAttrOperator
    PLUG_CLS = DataInt32ArrayPlugOperator
