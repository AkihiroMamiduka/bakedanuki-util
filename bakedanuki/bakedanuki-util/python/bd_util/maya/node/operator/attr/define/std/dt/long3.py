# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataLong3PlugOperator(
    DataNumericBasePlugOperator["DataLong3AttrOperator", int]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        """long3 dataプラグの現在値を3要素のintリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set_direct(self, value: list[int]) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[int]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Long, value)


class DataLong3AttrOperator(
    DataNumericBaseAttrOperator[DataLong3PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "long3"


class DataLong3Field(
    DataNumericBaseField[DataLong3AttrOperator, DataLong3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataLong3AttrOperator
    PLUG_CLS = DataLong3PlugOperator
