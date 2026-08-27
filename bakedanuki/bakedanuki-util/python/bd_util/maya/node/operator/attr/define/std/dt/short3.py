# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataShort3PlugOperator(
    DataNumericBasePlugOperator["DataShort3AttrOperator", int]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        """short3 dataプラグの現在値を3要素のintリストで取得する。"""
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
        self._set_data(om.MFnNumericData.k3Short, value)


class DataShort3AttrOperator(
    DataNumericBaseAttrOperator[DataShort3PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "short3"


class DataShort3Field(
    DataNumericBaseField[DataShort3AttrOperator, DataShort3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataShort3AttrOperator
    PLUG_CLS = DataShort3PlugOperator
