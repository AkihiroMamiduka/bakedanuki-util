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
    DataNumericBasePlugOperator["DataShort3AttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set_direct(self, values: list[int]):
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            values (list[int]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Short, values)


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
