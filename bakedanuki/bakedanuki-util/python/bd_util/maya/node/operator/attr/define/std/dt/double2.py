# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataDouble2PlugOperator(
    DataNumericBasePlugOperator["DataDouble2AttrOperator", float]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        """double2 dataプラグの現在値を2要素のfloatリストで取得する。"""
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
        self._set_data(om.MFnNumericData.k2Double, value)


class DataDouble2AttrOperator(
    DataNumericBaseAttrOperator[DataDouble2PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "double2"


class DataDouble2Field(
    DataNumericBaseField[DataDouble2AttrOperator, DataDouble2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataDouble2AttrOperator
    PLUG_CLS = DataDouble2PlugOperator
