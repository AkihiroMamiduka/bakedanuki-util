# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataFloat2PlugOperator(
    DataNumericBasePlugOperator["DataFloat2AttrOperator", float]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        """float2 dataプラグの現在値を2要素のfloatリストで取得する。"""
        x, y = self._get_data()
        return [x, y]

    # set
    def set_direct(self, value: list[float]) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[float]): x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Float, value)


class DataFloat2AttrOperator(
    DataNumericBaseAttrOperator[DataFloat2PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "float2"


class DataFloat2Field(
    DataNumericBaseField[DataFloat2AttrOperator, DataFloat2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataFloat2AttrOperator
    PLUG_CLS = DataFloat2PlugOperator
