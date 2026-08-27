# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataFloat3PlugOperator(
    DataNumericBasePlugOperator["DataFloat3AttrOperator", float]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        """float3 dataプラグの現在値を3要素のfloatリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set_direct(self, value: list[float]) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[float]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Float, value)


class DataFloat3AttrOperator(
    DataNumericBaseAttrOperator[DataFloat3PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "float3"


class DataFloat3Field(
    DataNumericBaseField[DataFloat3AttrOperator, DataFloat3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataFloat3AttrOperator
    PLUG_CLS = DataFloat3PlugOperator
