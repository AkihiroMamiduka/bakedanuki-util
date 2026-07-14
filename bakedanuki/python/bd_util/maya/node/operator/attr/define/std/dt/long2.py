# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataLong2PlugOperator(
    DataNumericBasePlugOperator["DataLong2AttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        x, y = self._get_data()
        return [x, y]

    # set
    def set_direct(self, values: list[int]):
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            values (list[int]): x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Long, values)


class DataLong2AttrOperator(
    DataNumericBaseAttrOperator[DataLong2PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "long2"


class DataLong2Field(
    DataNumericBaseField[DataLong2AttrOperator, DataLong2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataLong2AttrOperator
    PLUG_CLS = DataLong2PlugOperator
